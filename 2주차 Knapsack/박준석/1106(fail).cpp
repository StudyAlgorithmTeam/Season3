#include <iostream>
#include <algorithm>

using namespace std;


int cost[20] = { 0, };
int cust[20] = { 0, };
int C, N;
int dp[1001] = { 0, };
int Min;

int knap() {
	for (int i = 1; i <= 1000; i++) { //dp를 C까지 돌면서 채움
		for (int j = 0; j < N; j++) { //N개의 도시들중 최적
			if ((i - cust[j]) < 0);//뭐지
			else
				dp[i] = min(dp[i], dp[i - cust[j]] + cost[j]);
		}
	}
	Min = dp[C];
	for (int i = C; i < 1001; i++) {
		if (Min > dp[i])
			Min = dp[i];
	}

	for (int i = 0; i < 50; i++) {
		cout << "dp " << i << "  " << dp[i] << endl;
	}
	return Min;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> C >> N;

	for (int i = 0; i < N; i++) {
		cin >> cost[i] >> cust[i];
	}
	for (int i = 1; i <= 1000; i++) {
		dp[i] = 1000000;
	}//input

	cout << knap();

}
