#pragma once

#include <array>

#include "array.hpp"

namespace tinyarray {

// these three constructs are generic and should be generalized
// over all operators. This can be much more terse

template <char op, typename T, size_t N> struct generic_array_op {

  array<T, N> Left;
  array<T, N> Right;

  auto operator()() {

    array<T, N> result;

    for (int i = 0; i < N; ++i) {

      if constexpr (op == '+') {
        result[i] = Left[i] + Right[i];
      } else if constexpr (op == '-') {
        result[i] = Left[i] - Right[i];
      } else if constexpr (op == '*') {
        result[i] = Left[i] * Right[i];
      } else if constexpr (op == '/') {
        // TODO: make this work --> static_assert(*Right[i] != 0,
        // "ZeroDivisionError!");
        result[i] = Left[i] / Right[i];
      }
    }
    return result;
  }
};


template <char op, typename T, size_t N> struct generic_left_scalar_op {

  T Left;
  array<T, N> Right;

  auto operator()() {

    array<T, N> result;

    for (int i = 0; i < N; ++i) {

      if constexpr (op == '+') {
        result[i] = Left + Right[i];
      } else if constexpr (op == '-') {
        result[i] = Left - Right[i];
      } else if constexpr (op == '*') {
        result[i] = Left * Right[i];
      } else if constexpr (op == '/') {
        // TODO: make this work --> static_assert(*Right[i] != 0,
        // "ZeroDivisionError!");
        result[i] = Left / Right[i];
      }
    }
    return result;
  }
};


template <char op, typename T, size_t N> struct generic_right_scalar_op {

  array<T, N> Left;
  T Right;

  auto operator()() {

    array<T, N> result;

    for (int i = 0; i < N; ++i) {

      if constexpr (op == '+') {
        result[i] = Left[i] + Right;
      } else if constexpr (op == '-') {
        result[i] = Left[i] - Right;
      } else if constexpr (op == '*') {
        result[i] = Left[i] * Right;
      } else if constexpr (op == '/') {
        static_assert(Right != 0, "ZeroDivisionError!");
        result[i] = Left[i] / Right;
      }
    }
    return result;
  }
};


// array + array
template <typename T, size_t N> auto operator+(array<T, N> &a, array<T, N> &b) {
  // static_assert(a.size() == b.size(), "Arrays are incompatible size!");
  return generic_array_op<'+', T, N>{a, b}();
};

template <typename T, size_t N> auto operator-(array<T, N> &a, array<T, N> &b) {
  // static_assert(a.size() == b.size(), "Arrays are incompatible size!");
  return generic_array_op<'-', T, N>{a, b}();
};

template <typename T, size_t N> auto operator*(array<T, N> &a, array<T, N> &b) {
  // static_assert(a.size() == b.size(), "Arrays are incompatible size!");
  return generic_array_op<'*', T, N>{a, b}();
};

template <typename T, size_t N> auto operator/(array<T, N> &a, array<T, N> &b) {
  // static_assert(a.size() == b.size(), "Arrays are incompatible size!");
  return generic_array_op<'/', T, N>{a, b}();
};


// scalar + array
template <typename T, size_t N> auto operator+(T const &a, array<T, N> &b) {
  return generic_left_scalar_op<'+', T, N>{a, b}();
};

template <typename T, size_t N> auto operator-(T const &a, array<T, N> &b) {
  return generic_left_scalar_op<'-', T, N>{a, b}();
};

template <typename T, size_t N> auto operator*(T const &a, array<T, N> &b) {
  return generic_left_scalar_op<'*', T, N>{a, b}();
};

template <typename T, size_t N> auto operator/(T const &a, array<T, N> &b) {
  return generic_left_scalar_op<'/', T, N>{a, b}();
};


// array + scalar
template <typename T, size_t N> auto operator+(array<T, N> &a, T const &b) {
  return generic_right_scalar_op<'+', T, N>{a, b}();
};

template <typename T, size_t N> auto operator-(array<T, N> &a, T const &b) {
  return generic_right_scalar_op<'-', T, N>{a, b}();
};

template <typename T, size_t N> auto operator*(array<T, N> &a, T const &b) {
  return generic_right_scalar_op<'*', T, N>{a, b}();
};

template <typename T, size_t N> auto operator/(array<T, N> &a, T const &b) {
  return generic_right_scalar_op<'/', T, N>{a, b}();
};

} // namespace tinyarray
