/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 28279                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/28279                          #+#        #+#      #+#    */
/*   Solved: 2023/09/11 19:37:52 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

#define MAX 2000000

using namespace std;

class Deque
{
private:
    int deque[MAX];
    int head = MAX / 2;
    int tail = (MAX / 2) + 1;

public:
    void push_front(int X);
    void push_back(int X);
    int pop_front();
    int pop_back();
    int size();
    int empty();
    int front();
    int back();
};

int Deque::empty()
{
    if (head + 1 == tail)
        return 1;
    else
        return 0;
}

int Deque::size()
{
    return tail - head - 1;
}

int Deque::front()
{
    if (empty())
        return -1;
    else
        return deque[head + 1];
}

int Deque::back()
{
    if (empty())
        return -1;
    else
        return deque[tail - 1];
}

void Deque::push_back(int X)
{
    if (tail < MAX)
        deque[tail++] = X;
}

void Deque::push_front(int X)
{
    if (head > 0)
        deque[head--] = X;
}

int Deque::pop_back()
{
    if (!empty())
        return deque[--tail];
    else
        return -1;
}

int Deque::pop_front()
{
    if (!empty())
        return deque[++head];
    else
        return -1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Deque dq;
    int N;
    int temp;

    cin >> N;

    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        if (temp == 1)
        {
            cin >> temp;
            dq.push_front(temp);
        }
        else if (temp == 2)
        {
            cin >> temp;
            dq.push_back(temp);
        }
        else if (temp == 3)
        {
            cout << dq.pop_front() << '\n';
        }
        else if (temp == 4)
        {
            cout << dq.pop_back() << '\n';
        }
        else if (temp == 5)
        {
            cout << dq.size() << '\n';
        }
        else if (temp == 6)
        {
            cout << dq.empty() << '\n';
        }
        else if (temp == 7)
        {
            cout << dq.front() << '\n';
        }
        else if (temp == 8)
        {
            cout << dq.back() << '\n';
        }
    }

    return 0;
}