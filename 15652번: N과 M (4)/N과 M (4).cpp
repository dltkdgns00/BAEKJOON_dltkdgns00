/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 15652                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/15652                          #+#        #+#      #+#    */
/*   Solved: 2023/11/07 10:15:21 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

#define MAX 9

using namespace std;

void dfs(int k, int cnt, int N, int M, int arr[], bool visited[]);

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
    bool visited[MAX] = {
        0,
    };

    cin >> N >> M;

    dfs(1, 0, N, M, arr, visited);

    return 0;
}

void dfs(int k, int cnt, int N, int M, int arr[], bool visited[])
{
    if (cnt == M)
    {
        for (size_t i = 0; i < M; i++)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    for (size_t i = k; i <= N; i++)
    {
        visited[i] = true;
        arr[cnt] = i;
        dfs(i, cnt + 1, N, M, arr, visited);
        visited[i] = false;
    }
}