/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 15649                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/15649                          #+#        #+#      #+#    */
/*   Solved: 2023/10/03 21:48:29 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <vector>

#define MAX 9

using namespace std;

void dfs(int k, int N, int M, int arr[], bool visited[]);

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

    dfs(0, N, M, arr, visited);

    return 0;
}

void dfs(int k, int N, int M, int arr[], bool visited[])
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
        if (!visited[i])
        {
            visited[i] = true;
            arr[k] = i;
            dfs(k + 1, N, M, arr, visited);
            visited[i] = false;
        }
    }
}