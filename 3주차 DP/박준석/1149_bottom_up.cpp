#include <iostream>
#include <algorithm>

#define R 1
#define G 2
#define B 3

int N;
int RED[1001];
int GREEN[1001];
int BLUE[1001];
int dp[4][2000] = { 0, };


using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> RED[i] >> GREEN[i] >> BLUE[i];
	}

	dp[R][0] = RED[0];
	dp[G][0] = GREEN[0];
	dp[B][0] = BLUE[0];
	for (int K= 1; K < N+1; K++) {
		for (int RGB = 1; RGB < 4; RGB++) {
			if (RGB == R) {
				dp[R][K] = min(dp[G][K - 1], dp[B][K - 1]) + RED[K];
			}
			if (RGB == G) {
				dp[G][K] = min(dp[R][K - 1], dp[B][K - 1]) + GREEN[K];
			}
			if (RGB == B) {
				dp[B][K] = min(dp[R][K - 1], dp[G][K - 1]) + BLUE[K];
			}
		}
	}

	cout << min(dp[R][N], min(dp[G][N], dp[B][N]));

}
