#include <iostream>

using namespace std;

void	ft_print_width(int nbr);

int	main()
{
	int	T;
	int	H;
	int	W;
	int	N;
	int	height;
	int	width;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> H >> W >> N;
		height = N % H;
		width = N / H;
		if (height > 0)
			width++;
		else
			height = H;
		cout << height;
		ft_print_width(width);
	}
}

void	ft_print_width(int nbr)
{
	cout << nbr / 10 << nbr % 10 << endl;
}