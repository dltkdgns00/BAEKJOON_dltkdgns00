#include <iostream>

using namespace std;

int main()
{
	cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

	int N;
	cin >> N;
	
	int array[N+1];
	int smallest = 1000000;
	int biggest = -1000000;
	
	for(int i=0; i<N; i++)
    {
		cin >> array[i];
		if(smallest > array[i])
        {
			smallest = array[i];
		}
		if(biggest < array[i])
        {
			biggest = array[i];
		}
	}
	
	cout << smallest << " " << biggest << "\n";
	
	return 0;
}