#include <iostream>

using namespace std;
int main()
{
    int T;
    cin >> T;
    int A[T],B[T];
    for(int i=0;i<T;i++)
    {
        cin >> A[i] >> B[i];
    }
    for(int j=0;j<T;j++)
    {
        cout << A[j]+B[j] << endl;
    }
}