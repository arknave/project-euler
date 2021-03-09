#include <cstdint>
#include <iostream>
#include <vector>

std::vector<int32_t> gen_hand(int n) {
    std::vector<int32_t> hand = {3};
    while (hand.size() < n) {
        int32_t card = hand.back() * 3LL % (n + 1);
        hand.push_back(card);
    }

    return hand;
}

int main() {
    int32_t n;
    std::cin >> n;

    std::vector<int32_t> hand = gen_hand(n);
    std::vector<int32_t> pos(n);
    for (int32_t i = 0; i < n; ++i) {
        pos[--hand[i]] = i;
    }

    auto drag = [&pos](int i, int j) {
        return std::abs(pos[i] - pos[j]);
    };

    constexpr int32_t INF = 0x3f3f3f3f;
    std::vector<std::vector<int32_t>> dp(n, std::vector<int32_t>(n, INF));
    for (int32_t i = 0; i < n; ++i) {
        dp[i][i] = 0;
    }

    for (int s = 2; s <= n; ++s) {
        for (int i = 0; i + s <= n; ++i) {
            int j = i + s - 1;
            for (int k = i; k < j; ++k) {
                dp[i][j] = std::min(dp[i][j], dp[i][k] + dp[k + 1][j] + drag(k, j));
            }
        }
    }

    std::cout << dp[0][n - 1] << std::endl;

    return 0;
}
