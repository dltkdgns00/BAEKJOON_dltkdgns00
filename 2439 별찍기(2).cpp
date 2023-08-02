#include <iostream>

using namespace std;
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;
    for(int k=N;k>0;k--)
    {
        for(int l=0;l<k-1;l++)
        {
            cout << ' ';
        }
        for(int i=N;i>=k;i--)
        {
            cout << '*';
        }
        cout << "\n";
    }
}