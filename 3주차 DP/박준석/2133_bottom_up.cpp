#include <iostream>

using namespace std;

int dp[40] = { 0, };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	int N;
	cin >> N;
	dp[0] = 1;
	dp[2] = 3;

	for (int i = 4; i < N + 1; i += 2) {
		dp[i] += dp[i - 2] * 3;
		for (int j = i-4; j >= 0; j -= 2) {
			dp[i] += dp[j] * 2;
		}
	}

	cout << dp[N];


}
