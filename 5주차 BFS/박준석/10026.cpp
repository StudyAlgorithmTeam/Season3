#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<string> s;
	vector<vector<int>> visited(N, vector<int>(N, 0)); //N-12차원 visited 0으로 초기화
	string t;
	int t1, t2;
	queue<int> q1;
	queue <int> q2;
	int count = 0;
	for (int i = 0; i < N; i++) {
		cin >> t;
		s.push_back(t);
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 0) {//방문한 적이 없으면
				t = s[i][j];
				q1.push(i);
				q2.push(j);
				count++;
				while (!q1.empty()) {
					int width = q1.size();
					for (int x = 0; x < width; x++) {
						t1 = q1.front();
						t2 = q2.front();
						q1.pop();
						q2.pop();
						//4방향 확인후 하나씩 q에 넣기
						if (t1 > 0 && visited[t1 - 1][t2] == 0 && s[t1 - 1][t2] == t[0]) {
							q1.push(t1 - 1);
							q2.push(t2);
							visited[t1 - 1][t2] = 1;
						}
						if (t1 < N - 1 && visited[t1 + 1][t2] == 0 && s[t1 + 1][t2] == t[0]) {
							q1.push(t1 + 1);
							q2.push(t2);
							visited[t1 + 1][t2] = 1;
						}
						if (t2 > 0 && visited[t1][t2 - 1] == 0 && s[t1][t2 - 1] == t[0]) {
							q1.push(t1);
							q2.push(t2 - 1);
							visited[t1][t2 - 1] = 1;
						}
						if (t2 < N - 1 && visited[t1][t2 + 1] == 0 && s[t1][t2 + 1] == t[0]) {
							q1.push(t1);
							q2.push(t2 + 1);
							visited[t1][t2 + 1] = 1;
						}
					}
				}
			}
		}
	}
	cout << count;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			visited[i][j] = 0;
			if (s[i][j] == 'R')
				s[i][j] = 'G';
		}
	}
	count = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] ==0 ) {//방문한 적이 없으면
				t = s[i][j];
				q1.push(i);
				q2.push(j);
				count++;
				while (!q1.empty()) {
					int width = q1.size();
					for (int x = 0; x < width; x++) {
						t1 = q1.front();
						t2 = q2.front();
						q1.pop();
						q2.pop();
						//4방향 확인후 하나씩 q에 넣기
						if (t1 >0 && visited[t1-1][t2] == 0 && s[t1-1][t2] == t[0]) {
							q1.push(t1-1);
							q2.push(t2);
							visited[t1 - 1][t2] = 1;
						}
						if (t1 < N-1 && visited[t1+1][t2] == 0 && s[t1 + 1][t2] == t[0]) {
							q1.push(t1 + 1);
							q2.push(t2);
							visited[t1 + 1][t2] = 1;
						}
						if (t2 > 0 && visited[t1][t2-1] == 0 && s[t1][t2-1] == t[0]) {
							q1.push(t1);
							q2.push(t2-1);
							visited[t1][t2-1] = 1;
						}
						if (t2 < N-1 && visited[t1][t2+1] == 0 && s[t1][t2+1] == t[0]) {
							q1.push(t1);
							q2.push(t2+1);
							visited[t1][t2 + 1] = 1;
						}
					}
				}
			}
		}
	}

	cout  <<" " << count;
}
