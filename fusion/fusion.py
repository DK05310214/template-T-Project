
import torch
from torch import nn
import onnx

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.data = torch.randn(20,1,10,2)

    def forward(self, x):
        # x: 2 15 16
        # 1 2 5 3 4 4
        # 20 12 1 2
        output = torch.reshape(x, (1, 2, 5, 3, 4, 4))
        output = torch.permute(output, (2, 4, 3, 5, 0, 1))
        output = torch.reshape(output, (20,12,1,2))
        output = output + self.data
        return output

class Transform:
    def __init__(self, perm, shapeMap):
        self.perm = perm
        self.shapeMap = shapeMap
        
class Tensor:
    def __init__(self, shape, transform : Transform = Transform([], {})):
        self.shape = shape
        self.transform = transform
        if len(self.transform.perm) == 0:
            self.transform.perm = list(range(len(shape)))
        if len(self.transform.shapeMap) == 0:
            for i in range(len(shape)):
                self.transform.shapeMap[i] = [i]
    def print(self):
        print(f'Shape: {self.shape}\nTransform: \n  perm:{self.transform.perm}\n  shapeMap:{self.transform.shapeMap}')

def ApplyPerm(tensor, perm):
    if len(perm) != len(tensor.shape):
        raise ValueError("Invalid permutation")
    newShape = [tensor.shape[i] for i in perm]
    newPerm = [tensor.transform.perm[perm[i]] for i in range(len(perm))]
    return Tensor(newShape, Transform(newPerm, tensor.transform.shapeMap))

def InvPerm(perm):
    inv = [0] * len(perm)
    for i in range(len(perm)):
        inv[perm[i]] = i
    return inv

def SplitMap(shape1, shape2, orishapeMap = None):
    def add(i,j, shapeMap):
        if i not in shapeMap:
            shapeMap[i] = [j]
        else:
            shapeMap[i].append(j)
        return shapeMap
    acc1 = []
    acc2 = []
    for i in range(len(shape1)):
        acc = 1
        for j in range(i + 1):
            acc *= shape1[j]
        acc1.append(acc)
    for i in range(len(shape2)):
        acc = 1
        for j in range(i + 1):
            acc *= shape2[j]
        acc2.append(acc)
    
    i = 0
    j = 0
    splitMap = {}
    while i < len(acc1) and j < len(acc2):
        if acc2[j] < acc1[i]:
            splitMap = add(i, j, splitMap)
            j += 1
        elif acc2[j] == acc1[i]:
            preI = i - 1
            if orishapeMap is not None and preI in orishapeMap and preI in splitMap and \
                len(orishapeMap[preI]) > len(splitMap[preI]):
                if acc2[j] == acc2[j - 1]:
                    splitMap = add(preI, j, splitMap)
                else:
                    raise ValueError("Invalid splitMap")
                    return {}
            else:
                splitMap = add(i, j, splitMap)
                i += 1
            j += 1
    while j < len(acc2):
        if i - 1 not in splitMap:
            splitMap[i - 1] = [j]
        else:
            splitMap[i - 1].append(j)
        j += 1
    return splitMap

if __name__ == "__main__":

    # net = Net()     
    # inputs = (torch.randn(2,15,16),)
    # torch.onnx.export(net, inputs, "model.onnx")

    # t = Tensor([2, 3, 4, 5], Transform([0, 3, 1, 2], {
    #     0: [0], 
    #     1: [1],
    #     2: [2],
    #     3: [3],}))
    # t.print()

    # ApplyPerm(t, [2, 0, 1, 3]).print()

    # test splitMap

    splitMap = SplitMap([8,3,1], [2,4,3,1,1],
        {0: [0, 1], 1: [2, 3], 2: [4]})
    print(splitMap)

    # step1
    # splitMap = SplitMap([2,15,16], [1,2,5,3,4,4])    
    # dreInput = Tensor(
    #     [1,2,5,3,4,4],
    #     Transform(
    #         [4,5,0,2,1,3],
    #         splitMap)
    # )

    # dreOutput = ApplyPerm(dreInput, [2,4,3,5,0,1])
    # dreOutput.print()

    #step2
    cropShape = [5, 4, 3, 4, 1, 2]
    