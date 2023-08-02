#include <iostream>

using namespace std;

int	main()
{
	int	A;
	int	B;
	int	C;

	cin >> A >> B >> C;
	if (C <= B)
	{
		cout << -1;
		return 0;
	}
	cout << (A / (C - B)) + 1;
}