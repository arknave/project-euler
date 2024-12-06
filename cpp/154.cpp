#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

int64_t factorialExp(int64_t x, int64_t p) {
    int64_t res = 0;
    for (int64_t v = p; v <= x; v *= p) {
        res += x / v;
    }

    return res;
}

int64_t solve(int64_t n, int32_t k = 12) {
    std::vector<std::array<int64_t, 2>> a(n + 1);
    for (int64_t i = 0; i <= n; ++i) {
        a[i] = {factorialExp(i, 2), factorialExp(i, 5)};
    }

    std::array<int64_t, 2> goal = {a[n][0] - k, a[n][1] - k};
    int64_t ans = 0;
    for (int64_t x = 0; x <= n; ++x) {
        for (int64_t y = 0, z = n - x - y; x + y <= n; ++y, --z) {
            bool valid = true;
            for (auto idx = 0; idx < 2; ++idx) {
                valid &= a[x][idx] + a[y][idx] + a[z][idx] <= goal[idx];
            }
            ans += valid;
        }
    }

    return ans;
}

int main() {
    constexpr int32_t n = 200000;
    std::cout << solve(n) << '\n';

    return 0;
}
