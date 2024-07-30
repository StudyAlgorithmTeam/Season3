#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;


int n, m, r;
long long visited[100001];
vector<int> connect[100001];
long long cur[100001];

void bfs() {
    int cnrCount = 1;
    memset(visited, -1, sizeof(visited));
    queue<int> q;
    q.push(r);
    visited[r] = 0;
    cur[r] = 0;

    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (int i = 0; i < connect[x].size(); i++) {
            int temp = connect[x][i];
            if (visited[temp] == -1) {
                visited[temp] = visited[x] + 1;
                cur[temp] = ++cnrCount;
                q.push(temp);
            }
        }
    }

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

    cin >> n >> m >> r;
    
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        connect[x].push_back(y);
        connect[y].push_back(x);
    }

    long long answer = 0;
    for (int i = 1; i <= n; i++) {
        sort(connect[i].begin(), connect[i].end());
    }
    bfs();
    for (int i = 1; i <= n; i++) {
        answer += visited[i] * cur[i];
    }
    cout << answer;
    
    return 0;
}