/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11866                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11866                          #+#        #+#      #+#    */
/*   Solved: 2023/09/11 17:58:42 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    queue<int> circle;
    vector<int> josephus;
    int N;
    int K;

    cin >> N;
    cin >> K;

    for (size_t i = 1; i <= N; i++)
    {
        circle.push(i);
    }

    while (!circle.empty())
    {
        for (size_t i = 0; i < K - 1; i++)
        {
            circle.push(circle.front());
            circle.pop();
        }
        josephus.push_back(circle.front());
        circle.pop();
    }

    cout << '<';
    for (size_t i = 0; i < N; i++)
    {
        cout << josephus[i];
        if (!(i == N - 1))
        {
            cout << ", ";
        }
    }
    cout << '>';

    return 0;
}