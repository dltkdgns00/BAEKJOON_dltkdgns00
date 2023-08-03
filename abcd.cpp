#include <iostream>
#include <string>
#include <map>
using namespace std;

int n, m;
string str;
map<string, int> num;
string name[100001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        cin >> str;
        num.insert({str, i});
        name[i] = str;
    }
    for (int i = 1; i <= m; i++)
    {
        cin >> str;
        if (isdigit(str[0]))
        {
            cout << name[stoi(str)] << '\n';
        }
        else
        {
            cout << num.find(str)->second << '\n';
        }
    }
}