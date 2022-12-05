#include "tinyarray.hpp"

int main(void) {
  tinyarray::array<int, 5> x({1,2,3,4,5});
  tinyarray::array<int, 5> y({5,6,7,8,9});

  auto u = x * y;
  std::cout << u[0] << std::endl;

  auto w = x - y;
  std::cout << w[0] << std::endl;

  auto z = x + y;
  std::cout << z[0] << std::endl;


  return 0;
}
