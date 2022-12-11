#pragma once
#include <iostream>
#include <string>
#include <sstream>
#include <random>

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

  constexpr long size() const { return _size; }

  // declare operators
  T &operator[](int index);

  std::string to_string();
};

// define constructors
template <typename T, size_t R> array<T, R>::array(storage_t data) {
  this->_size = R;
  this->data = data;
};

template <typename T, size_t R> array<T, R>::array() {
  this->_size = R;
  storage_t data;
};

// define operators
template <typename T, size_t R> T &array<T, R>::operator[](int index) {
    if(index >= 0) {
      return data[index];
    } else {
        auto N = data.size();
        return data[N+index];
    }
};


template <typename T, size_t R> 
std::string array<T,R>::to_string() {
    std::stringstream out;
    out << "tinyarray (";
    for (int i = 0; i < _size; ++i) out << (i == 0 ? "" : " " ) << data[i]; 
    out << ")";
    return out.str();
};

// ones array
template <typename T, size_t N>
array<T,N> ones() {
    static_assert(std::is_arithmetic<T>::value, "Not an arithmetic type");
    array<T,N> out;
    for (int i=0; i<N; ++i) out[i] = (T)1;
    return out;
}

// zeros array
template <typename T, size_t N>
array<T,N> zeros() {
    static_assert(std::is_arithmetic<T>::value, "Not an arithmetic type");
    array<T,N> out;
    for (int i=0; i<N; ++i) out[i] = (T)0;
    return out;
}

// random array
template <size_t N>
array<double,N> rand() {

    array<double,N> out;

    auto static gen = std::mt19937(std::random_device{}());
    auto static dist  = std::uniform_real_distribution<>(0.0, 1.0);
    for (int i=0; i<N; ++i) out[i] = dist(gen);
    return out;
}

} // namespace tinyarray
