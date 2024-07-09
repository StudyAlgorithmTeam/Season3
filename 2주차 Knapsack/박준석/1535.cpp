#include <iostream>
#include <algorithm>

using namespace std;

int L[20] = { 0, };
int J[20] = { 0, };
int N;
int mem[20][101] = {0,};

int knap(int i, int hp) {
	if (hp <= 0) //죽으면 -100
		return -100;
	if (i == N) //다 돌면 끝
		return 0;
	if (mem[i][hp] != -1) // 이미 계산
		return mem[i][hp];
	mem[i][hp] = max((knap(i + 1, hp - L[i]) + J[i]), knap(i + 1, hp));
	return mem[i][hp];
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> L[i];
	}
	for (int i = 0; i < N; i++) {
		cin >> J[i];
	}
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 101; j++) {
			mem[i][j] = -1;
		}
	}

	cout << knap(0, 100);


}
