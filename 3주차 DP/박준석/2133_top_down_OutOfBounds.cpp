#include <iostream>

using namespace std;

int dp[40] = { 0, };

int knap(int N) {
	if (N == 0)
		return 1;
	if (N == 2)
		return 3;

	int res;
	if (dp[N - 2] != 0)
		res = 3 * dp[N - 2];
    else
	    res = 3*knap(N - 2);

	for (int i = N - 4; i >= 0; i -= 2) {
		if (dp[i] != 0)
			res += 2 * dp[i];
		else
			res += 2*knap(i);
	}

	dp[N] = res;
	return dp[N];
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	int N;
	cin >> N;
	dp[0] = 1;
	dp[2] = 3;

	cout << knap(N);
}
