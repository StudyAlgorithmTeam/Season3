#include <iostream>
#include <vector>
using namespace std;

int L[20];
int J[20];
int n;
int life;

int maxJoy(int i, int life) {
    if (life <= 0) return -1e9;
    if (i >= n) return 0;

    int skip = maxJoy(i + 1, life);
    int take = J[i] + maxJoy(i + 1, life - L[i]);

    return max(skip, take);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    life = 100;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> L[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> J[i];
    }

    int joy = maxJoy(0, life);
    cout << joy;

    return 0;
}
