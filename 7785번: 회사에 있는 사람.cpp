/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 7785                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/7785                           #+#        #+#      #+#    */
/*   Solved: 2023/08/03 19:51:16 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    int n;
    string name;
    string EorL;
    map<string, string, greater<>> log;

    cin >> n;
    for (size_t i = 0; i < n; i++)
    {
        cin >> name;
        cin >> EorL;
        if (log.find(name) != log.end())
        {
            log.erase(name);
        }
        else
        {
            log.insert({name, EorL});
        }
    }
    for (auto iter : log)
    {
        cout << iter.first << "\n";
    }

    return 0;
}