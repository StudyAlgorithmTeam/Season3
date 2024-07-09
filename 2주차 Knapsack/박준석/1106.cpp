#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int C, N;
	cin >> C >> N;

	int dp[100001] = { 0, };

	int cost[20] = { 0, };
	int cust[20] = { 0, };
	for (int i = 0; i < N; i++) {
		cin >> cost[i] >> cust[i];
	}
	//input

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 100001; j++) {
			if (j - cost[i] >= 0) //i번째 값을 빼도 0보다 같거나 크다면
				dp[j] = max(dp[j], dp[j - cost[i]] + cust[i]); // 0/1 중 큰것을 선택
		}
	}

	for (int j = 0; j < 100001; j++) {
		if (dp[j] >= C) {
			cout << j;
			break;
		}
	}

}
