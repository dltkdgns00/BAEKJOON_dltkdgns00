/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 15650                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/15650                          #+#        #+#      #+#    */
/*   Solved: 2023/11/06 20:11:32 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

using namespace std;

#define MAX 9

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
        if (!visited[i])
        {
            visited[i] = true;
            arr[cnt] = i;
            dfs(i + 1, cnt + 1, N, M, arr, visited);
            visited[i] = false;
        }
    }
}