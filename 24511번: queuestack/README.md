# 24511번: queuestack - <img src="https://static.solved.ac/tier_small/8.svg" style="height:20px" /> Silver III

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/24511)


<p>한가롭게 방학에 놀고 있던 도현이는 갑자기 재밌는 자료구조를 생각해냈다. 그 자료구조의 이름은 queuestack이다.</p>

<p>queuestack의 구조는 다음과 같다.&nbsp;$1$번, $2$번, ... , $N$번의 자료구조(queue 혹은 stack)가&nbsp;나열되어있으며, 각각의 자료구조에는 한 개의 원소가 들어있다.</p>

<p>queuestack의 작동은 다음과 같다.</p>

<ul>
<li>$x_0$을 입력받는다.</li>
<li>$x_0$을 $1$번 자료구조에 삽입한 뒤 $1$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_1$이라&nbsp;한다.</li>
<li>$x_1$을&nbsp;$2$번 자료구조에 삽입한 뒤 $2$번 자료구조에서 원소를 pop한다.&nbsp;그때 pop된 원소를 $x_2$이라&nbsp;한다.</li>
<li>...</li>
<li>$x_{N-1}$을&nbsp;$N$번 자료구조에 삽입한 뒤 $N$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_N$이라&nbsp;한다.</li>
<li>$x_N$을&nbsp;리턴한다.</li>
</ul>

<p>도현이는 길이 $M$의 수열 $C$를 가져와서 수열의 원소를 앞에서부터 차례대로&nbsp;queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다. (예제 $1$ 참고)</p>

<p>queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자.</p>



## 입력

첫째 줄에 queuestack을 구성하는 자료구조의 개수 $N$이 주어진다. ($1 \leq N \leq 100\,000$)

## 출력

수열 $C$의 원소를 차례대로 queuestack에 삽입했을 때의&nbsp;리턴값을 공백으로 구분하여 출력한다.

## 소스코드

[소스코드 보기](queuestack.cpp)