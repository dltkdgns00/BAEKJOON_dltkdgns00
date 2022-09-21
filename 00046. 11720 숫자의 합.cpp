#include <iostream>
#include <string>

using namespace std;

int main()
{
	int		N;
	string	nbrs;
	int		result;

	cin >> N >> nbrs;
	result = 0;
	for (int i = 0; i < N; i++)
		result += nbrs[i] - 48;
	cout << result;
}