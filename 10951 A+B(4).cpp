#include <iostream>

using namespace std;
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int A,B;
    int result[100];
    for(int i=0;i<100;i++)
    {
        cin >> A >> B;
        result[i] = A + B;
        if(A==0 && B==0)
            break;
    }
    for(int j=0;j<100;j++)
    {
        if(result[j]==0)
            break;
        else
            cout << result[j] << "\n";
    }
}