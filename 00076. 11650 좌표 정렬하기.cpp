#include <iostream>
#include <vector>
#include <algorithm>

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
    std::sort(v.begin(), v.end());
    for (auto a : v)
    {
        std::cout << a[0] << ' ' << a[1] << '\n';
    }
}