#include <iostream>

using namespace std;
int main()
{
    int hour, minute;
    int before, after;
    cin >> hour >> minute;
    before = (hour*60)+minute;
    if(before - 45<0)
    {
        after = 1440 + minute - 45;
    }
    else
        after = before - 45;
    int result_hour;
    int result_minute;
    result_hour = after / 60;
    result_minute = after % 60;
    cout << result_hour << ' ' << result_minute << endl;
}