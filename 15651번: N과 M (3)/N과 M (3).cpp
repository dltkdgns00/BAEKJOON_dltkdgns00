/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 15651                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/15651                          #+#        #+#      #+#    */
/*   Solved: 2023/11/06 21:35:59 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

#define MAX 7

using namespace std;

void dfs(int k, int N, int M, int arr[]);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int M;
    int arr[MAX] = {
        0,
    };

    cin >> N >> M;

    dfs(0, N, M, arr);

    return 0;
}

void dfs(int k, int N, int M, int arr[])
{
    if (k == M)
    {
        for (size_t i = 0; i < M; i++)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    for (size_t i = 1; i <= N; i++)
    {
        arr[k] = i;
        dfs(k + 1, N, M, arr);
    }
}