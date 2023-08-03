/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 14425                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/14425                          #+#        #+#      #+#    */
/*   Solved: 2023/08/03 19:25:53 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int M;
    int count;
    string temp;
    vector<string> vectorN;

    cin >> N;
    cin >> M;
    for (size_t i = 0; i < N; i++)
    {
        cin >> temp;
        vectorN.push_back(temp);
    }
    sort(vectorN.begin(), vectorN.end());
    count = 0;
    for (size_t i = 0; i < M; i++)
    {
        cin >> temp;
        if (binary_search(vectorN.begin(), vectorN.end(), temp))
            count++;
    }
    cout << count;
}