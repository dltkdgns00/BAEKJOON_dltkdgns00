/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2164                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2164                           #+#        #+#      #+#    */
/*   Solved: 2023/09/11 17:31:33 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    queue<int> deck;
    int N;

    cin >> N;
    for (size_t i = 1; i <= N; i++)
    {
        deck.push(i);
    }

    while (deck.size() != 1)
    {
        deck.pop();
        deck.push(deck.front());
        deck.pop();
    }

    cout << deck.front();

    return 0;
}