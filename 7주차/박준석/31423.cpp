#include <iostream>
#include<string>

using namespace std;

typedef struct Node {
	string data="";
	int last;
	Node* next = NULL;
}Node;

Node lst[500001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		string s;
		cin >> s;
		lst[i].data = s;
		lst[i].last = i;
	}

	int lastI=0;
	for (int k = 0; k < N-1; k++) {
		int i, j;
		cin >> i >> j;
		lastI = i;

		lst[lst[i].last].next = &lst[j];
		lst[i].last = lst[j].last;

	}	

	Node* point = &lst[lastI];

	while (true) {
		if (point == NULL)
			return 0;

		cout << point->data;
		point = point->next;
		
	}
	

}
