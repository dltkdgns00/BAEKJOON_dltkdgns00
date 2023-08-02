#include <iostream>

int main()
{
    int arr[5];
    int temp;
    int sum = 0;

    for (size_t i = 0; i < 5; i++)
    {
        std::cin >> arr[i];
        sum += arr[i];
    }
    for (size_t j = 0; j < 5; j++)
    {
        for (size_t i = 0; i < 4; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }

    std::cout << (sum / 5) << '\n';
    std::cout << arr[2] << '\n';
}