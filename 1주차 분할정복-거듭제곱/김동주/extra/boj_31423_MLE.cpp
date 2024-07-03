#include <iostream>
#include <list>
#include <string>

#define MAX_N 500000

using namespace std;


list<string> lists[MAX_N+1];


int main()
{
    int N;
    int n;
    int i;
    int j;
    string buf;
    list<string>::iterator it;

    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);

    cin >> N;

    // 리스트 초기화
    for (n = 1; n <= N; n++) {
        cin >> buf;
        lists[n].push_back(buf); // call by value 이므로 그냥 넘겨주면 된다.
    }

    // 쿼리 수행
    for (n = 0; n < N-1; n++) {
        cin >> i >> j;
        lists[i].insert(lists[i].end(), lists[j].begin(), lists[j].end());
    }

    // 마지막 문자열 출력
    for (it = lists[i].begin(); it != lists[i].end(); it++) {
        cout << *it;
    }

    return 0;
}