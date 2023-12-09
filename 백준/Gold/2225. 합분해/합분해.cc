#include <iostream>
using namespace std;

const long long mod = 1000000000LL;
int d[201][201];

int solve(int k,int n)
{
	for (int i = 0; i <= n; i++)
		d[1][i] = 1;

	for (int i = 1; i <= k; i++) {

		for (int j = 0; j <= n; j++) {

			for (int l = 0; l <= j; l++) {
				d[i][j] += d[i -1][j - l];
				d[i][j] %= mod;
			}

		}

	}
	return d[k][n];
}

int main()
{
	int n, k;
	cin >> n >> k;

	cout << solve(k, n)<<'\n';
	return 0;
}
