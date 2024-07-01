#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <immintrin.h>

using namespace std;

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

template<class DIST_TYPE = int> class tsp {
    public:
    static void init() {
        uint8_t a[64];
        #if defined(__AVX512VBMI__)
        for (int i = 0; i < 63; i++) {
            int c = 0;
            for (int j = 63 - i; j >= 0; j--) a[c++] = j;
            for (int j = 64 - i; j < 64; j++) a[c++] = j;
            index512_8.push_back(_mm512_loadu_si512(reinterpret_cast<__m512i*>(a)));
        }
        for (int i = 0; i < 31; i++) {
            int c = 0;
            for (int j = 31 - i; j >= 0; j--) a[c++] = j * 2, a[c++] = j * 2 + 1;
            for (int j = 32 - i; j < 32; j++) a[c++] = j * 2, a[c++] = j * 2 + 1;
            index512_16.push_back(_mm512_loadu_si512(reinterpret_cast<__m512i*>(a)));
        }
        #elif defined(__AVX512VL__)
        for (int i = 0; i < 31; i++) {
            int c = 0;
            for (int j = 31 - i; j >= 0; j--) a[c++] = j;
            for (int j = 32 - i; j < 32; j++) a[c++] = j;
            index256_8.push_back(_mm256_loadu_si256(reinterpret_cast<__m256i*>(a)));
        }
        for (int i = 0; i < 15; i++) {
            int c = 0;
            for (int j = 15 - i; j >= 0; j--) a[c++] = j * 2, a[c++] = j * 2 + 1;
            for (int j = 16 - i; j < 16; j++) a[c++] = j * 2, a[c++] = j * 2 + 1;
            index256_16.push_back(_mm256_loadu_si256(reinterpret_cast<__m256i*>(a)));
        }
        #elif defined(__SSSE3__)
        for (int i = 0; i < 15; i++) {
            int c = 0;
            for (int j = 15 - i; j >= 0; j--) a[c++] = j;
            for (int j = 16 - i; j < 16; j++) a[c++] = j;
            index128_8.push_back(_mm_loadu_si128(reinterpret_cast<__m128i*>(a)));
        }
        for (int i = 0; i < 7; i++) {
            int c = 0;
            for (int j = 7 - i; j >= 0; j--) a[c++] = j * 2, a[c++] = j * 2 + 1;
            for (int j = 8 - i; j < 8; j++) a[c++] = j * 2, a[c++] = j * 2 + 1;
            index128_16.push_back(_mm_loadu_si128(reinterpret_cast<__m128i*>(a)));
        }
        #endif
    }
    
    static vector<int> calc(const vector<vector<DIST_TYPE>>& dist, double time_limit, int start = 0) {
        if (dist.size() < 256) {
            return calc_inner<uint8_t>(dist, time_limit, start);
        } else {
            return calc_inner<uint16_t>(dist, time_limit, start);
        }
    }
    
    static vector<int> calc_path(const vector<vector<DIST_TYPE>>& dist, double time_limit, int start = -1) {
        int n = dist.size();
        vector<vector<DIST_TYPE>> new_dist(n + 1, vector<DIST_TYPE>(n + 1, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) new_dist[i][j] = dist[i][j];
        }
        if (start >= 0) {
            for (int i = 0; i < n; i++) {
                if (i != start) new_dist[i][n] = new_dist[n][i] = INF;
            }
        }
        vector<int> order = calc(new_dist, time_limit, n);
        order.pop_back();
        order.erase(order.begin());
        if (start >= 0 && order[0] != start) reverse(order.begin(), order.end());
        return order;
    }
    
    static vector<int> calc_path_keep(vector<vector<DIST_TYPE>>& dist, double time_limit, int start = -1) {
        int n = dist.size();
        dist.push_back(vector<int>(n + 1));
        for (int i = 0; i < n; i++) {
            if (i == start) {
                dist[i].push_back(0);
                dist[n][i] = 0;
            } else {
                dist[i].push_back(INF);
                dist[n][i] = INF;
            }
        }
        vector<int> order = calc(dist, time_limit, n);
        order.pop_back();
        order.erase(order.begin());
        if (start >= 0 && order[0] != start) reverse(order.begin(), order.end());
        return order;
    }
    
    private:
    constexpr static DIST_TYPE INF = 1e9;
    constexpr static DIST_TYPE DELTA = 1e-6;
    constexpr static int SWAP_TYPE3[64] = {-1, -1, -1, 1, -1, 2, 3, 0, 0, 2, 3, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, 3, 1, 0, 0, 3, 1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, -1, 1, 2, 0, 0, 1, 2, -1, 3, -1, -1, -1};
    #if defined(__AVX512VBMI__)
    static vector<__m512i> index512_8;
    static vector<__m512i> index512_16;
    #elif defined(__AVX512VL__)
    static vector<__m256i> index256_8;
    static vector<__m256i> index256_16;
    #elif defined(__SSSE3__)
    static vector<__m128i> index128_8;
    static vector<__m128i> index128_16;
    #endif
    
    template<class INDEX_TYPE> static vector<int> calc_inner(const vector<vector<DIST_TYPE>>& dist, double time_limit, int start) {
        int n = dist.size();
        vector<INDEX_TYPE> current_order = init_order<INDEX_TYPE>(dist, start), best_order = current_order, index(n);
        DIST_TYPE current_dist = calc_sum_dist(dist, current_order), best_dist = current_dist;
        
        vector<vector<pair<DIST_TYPE, int>>> sorted_dist(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) sorted_dist[i].emplace_back(dist[i][j], j);
            }
            sort(sorted_dist[i].begin(), sorted_dist[i].end());
        }
        
        int count = 0;
        timer timer;
        timer.start();
        while (timer.get_time() < time_limit) {
            count++;
            for (int i = 0; i < n; i++) index[current_order[i]] = i;
            while (true) {
                bool updated = false;
                for (int x = 0; x < n; x++) {
                    for (int dx = 0; dx <= 1; dx++) {
                        for (const pair<DIST_TYPE, int>& pxy : sorted_dist[current_order[x + dx]]) {
                            if (dist[current_order[x]][current_order[x + 1]] <= pxy.first) break;
                            for (int dy = 0; dy <= 1; dy++) {
                                int y = index[pxy.second] - 1 + dy;
                                if (y < 0) y += n;
                                DIST_TYPE diff = pxy.first - dist[current_order[x]][current_order[x + 1]] - dist[current_order[y]][current_order[y + 1]];
                                if (dx != dy) {
                                    DIST_TYPE next_dist = current_dist + diff + dist[current_order[x + 1 - dx]][current_order[y + dy]];
                                    if (next_dist + DELTA < current_dist) {
                                        updated = true;
                                        current_dist = next_dist;
                                        update_2opt(current_order, index, x, y);
                                        goto LOOP_END;
                                    }
                                }
                                for (const pair<DIST_TYPE, int>& pyz : sorted_dist[current_order[y + dy]]) {
                                    if (diff + pyz.first >= DELTA) break;
                                    for (int dz = 0; dz <= 1; dz++) {
                                        int z = index[pyz.second] - 1 + dz;
                                        if (z < 0) z += n;
                                        if (x == z || y == z) continue;
                                        DIST_TYPE next_dist = current_dist + diff + pyz.first - dist[current_order[z]][current_order[z + 1]] + dist[current_order[x + 1 - dx]][current_order[z + dz]];
                                        if (next_dist + DELTA < current_dist) {
                                            int swap_type = SWAP_TYPE3[((x < y) << 5) | ((x < z) << 4) | ((y < z) << 3) | (dx << 2) | (dy << 1) | dz];
                                            if (swap_type < 0) continue;
                                            updated = true;
                                            current_dist = next_dist;
                                            update_3opt(current_order, index, x, y, z, swap_type);
                                            goto LOOP_END;
                                        }
                                    }
                                }
                            }
                        }
                        LOOP_END: ;
                    }
                }
                if (!updated) break;
            }
            
            if (current_dist < best_dist) {
                best_dist = current_dist;
                best_order = current_order;
            }
            if (n <= 4) break;
            
            int x = random::get(1, n);
            int y = random::get(1, n - 1);
            int z = random::get(1, n - 2);
            int w = random::get(1, n - 3);
            if (y >= x) y++;
            if (x > y) swap(x, y);
            if (z >= x) z++;
            if (z >= y) z++;
            if (x > z) swap(x, z);
            if (y > z) swap(y, z);
            if (w >= x) w++;
            if (w >= y) w++;
            if (w >= z) w++;
            if (x > w) swap(x, w);
            if (y > w) swap(y, w);
            if (z > w) swap(z, w);
            current_order.clear();
            current_order.insert(current_order.end(), best_order.begin(), best_order.begin() + x);
            current_order.insert(current_order.end(), best_order.begin() + z, best_order.begin() + w);
            current_order.insert(current_order.end(), best_order.begin() + y, best_order.begin() + z);
            current_order.insert(current_order.end(), best_order.begin() + x, best_order.begin() + y);
            current_order.insert(current_order.end(), best_order.begin() + w, best_order.end());
            current_dist = calc_sum_dist(dist, current_order);
        }
        fprintf(stderr, "tsp count:%d\n", count);
        
        vector<int> order;
        for (INDEX_TYPE now : best_order) order.push_back(now);
        return order;
    }
    
    template<class INDEX_TYPE> static vector<INDEX_TYPE> init_order(const vector<vector<DIST_TYPE>>& dist, int start) {
        int n = dist.size();
        vector<INDEX_TYPE> order;
        vector<bool> used(n, false);
        used[start] = true;
        order.push_back(start);
        for (int i = 1; i < n; i++) {
            int last = order.back(), best = -1;
            for (int next = 0; next < n; next++) {
                if (used[next]) continue;
                if (best == -1 || dist[last][next] < dist[last][best]) best = next;
            }
            used[best] = true;
            order.push_back(best);
        }
        order.push_back(start);
        return order;
    }
    
    template<class INDEX_TYPE> static DIST_TYPE calc_sum_dist(const vector<vector<DIST_TYPE>>& dist, const vector<INDEX_TYPE>& order) {
        DIST_TYPE sum_dist = 0;
        for (int i = 0; i + 1 < order.size(); i++) sum_dist += dist[order[i]][order[i + 1]];
        return sum_dist;
    }
    
    template<class INDEX_TYPE> static void update_2opt(vector<INDEX_TYPE>& order, vector<INDEX_TYPE>& index, int x, int y) {
        x++; y++;
        if (x > y) swap(x, y);
        fast_reverse(order, x, y);
        for (int i = x; i < y; i++) index[order[i]] = i;
    }
    
    template<class INDEX_TYPE> static void update_3opt(vector<INDEX_TYPE>& order, vector<INDEX_TYPE>& index, int x, int y, int z, int swap_type) {
        x++; y++; z++;
        if (x > y) swap(x, y);
        if (x > z) swap(x, z);
        if (y > z) swap(y, z);
        if (swap_type == 0) { // x -> (y + 1 -> z) -> (x + 1 -> y) -> z + 1
            fast_reverse(order, x, y);
            fast_reverse(order, y, z);
            fast_reverse(order, x, z);
        } else if (swap_type == 1) { // x -> (y + 1 -> z) -> (y -> x + 1) -> z + 1
            fast_reverse(order, y, z);
            fast_reverse(order, x, z);
        } else if (swap_type == 2) { // x -> (y -> x + 1) -> (z -> y + 1) -> z + 1
            fast_reverse(order, x, y);
            fast_reverse(order, y, z);
        } else { // x -> (z -> y + 1) -> (x + 1 -> y) -> z + 1
            fast_reverse(order, x, y);
            fast_reverse(order, x, z);
        }
        for (int i = x; i < z; i++) index[order[i]] = i;
    }
    
    static void fast_reverse(vector<uint8_t>&v, int start, int end) {
        uint8_t *s = &v[start], *e = &v[end];
        #if defined(__AVX512VBMI__)
        while (e - s > 64) {
            e -= 64;
            __m512i lower = _mm512_loadu_si512(reinterpret_cast<__m512i*>(s));
            __m512i upper = _mm512_loadu_si512(reinterpret_cast<__m512i*>(e));
            _mm512_storeu_si512(reinterpret_cast<__m512i*>(s), _mm512_permutexvar_epi8(index512_8[0], upper));
            _mm512_storeu_si512(reinterpret_cast<__m512i*>(e), _mm512_permutexvar_epi8(index512_8[0], lower));
            s += 64;
        }
        if (e - s >= 2) {
            _mm512_storeu_si512(reinterpret_cast<__m512i*>(s), _mm512_permutexvar_epi8(index512_8[64 - (e - s)], _mm512_loadu_si512(reinterpret_cast<__m512i*>(s))));
        }
        #elif defined(__AVX512VL__)
        while (e - s > 32) {
            e -= 32;
            __m256i lower = _mm256_loadu_si256(reinterpret_cast<__m256i*>(s));
            __m256i upper = _mm256_loadu_si256(reinterpret_cast<__m256i*>(e));
            _mm256_storeu_si256(reinterpret_cast<__m256i*>(s), _mm256_permutexvar_epi8(index256_8[0], upper));
            _mm256_storeu_si256(reinterpret_cast<__m256i*>(e), _mm256_permutexvar_epi8(index256_8[0], lower));
            s += 32;
        }
        if (e - s >= 2) {
            _mm256_storeu_si256(reinterpret_cast<__m256i*>(s), _mm256_permutexvar_epi8(index256_8[32 - (e - s)], _mm256_loadu_si256(reinterpret_cast<__m256i*>(s))));
        }
        #elif defined(__SSSE3__)
        while (e - s > 16) {
            e -= 16;
            __m128i lower = _mm_loadu_si128(reinterpret_cast<__m128i*>(s));
            __m128i upper = _mm_loadu_si128(reinterpret_cast<__m128i*>(e));
            _mm_storeu_si128(reinterpret_cast<__m128i*>(s), _mm_shuffle_epi8(upper, index128_8[0]));
            _mm_storeu_si128(reinterpret_cast<__m128i*>(e), _mm_shuffle_epi8(lower, index128_8[0]));
            s += 16;
        }
        if (e - s >= 2) {
            _mm_storeu_si128(reinterpret_cast<__m128i*>(s), _mm_shuffle_epi8(_mm_loadu_si128(reinterpret_cast<__m128i*>(s)), index128_8[16 - (e - s)]));
        }
        #else
        reverse(v.begin() + start, v.begin() + end);
        #endif
    }
    
    static void fast_reverse(vector<uint16_t>&v, int start, int end) {
        uint16_t *s = &v[start], *e = &v[end];
        #if defined(__AVX512VBMI__)
        while (e - s > 32) {
            e -= 32;
            __m512i lower = _mm512_loadu_si512(reinterpret_cast<__m512i*>(s));
            __m512i upper = _mm512_loadu_si512(reinterpret_cast<__m512i*>(e));
            _mm512_storeu_si512(reinterpret_cast<__m512i*>(s), _mm512_permutexvar_epi8(index512_16[0], upper));
            _mm512_storeu_si512(reinterpret_cast<__m512i*>(e), _mm512_permutexvar_epi8(index512_16[0], lower));
            s += 32;
        }
        if (e - s >= 2) {
            _mm512_storeu_si512(reinterpret_cast<__m512i*>(s), _mm512_permutexvar_epi8(index512_16[32 - (e - s)], _mm512_loadu_si512(reinterpret_cast<__m512i*>(s))));
        }
        #elif defined(__AVX512VL__)
        while (e - s > 16) {
            e -= 16;
            __m256i lower = _mm256_loadu_si256(reinterpret_cast<__m256i*>(s));
            __m256i upper = _mm256_loadu_si256(reinterpret_cast<__m256i*>(e));
            _mm256_storeu_si256(reinterpret_cast<__m256i*>(s), _mm256_permutexvar_epi8(index256_16[0], upper));
            _mm256_storeu_si256(reinterpret_cast<__m256i*>(e), _mm256_permutexvar_epi8(index256_16[0], lower));
            s += 16;
        }
        if (e - s >= 2) {
            _mm256_storeu_si256(reinterpret_cast<__m256i*>(s), _mm256_permutexvar_epi8(index256_16[16 - (e - s)], _mm256_loadu_si256(reinterpret_cast<__m256i*>(s))));
        }
        #elif defined(__SSSE3__)
        while (e - s > 8) {
            e -= 8;
            __m128i lower = _mm_loadu_si128(reinterpret_cast<__m128i*>(s));
            __m128i upper = _mm_loadu_si128(reinterpret_cast<__m128i*>(e));
            _mm_storeu_si128(reinterpret_cast<__m128i*>(s), _mm_shuffle_epi8(upper, index128_16[0]));
            _mm_storeu_si128(reinterpret_cast<__m128i*>(e), _mm_shuffle_epi8(lower, index128_16[0]));
            s += 8;
        }
        if (e - s >= 2) {
            _mm_storeu_si128(reinterpret_cast<__m128i*>(s), _mm_shuffle_epi8(_mm_loadu_si128(reinterpret_cast<__m128i*>(s)), index128_16[8 - (e - s)]));
        }
        #else
        reverse(v.begin() + start, v.begin() + end);
        #endif
    }
};
#if defined(__AVX512VBMI__)
template<class DIST_TYPE> vector<__m512i> tsp<DIST_TYPE>::index512_8;
template<class DIST_TYPE> vector<__m512i> tsp<DIST_TYPE>::index512_16;
#elif defined(__AVX512VL__)
template<class DIST_TYPE> vector<__m256i> tsp<DIST_TYPE>::index256_8;
template<class DIST_TYPE> vector<__m256i> tsp<DIST_TYPE>::index256_16;
#elif defined(__SSSE3__)
template<class DIST_TYPE> vector<__m128i> tsp<DIST_TYPE>::index128_8;
template<class DIST_TYPE> vector<__m128i> tsp<DIST_TYPE>::index128_16;
#endif

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
        return memo2[dx][diff] = ans + 1 + calc2(diff, dx - 1, dx - 1);
    } else if (dx == diff + 1) {
        return memo2[dx][diff] = ans + 1;
    } else if (dx == diff) {
        return memo2[dx][diff] = ans;
    } else {
        int l = 0, r = diff / dx + 2;
        while (r - l > 1) {
            int m = (l + r) / 2;
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
    using score_type = unsigned;
    using hash_type = unsigned;
    constexpr static int MAX_TURN = 3000;
    constexpr static int BEAM_WIDTH = 200000;
    constexpr static int MAX_CANDIDATE = BEAM_WIDTH * 10;
    constexpr static int POOL_SIZE = MAX_TURN * BEAM_WIDTH + MAX_CANDIDATE;
    constexpr static int HASH_WIDTH = 26;
    constexpr static score_type TURN_SCORE = 1e3;
    constexpr static score_type FINISH_SCORE = 1e9;
    
    namespace duplicate {
        score_type data[1 << HASH_WIDTH];
        
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
        
        inline void init() {
            node::parent = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
            node::child = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
            node::prev = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
            node::next = (node_type*)malloc(sizeof(node_type) * POOL_SIZE);
            node::operation = (operation_type*)malloc(sizeof(operation_type) * POOL_SIZE);
            node::score = (score_type*)malloc(sizeof(score_type) * POOL_SIZE);
            node::hash = (hash_type*)malloc(sizeof(hash_type) * POOL_SIZE);
            next_node = 0;
            for (int i = 1; i < POOL_SIZE; i++) parent[i - 1] = i;
        }
        
        inline void init_node(node_type n) {
            parent[n] = child[n] = prev[n] = next[n] = EMPTY;
            score[n] = 100000;
            hash[n] = 0;
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
    
    vector<operation_type> search() {
        node::init();
        node_type top = node::get_node();
        node::init_node(top);
        
        node_type* candidates = (node_type*)malloc(sizeof(node_type) * (MAX_CANDIDATE * 2));
        node_type* leaves = candidates + MAX_CANDIDATE;
        node_type* leaves_end = leaves;
        score_type best_score = 0;
        for (int turn = 0; turn < MAX_TURN; turn++) {
            if (turn % 10 == 0) {
                fprintf(stderr, "%d\n", turn);
                fflush(stderr);
            }
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
            if (candidates == candidates_end) {
                fprintf(stderr, "ERROR %d\n", turn);
                break;
            }
            
            for (node_type* n = candidates; n != candidates_end; n++) {
                if (node::score[*n] >= FINISH_SCORE) {
                    return construct_results(*n);
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
        
        return construct_results(*max_element(leaves, leaves_end, [&](const node_type n1, const node_type n2) {
            return node::score[n1] < node::score[n2];
        }));
    }
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

vector<pair<int, int>> sort_tsp(const vector<pair<int, int>>& v) {
    vector<vector<int>> dist(v.size(), vector<int>(v.size()));
    for (int i = 0; i < v.size(); i++) {
        for (int j = 0; j < v.size(); j++) {
            int x = v[i].first, y = v[i].second, nx = v[j].first, ny = v[j].second;
            dist[i][j] = max(calc(x, nx), calc(y, ny));
        }
    }
    vector<int> path = tsp<int>::calc_path_keep(dist, 10.0, 0);
    vector<pair<int, int>> w;
    for (int p : path) w.push_back(v[p]);
    return w;
}

int main() {
    tsp<int>::init();
    
    while (true) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2) break;
        if (x == 0 && y == 0) continue;
        v.emplace_back(x, y);
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    v.insert(v.begin(), make_pair(0, 0));
    v = sort_tsp(v);
    
    vector<int> ans = beam_search::search();
    
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
        vector<vector<int>> dist(w.size(), vector<int>(w.size()));
        for (int i = 0; i < w.size(); i++) {
            for (int j = 0; j < w.size(); j++) {
                int x = w[i].first, y = w[i].second, nx = w[j].first, ny = w[j].second;
                dist[i][j] = max(calc(x, nx), calc(y, ny));
            }
        }
        
        vector<int> path = tsp<int>::calc_path_keep(dist, 10.0, 0);
        for (int i = 0; i + 1 < path.size(); i++) {
            int x = w[path[i]].first, y = w[path[i]].second, nx = w[path[i + 1]].first, ny = w[path[i + 1]].second;
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
    
    return 0;
}
