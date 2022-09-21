#include <iostream>
#include <string>

using namespace std;

int	ft_verify(string S, char c);

int main()
{
	string	S;

	cin >> S;
	for (char c = 'a'; c <= 'z'; c++)
	{
		cout << ft_verify(S, c) << ' ';
	}
}

int	ft_verify(string S, char c)
{
	for (int i = 0; S[i] != '\0'; i++)
	{
		if (c == S[i])
			return (i);
	}
	return (-1);
}