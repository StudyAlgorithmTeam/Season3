#include <iostream>
#include <map>
#define DIV 1000000007LL
using namespace std;

map<long long, long long> f;

long long fibo(long long n) {
	if (n == 0)return 0;
	if (n == 1) return 1;
	if (n == 2) return 1;
	if (f.count(n) > 0) return f[n];

	if (n % 2 == 0) {
		long long m = n / 2;
		long long temp1 = fibo(m - 1);
		long long temp2 = fibo(m+1);
		f[n] = fibo(m)*(temp1 + temp2) % DIV;
		return f[n];
	}
	else {
		long long m = (n + 1) / 2;
		long long temp1 = fibo(m);
		long long temp2 = fibo(m - 1);
		f[n] = (fibo(m) * fibo(m) + fibo(m-1)* fibo(m - 1)) % DIV;
		return f[n];
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	long long n;
	cin >> n;
	cout << fibo(n);
}