#include <bits/stdc++.h>

template <typename T>
struct Point {
    T x;
    T y;

    Point(T x={}, T y={}): x(x), y(y) {}

    using P = Point;

    bool operator<(P o) const {
        return std::tie(x, y) < std::tie(o.x, o.y);
    }

    bool operator==(P o) const {
        return (x == o.x) & (y == o.y);
    }

    P& operator+=(P other) {
        x += other.x;
        y += other.y;
        return *this;
    }

    P operator+(P other) const {
        return P{*this} += other;
    }

    P& operator-=(P other) {
        x -= other.x;
        y -= other.y;
        return *this;
    }

    P operator-(P other) const {
        return P{*this} -= other;
    }

    T dot(P other) const {
        return x * other.x + y * other.y;
    }

    T cross(P other) const {
        return x * other.y - y * other.x;
    }

    // Computes the cross product of a and b relative to this.
    T cross(P a, P b) const {
        return (a - *this).cross(b - *this);
    }

    double dist() const {
        return std::sqrt(static_cast<double>(dist2()));
    }

    T dist2() const {
        return dot(*this);
    }

    friend std::istream& operator>>(std::istream& is, P& pt) {
        return is >> pt.x >> pt.y;
    }

    friend std::ostream& operator<<(std::ostream& os, const P& pt) {
        return os << "(" << pt.x << ", " << pt.y << ")";
    }
};

using P = Point<double>;
std::pair<P, P> closestPair(std::vector<P> points) {
    std::sort(points.begin(), points.end(), [](const P& a, const P& b) { return a.y < b.y; });
    std::set<P> active;
    int32_t n = points.size();

    constexpr double INF = std::numeric_limits<double>::infinity();
    double ans = INF;
    std::pair<P, P> ret = std::pair{P{}, P{}};
    for (int32_t i = 0, j = 0; i < n; ++i) {
        auto sqrtAns = 1.0 + std::sqrt(ans);
        const P& a = points[i];
        while (a.y - points[j].y >= sqrtAns) {
            active.erase(points[j++]);
        }

        for (auto it = active.lower_bound(P{a.x - sqrtAns, a.y});
                  it != active.end() && it->x <= a.x + sqrtAns;
                  ++it) {
            double curDist = (a - *it).dist2();
            if (curDist < ans) {
                ans = curDist;
                ret = {*it, a};
            }
        }

        active.insert(a);
    }

    return ret;
}
 
int64_t nxt() {
    static constexpr int64_t MOD = 50515093;
    static int64_t s = 290797;

    int64_t res = s;
    s = s * s % MOD;

    return res;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout << std::fixed << std::setprecision(20);

    int32_t n;
    while (std::cin >> n) {
        if (!n) break;
        std::vector<P> points;
        points.reserve(n);
        for (int32_t i = 0; i < n; ++i) {
            int64_t x = nxt();
            int64_t y = nxt();

            points.emplace_back(x, y);
        }

        auto [p1, p2] = closestPair(points);

        std::cout << p1.x << ' ' << p1.y << ' ' << p2.x << ' ' << p2.y << '\n';
        std::cout << (p1 - p2).dist() << '\n';
    }

    return 0;
}
