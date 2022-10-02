#include <iostream>

using namespace std;

int	main()
{
	int	T;
	int	k;
	int	n;
	int result[15][15];

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> k;
		cin >> n;
		for (int j = 0; j <= k; j++)
		{
			for (int l = 1; l <= n; l++)
			{
				if (j == 0)
					result[0][l] = l;
				else if (l == 1)
					result[j][1] = 1;
				else
					result[j][l] = result[j][l - 1] + result[j - 1][l];
			}
		}
		cout << result[k][n] << endl;
	}
}