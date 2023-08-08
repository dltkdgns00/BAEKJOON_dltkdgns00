/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 28278                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/28278                          #+#        #+#      #+#    */
/*   Solved: 2023/08/08 16:02:57 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

#define MAX 1000000

using namespace std;

class Stack
{
private:
    int stack[MAX];
    int top = -1;

public:
    int empty();
    int size();
    int peek();
    void push(int number);
    int pop();
};

int Stack::empty()
{
    if (top == -1)
        return 1;
    else
        return 0;
}

int Stack::size()
{
    return top + 1;
}

int Stack::peek()
{
    if (!empty())
        return stack[top];
    else
        return top;
}

void Stack::push(int number)
{
    if (top < MAX)
    {
        top++;
        stack[top] = number;
    }
}

int Stack::pop()
{
    if (!empty())
    {
        top--;
        return stack[top + 1];
    }
    else
        return top;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Stack stack;
    int N;
    int command;
    int X;

    cin >> N;
    while (N--)
    {
        cin >> command;
        if (command == 1)
        {
            cin >> X;
            stack.push(X);
        }
        else if (command == 2)
        {
            cout << stack.pop() << '\n';
        }
        else if (command == 3)
        {
            cout << stack.size() << '\n';
        }
        else if (command == 4)
        {
            cout << stack.empty() << '\n';
        }
        else if (command == 5)
        {
            cout << stack.peek() << '\n';
        }
    }

    return 0;
}