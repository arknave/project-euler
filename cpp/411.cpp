#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

std::vector<int64_t> gen(int64_t n) {
    using A2 = std::array<int64_t, 2>;
    std::vector<A2> res;
    res.reserve(n + n + 1);
    {
        int64_t x = 1;
        int64_t y = 1;
        for (int64_t i = 0; i <= n + n; ++i) {
            res.push_back({x % n, y % n});
            x = x * 2 % n;
            y = y * 3 % n;
        }
    }

    std::sort(res.begin(), res.end());
    res.erase(std::unique(res.begin(), res.end()), res.end());

    std::vector<int64_t> pts;
    pts.reserve(res.size());

    for (auto [x, y] : res) {
        pts.push_back(y);
    }

    return pts;
}

int64_t solve(const std::vector<int64_t>& pts) {
    // find the LNDS
    std::vector<int64_t> tmp;
    for (auto x : pts) {
        auto it = std::upper_bound(tmp.begin(), tmp.end(), x);
        if (it == tmp.end()) {
            tmp.push_back(x);
        } else {
            *it = x;
        }
    }

    return tmp.size();
}

int main() {
    assert(solve(gen(22)) == 5);
    assert(solve(gen(123)) == 14);
    assert(solve(gen(10000)) == 48);

    int64_t ans = 0;
    for (int64_t k = 1; k <= 30; ++k) {
        ans += solve(gen(k * k * k * k * k));
    }

    std::cout << ans << '\n';

    return 0;
}
