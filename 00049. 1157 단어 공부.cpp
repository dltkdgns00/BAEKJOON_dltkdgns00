#include <iostream>
#include <string>

using namespace std;

int main()
{
	string	S;
	int		alpha[26] = { 0, };
	int		max;
	int		maxidx;
	int		count;

	cin >> S;
	for (int i = 0; S[i] != '\0'; i++)
	{
		if (S[i] >= 'A' && S[i] <= 'Z')
			alpha[S[i] - 65] += 1;
		if (S[i] >= 'a' && S[i] <= 'z')
			alpha[S[i] - 97] += 1;
	}
	max = 0;
	maxidx = 0;
	for (int j = 0; j < 26; j++)
	{
		if (alpha[j] > max)
		{
			max = alpha[j];
			maxidx = j;
		}
	}
	count = 0;
	for (int k = 0; k < 26; k++)
	{
		if (alpha[k] == max)
			count++;
	}
	if (count > 1)
		cout << '?';
	else
		cout << (char)(maxidx + 65);
}