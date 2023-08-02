#include <iostream>

using namespace std;

int	main()
{
	int	X;
	int	frac;

	cin >> X;
	for (frac = 0; frac < X; frac++)
		X -= frac;
	if (frac % 2 == 1)
		cout << frac + 1 - X << "/" << X;
	if (frac % 2 == 0)
		cout << X << "/" << frac + 1 - X;
	return (0);
}