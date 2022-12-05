#pragma once
#include <iostream>

namespace tinyarray {

template <typename T, size_t R> class array {
private:
  using storage_t = std::array<T, R>;
  storage_t data;
  int _size;

public:
  // data constructor
  array(storage_t data);
  array();

  int size() const { return _size; }

  // declare operators
  T &operator[](int index);
  auto operator+(T other);
  auto operator-(T other);

};

// define constructors
template <typename T, size_t R> array<T,R>::array(storage_t data) {
    this->_size = R;
    this->data = data;
};

template <typename T, size_t R> array<T,R>::array() {
    this->_size = R;
    storage_t data;
};

// define operators
template <typename T, size_t R> T &array<T, R>::operator[](int index) {
  return data[index];
};

template <typename T, size_t R> auto array<T, R>::operator+(T other) {
    auto out = array<T,R>(data);
    for (auto i=0; i < out.size(); i++ ){ out[i] += other; }
    return out;
};

template <typename T, size_t R> auto array<T, R>::operator-(T other) {
    auto out = array<T,R>(data);
    for (auto i=0; i < out.size(); i++ ){ out[i] -= other; }
    return out;
};


} // namespace tinyarray
