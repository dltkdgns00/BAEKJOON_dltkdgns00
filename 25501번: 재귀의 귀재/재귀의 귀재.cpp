/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 25501                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/25501                          #+#        #+#      #+#    */
/*   Solved: 2023/09/15 17:45:07 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int isPalindrome(const char *s);
int recursion(const char *s, int l, int r);

int recCount;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    string str;

    cin >> T;

    for (size_t i = 0; i < T; i++)
    {
        cin >> str;
        cout << isPalindrome(str.c_str());
        cout << ' ' << recCount << '\n';
    }

    return 0;
}

int isPalindrome(const char *s)
{
    recCount = 0;
    return recursion(s, 0, strlen(s) - 1);
}

int recursion(const char *s, int l, int r)
{
    recCount++;
    if (l >= r)
        return 1;
    else if (s[l] != s[r])
        return 0;
    else
        return recursion(s, l + 1, r - 1);
}