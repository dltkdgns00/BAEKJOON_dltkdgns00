#include <iostream>
#include <vector>
#include <algorithm>

bool cmp(std::vector<int> &v1, std::vector<int> &v2);

int main()
{
    int N;
    std::cin >> N;
    std::vector<std::vector<int>> v;
    v.assign(N, std::vector<int>(2, 0));

    for (int j = 0; j < N; j++)
    {
        for (int i = 0; i < 2; i++)
        {
            std::cin >> v[j][i];
        }
    }
    std::sort(v.begin(), v.end(), cmp);
    for (auto a : v)
    {
        std::cout << a[0] << ' ' << a[1] << '\n';
    }
}

bool cmp(std::vector<int> &v1, std::vector<int> &v2)
{
    if (v1[1] == v2[1])
        return v1[0] < v2[0];
    else
        return v1[1] < v2[1];
}