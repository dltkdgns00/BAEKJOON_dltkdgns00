#include <iostream>

using namespace std;

int	ft_recursive(int nbr);

int	main()
{
	int	N;

	cin >> N;
	ft_recursive(N);
}

int	ft_recursive(int nbr)
{
	int i;

	if (nbr <= 2)
		return (0);
	for (i = 2; i <= nbr; i++)
	{
		if (nbr == i)
		{
			cout << i << endl;
			return (0);
		}
		if (nbr % i == 0)
			break;
	}
	cout << i << endl;
	return (ft_recursive(nbr / i));
}