/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 12789                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/12789                          #+#        #+#      #+#    */
/*   Solved: 2023/08/09 19:23:09 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int temp;
    int goal;
    int i;
    vector<int> line;
    stack<int> templine;

    cin >> N;
    for (i = 0; i < N; i++)
    {
        cin >> temp;
        line.push_back(temp);
    }
    goal = 1;
    i = 0;
    while (1)
    {
        if (i < N && line[i] == goal)
        {
            i++;
            goal++;
        }
        else if (!templine.empty() && templine.top() == goal)
        {
            goal++;
            templine.pop();
        }
        else if (i < N)
        {
            templine.push(line[i]);
            i++;
        }
        else if (goal > N)
        {
            cout << "Nice";
            return 0;
        }
        else
        {
            cout << "Sad";
            return 0;
        }
    }
    return 0;
}