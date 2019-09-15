#include <bits/stdc++.h>

using namespace std;
using ll = long long;

inline int lower(int mask) {
    return mask & ((1 << 6) - 1);
}

inline int upper(int mask) {
    return mask >> 6;
}

inline int make(int a, int b, int c, int d) {
    return (a << 6) | (b << 4) | (c << 2) | d;
}

const int A = 0b00;
const int E = 0b01;
const int F = 0b10;
const int R = 0b11;
int vals[] = {make(F, R, E, E), make(F, A, R, E), make(A, R, E, A), make(R, E, E, F)};

int main() {
    vector<ll> dp(1 << 10, 0);
    for (int i = 0; i < (1 << 6); ++i) {
        dp[i] = 1;
    }

    int n;
    cin >> n;
    for (int k = 4; k <= n; ++k) {
        vector<ll> ndp(1 << 10, 0);
        for (int m = 0; m < (1 << 10); ++m) {
            if (!dp[m]) continue;

            for (int v = 0; v < 4; ++v) {
                int val = lower(m) << 2 | v;
                int match = -1;
                for (int i = 0; i < 4; ++i) {
                    if (val == vals[i]) {
                        match = i;
                    }
                }

                if (match > -1) {
                    if (upper(m) & (1 << match)) {
                        // pass
                    } else {
                        int new_m = ((upper(m) | (1 << match)) << 6) | lower(val);
                        ndp[new_m] += dp[m];
                    }
                } else {
                    int new_m = (upper(m) << 6) | lower(val);
                    ndp[new_m] += dp[m];
                }
            }
        }

        swap(dp, ndp);
    }

    long long ans = 0;
    for (int i = 0; i < (1 << 6); ++i) {
        ans += dp[(0xf << 6) | i];
    }

    cout << ans << '\n';
    return 0;
}
