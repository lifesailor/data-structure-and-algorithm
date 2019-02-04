# Chapter 1. 기초 개념

Chapter 1에서 다루는 데이터 구조는 "Stack", "Queue", "Bag"이다. 이들에 대한 깊이 있는 이해는 앞으로 데이터 구조와 알고리즘 공부에 세 가지 면에서 대단히 중요하다. 첫 째는 이들 데이터 타입은 좀 더 복잡한 고수준 데이터의 빌딩 블록이 된다. 두 번째로, 데이터 구조와 알고리즘이 어떤 관계로 엮이는지, 서로 상충되는 성능 요건을 달성하는 표본 역할을 한다. 세 번째로, 두 객체의 컬렉션에 대한 ADT로서 메서드를 더 강력하게 구현하는 데 집중하고 있어, 앞으로 구현들에 시작점이 되어 준다.



## 1. 데이터 구조(p158)

객체들의 컬렉션을 표현하는 방법으로 배열과 연결 리스트 두 가지 방법을 확보했다. 이 책에서는 이 두 가지 기초적인 데이터 구조를 조합하고 확장한 여러 가지 다양한 ADT를 구현하게 된다. 다중 링크 데이터 구조는 그러한 확장 데이터 구조의 중요한 한 예이다.

<table>
    <tr>
        <td>데이터 구조</td>
    	<td>배열</td>
    	<td>연결 리스트</td>
    </tr>
    <tr>
        <td>장점</td>
    	<td>어떤 항목이든 인덱스로 바로 접근 가능</td>
    	<td>실제 저장되는 항목 개수에 비례하여 공간 소요</td>
    </tr>
    <tr>
        <td>단점</td>
    	<td>초기화 시점에 미리 크기를 알아야 함</td>
    	<td>항목에 접근하기 위해 간점적인 참조 필요</td>
    </tr>
</table>

예를 들어, 3.2절과 3.3절에는 이진 트리라는 데이터 구조를 다루게 되는데 이진 트리에서는 각 노드가 두 개의 링크를 가진다. 또 다른 중요한 예로, 데이터 구조 조합이 있다. 스택의 백이나, 배열과 큐 같은 것들이 가능하다. 예를 들어 장에서는 배열의 백으로 표현되는 그래프를 다룬다. 이런 방식으로 어떤 종류의 복잡한 데이터 구조도 쉽게 정의할 수 있다. 추상 데이터 타입에 집중하는 중요한 이유 중 하나는 그러한 복잡도를 다룰 수 있는 수단을 확보하는 데 있다.

<br/>

## 2. 알고리즘 구현 절차(p158)

이 절에서 백, 스택을 설명한 방식은 이 책에서 다루어질 데이터 구조, 알고리즘에서도 동일하게 활용된다. 새로운 응용 분야에 접근할 때는 어떤 컴퓨팅 난제가 있는지 파악하고 데이터 추상화를 사용해 문제 해결을 시도한다. 

- API를 규정한다.
- 목적하는 응용 예에 맞추어 샘플 테스트 클라이언트를 작성한다.
- 데이터 구조를 고안한다. 앞서 정의한 API 동작 사항을 만족하도록 코드를 구현하는데 필요한 클래스 인스턴스 변수를 정한다.
- 알고리즘을 고안한다. 필요한 연산을 구현하기 위한 방법론으로, 클래스 인스턴스 메서드를 구현하는 기초 역할을 한다.
- 고안된 알고리즘의 성능 특징을 분석한다.

<br/>

## 3. 알고리즘 분석(p180)

### A. 실행 시간

컴퓨터 과학의 초창기에 커누스는 프로그램의 실행시간에 영향을 미치는 수많은 요소들에도 불구하고 원칙적으로 볼 때, 그 어떤 프로그램에도 적용할 수 있는 실행 시간에 대한 수학적 모델을 만들 수 있다고 전제했다. 커누스의 통찰은 단순했다. 전체 실행 시간은 다음 2가지 요인에 의해 결정된다.

- 각 구문의 실행 비용
- 각 구문의 실행 빈도

전자는 컴퓨터 자체에 대한 속성으로, 자바 컴파일러나 운영 체제와 연관이 있다. 후자는 프로그램과 그 입력값에 대한 속성이다. 만약 프로그램의 모든 명령문에 대해서 이 두 요인을 알고 있다면, 모든 명령문에 대해 이 두 값을 곱하고 더하여 프로그램의 전체 실행 시간을 계산할 수 있다.

<br/>

#### 틸다 근사와 증가 오더

(틸다 근사) ~$f(N)$은 임의의 함수 $f$에 대하여 $N$이 커질수록 ~$f(N)/f(N)$ 의 값이 1에 수렴하게 하는 함수를 말한다. 그리고 $g(N)$ / ~ $f(N)$ 은 $N$ 이 커질수록 $g(N)/f(N)$ 값이 1에 수렴하는 경우를 말한다. 이 때 $f(N)$ 을 $g(N)$ 의 증가 오더라고 말한다.

```python
class ThreeSum:
    def count(lst):
        N = len(lst)
        count = 0

        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if lst[i] + lst[j] + lst[k] == 0:
                        count += 1
        return count
```

속성 A: ThreeSum의 실행 시간 증가 오더는 $N^3$ 이다. (증가오더 가설)

속성 B: ThreeSum 문제의 완전 탐색 알고리즘은 N개의 숫자 중에서 합계가 0인 트리플의 개수를 구하기 위해 ~ $N^3/2​$ 번 접근한다. (비용 모델)

<br/>

#### 요약

대부분의 프로그램들에 있어서 실행 시간에 대한 수학적 모델을 만드는 과정은 다음과 같다.

- 문제 크기에 대한 정의와 더불어서 입력 모델을 만든다.
- 내부 루프를 찾아서 구분한다.
- 내부 루프 작업들을 포함하여 비용 모델을 정의한다.
- 주어진 입력에 따라, 작업들이 어떤 빈도로 수행되는지 파악한다. 이 작업은 수학적 분석이 필요할 수 있다. 이 부분에 대해서는 이 책의 나중에 몇몇 기초적인 알고리즘을 대상으로 예제를 살펴본다.

<br/>

### B. 메모리

메모리 사용에 대한 분석은 수많은 코드 중에서 변수 선언부와만 관련이 있다. 그리고 분석을 하다 보면 복잡한 객체들이 이해하고 쉽고 잘 정의된 기본 데이터 타입으로 수렴한다.

-  예를 들어서 LinkedList의 Node 객체는 1) 객체 오버헤드 - 16바이트 2) 추가 오버헤드 - 8바이트 3) item 참조 - 8바이트 4) node 참조 - 8바이트 총 40바이트로 이루어져있음을 알 수 있다.

<br/>

## 4. 사용 가능한 알고리즘 개발 순서

- Model the problem
- Find an algorithm to solve it.
- Fast enough? Fits in memory?
- If not, figure out why?
- Find a way to address the problem.
- Iterate until satisfied.




