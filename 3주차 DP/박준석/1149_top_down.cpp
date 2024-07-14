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

int knap(int RGB, int K) {
	if (K <= 0)
		return 0;

	if (RGB == R) {
		if (dp[R][K] == 0)
			dp[R][K] = min(knap(G, K - 1) + GREEN[K - 1], knap(B, K - 1) + BLUE[K - 1]);
		return dp[R][K];
	}
	if (RGB == G) {
		if (dp[G][K] == 0)
			dp[G][K] =  min(knap(R, K - 1) + RED[K - 1], knap(B, K - 1) + BLUE[K - 1]);
		return dp[G][K];
	}
	if (RGB == B) {
		if (dp[B][K] == 0)
			dp[B][K] = min(knap(R, K - 1) + RED[K - 1], knap(G, K - 1) + GREEN[K - 1]);
		return dp[B][K];
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> RED[i] >> GREEN[i] >> BLUE[i];
	}

	cout << min(knap(R, N),min( knap(G, N), knap(B, N)));

}
