#include <iostream>

using namespace std;

int	main()
{
	int	A;
	int	B;
	int	V;

	cin >> A >> B >> V;
	if ((V - A) % (A - B) == 0)
		cout << (V - A) / (A - B) + 1;
	else
		cout << (V - A) / (A - B) + 2;
}