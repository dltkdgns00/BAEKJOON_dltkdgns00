/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10870                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10870                          #+#        #+#      #+#    */
/*   Solved: 2023/09/15 17:10:49 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

using namespace std;

int fibonacci(int N);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    cout << fibonacci(N);

    return 0;
}

int fibonacci(int N)
{
    if (N == 0)
        return 0;
    if (N == 1)
        return 1;
    return fibonacci(N - 2) + fibonacci(N - 1);
}