/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10815                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10815                          #+#        #+#      #+#    */
/*   Solved: 2023/08/02 20:44:03 by dltkdgns00    ###          ###   ##.kr    */
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
    int temp;
    vector<int> vectorN;

    cin >> N;
    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        vectorN.push_back(temp);
    }
    sort(vectorN.begin(), vectorN.end());

    cin >> M;
    for (size_t i = 0; i < M; i++)
    {
        cin >> temp;
        if (binary_search(vectorN.begin(), vectorN.end(), temp))
        {
            cout << '1' << ' ';
        }
        else
        {
            cout << '0' << ' ';
        }
    }
}