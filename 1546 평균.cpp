#include <iostream>

using namespace std;

int main()
{
    int N = 0;
    double biggest, sum=0;

    cin >> N;

    double array[N];

    for(int i=0;i<N;i++)
    {
        cin>>array[i];
        if(biggest < array[i])
            biggest = array[i];
    }
    for(int j=0;j<N;j++)
    {
        array[j] = array[j]/biggest*100.0;
        sum += array[j];
    }
    cout << sum/(double)N;
    return 0;
}