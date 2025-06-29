#include <iostream>
#include <Eigen/Eigen>

int main(int, char**){
    std::cout << "Hello, from test!\n";

    Eigen::MatrixXf matrix1(3,4);
    Eigen::Vector3f vector1;

    matrix1 = Eigen::MatrixXf::Zero(3,4);
    vector1 = Eigen::Vector3f::Ones();

    std::cout << "------ matrix1 ------" << std::endl << matrix1 << std::endl;
    std::cout << "------ vector1 ------" << std::endl << vector1 << std::endl;
}