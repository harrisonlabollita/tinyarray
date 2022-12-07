#pragma once

#include "array.hpp"
#include <array>

namespace tinyarray {

// these three constructs are generic and should be generalized
// over all operators. This can be much more terse

//scalar + array
template <typename T, size_t R>
array<T, R> operator+(T a1, array<T, R> &a2) {
  array<T, R> res;
  for (int i = 0; i < R; ++i)
    res[i] = a1 + a2[i];
  return res;
}

//array + scalar
template <typename T, size_t R>
array<T, R> operator+(array<T, R> &a1, T &a2) {
  array<T, R> res;
  for (int i = 0; i < R; ++i)
    res[i] = a1[i] + a2;
  return res;
}

//array + array
template <typename T, size_t R>
array<T, R> operator+(array<T, R> &a1, array<T, R> &a2) {
  array<T, R> res;
  for (int i = 0; i < R; ++i)
    res[i] = a1[i] + a2[i];
  return res;
}

template <typename T, size_t R>
array<T, R> operator-(array<T, R> &a1, array<T, R> &a2) {
  array<T, R> res;
  for (int i = 0; i < R; ++i)
    res[i] = a1[i] - a2[i];
  return res;
}

template <typename T, size_t R>
array<T, R> operator*(array<T, R> &a1, array<T, R> &a2) {
  array<T, R> res;
  for (int i = 0; i < R; ++i)
    res[i] = a1[i] * a2[i];
  return res;
}

template <typename T, size_t R>
array<T, R> operator/(array<T, R> &a1, array<T, R> &a2) {
  array<T, R> res;
  for (int i = 0; i < R; ++i)
    res[i] = a1[i] * a2[i];
  return res;
}
} // namespace tinyarray
