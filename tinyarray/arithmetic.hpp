#pragma once

#include <array>
#include "array.hpp"

namespace tinyarray {

    template <typename T, size_t R>
        array<T,R> operator+(array<T,R> &a1, array<T,R> &a2){
            array<T,R> res;
            for (int i = 0; i < R; ++i) res[i] = a1[i] + a2[i];
            return res;
        }

    template <typename T, size_t R>
        array<T,R> operator-(array<T,R> &a1, array<T,R> &a2){
            array<T,R> res;
            for (int i = 0; i < R; ++i) res[i] = a1[i] - a2[i];
            return res;
        }

    template <typename T, size_t R>
        array<T,R> operator*(array<T,R> &a1, array<T,R> &a2){
            array<T,R> res;
            for (int i = 0; i < R; ++i) res[i] = a1[i] * a2[i];
            return res;
        }
}
