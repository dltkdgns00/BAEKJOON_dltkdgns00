/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11729                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11729                          #+#        #+#      #+#    */
/*   Solved: 2023/10/03 14:56:18 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <cmath>

using namespace std;

void hanoi(int n, int start, int bypass, int dest);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    cout << (int)pow(2, N) - 1 << '\n';
    hanoi(N, 1, 2, 3);

    return 0;
}

void hanoi(int n, int start, int bypass, int dest)
{
    if (n == 1)
    {
        cout << start << ' ' << dest << '\n';
        return;
    }

    hanoi(n - 1, start, dest, bypass);
    cout << start << ' ' << dest << '\n';
    hanoi(n - 1, bypass, start, dest);
}