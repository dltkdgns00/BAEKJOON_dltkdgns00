/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 4779                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/4779                           #+#        #+#      #+#    */
/*   Solved: 2023/09/20 18:25:29 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <cmath>

using namespace std;

void cantor(int N);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;

    while (cin >> N)
    {
        cantor(N);
        cout << '\n';
    }

    return 0;
}

void cantor(int N)
{
    if (N == 0)
    {
        cout << '-';
        return;
    }

    cantor(N - 1);
    for (size_t i = 0; i < pow(3, N - 1); i++)
    {
        cout << ' ';
    }
    cantor(N - 1);
}