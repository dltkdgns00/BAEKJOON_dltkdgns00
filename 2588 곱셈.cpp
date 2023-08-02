#include <iostream>

using namespace std;
int main()
{
    int x,y;
    cin >> x >> y;
    int first_place, second_place, third_place;
    int first_result, second_result, third_result, result;
    first_place = y % 10;
    second_place = (y % 100) / 10;
    third_place = (y % 1000) / 100;
    first_result = first_place * x;
    second_result = second_place * x;
    third_result = third_place * x;
    result = x * y;
    cout << first_result << endl << second_result << endl << third_result << endl << result;
}