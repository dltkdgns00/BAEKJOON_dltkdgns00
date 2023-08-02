#include <iostream>

using namespace std;

int main()
{
    int chess[6]= { 1,1,2,2,2,8 };
    int input[6];
    int output[6];
    for(int i=0;i<=5;i++)
    {
        cin >> input[i];
    }
    for(int n=0;n<=5;n++)
    {
        output[n] = chess[n]-input[n];
    }
    for(int j=0;j<=5;j++)
    {
        cout << output[j] << ' ';
    }
}