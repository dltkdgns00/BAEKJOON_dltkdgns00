/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1269                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1269                           #+#        #+#      #+#    */
/*   Solved: 2023/08/05 01:07:31 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int main()
// {
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);

//     int N;
//     int M;
//     int temp;
//     int ans;
//     vector<int> A;

//     cin >> N >> M;
//     for (size_t i = 0; i < N; i++)
//     {
//         cin >> temp;
//         A.push_back(temp);
//     }
//     sort(A.begin(), A.end());
//     ans = 0;
//     for (size_t i = 0; i < M; i++)
//     {
//         cin >> temp;
//         if (binary_search(A.begin(), A.end(), temp))
//         {
//             ans++;
//         }
//     }
//     cout << M + N - ans * 2;

//     return 0;
// } // mem: 3688, time: 72ms

#include <iostream>
#include <set>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int M;
    int temp;
    set<int> s;

    cin >> N >> M;
    for (size_t i = 0; i < N + M; i++)
    {
        cin >> temp;
        if (s.find(temp) != s.end())
        {
            s.erase(temp);
        }
        else
        {
            s.insert(temp);
        }
    }
    cout << s.size();

    return 0;
} // mem: 20768kb, time: 240ms