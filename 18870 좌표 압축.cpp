#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> v(N);
    vector<int> idx(N);

    for (int i = 0; i < N; i++)
    {
        cin >> v[i];
        idx[i] = v[i];
    }
    sort(v.begin(), v.end());
    v.resize(unique(v.begin(), v.end()) - v.begin());
    for (int a : idx)
    {
        int pos = lower_bound(v.begin(), v.end(), a) - v.begin();
        cout << pos << ' ';
    }
    return 0;
}