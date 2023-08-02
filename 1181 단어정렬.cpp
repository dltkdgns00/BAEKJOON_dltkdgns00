#include <iostream>
#include <algorithm>

bool cmp(std::string str1, std::string str2);

int main()
{
    int N;
    std::cin >> N;
    std::string str[N];
    int arr[N];

    for (size_t i = 0; i < N; i++)
    {
        std::cin >> str[i];
        arr[i] = str[i].length();
    }
    std::sort(str, str + N, cmp);
    std::string before;
    for (size_t i = 0; i < N; i++)
    {
        if (before == str[i])
            continue;
        std::cout << str[i] << '\n';
        before = str[i];
    }
}

bool cmp(std::string str1, std::string str2)
{
    if (str1.length() != str2.length())
        return str1.length() < str2.length();
    else
        return str1 < str2;
}