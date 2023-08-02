#include <iostream>

using namespace std;
int main()
{
    int N;
    cin >> N;
    for(int i=0;i<9;i++)
    {
        int result = (i+1) * N;
        cout << N << " * " << i+1 << " = " << result << endl;
    }
}