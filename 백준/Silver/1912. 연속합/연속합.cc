#include <iostream>
using namespace std;
//d[i] : i번째 수로 끝나는 수열의 가장 큰 연속합
int d[100001] = {};
int a[100001] = {};

int solve(int n)
{
	int max = 0;

	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}

	max = a[1];

	for (int i = 1; i <= n; i++) {
		d[i] = a[i];
		if (i == 1) 
			continue;
	
		if (d[i] < d[i - 1] + a[i]) {
			d[i] = d[i - 1] + a[i];
		}

		if (max < d[i])
			max = d[i];
	}
	return max;
}

int main()
{
	int n;
	cin >> n;

	cout << solve(n) << '\n';
	
	return 0;

}
