/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1065                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1065                           #+#        #+#      #+#    */
/*   Solved: 2023/08/08 23:16:57 by dltkdgns00    ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>

using namespace std;

int main()
{
    int N;
    int count;

    cin >> N;
    count = 0;
    for (int i = 1; i <= N; i++)
    {
        if (i < 100)
            count++;
        else if (((i / 100) - ((i % 100) / 10)) == (((i % 100) / 10) - (i % 10)))
            count++;
    }
    cout << count << endl;
}