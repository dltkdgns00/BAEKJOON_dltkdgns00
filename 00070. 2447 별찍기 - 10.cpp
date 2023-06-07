#include <iostream>

void drawstar(int N, int j);

int main()
{
    int N;

    std::cin >> N;

    drawstar(N, 0);
    return 0;
}

void drawstar(int N, int j)
{
    for (int i = 0; i <= 3; i++)
    {
        if (i == 3)
            std::cout << std::endl;
        else
            std::cout << '*';
    }
    for (int i = 0; i <= 3; i++)
    {

        if (i == 1)
            std::cout << ' ';
        else if (i == 3)
            std::cout << std::endl;
        else
            std::cout << '*';
    }
    for (int i = 0; i <= 3; i++)
    {
        if (i == 3)
            std::cout << std::endl;
        else
            std::cout << '*';
    }
    if (j < N / 3)
    {
        j++;
        drawstar(N, j);
    }
}