#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, R;
	cin >> N >> M >> R;

	int u, v;
	vector<vector<int>> E(N+1,vector<int>(0,0));
	vector<int> visited(N+1,0);
	queue<int> q;

	for (int i = 0; i < M; i++) {
		cin >> u >> v;
		E[u].push_back(v);
		E[v].push_back(u);
	}

	for (int i = 1; i < N + 1; i++) {
		sort(E[i].begin(), E[i].end());
	}

	visited[R] = 1;
	q.push(R);
	
	long long depth = 0;
	long long n_visited = 1;
	long long res = 0;

	while (!q.empty()) {
		int width = q.size();
		for (int i = 0; i < width; i++) {
			u = q.front();
			q.pop();
			res += n_visited * depth;
			n_visited++;
			for (int j=0 ; j < E[u].size();j++) {
				if (visited[E[u][j]] == 0) {
					visited[E[u][j]] = 1;
					q.push(E[u][j]);
				}
			}
		}
		depth ++;
	}

	cout << res;
}
