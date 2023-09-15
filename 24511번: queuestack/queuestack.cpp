/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 24511                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/24511                          #+#        #+#      #+#    */
/*   Solved: 2023/09/15 14:46:48 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int temp;
    vector<bool> flag;
    deque<int> dq;

    cin >> N;
    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        flag.push_back(temp);
    }

    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        if (flag[i] == 0)
            dq.push_back(temp);
    }

    cin >> N;
    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        dq.push_front(temp);
        cout << dq.back() << " ";
        dq.pop_back();
    }

    return 0;
}