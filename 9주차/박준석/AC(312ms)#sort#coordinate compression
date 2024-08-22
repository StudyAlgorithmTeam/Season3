#include <iostream>
#include <algorithm>
#include<vector>

#define INT long long

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	INT N;
	cin >> N;

	vector<INT> arr;
	vector<pair<INT,INT>> sarr;

	//N
	for (INT i = 0; i < N; i++) {
		INT a;
		cin >> a;
		arr.push_back(a);
		sarr.push_back(make_pair(a,i));
	}

	//N log N
	//좌표 크기에 따라 정렬
	sort(sarr.begin(), sarr.end());

	INT k = 0;
	//N
	arr[sarr[0].second] = k;
	for (INT i = 1; i < N; i++) {
		if (sarr[i].first != sarr[i - 1].first) {
			k++;
		}
		arr[sarr[i].second] = k;
	}
	
	//N
	for (INT i = 0; i < N; i++) {
		cout << arr[i] << " ";
	}
}
