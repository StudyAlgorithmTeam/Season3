#include <iostream>
#include <vector>
#define MOD 1000000007

using namespace std;

vector<vector<long long int>> vecMul(vector<vector<long long int>> arr1, vector<vector<long long int>> arr2){
	vector<vector<long long int>> answer = { {0,0},{0,0} };

	answer[0][0] = arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0];
	answer[0][1] = arr1[0][0] * arr2[0][1] + arr1[0][1] * arr2[1][1];
	answer[1][0] = arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0];
	answer[1][1] = arr1[1][0] * arr2[1][0] + arr1[1][1] * arr2[1][1];

	return answer;
}
vector<vector<long long int>> vecDiv(vector<vector<long long int>> arr) {
	vector<vector<long long int>> answer = { {0,0},{0,0} };
	answer[0][0] = arr[0][0]%MOD;
	answer[0][1] = arr[0][1] % MOD;
	answer[1][0] = arr[1][0] % MOD;
	answer[1][1] = arr[1][1] % MOD;
	return answer;
}

vector<vector<long long int>> pow(vector<vector<long long int>> a, long long int b) {
	if (b == 1)
		return vecDiv(a);
	vector<vector<long long int>> i = pow(a, b / 2);
	if (b % 2 == 0)
		return vecDiv(vecMul(i, i));
	else
		return vecDiv(vecMul(vecDiv(vecMul(i, i)), a));
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long long int n;
	cin >> n;

	vector<vector<long long int>> A = { {1,1},{1,0} };

	cout << pow(A, n)[0][1];

}
