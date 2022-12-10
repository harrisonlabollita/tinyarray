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
    auto operator+(array<T,N> &a, array<T,N> &b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'+', T, N>{a, b}();
    };

    template<typename T, size_t N>
    auto operator-(array<T,N> &a, array<T,N> &b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'-', T, N>{a, b}();
    };

    template<typename T, size_t N>
    auto operator*(array<T,N> &a, array<T,N> &b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'*', T, N>{a, b}();
    };

    template<typename T, size_t N>
    auto operator/(array<T,N> &a, array<T,N> &b) {
        //static_assert(a.size() == b.size(), "Arrays are incompatible size!");
        return generic_op<'/', T, N>{a, b}();
    };

}

