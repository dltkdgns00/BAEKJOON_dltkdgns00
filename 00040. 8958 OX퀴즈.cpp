#include <iostream>
#include <string>

using namespace std;

int main()
{
	int		N;
	int		result;
	string	OorX;
	int		i;
	int		j;
	int		k;

	cin >> N;
	i = 0;
	while(i < N)
	{
		cin >> OorX;
		result = 0;
		k = 0;
		j = 0;
		while (OorX[j] != '\0')
		{
			if (OorX[j] == 'O')
			{
				k++;
			}
			else if (OorX[j] == 'X')
			{
				k = 0;
			}
			result += k;
			j++;
		}
		cout << result << endl;
		i++;
	}
}