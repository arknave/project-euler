#include <cstdio>
#include <vector>

using namespace std;

using ll = long long;

constexpr int MAXN = 10000000;
constexpr int MAXP = 700000;
int sieve[MAXN + 1];
vector<int> primes;

vector<int> moves[MAXN + 1];
int vals[MAXP];

void gen_sieve() {
    primes.push_back(2);
    for (int i = 3; i <= MAXN; i += 2) {
        if (!sieve[i]) {
            primes.push_back(i);
            for (ll j = 1LL * i * i; j <= MAXN; j += 2 * i) {
                sieve[j] = i;
            }
        }
    }
}

int modpow(int b, int e, int m) {
    if (e == 0)
        return 1;
    if (e % 2 == 1)
        return 1LL * b * modpow(b, e - 1, m) % m;
    return modpow(1LL * b * b % m, e / 2, m);
}

int main() {
    gen_sieve();
    int m = primes.size();

    printf("m = %d\n", m);
    for (int i = 0; i < m; ++i) {
        vals[i] = 1;
        int p = primes[i];
        ll x = p;
        while (x <= MAXN) {
            for (int j = x; j <= MAXN; j += x) {
                moves[j].push_back(i);
            }

            x *= p;
        }
    }

    constexpr int MOD = 1e9 + 87;
    int res = 0;
    int cur = 1;
    for (int i = 2; i <= MAXN; ++i) {
        for (int idx : moves[i]) {
            cur = 1LL * cur * modpow(vals[idx], MOD - 2, MOD) % MOD;
            vals[idx] += 2;
            cur = 1LL * cur * vals[idx] % MOD;
        }

        res += cur;
        if (res >= MOD)
            res -= MOD;
    }

    printf("%d\n", res);
}
