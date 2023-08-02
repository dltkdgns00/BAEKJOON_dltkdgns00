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
	for (i = 0; str[i] != '\0'; i++)
	{
		if (str[i] == 'c' && (str[i + 1] == '=' || str[i + 1] == '-'))
			i++;
		if (str[i] == 'd' && str[i + 1] == '-')
			i++;
		if (str[i] == 'd' && str[i + 1] == 'z' && str[i + 2] == '=')
			i += 2;
		if (str[i] == 'l' && str[i + 1] == 'j')
			i++;
		if (str[i] == 'n' && str[i + 1] == 'j')
			i++;
		if (str[i] == 's' && str[i + 1] == '=')
			i++;
		if (str[i] == 'z' && str[i + 1] == '=')
			i++;
		count++;
	}
	cout << count;
}