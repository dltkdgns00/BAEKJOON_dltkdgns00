#include <iostream>

using namespace std;

int main()
{
	int		N;
	int		C;
	int		sum;
	int		score[1000];
	float	w;
	float	result;
	
	cin >> C;
	for (int i = 0; i < C; i++)
	{
		cin >> N;
		sum = 0;
		for (int j = 0; j < N; j++)
		{
			cin >> score[j];
			sum += score[j];
		}
		w = 0;
		for (int l = 0; l < N; l++)
		{
			if (score[l] > sum / N)
				w++;
		}
		result = w / N * 100;
		printf("%0.3f", result);
		cout << '%' << endl;
	}
}