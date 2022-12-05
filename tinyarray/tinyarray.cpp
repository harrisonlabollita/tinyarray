#include <new>
#include <array>
#include <iostream>

namespace tinyarray {

template <typename T, size_t R> class array {
private:
  using storage_t = std::array<T, R>;
  storage_t data;

public:
  // data constructor
  array(storage_t data);

  // declare operators
  T &operator[](int index);
};

// define constructors
template <typename T, size_t R> array<T,R>::array(storage_t data) {
    this->data = data;
};

// define operators
template <typename T, size_t R> T &array<T, R>::operator[](int index) {
  return data[index];
};

} // namespace tinyarray

int main(void) {

  tinyarray::array<int, 5> x({1,2,3,4,5});
  std::cout << x[0] << std::endl;

  return 0;
}
