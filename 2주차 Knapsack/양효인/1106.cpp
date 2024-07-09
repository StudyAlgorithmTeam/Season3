#include <iostream>
using namespace std;

int c, n;
int input[20][2];
int dp[100001];

int countDP(int customer, int cityNum) {
	int min = 100 * 1000;
	int cost;
	if (customer <= 0) return 0;
	else if (dp[customer] > 0) return dp[customer];
	else {
		for (int i = 0; i < cityNum; i++) {
			cost = countDP(customer - input[i][1], cityNum) + input[i][0];
			min = cost < min ? cost : min;
		}
		dp[customer] = min;
		return min;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	cin >> c >> n;
	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		input[i][0] = a;
		input[i][1] = b;
	}

	cout << countDP(c, n);

	return 0;

}
