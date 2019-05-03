#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    constexpr int M = 10000019;
    constexpr int exp = 32;
    vector<int> powers = {1};
    for (int i = 0; i <= exp; ++i) {
        powers.push_back(10LL * powers.back() % M);
    }

    int ans = 0;
    for (int len = 7; len <= exp; ++len) {
        cout << "len: " << len << '\n';
        int half = (len + 1) >> 1;
        vi coeffs(half);
        int s = 0;
        int e = len - 1;
        for (int i = 0; s <= e; ++i, ++s, --e) {
            coeffs[i] = powers[s];
            if (s != e)
                coeffs[i] += powers[e];

            if (coeffs[i] >= M)
                coeffs[i] -= M;
        }

        // dp[i][j] = how many ways can you get sum j using first i terms
        vector<vector<ll>> dp(half, vector<ll>(M, 0));
        {
            int v = coeffs[0];
            for (int x = 1; x <= 9; ++x) {
                dp[0][v] = 1;
                v += coeffs[0];
                if (v >= M)
                    v -= M;
            }
        }

        for (int i = 0; i + 1 < half; ++i) {
            for (int j = 0; j < M; ++j) {
                if (dp[i][j] == 0) continue;
                int jj = j;
                for (int k = 0; k < 10; ++k) {
                    dp[i + 1][jj] += dp[i][j];
                    jj += coeffs[i + 1];
                    if (jj >= M)
                        jj -= M;
                }
            }
        }

        ans += dp.back()[0];
    }

    cout << ans << '\n';
    return 0;
}
