/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2346                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2346                           #+#        #+#      #+#    */
/*   Solved: 2023/09/15 13:38:19 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <deque>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int temp;
    deque<pair<int, int>> balloons;

    cin >> N;

    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        balloons.push_back(make_pair(temp, i + 1));
    }

    while (!balloons.empty())
    {
        temp = balloons.front().first;
        cout << balloons.front().second << ' ';
        balloons.pop_front();
        if (temp > 0)
        {
            for (int i = 0; i < temp - 1; i++)
            {
                balloons.push_back(balloons.front());
                balloons.pop_front();
            }
        }
        else
        {
            for (int i = 0; i < (-1) * temp; i++)
            {
                balloons.push_front(balloons.back());
                balloons.pop_back();
            }
        }
    }

    return 0;
}