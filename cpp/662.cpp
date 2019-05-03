#include <bits/stdc++.h>

using namespace std;

using pii = pair<int, int>;
using vi = vector<int>;

constexpr int MOD = 1e9 + 7;
constexpr int BOARD = 10000;
constexpr int CAP = 1.41421356 * BOARD + 10;

int main() {
    vector<int> fib = {1, 2};
    while (fib.back() < CAP) {
        fib.push_back(fib[fib.size() - 1] + fib[fib.size() - 2]);
    }
    cout << "Found " << fib.size() << " fibs\n";

    set<int> fib_set(begin(fib), end(fib));
    vector<pii> moves;
    for (int dx = 0; dx <= BOARD; ++dx) {
        for (int dy = dx; dy <= BOARD; ++dy) {
            int s = sqrt(dx * dx + dy * dy) + 0.5;
            if (1LL * s * s == 1LL * dx * dx + 1LL * dy * dy
                    and fib_set.count(s)) {
                moves.emplace_back(dx, dy);
                if (dx != dy)
                    moves.emplace_back(dy, dx);
            }
        }
    }

    cout << "Found " << moves.size() << " moves\n";

    vector<vi> dp(BOARD + 1, vi(BOARD + 1, 0));
    dp[0][0] = 1;
    for (int i = 0; i <= BOARD; ++i) {
        for (int j = 0; j <= BOARD; ++j) {
            if (dp[i][j] == 0) continue;
            for (auto& move : moves) {
                int nx = i + move.first;
                int ny = j + move.second;
                if (nx <= BOARD and ny <= BOARD) {
                    dp[nx][ny] += dp[i][j];
                    if (dp[nx][ny] >= MOD)
                        dp[nx][ny] -= MOD;
                }
            }
        }
    }

    cout << dp[BOARD][BOARD] << '\n';

    return 0;
}
