#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 1000

int n /*몇개구매할건지*/,d[MAX] /*i개 구매시 드는 최대비용*/,p[MAX]; /*i개 들어잇는 카드팩 구매시 드는비용*/

void solve()
{
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			d[i] = max(d[i], d[i - j] + p[j]);
		}
	}
}

int main()
{
	cin >> n;
	
	for (int i = 1; i <= n; i++) {
		cin >> p[i];
	}
	solve();
	cout << d[n];

	return 0;
}