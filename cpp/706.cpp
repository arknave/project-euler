#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

constexpr int MOD = 1e9 + 7;

// a - len
// b - suffixes == 0
// c - suffixes == 1
constexpr int MAXN = 100000;
int dp[MAXN + 1][3][3];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    for (int d = 1; d < 10; ++d) {
        dp[1][d % 3 == 0][d % 3 == 1]++;
    }

    for (int len = 1; len < MAXN; ++len) {
        for (int suf0 = 0; suf0 < 3; ++suf0) {
            for (int suf1 = 0; suf1 < 3; ++suf1) {
                int cur = dp[len][suf0][suf1];
                if (cur == 0) continue;

                int suf2 = (len + 6 - suf0 - suf1) % 3;

                for (int d = 0; d < 10; ++d) {
                    int new_len = len + 1;
                    int new_suf0, new_suf1;
                    int k = d % 3;
                    if (k == 0) {
                        new_suf0 = (suf0 + 1) % 3;
                        new_suf1 = suf1;
                    } else if (k == 1) {
                        new_suf0 = suf2;
                        new_suf1 = (suf0 + 1) % 3;
                    } else {
                        new_suf0 = suf1;
                        new_suf1 = suf2;
                    }

                    int& res = dp[new_len][new_suf0][new_suf1];
                    res += cur;
                    if (res >= MOD)
                        res -= MOD;
                }
            }
        }
    }

    int ans = 0;
    for (int suf0 = 0; suf0 < 3; ++suf0) {
        for (int suf1 = 0; suf1 < 3; ++suf1) {
            int suf2 = (MAXN + 6 - suf0 - suf1) % 3;
            int sub = (suf0 * (suf0 + 1)) * 2 + (suf1 * (suf1 - 1)) * 2 + (suf2 * (suf2 - 1)) * 2;
            if (sub % 3 == 0) {
                ans += dp[MAXN][suf0][suf1];
                if (ans >= MOD)
                    ans -= MOD;
            }
        }
    }

    cout << ans << '\n';

    return 0;
}
