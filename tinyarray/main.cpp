#include "tinyarray.hpp"


int main(void) {

  tinyarray::array<double, 5> x({1.0, 2.0, 3.0, 4.0, 5.0});
  tinyarray::array<double, 5> y({0.01, 6.3, 7.5, 8.2, 9.4});

  auto u = x * y;
  std::cout << u.to_string() << std::endl;

  auto w = x - y;
  std::cout << w.to_string() << std::endl;

  auto z1 = x + y;
  std::cout << z1.to_string() << std::endl;

  auto z2 = x / y;
  std::cout << z2.to_string() << std::endl;

  auto z3 = x + 0.5;
  std::cout << z3.to_string() << std::endl;

  auto z4 = 1.4 + x;
  std::cout << z4.to_string() << std::endl;

  auto A = tinyarray::rand<10>();
  std::cout << A.to_string() << std::endl;
  auto B = tinyarray::rand<10>();
  std::cout << B.to_string() << std::endl;
  auto C = A + B;
  std::cout << C.to_string() << std::endl;
  return 0;
}
