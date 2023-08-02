#include <iostream>

using namespace std;
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int X;
    int result[42]={0};
    int count=0;
    int temp=0;
    for(int i=0;i<10;i++)
    {
        cin >> X;
        result[X%42] = 1;
    }
    for(int j=0;j<42;j++)
    {
        if(result[j]==1)
            count++;
    }

    cout << count;
}