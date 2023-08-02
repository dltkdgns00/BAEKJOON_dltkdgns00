#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

bool cmp(std::pair<int, std::string> a, std::pair<int, std::string> b);

int main()
{
    int N;
    std::cin >> N;
    std::vector<std::pair<int, std::string>> v;
    for (size_t i = 0; i < N; i++)
    {
        std::pair<int, std::string> p;
        std::cin >> p.first >> p.second;
        v.push_back(p);
    }
    stable_sort(v.begin(), v.end(), cmp);
    for (int i = 0; i < N; i++)
        std::cout << v[i].first << ' ' << v[i].second << '\n';
}

bool cmp(std::pair<int, std::string> a, std::pair<int, std::string> b)
{
    return a.first < b.first;
}