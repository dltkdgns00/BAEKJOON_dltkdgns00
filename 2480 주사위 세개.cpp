#include <iostream>

using namespace std;
int main()
{
    int dice1;
    int dice2;
    int dice3;

    cin >> dice1 >> dice2 >> dice3;

    int reward;
    if(dice1 == dice2 && dice2 == dice3)
    {
        reward = 10000 + (dice1*1000);
    }
    else if((dice1 == dice2 && dice2 != dice3) || (dice1 == dice3 && dice1 != dice2))
    {
        reward = 1000 + (dice1*100);
    }
    else if(dice2 == dice3 && dice3 != dice1)
    {
        reward = 1000 + (dice2*100);
    }
    else if(dice1 != dice2 && dice2 != dice3 && dice1 > dice2 && dice1 > dice3)
    {
        reward = dice1 * 100;
    }
    else if(dice1 != dice2 && dice2 != dice3 && dice2 > dice1 && dice2 > dice3)
    {
        reward = dice2 * 100;
    }
    else if(dice1 != dice2 && dice2 != dice3 && dice3 > dice2 && dice3 > dice1)
    {
        reward = dice3 * 100;
    }

    cout << reward << endl;
}