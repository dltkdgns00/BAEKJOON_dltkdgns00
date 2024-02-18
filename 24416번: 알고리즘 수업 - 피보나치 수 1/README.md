# 24416번: 알고리즘 수업 - 피보나치 수 1 - <img src="https://static.solved.ac/tier_small/5.svg" style="height:20px" /> Bronze I

<!-- performance -->
### 성능 요약
메모리: 125276 KB, 시간: 1940 ms
<!-- end -->

## 문제

[문제 링크](https://boj.kr/24416)


<p>오늘도 서준이는 동적 프로그래밍&nbsp;수업 조교를 하고 있다.&nbsp;아빠가 수업한&nbsp;내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p>오늘은 <em>n</em>의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여&nbsp;<em>n</em>의 피보나치 수를 구할 경우 코드1&nbsp;코드2 실행&nbsp;횟수를 출력하자.</p>

<p>피보나치 수 재귀호출 의사 코드는&nbsp;다음과 같다.</p>

<pre>fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
&nbsp;   else return (fib(n - 1) + fib(n - 2));
}</pre>

<p>피보나치 수 동적 프로그래밍 의사 코드는&nbsp;다음과 같다.</p>

<pre>fibonacci(n) {
    f[1] &lt;- f[2] &lt;- 1;
&nbsp;   for i &lt;- 3 to n
&nbsp;       f[i] &lt;- f[i - 1] + f[i - 2];  # 코드2
&nbsp;   return f[n];
}</pre>



## 입력


<p>첫째 줄에 <i>n</i>(5&nbsp;≤&nbsp;<em>n</em>&nbsp;≤ 40)이&nbsp;주어진다.</p>



## 출력


<p>코드1 코드2 실행 횟수를 한 줄에&nbsp;출력한다.</p>



## 소스코드

[소스코드 보기](알고리즘%20수업%20-%20피보나치%20수%201.py)