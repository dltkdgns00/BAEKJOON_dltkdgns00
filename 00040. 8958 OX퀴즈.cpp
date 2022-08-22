#include <iostream>

using namespace std;
int main()
{
    int N;
    cin >> N;
    string array;
    int score[80]={0};
    int result;
    for(int i=0;i<N;i++)
    {
        cin >> array;
        for(int k=0;k<sizeof(array);k++)
        {
            if(array[k]=='X')
            {
                score[k] = 0;
            }
            else if(score[k]=='0')
            {
                if(array[k-1]=='0')
                    {score[k] = score[k]+1;}
                else
                    {score[k] = 1;}
            }
            result += score[k];
        }
        cout << result << "\n";
    }
}