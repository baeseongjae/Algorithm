#include <iostream>
#include <algorithm>
using namespace std;

long long d[100001] = {};

int solve(int n)
{
	for (int i = 1; i <= n; i++) {
		d[i] = i;
		for (int j = 1; j*j <= i; j++) {
			if (d[i] > d[i - j*j] + 1)
				d[i] = d[i - j*j] + 1;
		}
	}
	return d[n];
}

int main()
{
	int n;
	cin >> n;
	cout << solve(n) << '\n';

	return 0;
}