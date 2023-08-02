#include <iostream>

using namespace std;

int	main()
{
	int	N;
	int	count;
	int	range;
	int	temp;

	cin >> N;
	count = 1;
	range = 1;
	temp = 1;
	while (1)
	{
		if (range >= N)
			break;
		temp = 6 * (count++);
		range += temp;
	}
	cout << count;
}