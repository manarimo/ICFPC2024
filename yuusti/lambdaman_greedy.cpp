#include <iostream>
#include <vector>

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

void dfs(int cx, int cy) {
    if (cnt == 0) return;

    for (int d = 0; d < 4; ++d) {
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

    visited[cx][cy] = 1;
    dfs(cx, cy);

    for (int d: path) {
        cout << ds[d];
    }
    cout << endl;
}