#include <iostream>

using namespace std;
int main()
{
    int A, B;
    cout << fixed;
    cout.precision(10);
    cin >> A >> B;
    cout << A+B << endl << A-B << endl << A*B << endl << A/B << endl << A%B << endl;
    return 0;
}