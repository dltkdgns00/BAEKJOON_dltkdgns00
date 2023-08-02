#include <iostream>
#include <string>

using namespace std;

bool	ft_Check(string str);

int	main()
{
	string	str;
	int		N;
	int		count;

	cin >> N;
	count = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> str;
		if(ft_Check(str))
			count++;
	}
	cout << count;
}

bool	ft_Check(string str)
{
	bool	alpha[26] = {false};
	char	temp;

	for (int i = 0; i < str.length(); i++)
	{
		if (alpha[str[i] - 'a'])
			return false;
		else
		{
			temp = str[i];
			alpha[str[i] - 'a'] = true;
			while(str[i])
			{
				if (temp != str[i])
				{
					i--;
					break;
				}
				i++;
			}
		}
	}
	return true;
}