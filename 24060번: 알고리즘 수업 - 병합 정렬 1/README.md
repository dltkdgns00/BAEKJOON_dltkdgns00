# 24060번: 알고리즘 수업 - 병합 정렬 1 - <img src="https://static.solved.ac/tier_small/8.svg" style="height:20px" /> Silver III

<!-- performance -->
### 성능 요약
메모리: 5808 KB, 시간: 132 ms
<!-- end -->

## 문제

[문제 링크](https://boj.kr/24060)


<p>오늘도 서준이는 병합 정렬&nbsp;수업 조교를 하고 있다.&nbsp;아빠가 수업한&nbsp;내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 서로 다른 양의&nbsp;정수가 저장된&nbsp;배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에&nbsp;<em>K&nbsp;</em>번째 저장되는&nbsp;수를 구해서 우리 서준이를 도와주자.</p>

<p>크기가&nbsp;<em>N</em>인 배열에 대한&nbsp;병합 정렬&nbsp;의사 코드는&nbsp;다음과 같다.</p>

<pre>merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p &lt; r) then {
        q &lt;- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
&nbsp;       merge_sort(A, p, q);      # 전반부 정렬
&nbsp;       merge_sort(A, q + 1, r);  # 후반부 정렬
&nbsp;       merge(A, p, q, r);        # 병합
&nbsp;   }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i &lt;- p; j &lt;- q + 1; t &lt;- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
&nbsp;       then tmp[t++] &lt;- A[i++]; # tmp[t] &lt;- A[i]; t++; i++;
&nbsp;       else tmp[t++] &lt;- A[j++]; # tmp[t] &lt;- A[j]; t++; j++;
&nbsp;   }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
&nbsp;       tmp[t++] &lt;- A[i++];
&nbsp;   while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
&nbsp;       tmp[t++] &lt;- A[j++];
&nbsp;   i &lt;- p; t &lt;- 1;
&nbsp;   while (i ≤ r)  # 결과를 A[p..r]에 저장
&nbsp;       A[i++] &lt;- tmp[t++]; 
}</pre>



## 입력


<p>첫째 줄에 배열 A의 크기&nbsp;<em>N</em>(5&nbsp;≤&nbsp;<em>N</em>&nbsp;≤ 500,000), 저장 횟수&nbsp;<em>K</em>(1 ≤&nbsp;<em>K</em>&nbsp;≤ 10<sup>8</sup>)가&nbsp;주어진다.</p>

<p>다음&nbsp;줄에 서로 다른 배열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다.&nbsp;(1&nbsp;≤ A<sub>i</sub>&nbsp;≤ 10<sup>9</sup>)</p>



## 출력


<p>배열 A에 <em>K&nbsp;</em>번째 저장 되는&nbsp;수를 출력한다. 저장 횟수가&nbsp;<em>K&nbsp;</em>보다 작으면 -1을 출력한다.</p>



## 소스코드

[소스코드 보기](알고리즘%20수업%20-%20병합%20정렬%201.cpp)