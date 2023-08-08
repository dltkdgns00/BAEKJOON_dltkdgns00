/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 9012                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/9012                           #+#        #+#      #+#    */
/*   Solved: 2023/08/08 20:11:52 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    string input;
    string result;
    stack<char> paranthesis;

    cin >> T;
    for (size_t i = 0; i < T; i++)
    {
        cin >> input;
        result = "YES";
        for (int j = 0; j < input.length(); j++)
        {
            if (input[j] == '(')
                paranthesis.push(input[j]);
            else if (!paranthesis.empty() && input[j] == ')' && paranthesis.top() == '(')
                paranthesis.pop();
            else
            {
                result = "NO";
                break;
            }
        }

        if (!paranthesis.empty())
            result = "NO";

        cout << result << '\n';
        paranthesis = stack<char>();
    }
}
