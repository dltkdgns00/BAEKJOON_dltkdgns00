# 25192번: 인사성 밝은 곰곰이 - <img src="https://static.solved.ac/tier_small/7.svg" style="height:20px" /> Silver IV

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/25192)


<p style="text-align: center;"><img alt="인사하는 곰곰이" src="https://upload.acmicpc.net/cd52b787-5b7c-4857-b917-a95c10fe6ee9/-/preview/" style="max-height:120px; object-fit:contain; display:inline-block;"></p>

<p>알고리즘&nbsp;입문방&nbsp;오픈 채팅방에서는&nbsp;새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 한다. 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구해 보기로 했다.</p>

<p><code>ENTER</code>는 새로운 사람이 채팅방에 입장했음을 나타낸다.&nbsp;그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.</p>

<p>새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.</p>

<p>채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!</p>



## 입력


<p>첫 번째 줄에는 채팅방의 기록 수를 나타내는 정수&nbsp;$N$ 이 주어진다.&nbsp;($1 \le&nbsp;N&nbsp;\le&nbsp;100\,000$)</p>

<p>두 번째 줄부터 $N$ 개의 줄에 걸쳐 새로운 사람의 입장을 나타내는 <code>ENTER</code>, 혹은 채팅을 입력한 유저의 닉네임이&nbsp;문자열로 주어진다. ($1 \le \texttt{문자열 길이}&nbsp;\le 20$)</p>

<p>첫 번째 주어지는 문자열은 무조건 <code>ENTER</code>이다.</p>



## 출력


<p>채팅 기록 중 곰곰티콘이 사용된 횟수를 출력하시오.</p>



## 소스코드

[소스코드 보기](인사성%20밝은%20곰곰이.py)