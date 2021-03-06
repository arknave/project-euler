#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct modint {
    static constexpr int MOD = 1020202009;

    int v;
    modint(const int _v = 0): v(_v % MOD) {
        if (v < 0) v += MOD;
    }

    modint(const modint& other) {
        v = other.v;
    }

    bool operator==(const modint& other) const {
        return v == other.v;
    }

    modint& operator+=(const modint& other) {
        v += other.v;
        if (v >= MOD)
            v -= MOD;
        return *this;
    }

    modint& operator-=(const modint& other) {
        v -= other.v;
        if (v < 0)
            v += MOD;
        return *this;
    }

    modint& operator*=(const modint& other) {
        v = 1LL * v * other.v % MOD;
        return *this;
    }

    modint& operator/=(const modint& other) {
        *this *= other.inv();
        return *this;
    }

    modint operator+(const modint& other) const {
        return modint(v) += other;
    }

    modint operator-(const modint& other) const {
        return modint(v) -= other;
    }

    modint operator*(const modint& other) const {
        return modint(v) *= other;
    }

    modint operator/(const modint& other) const {
        return modint(v) /= other;
    }

    static modint pow(const modint& b, ll e) {
        if (e == 0) return 1;
        modint x = pow(b * b, e / 2);
        return (e % 2) ? b * x : x;
    }

    modint pow(ll e) const {
        return pow(*this, e);
    }

    modint inv() const {
        return pow(MOD - 2);
    }

    friend ostream& operator<<(ostream& os, modint m) {
        return os << m.v;
    }
};

constexpr int GOAL = 24680;
constexpr int MAXN = GOAL + 1;

modint fact[MAXN], tcaf[MAXN];

void gen_fact() {
    fact[0] = 1;
    for (int i = 1; i < MAXN; ++i) {
        fact[i] = fact[i - 1] * i;
    }

    tcaf[MAXN - 1] = modint(1) / fact[MAXN - 1];
    for (int i = MAXN - 2; i >= 0; --i) {
        tcaf[i] = tcaf[i + 1] * (i + 1);
    }
}

modint choose(int n, int k) {
    return fact[n] * tcaf[k] * tcaf[n - k];
}

modint dp[MAXN];

int main() {
    gen_fact();
    modint INV2 = modint(1) / 2;
    dp[0] = dp[1] = 1;
    for (int n = 1; n < GOAL; ++n) {
        modint& res = dp[n + 1];
        res = 0;
        for (int k = 0; k <= n; ++k) {
            res += choose(n, k) * dp[k] * dp[n - k];
        }

        res *= INV2;
    }

    cout << dp[GOAL] << '\n';
}
