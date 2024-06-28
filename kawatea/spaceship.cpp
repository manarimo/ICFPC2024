#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solve(int now, int next) {
    int diff = abs(next - now), c = 1;
    vector<int> ans;
    if (diff == 0) return ans;
    while ((c + 1) * (c + 1) <= diff) c++;
    diff -= c * c;
    for (int i = 0; i < c; i++) ans.push_back(1);
    for (int i = c; i > 0; i--) {
        while (diff >= i) {
            ans.push_back(0);
            diff -= i;
        }
        ans.push_back(-1);
    }
    if (now > next) {
        for (int i = 0; i < ans.size(); i++) ans[i] = -ans[i];
    }
    return ans;
}

int main() {
    vector<pair<int, int>> v;
    v.emplace_back(0, 0);
    while (true) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2) break;
        v.emplace_back(x, y);
    }
    
    vector<int> ans;
    for (int i = 0; i + 1 < v.size(); i++) {
        int x = v[i].first, y = v[i].second, nx = v[i + 1].first, ny = v[i + 1].second;
        vector<int> dx = solve(x, nx);
        vector<int> dy = solve(y, ny);
        while (dx.size() < dy.size()) dx.push_back(0);
        while (dx.size() > dy.size()) dy.push_back(0);
        for (int i = 0; i < dx.size(); i++) {
            int mv = 5;
            if (dx[i] == 1) {
                mv++;
            } else if (dx[i] == -1) {
                mv--;
            }
            if (dy[i] == 1) {
                mv += 3;
            } else if (dy[i] == -1) {
                mv -= 3;
            }
            ans.push_back(mv);
        }
    }
    
    if (ans.size() > 10000000) {
        puts("TOO LONG");
        exit(0);
    }
    
    for (int x : ans) printf("%d", x);
    puts("");
    
    return 0;
}
