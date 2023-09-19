/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 24060                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/24060                          #+#        #+#      #+#    */
/*   Solved: 2023/09/19 18:56:22 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

using namespace std;

void merge_sort(int *A, int start, int end, int K);
void merge(int *A, int p, int q, int r, int K);
int inputcnt = 0;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int K;
    int *A;

    cin >> N >> K;

    A = new int[N];
    for (int i = 0; i < N; i++)
        cin >> A[i];

    merge_sort(A, 0, N - 1, K);
    if (inputcnt < K)
        cout << -1;

    return 0;
}

void merge_sort(int *A, int start, int end, int K)
{
    int p = start, r = end, q;
    if (p < r)
    {
        q = (p + r) / 2;
        merge_sort(A, p, q, K);
        merge_sort(A, q + 1, r, K);
        merge(A, p, q, r, K);
    }
}

void merge(int *A, int p, int q, int r, int K)
{
    int tmp[r + 2];
    int i = p, j = q + 1, t = 1;
    while (i <= q && j <= r)
    {
        if (A[i] <= A[j])
            tmp[t++] = A[i++];
        else
            tmp[t++] = A[j++];
    }
    while (i <= q)
        tmp[t++] = A[i++];
    while (j <= r)
        tmp[t++] = A[j++];
    i = p, t = 1;
    while (i <= r)
    {
        A[i++] = tmp[t++];
        if (++inputcnt == K)
            cout << tmp[t - 1];
    }
}