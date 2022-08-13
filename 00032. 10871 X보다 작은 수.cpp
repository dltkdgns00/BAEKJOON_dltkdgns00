#include <iostream>

using namespace std;
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int N,X;
    int A[N];
    cin >> N >> X;
    for(int i=0;i<N;i++)
    {
        cin >> A[i];
    }
    for(int j=0;j<N;j++)
    {
        if(A[j]<X)
        {
            cout << A[j] << ' ';
        }
    }
}