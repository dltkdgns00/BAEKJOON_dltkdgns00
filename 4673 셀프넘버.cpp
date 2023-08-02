#include <iostream>

using namespace std;

int	ft_is_self_nbr(int nbr);
int	ft_sum(int nbr);

int	main()
{
	for (int i = 1; i <= 10000; i++)
	{
		if (ft_is_self_nbr(i) == 1)
			cout << i << endl;
	}
}

int	ft_is_self_nbr(int nbr)
{
	for (int i = 0; i < nbr; i++)
	{
		if (ft_sum(i) == nbr)
			return (0);
	}
	return (1);
}

int	ft_sum(int nbr)
{
	int	sum;

	sum = nbr;
	while (nbr > 0)
	{
		sum += nbr % 10;
		nbr /= 10;
	}
	return (sum);
}