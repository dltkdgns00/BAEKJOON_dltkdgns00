#include <iostream>

using namespace std;

int	ft_is_prime(int nb);

int	main()
{
	int M;
	int	N;

	cin >> M >> N;

	for (int i = M; i <= N; i++)
	{
		if (ft_is_prime(i) == 1)
			cout << i << endl;
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