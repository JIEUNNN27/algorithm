***추가중

# 선형 자료구조

### Deaque

- 스택과 큐 기능을 모두 가지고 있다.

- 양쪽 끝에서 삽입/삭제가 모두 가능

- `from collections import deque`

- ``````python
  from collections import deque
  data = [1, 2, 3, 4, 5]
  d = deque(data)
  
  #함수 목록
  d.append(x) #맨 오른쪽에 x 추가
  
  d.appendleft(x) #맨 왼쪽에 x 추가
  
  d.clear() #모든 원소 삭제
  
  d.copy() #shallow copy를 리턴
  
  d.count(x) #x의 개수 리턴, 없을 시 0 리턴
  
  d.extend(iterable) #오른쪽에 iterable 한 원소들을 추가
  #(파이썬 'str' 객체(object)는 iterable 하고, 'int' 객체는 iterable 하지 않다.)
  #iterable 하지 않은 원소를 추가하면 TypeError가 발생
  
  d.extendleft(iterable) #왼쪽에 iterable 한 인자들을 추가
  #(파이썬 'str' 객체(object)는 iterable 하고, 'int' 객체는 iterable 하지 않다.)
  #iterable 하지 않은 원소를 추가하면 TypeError가 발생
  
  d.index(x[, start[, stop]]) #deque 안에 있는 x의 인덱스를 리턴
  #일치하는 원소가 여러 개일 경우 가장 작은 인덱스를 리턴
  #[]는 없어도 되고, 있으면 start에서 stop 사이의 범위 내로 한정
  #x가 deque 안에 없으면 ValueError가 발생한다.
  
  d.insert(i,x) #x를 i 번째 인덱스에 삽입한다.
  #deque의 범위를 넘어서 i가 접근할 경우 IndexError가 발생
  
  d.maxlen() #큐의 길이 반환
  
  d.pop() #오른쪽에 있는 원소를 삭제하고 삭제한 원소를 리턴
  #원소가 없을 시 IndexError가 발생
  
  d.popleft() #맨 왼쪽에 있는 원소를 삭제하고 삭제한 원소를 리턴
  #원소가 없을 시 IndexError가 발생
  
  d.remove(x) #x와 일치하는 원소를 제거
  #일치하는 원소가 여러 개일 경우 가장 작은 인덱스의 원소를 지움
  #x에 해당하는 원소가 없을 시 ValueError가 발생
  
  d.reverse() # 원소들을 뒤집는다.
  #다시 말하면, deque의 모든 원소들의 현재 인덱스 값을 (deque의 맨 끝 인덱스 값 - 현재 인덱스 값)으로 바꾼다.
  
  d.rotate(k) #원소들을 k 번씩 이동시킨다.
  #k에 양수를 넣으면 오른쪽으로, 음수를 넣으면 왼쪽으로 이동
  #맨 오른쪽에 있는 원소는 오른쪽으로 이동하면 맨 왼쪽으로, 맨 왼쪽에 있는 원소는 왼쪽으로 이동하면 맨 오른쪽으로 온다.
  #다시 말하면, deque의 모든 원소들의 현재 인덱스 값을 {(현재 인덱스 값 + k) % (deque의 맨 끝 인덱스 값)}으로 바꾼다.
  ``````

- 예시문제



# 비선형 자료구조

## 그래프

**오일러 경로** ⇒ 간선 기준

- 모든 정점이 짝수 개의 차수를 갖는다면 모든 다리를 한 번씩만 건너서 도달하는 것이 성립함
- 모든 간선을 한 번씩 방문하는 유한 그래프(Finite Graph)를 일컬어 오일러 경로 (Eulerial Trail/Eulerian Path)

**해밀턴 경로** ⇒ 정점 기준, 한 번만 방문하는 경로

- 각 정점을 한 번씩 방문하는 무항 또는 유항 그래프 경로

- 최적 알고리즘이 없는 대표적인 NP-Complete 문제

- 해밀턴 순환

   ⇒ 한 번만 방문하여 출발지로 돌아오는

  - 원래의 출발점으로 돌아오는 경로

  - 최단 거리를 찾는 문제 → 

    외판원 문제

    (Salesman Problem, TSP)

    - 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 문제.
    - 최단 거리인 해밀턴 순환을 찾는 문제

### 그래프 순회

그래프 순회란 그래프 탐색(search)이라 고도 불림, 그래프의 각 정점을 방문하는 과정

- 그래프 표현 방법

  - 인접 행렬 (Adjacency Matrix)

  - 인접 리스트 (Adjacency List)

    - key: 출발 노드, value: 도착 노드 (파이썬 dictionary)

    ```python
    graph = {
    	1: [2, 3, 4],
    	2: [5],
    	3: [5],
    	4: [],
    	5: [6, 7],
    	6: [],
    	7: [3], 
    }
    ```



### 깊이 우선 탐색 (Depth-Fist Search, DFS)

