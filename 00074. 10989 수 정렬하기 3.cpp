// #include <iostream>

// int main()
// {
//     cin.tie(NULL);
//     cout.tie(NULL);
//     ios::sync_with_stdio(false);

//     int N;
//     std::cin >> N;

//     int arr[N];
//     int biggest = 0;

//     for (size_t i = 0; i < N; i++)
//     {
//         std::cin >> arr[i];
//         if (biggest < arr[i])
//         {
//             biggest = arr[i];
//         }
//     }

//     int countArr[biggest + 1];
//     for (size_t i = 0; i < biggest; i++)
//     {
//         countArr[i] = 0;
//     }

//     for (size_t i = 0; i < (biggest + 1); i++)
//     {
//         for (size_t j = 0; j < N; j++)
//         {
//             if (arr[j] == i)
//             {
//                 countArr[i]++;
//             }
//         }
//     }

//     for (size_t i = 0; i < (biggest + 1); i++)
//     {
//         for (size_t j = 0; j < countArr[i]; j++)
//         {
//             std::cout << i << '\n';
//         }
//     }
// }

#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios::sync_with_stdio(false);

    int N;
    std::cin >> N;

    int arr[10001] = {
        0,
    };
    for (size_t i = 0; i < N; i++)
    {
        int temp;
        std::cin >> temp;
        arr[temp]++;
    }
    for (size_t i = 0; i < 10001; i++)
    {
        for (size_t j = 0; j < arr[i]; j++)
        {
            std::cout << i << '\n';
        }
    }
}