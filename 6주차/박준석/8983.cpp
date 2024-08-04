#include <iostream>
#include<ctype.h>
#include <vector>
#include<algorithm>
#include<cmath>
#define INT int 

using namespace std;

// x좌표가 a<b이면 true, x같으면 y좌표 a<b면 true  
bool comp(pair<INT, INT> a, pair<INT, INT> b) {
	if (a.first == b.first) return a.second < b.second;
	return a.first < b.first;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	INT M, N, L;
	//O(1)
	cin >> M >> N >> L;
	//M: 100,000 N:100,000 L:1,000,000,000

	int n;
	vector<INT> Xi;
	//O(M)
	for (int i = 0; i < M; i++) {
		cin >> n;
		Xi.push_back(n);
	}

	int x, y;
	vector<pair<INT, INT>> co;
	//O(N)
	for (int i = 0; i < N; i++) {
		cin >> x >> y;
		co.push_back(make_pair(x, y));
	}

	// x오름차순, 같으면 y오름차순
	//퀵소트임 O(M log M)
	sort(Xi.begin(), Xi.end());
	//O(N log N)
	sort(co.begin(), co.end(),comp);


	int res = 0;
	//O(N) => O(N * log M)
	for (int i = 0; i < co.size(); i++) {
		INT left = 0, right = Xi.size(), mid;
		//O(log M) Xi크기에 비례하여 이분탐색을 진행
		while (left <= right) {
			mid = left + (right-left) / 2;
			INT check = abs((int)(Xi[mid] - co[i].first)) + co[i].second;
			// check한 거리가 L 즉 사정권 안에 있다면 res증가 후 break
			if (check <= L) {
				res++;
				break;
			}
			//check한거리가 L 밖이라면 이분탐색을 진행.
			else {
				//동물이 현재 확인중인 사대보다 오른쪽이면 left <- mid+1, 아니면 right <-mid-1
				if (co[i].first >= Xi[mid])
					left = mid + 1;
				else
					right = mid - 1;
			}
		}
		

	}
	cout << res;
	
	//O((N+M) * log M) 인가?...
	//동물을 차례대로 보면서 가장 가까운 사대에대해서 사정거리에 있는지 확인.
}
