/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1620                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1620                           #+#        #+#      #+#    */
/*   Solved: 2023/08/03 20:43:45 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <typeinfo>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int M;
    string pokemon;
    map<string, int> pokedex;
    vector<string> name;
    string input;

    cin >> N;
    cin >> M;
    for (size_t i = 1; i <= N; i++)
    {
        cin >> pokemon;
        pokedex.insert({pokemon, i});
        name.push_back(pokemon);
    }
    for (size_t i = 0; i < M; i++)
    {
        cin >> input;

        if (isdigit(input[0]))
        {
            cout << name[stoi(input) - 1] << '\n';
        }
        else
        {
            cout << pokedex.find(input)->second << '\n';
        }
    }

    return 0;
}