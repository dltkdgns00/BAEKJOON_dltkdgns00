#include <iostream>
#define MAX 100000

using namespace std;
int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;

    int temp;
    temp = N;
    int i;
    for(i=1;i<MAX;i++)
    {
        temp = ((temp%10)*10)+(((temp/10)+(temp%10))%10);
        if(N==temp)
        {
            break;
        }
    }
    cout << i;
}