/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10773                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10773                          #+#        #+#      #+#    */
/*   Solved: 2023/08/08 19:47:15 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int K;
    int money;
    int result;
    stack<int> accountBook;

    cin >> K;
    while (K--)
    {
        cin >> money;
        if (money == 0)
            accountBook.pop();
        else
            accountBook.push(money);
    }
    result = 0;
    while (!accountBook.empty())
    {
        result += accountBook.top();
        accountBook.pop();
    }

    cout << result;

    return 0;
}