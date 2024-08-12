#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	int n, m;
	string s;
	cin >> n >> m >> s;
	int result = 0;
	
	vector<char> pa(2 * n + 1);
	for (int idx = 0; idx < pa.size(); idx++) {
		if (idx % 2 == 0) pa[idx] = 'I';
		else pa[idx] = 'O';
	}
	

	for (int i = 0; i < s.size(); i++) {
		bool isP = false;

		if (s[i] == 'I') {
			for (int j = 0; j < pa.size(); j++) {
				if (s[i+j] == pa[j]) {
					isP = true;
				}
				else {
					isP = false;
					break;
				}
			}
			if (isP) result++;
		}
		else
			continue;

	}
	cout << result;

    return 0;
}