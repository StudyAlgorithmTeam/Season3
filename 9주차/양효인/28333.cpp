#include <iostream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

vector<int> graph[1001], path[1001];
int dist[1001];

// O(N + M)
void bfs(int start) {
	queue<int> q;
	q.push(start);
	dist[start] = 1;

	// O(N + M)
	while (!q.empty()) {
		int x = q.front();
		q.pop();

		// O(N)
		for (int i = 0; i < graph[x].size(); i++) {
			int y = graph[x][i];
			int cost = dist[x] + 1;

			if (!dist[y]) {
				q.push(y);
				dist[y] = cost;
				path[y].push_back(x);
			}
			else if (cost == dist[y]) {
				path[y].push_back(x);
			}
		}
	}
}

// O(N+M)
void backtrack(int n) {
	set<int> ans{ n };
	queue<int> q;
	q.push(n);
	vector<bool> visited(1001, false);
	visited[n] = true;

	// O(M)
	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (int next : path[now]) {
			if (!visited[next]) {
				visited[next] = true;
				ans.insert(next);
				q.push(next);
			}
		}
	}

	// O(N)
	for (auto& node : ans) {
		cout << node << ' ';
	}
	cout << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int t;
	cin >> t;

	// O(t * (N+M))
	while (t--) {
		int n, m;
		cin >> n >> m;

		for (int i = 1; i <= n; i++) {
			graph[i].clear();
			path[i].clear();
			dist[i] = 0;
		}

		for (int i = 0; i < m; i++) {
			int a, b;
			cin >> a >> b;
			graph[a].push_back(b);
		}

		// O(N+M)
		bfs(1);

		// O(N+M)
		backtrack(n);
	}

	return 0;
}
