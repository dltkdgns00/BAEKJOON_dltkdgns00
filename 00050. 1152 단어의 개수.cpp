#include <iostream>
#include <string>

using namespace std;

int	main()
{
	string	str;
	int		count;
	int		i;

	getline(cin, str);
	count = 0;
	if (str[0] == ' ')
		i = 1;
	else
		i = 0;
	while (str[i] != '\0')
	{
		if (str[i] == ' ')
			count++;
		i++;
	}
	if (str[i - 1] == ' ')
		cout << count;
	else
		cout << count + 1;
}