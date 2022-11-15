#include <iostream>

using namespace std;

int	ft_is_prime(int nb);

int	main()
{
	int M;
	int	N;
	int	sum;
	int	count;
	int	arr[10000];
	int	j;

	cin >> M >> N;

	sum = 0;
	count = 0;
	j = 0;
	for (int i = M; i <= N; i++)
	{
		if (ft_is_prime(i) == 1)
		{
			sum += i;
			count++;
			arr[j] = i;
			j++;
		}

	}
	if (count == 0)
	{
		cout << -1;
		return (0);
	}

	cout << sum << endl << arr[0];
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