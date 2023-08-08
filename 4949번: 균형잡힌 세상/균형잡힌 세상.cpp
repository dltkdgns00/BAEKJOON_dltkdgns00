/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4949                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4949                           #+#        #+#      #+#    */
/*   Solved: 2023/08/08 21:15:36 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string input;
    stack<char> s;
    bool flag;

    while (1)
    {
        getline(cin, input);

        if (input == ".")
            break;

        flag = 0;
        for (int i = 0; i < input.length(); i++)
        {
            if ((input[i] == '(') || (input[i] == '['))
            {
                s.push(input[i]);
            }
            else if (input[i] == ')')
            {
                if (!s.empty() && s.top() == '(')
                {
                    s.pop();
                }
                else
                {
                    flag = 1;
                    break;
                }
            }
            else if (input[i] == ']')
            {
                if (!s.empty() && s.top() == '[')
                {
                    s.pop();
                }
                else
                {
                    flag = 1;
                    break;
                }
            }
        }

        if (flag == 0 && s.empty())
        {
            cout << "yes" << endl;
        }
        else
        {
            cout << "no" << endl;
        }
        s = stack<char>();
    }
}