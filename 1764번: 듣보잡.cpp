/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1764                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1764                           #+#        #+#      #+#    */
/*   Solved: 2023/08/05 00:40:39 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int M;
    string temp;
    vector<string> neverHeard;
    vector<string> result;

    cin >> N >> M;
    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        neverHeard.push_back(temp);
    }
    sort(neverHeard.begin(), neverHeard.end());

    for (size_t i = 0; i < M; i++)
    {
        cin >> temp;
        if (binary_search(neverHeard.begin(), neverHeard.end(), temp))
        {
            result.push_back(temp);
        }
    }

    sort(result.begin(), result.end());
    cout << result.size() << '\n';
    for (size_t i = 0; i < result.size(); i++)
    {
        cout << result[i] << '\n';
    }

    return 0;
}