#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <random>
#include <algorithm>

using namespace std;

const int ddx[10] = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
const int ddy[10] = {0, -1, -1, -1, 0, 0, 0, 1, 1, 1};
vector<pair<int, int>> v;
int now, px, py, dx, dy;
map<int, int> memo;
map<int, int> memo2[256];

int calc(int now, int next) {
    int diff = abs(next - now), d = diff, c = 1, ans = 0;
    if (d == 0) return ans;
    if (memo.count(d)) return memo[d];
    c = sqrt(d);
    while ((c + 1) * (c + 1) <= diff) c++;
    diff -= c * c;
    ans += c * 2;
    ans += (diff + c - 1) / c;
    return memo[d] = ans;
}

int calc2(int sx, int tx, int dx) {
    int diff = tx - sx, ans = 0;
    if (diff < 0) {
        diff = -diff;
        dx = -dx;
    }
    if (dx < 0) {
        dx = -dx;
        ans += dx;
        diff += dx * (dx + 1) / 2;
        dx = 0;
    }
    if (memo2[dx].count(diff)) return ans + memo2[dx][diff];
    if (dx == 0) {
        int t = sqrt(diff);
        while (t * (t + 1) / 2 < diff) t++;
        return memo2[dx][diff] = ans + t;
    } else if (dx > diff + 1) {
        return memo2[dx][diff] = ans + 1 + calc2(dx - 1, diff, dx - 1);
    } else if (dx == diff + 1) {
        return memo2[dx][diff] = ans + 1;
    } else if (dx == diff) {
        return memo2[dx][diff] = ans;
    } else {
        int l = 0, r = diff / dx + 2;
        while (r - l > 1) {
            long long m = (l + r) / 2;
            if (dx * m + m * (m + 1) / 2 < diff) {
                l = m;
            } else {
                r = m;
            }
        }
        return memo2[dx][diff] = ans + l;
    }
}

namespace beam_search {
    using node_type = int;
    using operation_type = int;
    using score_type = unsigned long long;
    using hash_type = unsigned;
    constexpr static size_t MAX_TURN = 3000;
    constexpr static size_t BEAM_WIDTH = 1000;
    constexpr static size_t MAX_CANDIDATE = BEAM_WIDTH * 10;
    constexpr static size_t POOL_SIZE = MAX_TURN * BEAM_WIDTH + MAX_CANDIDATE;
    constexpr static int HASH_WIDTH = 26;
    constexpr static score_type TURN_SCORE = 1e5;
    constexpr static score_type FINISH_SCORE = 1e18;
    
    namespace duplicate {
        score_type data[1 << HASH_WIDTH];
        
        inline void clear() {
            for (int i = 0; i < (1 << HASH_WIDTH); i++) data[i] = 0;
        }
        
        inline bool add(hash_type hash, score_type score) {
            if (data[hash] >= score) return false;
            data[hash] = score;
            return true;
        }
        
        inline bool valid(hash_type hash, score_type score) {
            return data[hash] == score;
        }
    }
    
    namespace operation {
        inline void try_apply(operation_type& operation, score_type& score, hash_type& hash, int turn) {
            int mv = (operation & 0xF), ndx = dx + ddx[mv], ndy = dy + ddy[mv], nx = px + ndx, ny = py + ndy, next = now;
            if (nx == v[next + 1].first && ny == v[next + 1].second) {
                next++;
                operation |= (1 << 4);
            }
            hash = ((next & 0x3) << 24) | ((ndx & 0x3F) << 18) | ((ndy & 0x3F) << 12) | ((nx & 0x3F) << 6) | (ny & 0x3F);
            score = TURN_SCORE * (turn + 1) + next * 100;
            if (next + 1 == v.size()) {
                score += FINISH_SCORE;
            } else {
                //score -= max(calc(nx, v[next + 1].first), calc(ny, v[next + 1].second));
                score -= max(calc2(nx, v[next + 1].first, ndx), calc2(ny, v[next + 1].second, ndy));
            }
        }
        
        inline void apply(operation_type operation) {
            int add = (operation >> 4), mv = (operation & 0xF);
            if (add) now++;
            dx += ddx[mv];
            dy += ddy[mv];
            px += dx;
            py += dy;
        }
        
        inline void revert(operation_type operation) {
            int add = (operation >> 4), mv = (operation & 0xF);
            if (add) now--;
            px -= dx;
            py -= dy;
            dx -= ddx[mv];
            dy -= ddy[mv];
        }
    }
    
    namespace node {
        constexpr static node_type EMPTY = -1;
        node_type next_node;
        node_type* parent;
        node_type* child;
        node_type* prev;
        node_type* next;
        operation_type* operation;
        score_type* score;
        hash_type* hash;
        
        inline void init(bool first) {
            if (first) {
                node::parent = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
                node::child = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
                node::prev = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
                node::next = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
                node::operation = (operation_type*)malloc(sizeof(operation_type) * POOL_SIZE);
                node::score = (score_type*)malloc(sizeof(score_type) * POOL_SIZE);
                node::hash = (hash_type*)malloc(sizeof(hash_type) * POOL_SIZE);
            }
            next_node = 0;
            for (size_t i = 1; i < POOL_SIZE; i++) parent[i - 1] = i;
        }
        
        inline void init_node(node_type n) {
            parent[n] = child[n] = prev[n] = next[n] = EMPTY;
            score[n] = 100000;
            hash[n] = 0;
            now = px = py = dx = dy = 0;
        }
        
        inline node_type get_node() {
            node_type n = next_node;
            next_node = parent[n];
            return n;
        }
        
        inline void return_node(node_type n) {
            parent[n] = next_node;
            next_node = n;
        }
        
        inline void add_node(node_type n) {
            child[n] = prev[n] = EMPTY;
            next[n] = child[parent[n]];
            child[parent[n]] = n;
            if (next[n] != EMPTY) prev[next[n]] = n;
        }
        
        inline void delete_node(node_type n) {
            while (prev[n] == EMPTY && next[n] == EMPTY) {
                node_type next = parent[n];
                return_node(n);
                n = next;
            }
            if (prev[n] == EMPTY) {
                child[parent[n]] = next[n];
            } else {
                next[prev[n]] = next[n];
            }
            if (next[n] != EMPTY) prev[next[n]] = prev[n];
            return_node(n);
        }
        
        inline void add_candidates(node_type*& candidates, node_type now, int turn) {
            for (int i = 1; i <= 9; i++) {
                int ndx = dx + ddx[i], ndy = dy + ddy[i];
                if (abs(ndx) > 128 || abs(ndy) > 128) continue;
                operation_type op = i;
                score_type next_score = score[now];
                hash_type next_hash = hash[now];
                operation::try_apply(op, next_score, next_hash, turn);
                if (duplicate::add(next_hash, next_score)) {
                    node_type candidate = get_node();
                    parent[candidate] = now;
                    operation[candidate] = op;
                    score[candidate] = next_score;
                    hash[candidate] = next_hash;
                    *candidates++ = candidate;
                }
            }
        }
    }
    
    vector<operation_type> construct_results(node_type top) {
        vector<operation_type> ans;
        while (node::parent[top] != node::EMPTY) {
            ans.push_back(node::operation[top] & 0xF);
            top = node::parent[top];
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
    
    vector<operation_type> search(bool first) {
        node::init(first);
        duplicate::clear();
        node_type top = node::get_node();
        node::init_node(top);
        
        node_type* candidates = (node_type*)malloc(sizeof(node_type) * (MAX_CANDIDATE * 2));
        node_type* leaves = candidates + MAX_CANDIDATE;
        node_type* leaves_end = leaves;
        node_type* origin = candidates;
        score_type best_score = 0;
        for (int turn = 0; turn < MAX_TURN; turn++) {
            while (node::child[top] != node::EMPTY && node::next[node::child[top]] == node::EMPTY) {
                top = node::child[top];
                operation::apply(node::operation[top]);
            }
            
            node_type* candidates_end = candidates;
            node_type now = top;
            do {
                while (node::child[now] != node::EMPTY) {
                    now = node::child[now];
                    operation::apply(node::operation[now]);
                }
                
                node::add_candidates(candidates_end, now, turn);
                
                while (now != top) {
                    operation::revert(node::operation[now]);
                    if (node::next[now] == node::EMPTY) {
                        now = node::parent[now];
                    } else {
                        now = node::next[now];
                        operation::apply(node::operation[now]);
                        break;
                    }
                }
            } while (now != top);

            for (node_type* n = candidates; n != candidates_end; n++) {
                if (!duplicate::valid(node::hash[*n], node::score[*n])) {
                    node::return_node(*n);
                    *n-- = *--candidates_end;
                }
            }
            
            if (candidates_end - candidates > BEAM_WIDTH) {
                nth_element(candidates, candidates + BEAM_WIDTH, candidates_end, [&](const node_type n1, const node_type n2) {
                    return node::score[n1] > node::score[n2];
                });
                for (node_type* n = candidates + BEAM_WIDTH; n != candidates_end; n++) node::return_node(*n);
                candidates_end = candidates + BEAM_WIDTH;
            }
            if (candidates == candidates_end) break;
            
            for (node_type* n = candidates; n != candidates_end; n++) {
                if (node::score[*n] >= FINISH_SCORE) {
                    vector<operation_type> ans = construct_results(*n);
                    free(origin);
                    return ans;
                } else {
                    node::add_node(*n);
                }
            }
            for (node_type* n = leaves; n != leaves_end; n++) {
                if (node::child[*n] == node::EMPTY) node::delete_node(*n);
            }
            swap(candidates, leaves);
            leaves_end = candidates_end;
        }
        
        free(origin);
        return vector<operation_type>();
    }
}

class timer {
    public:
    void start() {
        origin = rdtsc();
    }
    
    inline double get_time() {
        return (rdtsc() - origin) * SECONDS_PER_CLOCK;
    }
    
    private:
    constexpr static double SECONDS_PER_CLOCK = 1 / 2.9e9;
    unsigned long long origin;
    
    inline static unsigned long long rdtsc() {
        unsigned long long lo, hi;
        __asm__ volatile ("rdtsc" : "=a" (lo), "=d" (hi));
        return (hi << 32) | lo;
    }
};

class random {
    public:
    // [0, x)
    inline static unsigned get(unsigned x) {
        return ((unsigned long long)xorshift() * x) >> 32;
    }
    
    // [x, y]
    inline static unsigned get(unsigned x, unsigned y) {
        return get(y - x + 1) + x;
    }
    
    // [0, x] (x = 2^c - 1)
    inline static unsigned get_fast(unsigned x) {
        return xorshift() & x;
    }
    
    // [0.0, 1.0]
    inline static double probability() {
        return xorshift() * INV_MAX;
    }
    
    inline static bool toss() {
        return xorshift() & 1;
    }
    
    private:
    constexpr static double INV_MAX = 1.0 / 0xFFFFFFFF;
    
    inline static unsigned xorshift() {
        static unsigned x = 123456789, y = 362436039, z = 521288629, w = 88675123;
        unsigned t = x ^ (x << 11);
        x = y, y = z, z = w;
        return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
    }
};

class simulated_annealing {
    public:
    simulated_annealing();
    inline bool end();
    inline bool accept(double current_score, double next_score);
    void print() const;
    
    private:
    constexpr static bool MAXIMIZE = false;
    constexpr static int LOG_SIZE = 0x10000;
    constexpr static int UPDATE_INTERVAL = 0xF;
    constexpr static double TIME_LIMIT = 1.95 * 1000;
    constexpr static double START_TEMP = 0.75;
    constexpr static double END_TEMP = 1e-9;
    constexpr static double TEMP_RATIO = (END_TEMP - START_TEMP) / TIME_LIMIT;
    double log_probability[LOG_SIZE];
    long long iteration = 0;
    long long accepted = 0;
    long long rejected = 0;
    double time = 0;
    double temp = START_TEMP;
    timer sa_timer;
};

simulated_annealing::simulated_annealing() {
    sa_timer.start();
    double inv = 1.0 / LOG_SIZE;
    for (int i = 0; i < LOG_SIZE; i++) log_probability[i] = log((i + 0.5) * inv);
    mt19937 engine;
    shuffle(log_probability, log_probability + LOG_SIZE, engine);
}

inline bool simulated_annealing::end() {
    iteration++;
    if ((iteration & UPDATE_INTERVAL) == 0) {
        time = sa_timer.get_time();
        temp = START_TEMP + TEMP_RATIO * time;
        return time >= TIME_LIMIT;
    } else {
        return false;
    }
}

inline bool simulated_annealing::accept(double current_score, double next_score) {
    double diff = (MAXIMIZE ? next_score - current_score : current_score - next_score);
    static unsigned short index = 0;
    if (diff >= 0 || diff > log_probability[index++] * temp) {
        accepted++;
        return true;
    } else {
        rejected++;
        return false;
    }
}

void simulated_annealing::print() const {
    fprintf(stderr, "iteration: %lld\n", iteration);
    fprintf(stderr, "accepted: %lld\n", accepted);
    fprintf(stderr, "rejected: %lld\n", rejected);
}

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

bool far(int x, int y, int z) {
    int d1 = max(calc2(v[x].first, v[y].first, 0), calc2(v[x].second, v[y].second, 0));
    int d2 = max(calc2(v[x].first, v[z].first, 0), calc2(v[x].second, v[z].second, 0));
    return d2 >= d1 * 5;
}

int main() {
    while (true) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2) break;
        if (x == 0 && y == 0) continue;
        v.emplace_back(x, y);
    }
    v.insert(v.begin(), make_pair(0, 0));
    
    random_device rng;
    int r = rng() % 65536;
    for (int i = 0; i < r; i++) random::toss();
    
    bool updated = false;
    vector<int> ans = beam_search::search(true);
    vector<int> best_ans = ans;
    vector<pair<int, int>> best_v = v;
    int start = 1, end = v.size() - 1;
    simulated_annealing sa;
    while (!sa.end()) {
        int select = random::get(100), p1, p2;
        vector<pair<int, int>> w = v;
        while (true) {
            p1 = random::get(start, end);
            p2 = random::get(start, end);
            if ((p1 == start && p2 == end) || (p1 == end && p2 == start)) continue;
            if (p1 != p2) break;
        }
        if (select < 10) {
            if (p1 < p2) {
                if (p2 < end && far(p2, p2 + 1, p1)) continue;
            } else {
                if (far(p2 - 1, p2, p1)) continue;
            }
            w.erase(w.begin() + p1);
            w.insert(w.begin() + p2, v[p1]);
        } else if (select < 70) {
            if (p1 > p2) swap(p1, p2);
            int p3;
            while (true) {
                p3 = random::get(start, min(end, (int)v.size() - (p2 - p1 + 1)));
                if (p1 != p3) break;
            }
            if (p3 < p1) {
                if (far(p3, p3 + 1, p1) || far(p3, p3 + 1, p2)) continue;
            } else {
                int p = p3 + p2 - p1 + 1;
                if (p != v.size() && (far(p, p + 1, p1) || far(p, p + 1, p2))) continue;
            }
            w.erase(w.begin() + p1, w.begin() + p2 + 1);
            w.insert(w.begin() + p3, v.begin() + p1, v.begin() + p2 + 1);
        } else {
            if (p1 > p2) swap(p1, p2);
            if (far(p1 - 1, p1, p2) || (p2 + 1 < w.size() && far(p2, p2 + 1, p1))) continue;
            reverse(w.begin() + p1, w.begin() + p2 + 1);
        }
        v.swap(w);
        vector<int> new_ans = beam_search::search(false);
        v.swap(w);
        if (new_ans.empty()) continue;
        if (sa.accept(ans.size(), new_ans.size())) {
            fprintf(stderr, "%d %d\n", ans.size(), new_ans.size());
            v = w;
            ans = new_ans;
            if (ans.size() < best_ans.size()) {
                updated = true;
                best_ans = ans;
                best_v = v;
            }
        }
    }
    sa.print();
    ans = best_ans;
    
    int x = 0, y = 0, dx = 0, dy = 0;
    set<pair<int, int>> s;
    for (int i = 1; i < v.size(); i++) s.insert(v[i]);
    for (int mv : ans) {
        dx += ddx[mv];
        dy += ddy[mv];
        x += dx;
        y += dy;
        s.erase(make_pair(x, y));
    }
    
    if (!s.empty()) {
        fprintf(stderr, "ERROR\n");
        exit(0);
        while (dx != 0 || dy != 0) {
            int mv = 5;
            if (dx > 0) {
                dx--;
                mv--;
            } else if (dx < 0) {
                dx++;
                mv++;
            }
            if (dy > 0) {
                dy--;
                mv -= 3;
            } else if (dy < 0) {
                dy++;
                mv += 3;
            }
            x += dx;
            y += dy;
            s.erase(make_pair(x, y));
            ans.push_back(mv);
        }
        
        vector<pair<int, int>> w;
        for (const pair<int, int>& p : s) w.push_back(p);
        w.insert(w.begin(), make_pair(x, y));
        for (int i = 0; i + 1 < w.size(); i++) {
            int x = w[i].first, y = w[i].second, nx = w[i + 1].first, ny = w[i + 1].second;
            vector<int> dx = solve(x, nx);
            vector<int> dy = solve(y, ny);
            while (dx.size() < dy.size()) dx.push_back(0);
            while (dx.size() > dy.size()) dy.push_back(0);
            for (int k = 0; k < dx.size(); k++) {
                int mv = 5;
                if (dx[k] == 1) {
                    mv++;
                } else if (dx[k] == -1) {
                    mv--;
                }
                if (dy[k] == 1) {
                    mv += 3;
                } else if (dy[k] == -1) {
                    mv -= 3;
                }
                ans.push_back(mv);
            }
        }
    }
    
    for (int x : ans) printf("%d", x);
    puts("");
    
    fprintf(stderr, "size:%d\n", ans.size());
    
    if (updated) {
        for (const pair<int, int>& p : best_v) fprintf(stderr, "%d %d\n", p.first, p.second);
    }
    
    return 0;
}
