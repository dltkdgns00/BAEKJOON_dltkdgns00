#include <iostream>

int main()
{
    int N;
    std::cin >> N;

    int arr[N];
    int temp;

    for (size_t i = 0; i < N; i++)
    {
        std::cin >> arr[i];
    }
    for (size_t j = 0; j < N; j++)
    {
        for (size_t i = 0; i < N - 1; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }

    for (size_t i = 0; i < N; i++)
    {
        std::cout << arr[i] << '\n';
    }
}