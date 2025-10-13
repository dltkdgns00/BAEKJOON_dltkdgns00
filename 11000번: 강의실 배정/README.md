# 11000번: 강의실 배정 - <img src="https://static.solved.ac/tier_small/12.svg" style="height:20px" /> Gold IV

<!-- performance -->
### 성능 요약
메모리: 135184 KB, 시간: 372 ms
<!-- end -->

## 문제

[문제 링크](https://boj.kr/11000)

<p>수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.&nbsp;</p>

<p>김종혜 선생님한테는 S<sub>i</sub>에 시작해서 T<sub>i</sub>에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.&nbsp;</p>

<p>참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, T<sub>i</sub> ≤ S<sub>j</sub> 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)</p>

<p>수강신청 대충한 게 찔리면, 선생님을 도와드리자!</p>

## 입력

<p>첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)</p>

<p>이후 N개의 줄에 S<sub>i</sub>, T<sub>i</sub>가 주어진다. (0 ≤ S<sub>i</sub> &lt; T<sub>i</sub>&nbsp;≤&nbsp;10<sup>9</sup>)</p>

## 출력

<p>강의실의 개수를 출력하라.</p>

## 소스코드

[소스코드 보기](강의실%20배정.py)