#include <iostream>

using namespace std;
int main()
{
    int X;
    int N;
    cin >> X;
    cin >> N;
    int a[N],b[N];
    int sum=0;
    for(int i=0;i<N;i++)
    {
        cin >> a[i] >> b[i];
        sum += a[i]*b[i];
    }
    if(sum==X)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
}