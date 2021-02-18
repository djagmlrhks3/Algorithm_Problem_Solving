# 📌 Study_Algorithm



## 💡 그리디

'현재 상황에서 지금 당장 좋은 것만 고르는 방법'을 의미한다. - 탐욕법

매 순간 가장 좋아보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.

다른 알고리즘에 비해 사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형들이 많지만 '정렬', '최단 경로' 등의 알고리즘 유형은 이미 그 알고리즘의 사용방법을 정확히 알고 있어야만 해결 가능한 경우가 많다.

ex) 플로이드 워셜, 다익스트라 알고리즘

따라서, 그리디 알고리즘 유형은 매우 다양하기 때문에 암기가 아닌 다양한 유형의 문제를 접해보고 훈련해야 한다.



어떤 코딩 테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심해보자. 만약 오랜 시간을 고민해도 그리디 알고리즘으로 해결 방법을 찾을 수 없다면, 다이나믹 프로그래밍이나 그래프 알고리즘 등으로 문제를 해결할 수 있는지 재차 고민하자.



## 💡 구현

문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형 - '시뮬레이션'



C/C++와 자바에서는 정수형을 표현할 때 크기에 따른 자료형의 지정을 고려해야하지만, 파이썬은 프로그래머가 직접 자료형을 지정할 필요가 없다.(BigInteger 지원)



### 파이썬에서 리스트 크기

>  int 자료형 데이터의 개수에 따른 메모리 사용량

| 데이터의 개수(리스트의 길이) | 메모리 사용량 |
| ---------------------------- | ------------- |
| 1,000                        | 약 4KB        |
| 1,000,000                    | 약 4MB        |
| 10,000,000                   | 약 40MB       |

 

### 채점 환경

파이썬 3.7로 코드를 작성할 때, 자신의 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하고 문제를 풀면 실행 시간 제한에 안정적이다.

시간제한이 1초이고, 데이터의 개수가 100만 개인 문제가 있다면 일반적으로 시간 복잡도 O(NlogN) 이내의 알고리즘을 이용하여 문제를 풀어야 한다. → N = 1,000,000이면 NlogN은 20,000,000이기 때문!



## 💡 DFS/BFS

스택과 큐의 자료구조를 이해해야 한다.

※ 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조

* 오버플로우(Overflow) : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생
* 언더플로우(Underflow) : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할 때 발생



### 재귀 함수

컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다.

함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다.



### DFS

깊이 우선 탐색(Depth First Search) : 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

1. 인접행렬
2. 인접 리스트 - '연결 리스트'라는 자료구조를 이용(TMI : C++나 자바에서는 별도로 연결 리스트 기능을 위한 표준 라이브러리 제공)



인접행렬 vs 인접리스트

> 메모리

인접행렬은 노드 개수가 많을수록 메모리가 불필요하게 낭비된다.

반면에 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모를 효율적으로 사용한다.



> 시간

특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도는 인접 행렬이 빠르다.

ex) 노드 1 - 노드 7

인접행렬 : `graph[1][7]`

인접리스트 : 노드1에 대한 인접 리스트를 앞에서부터 차례대로 확인



### BFS

너비 우선 탐색(Breadth First Search) : 가까운 노드부터 탐색하는 알고리즘

※ 일반적인 경우 실제 수행 시간은 BFS > DFS다.



## 💡 정렬

데이터를 특정한 기준에 따라서 순서대로 나열

※ 파이썬에서 리스트의 원소를 뒤집는 메서드 reverse는 O(N)의 복잡도를 가진다.



### 선택정렬

가장 원시적인 방법으로 매번 '가장 작은 것을 선택'한다는 의미에서 **선택 정렬**알고리즘이라고 한다.

시간복잡도는 O(N<sup>2</sup>) 

cf) 기본 정렬 라이브러리 또는 다른 알고리즘에 비해 매우 비효율적이다.

다만, 가장 작은 데이터를 찾는 일에서 쓰일 수 있다.



### 삽입 정렬

특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 **삽입 정렬**이라고 한다.

삽입 정렬은 두 번째 데이터부터 시작한다. → 첫 번쨰 데이터는 그 자체로 정렬되어 있다고 판단!

'데이터가 거의 정렬 되어 있을 때' 훨씬 효율적이다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```



삽입 정렬의 시간 복잡도는 O(N<sup>2</sup>)이다

하지만, 데이터가 거의 정렬되어 있다면 훨씬 효율적이다(퀵 정렬보다 더 강력하다.). → O(N)



### 퀵 정렬

대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘

기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작

→ 피벗(Pivot)이 사용 - 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'



피벗을 설정하고 리스트를 분할하는 방법에 따라서 여러 가지 방식으로 퀵 정렬을 구분한다.

※ 책에서는 가장 대표적인 호어 분할(Hoare Partition)방식을 설명

1. 리스트에서 첫 번째 데이터를 피벗으로 정한다.

2. 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.

3. 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.

4. 만약, 큰 데이터와 작은 데이터의 위치가 서로 엇갈린다면 '작은 데이터'와 '피벗'의 위치를 서로 변경한다. → 분할(혹은 파티션)완료
5. 분할이 진행되면 재귀를 통해 왼쪽, 오른쪽 부분에 대해 1 ~ 4과정을 반복 진행한다(리스트의 데이터 개수가 1개가 될 때 까지!)

> 퀵 정렬 소스코드

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
```



> 파이썬의 장점을 살린 퀵 정렬 소스코드

```python
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```



퀵 정렬의 평균 시간 복잡도는 O(NlogN)이다.

하지만 최악의 경우 시간복잡도는 O(N<sup>2</sup>)이다.

※ 최악의 경우 선택정렬, 삽입정렬, 퀵 정렬 모두 O(N<sup>2</sup>)이다.



퀵 정렬은 이미 데이터가 정렬되어 있는 경우 매우 느리게 동작한다.

cf) 삽입 정렬은 이미 데이터가 정렬되어 있는 경우 매우 빠르게 동작한다.



### 계수 정렬

계수 정렬(Count Sort)은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.

데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용할 수 있다.

데이터의 개수가 N, 데이터 중 최대값이 K일 때, 계수 정렬은 최악의 경우도 O(N+K)를 보장한다.

일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적이다.

ex) 0이상 100이하인 성적 데이터



계수 정렬이 이러한 특징을 가지는 이유는, '모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언'해야 하기 때문이다. 

→ 따라서, 공간 복잡도에 심각한 비효율성을 초래할 수 있다. - 공간복잡도 O(N+K)

ex) 데이터가 0과 999,999 단 2개만 존재할 경우 리스트의 크기는 100만이 되도록 선언해야 한다.

cf) 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다. - 데이터의 특성 파악이 중요!



최대값+1만큼의 배열을 만든후(0을 포함해야 하므로) 인덱스로 접근하여 리스트의 각 데이터가 몇 번 등장했는지 횟수를 기록한다.

이후 인덱스와 횟수에 맞게 출력해주면 끝!



### 파이썬의 정렬 라이브러리

퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌는데, 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다는 특징이 있다.





## 💡 이진 탐색

파이썬에서 사용되는 count()함수도 순차탐색이다. 따라서, 최악의 경우 시간복잡도는 O(N)이다.



이진 탐색(Binary Search)는 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.

이진 탐색은 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)이다. - 퀵 정렬과 유사



TIP) 어려운 알고리즘에서 활용도가 높으므로 암기하자!

탐색 범위가 2,000만을 넘어가거나 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 내야 하는 알고리즘을 떠올려야 한다.



> 재귀 함수로 구현한 이진 탐색 소스코드

 ```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
 ```



> 반복문으로 구현한 이진 탐색 소스코드

```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```



### 트리 자료구조

트리 자료구조는 노드와 노드의 연결로 표현한다.

트리 자료구조는 그래프 자료구조의 일종으로 데이터베이스 시스템이나 파일 시스템 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용된다.

데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정렬되어 있다.

데이터베이스에서의 탐색은 이진 탐색과는 조금 다르지만, 이진 탐색과 유사한 방법을 이용해 탐색을 항상 빠르게 수행하도록 설계되어 있어서 데이터가 많아도 탐색하는 속도가 빠르다.

#### 트리 자료구조의 주요한 특징

* 트리는 부모 노드와 자식 노드의 관계로 표현된다.
* 트리의 최상단 노드를 루트 노드라고 한다.
* 트리의 최하단 노드를 단말 노드라고 한다.
* 트리에서 일부를 떼어내도 트리구조이며 이를 서브 트리라 한다.

* 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

큰 데이터를 처리하는 소프트웨어는 대부분 데이터를 트리 자료구조로 저장해서 이진 탐색과 같은 탐색 기법을 이용해 빠르게 탐색이 가능하다.

### 이진 탐색 트리

트리 자료구조 중에서 가장 간단한 형태 (= 모든 트리가 다 이진 탐색 트리는 아니다.)

이진 탐색 트리란 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조다.



이진 탐색 트리는 다음과 같은 특징을 가진다.

* 부모 노드보다 왼쪽 자식 노드가 작다.
* 부모 노드보다 오른쪽 자식 노드가 크다.

(왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드)



탐색 : 루트 노드부터 시작하며 찾고자 하는 값은 부모노드를 기준으로 자식노드(좌/우)를 비교한다.



**이진 탐색의 활용**

이진 탐색 문제 + 파라메트릭 서치(최적화 문제를 결정 문제로 바꾸어 해결하는 기법)

'원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 활용한다.

ex) 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.



※결정문제는 '예' 혹은 '아니오'로 답하는 문제를 말한다.



## 💡 다이나믹 프로그래밍

다이나믹 프로그래밍은 다음 조건을 만족할 때 사용할 수 있다.

1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에도 동일하다.



**메모이제이션(Memoization) 기법**

다이나믹 프로그래밍을 구현하는 방법 중 한 종류로, 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법



메모이제이션은 값을 저장하는 방법으로 캐싱(Caching)이라고도 한다.

> 대표적인 예시 : 피보나치 수열 소스코드(재귀적)

```python
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
    	return d[x]
   	d[x] = fibo(x- 1) + fibo(x - 2)
    return d[x]

print(fibo(99))
```



Top-Down 방식(하향식) : 재귀 함수를 이용하여 다이나믹 프로그래밍 소스코드를 작성하는 방법 / 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식

Bottom-Up 방식(상향식) : 단순히 반복문을 이용하여 소스코드를 작성하는 경우 / 작은 문제부터 차근차근 답을 도출하는 방식



다이나믹 프로그래밍의 전형적인 형태는 Bottom-Up 방식이다. 

Bottom-Up 방식에서 사용되는 결과 저장용 리스트는 'DP 테이블'이라고 부르며, 메모이제이션은 Top-Down 방식에 국한되어 사용되는 표현이다.



다이나믹 프로그래밍 vs 메모이제이션

메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미

→ 메모이제이션이 꼭 다이나믹 프로그래밍을 위해 활용하지 않을 수 있다.



재귀의 깊이가 깊어져 'recursion depth'와 관련된 오류가 발생할 경우 sys 라이브러리에 포함되어 있는 setrecursionlimit() 함수를 호출하여 재귀 제한을 완화시킬 수 있다.



## 💡 최단 경로

가장 짧은 경로를 찾는 알고리즘(= 길 찾기 문제)



### 다익스트라 최단 경로 알고리즘

그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘

'음의 간선'이 없을 때 정상적으로 동작한다. - GPS 소프트웨어의 기본 알고리즘으로 채택되곤 한다.

그리디 알고리즘으로 분류된다. - 매번 '가장 비용이 적은 노드'를 선택해서 임의의 과정을 반복하기 때문이다.



> 알고리즘 원리

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3과 4번을 반복한다.

최단 경로를 구하는 과정에서 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다는 특징이 있다. → 최단 거리 테이블(1차원 리스트)

한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다.



### 방법 1. 간단한 다익스트라 알고리즘

O(V<sup>2</sup>)의 시간 복잡도를 가진다. (V는 노드의 개수)

단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)한다.



> 간단한 다익스트라 알고리즘 소스코드

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a → b로 갈 때 비용(c)
   	graph[a].append((b, c))
  
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value nand not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# 입력 예시
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
# 출력 예시
"""
0
2
3
1
2
4
"""
```



### 방법2. 개선된 다익스트라 알고리즘

최악의 경우에도 시간 복잡도 O(ElogV)를 보장하여 해결할 수 있다.

* V는 노드의 개수
* E는 간선의 개수

최단 거리가 가장 짧은 노드를 단순히 선형적으로 찾는 것이 아니라 힙(Heap)자료구조를 이용하여 더욱더 빠르게 찾는다.



#### 힙 설명

힙 자료구조는 우선순위 큐(Priority Queue)를 구현하기 위하여 사용하는 자료구조 중 하나

**우선순위 큐**는 우선순위가 가장 높은 데이터를 가장 먼저 삭제 한다는 점이 특징!



우선순위 큐를 지원하는 라이브러리로 **PriorityQueue**와 **heapq**가 있는데 일반적으로 heapq가 더 빠르게 동작하기 때문에 heapq 사용을 권장!

우선순위큐는 최소 힙, 최대 힙을 이용하는데 파이썬의 우선순위 큐 라이브러리는 최소 힙에 기반하고 있다.(최대 힙의 경우 음수를 붙여서 활용하면 된다.)

> 우선순위 큐 구현 방식 - 리스트 vs 힙

| 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
| --------------------- | --------- | --------- |
| 리스트                | O(1)      | O(N)      |
| 힙(Heap)              | O(logN)   | O(logN)   |



(개선된) 다익스트라 알고리즘 with 우선순위 큐

* 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
* (거리, 노드) 형태로 우선순위 큐에 넣는다. - 튜플의 첫 번째 원소(거리)를 기준으로 정렬된다.

우선순위 큐에서 노드를 꺼낸 뒤에 해당 노드를 이미 처리한 적이 있다면 무시하면 되고, 아직 처리하지 않은 노드에 대해서만 처리하면 된다.

```python
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a → b로 갈 때 비용(c)
   	graph[a].append((b, c))
  

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최다 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
          
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# 입력 예시
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
# 출력 예시
"""
0
2
3
1
2
4
"""
```



### 플로이드 워셜 알고리즘

반면, 플로이드 워셜 알고리즘은 '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우'에 사용할 수 있는 알고리즘이다.

cf) 다익스트라 알고리즘은 '한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우'에 사용

단계마다 O(N<sup>2</sup>)의 연산을 통해 '현재 노드를 거쳐 가는' 모든 경로를 고려한다.

따라서, 플로이드 워셜 알고리즘의 총시간 복잡도는 O(N<sup>3</sup>)이다.



플로이드 워셜 알고리즘은 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보를 담아야 하기 때문에 2차원 리스트에 '최단 거리'정보를 저장한다.

→ 즉 N번의 단계마다 O(N<sup>2</sup>)의 시간 소요



또한 다익스트라 알고리즘은 그리디 알고리즘인데, 플로이드 워셜 알고리즘은 다이나믹 프로그래밍이다.



'A에서 B로 가는 최소 비용'과 'A에서 K를 거쳐 B로 가는 비용'을 비교하여 더 작은 값으로 갱신하는 것이 핵심

(= '바로 이동하는 거리'가 '특정한 노드를 거쳐서 이동하는 거리'보다 더 많은 비용을 가진다면 이를 더 짧은 것으로 갱신)



> 플로이드 워셜 알고리즘 소스코드

```python
import sys

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()

# 입력
"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""

# 출력
"""
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
"""
```



## 💡 그래프 이론

그래프란 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조를 의미한다.



그래프 vs 트리

|                     | 그래프                         | 트리             |
| ------------------- | ------------------------------ | ---------------- |
| 방향성              | 방향 그래프 혹은 무방향 그래프 | 방향 그래프      |
| 순환성              | 순환 및 비순환                 | 비순환           |
| 루트 노드 존재 여부 | 루트 노드가 없음               | 루트 노드가 존재 |
| 노드간 관계성       | 부모와 자식 관계 없음          | 부모와 자식 관계 |
| 모델의 종류         | 네트워크 모델                  | 계층 모델        |



복습)

우선순위 큐를 이용하는 다익스트라 최단 경로 알고리즘은 인접 리스트를 이용하는 방식

플로이드 워셜 알고리즘은 인접 행렬을 이용하는 방식



### 서로소 집합

서로소 집합(Disjoint Sets)이란 공통 원소가 없는 두 집합

서로소 집합 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

* union : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
* find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

따라서, 서로소 집합 자료구조는 union-find 자료구조라고 불리기도 한다.



#### 서로소 집합 자료구조

서로소 집합 자료구조는 트리 자료구조를 이용하여 집합을 표현



> 트리 자료구조를 이용해서 집합을 표현하는 서로소 집합 계산 알고리즘

1. union (합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
   1. A와 B의 ㄹ트 노드 A', B'를 각각 찾는다.
   2. A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다).
2. 모든 union (합집합) 연산을 처리할 때까지 1번 과정을 반복한다.



> 기본적인 서로소 집합 알고리즘 소스코드

```python
import sys

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

# 입력
"""
6 4
1 4
2 3
2 4
5 6
"""

# 출력
"""
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 2 1 5 5
"""
```



find 함수 최적화

만약, 1 ← 2 ← 3 ← 4 ← 5와 같은 상황이 주어진다고 하면 find 함수는 매우 비효율적이게 된다.

노드의 개수가 V이고 find 혹은 union 연산의 개수가 M개일 때, 전체 시간 복잡도는 O(VM)



이러한 find함수는 경로 압축 기법을 적용하면 시간 복잡도를 개선시킬 수 있다.

→ 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법



> 경로 압축 기법 소스코드(find_parent 함수)

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```



> 개선된 서로소 집합 알고리즘 소스코드

```python
import sys

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
© 2021 GitHub, Inc.
```



#### 서로소 집합을 활용한 사이클 판별

무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다.

TMI) 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.



union 연산은 그래프에서 간선으로 표현될 수 있다고 했기 때문에 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는 것만으로도 사이클을 판별할 수 있다.

1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
   1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
   2. 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것이다.
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.



> 서로소 집합을 활용한 사이클 판별 소스코드

```python
import sys

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
```



### 신장 트리

하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

→ 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립 조건이기도 하다.



#### 크루스칼 알고리즘

신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘을 '최소 신장 트리 알고리즘'이라고 한다.

대표적인 최소 신장 트리 알고리즘이 크루스칼 알고리즘이다.

크루스칼 알고리즘은 그리디 알고리즘으로 분류된다.



> 크루스칼 알고리즘 순서

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
   1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
   2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.



신장 트리에 포함되는 간선의 개수가 노드의 개수 -1과 같다.

크루스칼 알고리즘의 핵심 원리는 가장 거리가 짧은 간선부터 차례대로 집합에 추가하고면 된다. 다만,  사이클을 발생시키는 간선은 제외하고 연결한다. → 항상 최적의 해 보장



> 크루스칼 알고리즘 소스코드

```python
import sys

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 입력
"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
# 출력
"""
159
"""
```



#### 크루스칼 알고리즘의 시간 복잡도

간선의 개수가 E일 때 O(ElogE)의 시간 복잡도를 가진다

→ 크루스칼 알고리즘에서 시간이 가장 오래 걸리는 부분이 간선을 정렬하는 작업이기 때문! 



### 위상 정렬

정렬 알고리즘의 일종이며, 순서가 정해져 있는 일련의 작업을 차례대로 수행해야할 때 사용할 수 있는 알고리즘이다.

좀 더 이론적으로 설명하자면, 위상 정렬이란 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'이다.

ex) 선수과목을 고려한 학습 순서 설정



위상 정렬 알고리즘을 자세히 살펴보기 전에, 먼저 진입차수(Indegree)를 알아야 한다.

진입차수란 특정한 노드로 '들어오는' 간선의 개수를 의미한다.



> 위상 정렬 알고리즘

1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
   1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
   2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

큐가 빌 때까지 큐에서 원소를 계속 꺼내서 처리하는 과정을 반복한다. 이 때 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.

다시 말해 큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클이 발생한 것!

※ 단, 기본적으로 위상 정렬 문제에서는 사이클이 발생하지 않는다고 명시하는 경우가 많다.



> 위상 정렬 소스코드

```python
import sys

from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

# 입력
"""
7 8
1 2
1 5 
2 3
2 6
3 4
4 7
5 6
6 4
"""
# 출력
"""
1 2 5 3 6 4 7
"""
```



#### 위상 정렬의 시간 복잡도

위상 정렬의 시간 복잡도는 O(V+E)이다.

차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거해야 한다.

결과적으로 노드와 간선을 모두 확인한다는 측면에서 O(V+E)의 시간이 소요된다.



## 주요 라이브러리의 문법과 유의점

표준 라이브러리 : 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리



파이썬에서 지원하는 표준 라이브러리는 굉장히 다양하지만, 그중 6가지 라이브러리에 대해서 알아보자.

* 내장함수

  * eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환

    ex) eval("(3 + 5 ) * 7") = 56

* itertools : 순열, 조합

  * permutations

  * combinations

  * product : 중복 순열

    product(iterable, repeat=2) # 2개를 뽑는 모든 순열(중복 허용)

  * combinations_with_replacement : 중복 조합

    combinations_with_replacement(iterable, 2)

* heapq : 힙(Heap) 기능을 제공 / 우선순위큐 구현

* bisect : 이진 탐색 기능을 제공하는 라이브러리다.

  * bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드

  * bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

    ```python
    from bisect import bisect_left, bisect_right
    
    a = [1, 2, 4, 4, 8]
    x = 4
    
    print(bisect_left(a, x)) # 2
    print(bisect_right(a, x)) # 4
    ```

    

* collections : 덱(deque), 카운터(Counter)등의 유용한 자료구조를 포함

* math : 필수적인 수학적 기능을 제공하는 라이브러리다. 
  
  * 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, 파이(pi)



## 자신만의 알고리즘 노트 만들기

> https://github.com/ndb796/Python-Competitive-Programming-Team-Notes



## 개발형 코딩 테스트

개발형 코딩 테스트는 정해진 목적에 따라서 동작하는 완성된 프로그램을 개발하는 것을 요구한다.

### REST API란?

REST(Representationsal State Trasfer)는 각 자원(Resource)에 대하여 자원의 상태에 대한 정보를 주고받는 개발 방식

API는 프로그램이 상호작용하기 위한 인터페이스(서버-클라이언트의 상호작용을 위한 인터페이스)

REST API는 REST 아키텍처를 따르는 API를 의미한다.

따라서, REST API 호출이란, REST 방식을 따르고 있는 서버에 특정한 요청을 보내서 데이터를 가져오는 것을 말한다.



REST의 구성요소

1. 자원(Resource) : URI를 이용하여 표현(명사의 형태로 표현)
2. 행위(Verb) : HTTP 메서드를 이용하여 표현
3. 표현(Representations)



### JSON

데이터를 주고받는 데 사용하는 경량의 데이터 형식

JSON 인코딩은 파이썬의 기본 자료형을 JSON 객체로 변환하는 작업을 의미한다.

파이썬 JSON 라이브러리의 json.dumps() 메서드를 이용

> JSON 인코딩 예시

```python
import json

user = {
    "id": "gildong",
    "password": "123456",
    "age": 30,
    "hobby": {"soccer", "game"}
}

# 인코딩: 파이썬 변수를 JSON 객체로 변환(띄어쓰기 네 칸 들여쓰기 적용)
json_data = json.dumps(user, indent = 4)
print(json_data)
```



JSON 디코딩은 인코딩과 반대로 JSON 객체를 파이썬의 기본 자료형으로변환하는 작업니다.

JSON 라이브러리의 json.loads()메서드를 이용

> JSON 디코딩 예시

```python
import json

user = {
    "id": "gildong",
    "password": "123456",
    "age": 30,
    "hobby": {"soccer", "game"}
}

# 인코딩: 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user)

# 디코딩: JSON 객체를 파이썬 변수로 변환
data = json.loads(json_data)
print(data)
```



> JSON 파일 생성하기

```python
import json

user = {
    "id": "gildong",
    "password": "123456",
    "age": 30,
    "hobby": {"soccer", "game"}
}

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent = 4)
```



> REST API를 호출하여 회원 정보를 처리하는 예시

```python
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

# 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
data = response.json()

# 모든 사용자(user) 정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user["name"])
print(name_list)
```



---



참고 : 이것이 취업을 위한 코딩 테스트다 with 파이썬(도서)