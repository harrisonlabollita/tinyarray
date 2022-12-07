#include "tinyarray.hpp"


int main(void) {
  tinyarray::array<int, 5> x({1, 2, 3, 4, 5});
  tinyarray::array<int, 5> y({5, 6, 7, 8, 9});

  auto u = x * y;
  std::cout << u.to_string() << std::endl;

  auto w = x - y;
  std::cout << w.to_string() << std::endl;

  auto z1 = x + y;
  std::cout << z1.to_string() << std::endl;

  auto z2 = x + 1;
  std::cout << z2.to_string() << std::endl;

  auto z3 = 1 + x;
  std::cout << z3.to_string() << std::endl;

  return 0;
}
