#include <iostream>

using namespace std;

int arr[200001] = { 0, };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	int pt1 = 0, pt2 = 0;
	int count[100001] = { 0, };
	int maxlen = 0;
	int len = 1;

	count[arr[pt2]] = 1;
	while (pt2 < N-1) {
		if (count[arr[pt2 + 1]] < K) {
			pt2++;
			count[arr[pt2]]++;
			len = pt2 - pt1 + 1;
			if (maxlen < len) {
				maxlen = len;
			}
		}
		else{
			count[arr[pt1]]--;
			pt1++;
		}
	}
	cout << maxlen;
}
