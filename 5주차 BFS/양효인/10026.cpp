#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#include <vector>
using namespace std;


int n, cnt;
char grid[101][101];
bool visited[101][101];

int dx[] = { 1, -1, 0, 0 };
int dy[] = { 0, 0, 1, -1 };

void dfs(int nowx, int nowy) {
    if (visited[nowx][nowy]) return;

    visited[nowx][nowy] = true;
    for (int i = 0; i < 4; i++) {
        int x = dx[i] + nowx;
        int y = dy[i] + nowy;
        if ((grid[nowx][nowy] == grid[x][y] && !visited[x][y])) {
            dfs(x, y);
        }
    }

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
    
    int n;
    cin >> n;

    // 정상
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                dfs(i, j);
                cnt++;
            }
        }
    }
    cout << cnt << " ";

    // 적록색약
    cnt = 0;
    memset(visited, false, sizeof(visited));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 'G') grid[i][j] == 'R';
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                dfs(i, j);
                cnt++;
            }
        }
    }
    cout << cnt;

    return 0;
}