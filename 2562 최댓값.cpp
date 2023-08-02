#include <iostream>

using namespace std;
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int biggest = -1000000;
    int array[9];
    for(int i=0;i<9;i++)
    {
        cin >> array[i];
        if(biggest < array[i])
        {
			biggest = array[i];
		}
    }
    for(int j=0;j<9;j++)
    {
        if(biggest == array[j])
        cout << biggest << "\n" << j+1;
    }
}