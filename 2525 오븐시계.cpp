#include <iostream>

using namespace std;
int main()
{
    int current_hour, current_minute;
    int duration_time;
    int before, after;
    cin >> current_hour >> current_minute >> duration_time;
    before = (current_hour*60)+current_minute;
    if(before + duration_time >= 1440)
    {
        after = before + duration_time - 1440;
    }
    else
        after = before + duration_time;
    int result_hour;
    int result_minute;
    result_hour = after / 60;
    result_minute = after % 60;
    cout << result_hour << ' ' << result_minute << endl;
}