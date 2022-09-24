#include <iostream>
#include <string>

using namespace std;

int	main()
{
	string	str;
	int		result;

	cin >> str;
	result = 0;
	for (int i = 0; str[i] != '\0'; i++)
	{
		if (str[i] >= 'A' && str[i] <= 'C')
			result += 3;
		if (str[i] >= 'D' && str[i] <= 'F')
			result += 4;
		if (str[i] >= 'G' && str[i] <= 'I')
			result += 5;
		if (str[i] >= 'J' && str[i] <= 'L')
			result += 6;
		if (str[i] >= 'M' && str[i] <= 'O')
			result += 7;
		if (str[i] >= 'P' && str[i] <= 'S')
			result += 8;
		if (str[i] >= 'T' && str[i] <= 'V')
			result += 9;
		if (str[i] >= 'W' && str[i] <= 'Z')
			result += 10;
	}
	cout << result;
}