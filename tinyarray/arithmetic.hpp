#pragma once

#include <array>

#include "array.hpp"

namespace tinyarray {

// these three constructs are generic and should be generalized
// over all operators. This can be much more terse

    template <char op, typename T, size_t N>
    struct generic_op {

        array<T,N> Left;
        array<T,N> Right;

        auto operator()(){

            array<T,N> result;

            for (int i = 0; i < N; ++i){

                if constexpr ( op == '+') {
                    result[i] = Left[i] + Right[i];
                } else if constexpr (op == '-') {
                    result[i] = Left[i] - Right[i];
                } else if constexpr (op == '*') {
                    result[i] = Left[i] * Right[i];
                } else if constexpr (op == '/') {
                    // TODO: make this work --> static_assert(*Right[i] != 0, "ZeroDivisionError!");
                    result[i] = Left[i] / Right[i];
                }
            }
            return result;
        }
    };

    //array + array
    template<typename T, size_t N>
    auto operator+(array<T,N> a, array<T,N> b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'+', T, N>{a, b}();
    };

    template<typename T, size_t N>
    auto operator-(array<T,N> a, array<T,N> b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'-', T, N>{a, b}();
    };

    template<typename T, size_t N>
    auto operator*(array<T,N> a, array<T,N> b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'*', T, N>{a, b}();
    };

    template<typename T, size_t N>
    auto operator/(array<T,N> a, array<T,N> b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'/', T, N>{a, b}();
    };

}

//template <typename T, size_t R>
//array<T, R> operator-(array<T, R> &a1, array<T, R> &a2) {
//  array<T, R> res;
//  for (int i = 0; i < R; ++i)
//    res[i] = a1[i] - a2[i];
//  return res;
//}

//template <typename T, size_t R>
//array<T, R> operator*(array<T, R> &a1, array<T, R> &a2) {
//  array<T, R> res;
//  for (int i = 0; i < R; ++i)
//    res[i] = a1[i] * a2[i];
//  return res;
//}

//template <typename T, size_t R>
//array<T, R> operator/(array<T, R> &a1, array<T, R> &a2) {
//  array<T, R> res;
//  for (int i = 0; i < R; ++i)
//    res[i] = a1[i] * a2[i];
//  return res;
//}

//scalar + array
//template <typename T, size_t R>
//array<T, R> operator+(T a1, array<T, R> &a2) {
//  array<T, R> res;
//  for (int i = 0; i < R; ++i)
//    res[i] = a1 + a2[i];
//  return res;
//}

//array + scalar
//template <typename T, size_t R>
//array<T, R> operator+(array<T, R> &a1, T &a2) {
//  array<T, R> res;
//  for (int i = 0; i < R; ++i)
//    res[i] = a1[i] + a2;
//  return res;
//}

