#include <iostream>
using namespace std;

int dp[100000+1][3];
int n;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	cin >> n;
	int mod = 9901;

	dp[1][0] = 1;
	dp[1][1] = 1;
	dp[1][2] = 1;

	// O(n)
	for (int idx = 2; idx <= n; idx++) {
		dp[idx][0] = (dp[idx - 1][1] + dp[idx - 1][2]) % mod;
		dp[idx][1] = (dp[idx - 1][0] + dp[idx - 1][2]) % mod;
		dp[idx][2] = (dp[idx - 1][0] + dp[idx - 1][1] + dp[idx - 1][2]) % mod;
	}
	cout << (dp[n][0] + dp[n][1] + dp[n][2]) % mod;

    return 0;
}