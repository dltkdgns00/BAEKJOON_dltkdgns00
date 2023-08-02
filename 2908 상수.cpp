#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int	main()
{
	string	num1;
	string	num2;
	int		i_num1;
	int		i_num2;

	cin >> num1 >> num2;
	for (int i = 0; i < num1.length() / 2; i++)
	{
		swap(num1[i], num1[num1.length() - i - 1]);
	}
	for (int i = 0; i < num2.length() / 2; i++)
	{
		swap(num2[i], num2[num2.length() - i - 1]);
	}
	i_num1 = stoi(num1);
	i_num2 = stoi(num2);
	if (i_num1 > i_num2)
		cout << i_num1;
	else if (i_num2 > i_num1)
		cout << i_num2;
}