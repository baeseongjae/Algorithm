#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main()
{	
	int n,i;

	cin >> n;
	vector<int> a(n);
	vector<int> ans(n);
	
	stack<int> s;

	for (i = 0; i < n; i++)
		cin >> a[i];

	s.push(0);
	
	for (i = 1; i < n; i++) {
		if (s.empty())
			s.push(1);
		while (!s.empty() && a[s.top()] < a[i]) {
			ans[s.top()] = a[i];
			s.pop();
		}
		s.push(i);
	}
	while (!s.empty()) {
		ans[s.top()] = -1;
		s.pop();
	}

	for (int i = 0; i < n; i++) {
		cout << ans[i] << ' ';
	}
	cout << '\n';
	return 0;
}