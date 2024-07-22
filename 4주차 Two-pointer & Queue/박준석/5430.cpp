#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T, n;
	int reverse = 0;
	int error = 0;
	string textp;
	string textnum;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> textp;
		cin >> n;
		cin >> textnum;

		deque<int> dq;
		string s = "";

		if(n!=0){
			for (int j = 0; j < textnum.length(); j++) {
				if (textnum[j] == '[' || textnum[j] == ',' || textnum[j] == ']') {
					if (textnum[j] != '[') dq.push_back(stoi(s));
					s = "";
				}
				else s += textnum[j];
			}
		}

		for (int j = 0; j < textp.length(); j++) {
			if (textp[j] == 'R') {
				if (reverse == 0) reverse = 1;
				else reverse = 0;
			}
			if (textp[j] == 'D') {
				if (dq.empty() == 1) {
					error = 1;
					break;
				}

				if (reverse == 0) {
					dq.pop_front();
				}
				else if (reverse == 1) {
					dq.pop_back();
				}
			}
		}


		if (error == 1)
			cout << "error" << endl;
		else if (dq.empty() != 1) {
			if (reverse == 0) {
				cout << "[";
				for (int j = 0; j < dq.size() - 1; j++) {
					cout << dq[j] << ",";
				}
				cout << dq[dq.size() - 1] << "]" << endl;
			}
			if (reverse == 1) {
				cout << "[";
				for (int j = dq.size() - 1; j > 0; j--) {
					cout << dq[j] << ",";
				}
				cout << dq[0] << "]" << endl;
			}
		}
		else
			cout << "[]"<<endl;

		reverse = 0, error = 0;
	}
}
