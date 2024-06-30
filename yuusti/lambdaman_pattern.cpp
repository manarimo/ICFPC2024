#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

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

bool check_dfs(int cx, int cy) {
    for (int d = 0; d < 4; ++d) {
        int nx = cx + dx[d];
        int ny = cy + dy[d];
        if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
        if (board[nx][ny] != '#') return true;
        if (visited[nx][ny]) continue;
        visited[nx][ny] = 1;

        if (check_dfs(nx, ny)) return true;
    }

    return false;
}

bool check() {
    int cnt = 0;
    queue<pair<int, int>> q;
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (board[i][j] == '#' && !visited[i][j]) {
                if(!check_dfs(i, j)) ++cnt;
            }
        }
    }

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            visited[i][j] = 0;
        }
    }

    int space = 0;
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            int wallcnt = 9;
            for (int dx = -1; dx <= 1; ++dx) {
                for (int dy = -1; dy <= 1; ++dy) {
                    int nx = i + dx;
                    int ny = j + dy;
                    if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
                    if (board[nx][ny] == '#') continue;
                    wallcnt--;
                }
            } 
            if (wallcnt == 0) ++space;
        }
    }

    return cnt == 0 && space == 0;
}

pair<int, int> try_move(int cx, int cy, int d) {
    int nx = cx + dx[d];
    int ny = cy + dy[d];
    
    if (nx < 0 || nx >= h || ny < 0 || ny >= w) return make_pair(cx, cy);
    if (board[nx][ny] == '#') return make_pair(cx, cy);

    return make_pair(nx, ny);
}

int count_visited() {
    int cnt = 0;
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (board[i][j] != '.') continue;
            if (visited[i][j]) ++cnt;
        }
    }

    return cnt;
}

void print(int cx = -1, int cy = -1) {
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (i == cx && j == cy) cout << "L";
            else if (board[i][j] == '#') cout << board[i][j];
            else cout << (visited[i][j]?"*":".");
        }
        cout << endl;
    }
    cout << endl;
}

pair<int, int> pos[1000000];
pair<int, int> pattern(int cx, int cy, int d, int step, vector<int> &pt, int pi) {
    if (pos[pi] == make_pair(cx, cy)) {
        cout << "end: " << cx << ' ' << cy << endl;
        cout << "pi = " << pi << endl;
        return make_pair(cx, cy);
    }
    pos[pi] = make_pair(cx, cy);

    if (step <= 0) return make_pair(cx, cy);
    visited[cx][cy] = 1;
    int nd = pt[pi];
    auto p = try_move(cx, cy, nd % 4);
    if (p.first != cx || p.second != cy) {
        cx = p.first;
        cy = p.second;
    }


    return pattern(cx, cy, d, step - 1, pt, (pi + 1) % pt.size());
}

void clear_visited() {
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            visited[i][j] = 0;
        }
    }
    for (int i = 0; i < 1000; ++i) {
        pos[i] = make_pair(-1, -1);
    }
}

int main(int argc, char **argv) {
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
    cerr << cnt << endl;

    // cerr << "count(.)=" << cnt << endl;
    // cerr << "check=" << check() << endl;

    clear_visited();
    
    string pattern_str;
    ifstream f(argv[1]);
    f >> pattern_str;

    vector<int> pt;
    for (char c: pattern_str) {
        for (int i = 0; i < 4; ++i) {
            if (c == ds[i]) pt.push_back(i);
        }
    }
    visited[cx][cy] = 1;
    auto p = pattern(cx, cy, 0, pattern_str.size(), pt, 0);
    int score = count_visited();
    // for (auto e : pt) {
    //     cout << e << " ";
    // }
    cout << score << "/" << cnt << endl;
    print(p.first, p.second);

    // cerr << "path size: " << path.size() << endl;

    // string ans;
    // for (int d: path) {
    //     ans += ds[d];
    // }
    // cout << ans << endl;
}
