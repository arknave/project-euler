// warning: o(p^2) where p is 6M. Takes over an hour to run...
#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

constexpr int MAXN = 6000000;
// constexpr int MAXN = 600000;
int sieve[MAXN + 1];
vector<int> primes;

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

int64_t faster(int64_t p) {
    // couple of notes:
    // if x mod p is a cube, then -x mod p is a cube
    // therefore if x + y = z mod p where all are cubes,
    // then also y + x = z and z - y = x are valid statements
    // by experiment, all cubes appear in statemnets an equal number of times
    // therefore, just find number of cubes that are 1 apart and do some multiplications
    vector<char> valid(p, false);
    valid[1] = true;
    valid[p - 1] = true;
    int rem = (p - 1) / 6;
    --rem;
    for (int64_t i = 2; rem > 0 && i < p; ++i) {
        int64_t j = i * i % p * i % p;
        if (!valid[j])
            --rem;
        valid[j] = valid[p - j] = true;
    }

    int64_t cur = 0;
    for (int64_t i = 1; i + 1 < p; ++i) {
        cur += valid[i] & valid[i + 1];
    }

    return cur;
}

int64_t brute(int64_t p) {
    vector<int64_t> freq(p, 0);
    for (int64_t i = 1; i < p; ++i) {
        int64_t j = 1LL * i * i % p * i % p;
        ++freq[j];
    }

    vector<int32_t> occ(p, 0);
    int64_t res = 0;
    for (int64_t i = 1; i < p; ++i) {
        if (!freq[i]) continue;
        for (int64_t j = 1; j < p; ++j) {
            if (!freq[j]) continue;

            // int64_t ways = i == j ? 1 : 2;
            int64_t s = i + j;
            if (s >= p) s -= p;
            if (freq[i] && freq[j] && freq[s]) {
                // cout << i << " " << j << " " << s << endl;
                occ[s] += freq[s];
                occ[i] += freq[i];
                occ[j] += freq[j];
            }
            res += freq[s] * freq[i] * freq[j];
        }
    }
    
    return res;
}

int main() {
    gen_sieve();

    int64_t ans = 0;
    for (int p : primes) {
        int64_t cur;
        if (p < 5) {
            cur = brute(p);
        } else if (p % 3 == 1) {
            /*
            cur = brute(p);
            cout << "tests: " << 27 * 2 * terms << " " << 27 * 3 * terms << " " << cur << endl;
            cout << "scale: " << terms << " " << cur / 27 / terms << '\n';
            cout << "faster: " << faster(p) << endl;
            */

            int64_t ff = faster(p);
            int64_t terms = (p - 1) / 3;
            cur = 27LL * ff * terms;

            // assert(cur == brute(p));
        } else {
            cur = 1LL * (p - 1) * (p - 2);
        }

        // cout << p << " " << cur << '\n' << '\n';
        // assert(cur == brute(p));
        ans += cur;
    }

    cout << ans << endl;
}
