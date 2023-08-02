#include <iostream>

using namespace std;

int	ft_is_prime(int nb);

int	main()
{
	int	n;
	int	count;

	while (1)
	{
		cin >> n;

		if (n == 0)
			break;
		count = 0;
		for (int i = n + 1; i <= 2 * n; i++)
		{
			if (ft_is_prime(i) == 1)
				count++;
		}
		cout << count << endl;
	}
}

int	ft_is_prime(int nb)
{
	long	i;

	if (nb == 1)
		return (0);
	i = 2;
	while (i * i <= nb)
	{
		if (nb % i == 0)
			return (0);
		i++;
	}
	return (1);
}