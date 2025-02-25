#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int n, k;
	cin >> n >> k;

	// O(N)
	vector<int> nums(n);
	for (int i = 0; i < n; i++) {
		cin >> nums[i];
	}
	int dupliNums[100001] = { 0 };

	queue<int> q;
	int maxNum = 0;

	// O(N)
	for (int i = 0; i < n; i++) {
		// O(1)
		q.push(nums[i]);
		dupliNums[nums[i]]++;

		// O(1)
		if (dupliNums[nums[i]] >= k) {
			int temp = q.front();
			q.pop();
			dupliNums[temp]--;
		}

		maxNum = max(maxNum, (int)q.size());
	}
	cout << maxNum;

}
