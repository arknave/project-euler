#include <bits/stdc++.h>

using namespace std;

using ll = long long;
constexpr int N = 1e8;

int sieve[N];

int main() {
    int ans = 0;
    for (int i = 2; i < N; ++i) {
        if (sieve[i] == 2) {
            ++ans;
        } else if (sieve[i] == 0) {
            for (ll x = i; x < N; x *= i) {
                for (int j = x; j < N; j += x) {
                    ++sieve[j];
                }
            }
        }
    }

    cout << ans << '\n';
}
