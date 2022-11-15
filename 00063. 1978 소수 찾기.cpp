#include <iostream>

using namespace std;

int	ft_is_prime(int nb);

int	main()
{
	int	N;
	int	nb;
	int	count;
	
	cin >> N;

	count = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> nb;
		if (ft_is_prime(nb) == 1)
			count++;
	}

	cout << count;
}

int	ft_is_prime(int nb)
{
	long	i;

	if (nb == 0 || nb == 1)
		return (0);
	i = 2;
	while (i * i <= nb)
	{
		if (i != nb && nb % i == 0)
			return (0);
		i++;
	}
	return (1);
}