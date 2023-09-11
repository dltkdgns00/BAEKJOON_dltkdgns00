/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 18258                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/18258                          #+#        #+#      #+#    */
/*   Solved: 2023/09/07 19:06:00 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>

#define MAX 2000000

using namespace std;

class Queue
{
private:
    int queue[MAX];
    int head = 0;
    int tail = 0;

public:
    void push(int X);
    int pop();
    int size();
    int empty();
    int front();
    int back();
};

int Queue::empty()
{
    if (head == tail)
        return 1;
    else
        return 0;
}

int Queue::size()
{
    return tail - head;
}

int Queue::front()
{
    if (empty())
        return -1;
    else
        return queue[head];
}

int Queue::back()
{
    if (empty())
        return -1;
    else
        return queue[tail - 1];
}

void Queue::push(int X)
{
    queue[tail] = X;
    tail++;
}

int Queue::pop()
{
    if (!empty())
        return queue[head++];
    else
        return -1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Queue queue;
    int N;
    int X;
    string temp;

    cin >> N;
    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        if (temp == "push")
        {
            cin >> X;
            queue.push(X);
        }
        else if (temp == "pop")
        {
            cout << queue.pop() << '\n';
        }
        else if (temp == "size")
            cout << queue.size() << '\n';
        else if (temp == "empty")
        {
            cout << queue.empty() << '\n';
        }
        else if (temp == "front")
        {
            if (!queue.empty())
                cout << queue.front() << '\n';
            else
                cout << -1 << '\n';
        }
        else if (temp == "back")
        {
            if (!queue.empty())
                cout << queue.back() << '\n';
            else
                cout << -1 << '\n';
        }
    }
    return 0;
}