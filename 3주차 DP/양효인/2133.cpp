#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> dp;

int check(int n);

void f(int n) {
	if (n <= 0) return;
	else if (n % 2 != 0)
		dp[n] = 0;
	else
		dp[n] = dp[n - 2] * dp[2] + check(n);
}

int check(int n) {
	if (n <= 4) return 2;
	return dp[n - 4] * 2 + check(n-2);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	int n;
	cin >> n;

	dp.resize(n+1);
	dp[0] = 0;
	dp[1] = 0;
	dp[2] = 3;
	for (int i = 3; i <= n; i++) {
		f(i);
	}
	cout << dp[n];

}
