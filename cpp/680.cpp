#include <bits/stdc++.h>

using namespace std;
using ll = long long;

struct state {
    ll l, r;
    bool is_rev;

    bool operator<(const state& other) const {
        return l < other.l;
    }
};

ll tot = 0LL;
void rev(set<state>& s, ll a, ll b) {
    // for each interval, flip the reverse tag
    // now to hash, consider the hash of the whole interval
    // add some prefix to it
    tot += abs(b - a) + 1;
}

int main() {
    ll n;
    int k;
    cin >> n >> k;

    set<state> s = {state{0, n - 1, false}};

    ll a = 1;
    ll b = 1;
    for (int op = 0; op < k; ++op) {
        rev(s, a, b);

        ll c = a + b;
        a = c >= n ? c - n : c;
        ll d = b + a;
        b = d >= n ? d - n : d;
    }

    cout << tot << '\n';

    return 0;
}
