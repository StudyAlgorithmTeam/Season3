#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#define INT_MIN (-2147483647 - 1);

int t, n;
int yeong[3];
int jong[3];
int dp[10010];

int day[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

bool is_leap(int y) {
	return !(y % 400) || ((y % 100) && !(y % 4));
}

int days(int y, int m, int d) {
	int result = 0;
	for (int i = 0; i < y; i++) {
		if (is_leap(i))
			result += 366;
		else
			result += 365;
	}
	bool leap = is_leap(y);

	// O(1) (그냥 12개 체크한 거)
	for (int i = 1; i < m; i++) {
		if (leap && i == 2)
			result += day[i - 1] + 1;
		else
			result += day[i - 1];
	}
	result += d;
	return result;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	for (int i = 0; i < 3; i++) {
		cin >> yeong[i];
	}
	for (int i = 0; i < 3; i++) {
		cin >> jong[i];
	}

	cin >> t >> n;

	int diff = days(jong[0], jong[1], jong[2]) - days(yeong[0], yeong[1], yeong[2]);

	// O(N)
	while(n--) {
		int op, c, k;
		cin >> op >> c >> k;
		if (op == 3) k *= 30;
		for (int i = t; i >= c; i--) {
			dp[i] = max(dp[i], dp[i - c] + k);
		}
	}

	cout << abs(diff - *max_element(dp, dp + t + 1));
    return 0;
}