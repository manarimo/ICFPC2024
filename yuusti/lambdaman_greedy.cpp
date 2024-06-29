#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

string ds = "RDLU";

const int N = 5000;
string board[N];
int visited[N][N];
int h, w;

vector<int> path;
int cnt;

vector<int> ord;

void dfs(int cx, int cy) {
    if (cnt == 0) return;

    for (int dd = 0; dd < 4; ++dd) {
        int d = ord[dd];
        int nx = cx + dx[d];
        int ny = cy + dy[d];
        if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
        if (board[nx][ny] == '#') continue;
        if (visited[nx][ny]) continue;
        visited[nx][ny] = 1;
        --cnt;
        path.push_back(d);
        dfs(nx, ny);
        if (cnt > 0) {
            path.push_back((d + 2) % 4);
        }
    }
}

int main() {
    string s;
    int i = 0;
    while (cin >> s) {
        board[i++] = s;
    }

    h = i;
    w = s.size();

    cerr << h <<  ' ' << w << endl;

    int cx, cy;
    for (int x = 0; x < h; ++x) {
        for (int y = 0; y < w; ++y) {
            if (board[x][y] == 'L') {
                cx = x, cy = y;
            }
            if (board[x][y] == '.') {
                ++cnt;
            }
        }
    }

    int ccnt = cnt;
    vector<int> best_path;
    for (int i = 0; i < 4; ++i) ord.push_back(i);

    vector<int> first;

    do {
        cnt = ccnt;
        path.clear();
        for (int i = 0; i < h; ++i) for (int j = 0; j < w; ++j) visited[i][j] = 0;

        visited[cx][cy] = 1;
        dfs(cx, cy);

        if (best_path.size() == 0 || path.size() < best_path.size()) {
            best_path = path;
        }

        if (first.empty()) {
            first = path;
        }
    } while(next_permutation(ord.begin(), ord.end()));

    cerr << "first: " << first.size() << endl;
    cerr << "best:" << best_path.size() << endl;

    for (int d: best_path) {
        cout << ds[d];
    }
    cout << endl;

}