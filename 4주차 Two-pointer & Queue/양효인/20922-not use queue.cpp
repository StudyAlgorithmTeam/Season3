#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	int n, k;
	cin >> n >> k;

	vector<int> nums(n);
	for (int i = 0; i < n; i++) {
		cin >> nums[i];
	}
	int dupliNums[100001] = { 0 };

	int left = 0; int right = 0; int maxNum = 0;

	while (left <= right && right < n) {
		if (dupliNums[nums[right]] < k) {
			dupliNums[nums[right]]++;
			right++;
			maxNum = max(maxNum, right - left);
		}
		else if (dupliNums[nums[right]] == k) {
			dupliNums[nums[right]]--;
			left++;
		}
	}

	cout << maxNum;

}
