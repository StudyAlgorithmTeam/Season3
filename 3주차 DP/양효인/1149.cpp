#include <iostream>
#include <vector>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	int n;
	cin >> n;

	vector<int> colorR(n), colorG(n), colorB(n);

	for (int i = 0; i < n; i++) {
		cin >> colorR[i] >> colorG[i] >> colorB[i];
	}

	vector<int> dpR(n), dpG(n), dpB(n);

	dpR[0] = colorR[0];
	dpG[0] = colorG[0];
	dpB[0] = colorB[0];

	for (int i = 1; i < n; i++) {
		dpR[i] = min(dpG[i - 1], dpB[i - 1]) + colorR[i];
		dpG[i] = min(dpR[i - 1], dpB[i - 1]) + colorG[i];
		dpB[i] = min(dpR[i - 1], dpG[i - 1]) + colorB[i];
	}

	int sum = min({ dpR[n - 1],dpG[n - 1],dpB[n - 1] });

	cout << sum;
}
