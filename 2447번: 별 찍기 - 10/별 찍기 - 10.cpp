/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2447                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2447                           #+#        #+#      #+#    */
/*   Solved: 2023/09/20 19:37:05 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

using namespace std;

void star(int N, int i, int j);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;

    cin >> N;

    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
            star(N, i, j);
        cout << '\n';
    }

    return 0;
}

void star(int N, int i, int j)
{
    if ((i / N) % 3 == 1 && (j / N) % 3 == 1)
    {
        cout << ' ';
    }
    else
    {
        if (N / 3 == 0)
            cout << '*';
        else
            star(N / 3, i, j);
    }
}