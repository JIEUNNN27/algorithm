***추가중

[toc]

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

- 연습문제



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



#### 깊이 우선 탐색 (Depth-Fist Search, DFS)

- 핵심 아이디어: 현재 분기(Branch)를 끝까지 깊게 가본 다음에, 다음 분기로 이동

- 장점: BFS에 비해 이해, 구현 쉬움

- 단점: 그래프에 따라서 무슨 순서로 갈지 아무도 모른다(?)
  - 그래프 → 최단거리가 많이 나온다. 그러나 이걸로는 최단거리 못구함
  
- Keyword: 재귀 호출(Recursion), 스택

- 방문확인을 위한 정점 배열이 필요하다는 것을 기억할 것.

- 일반적으로 BFS에 비해 더 널리 쓰임

- **스택** or **재귀**로 구현

  - 일반적으로 스택으로 구현, 재귀를 이용하면 좀 더 간단하게 구현 가능 (코테 에서도 재귀 구현이 더 선호)
  - 대부분의 경우 재귀 구현은 반복으로, 반복 구현은 재귀로 서로 바꿔서 알고리즘을 구현할 수 있으므로 둘다 익숙해 질 때까지 연습하기

- 재귀 구조로 구현

  - 사전적 순서로 방문 (Lexicographical Order)

  - 수도 코드: 정점 v의 모든 인접 유향(Directed) 간선들을 반복

    ```python
    #수도코드
    DFS(G, v)
    	label v as discovered
    	for all directed edges from v to w that are in G.adjacentEdges(v) do
    		if vertex w is not labeled as discovered then
    			recursively call DFS(G, w)
    ```

  - 파이썬 코드: 방문했던 정점, 즉 discovered를 계속 누적된 결과로 만들기 위해 리턴하는 형태만 받아 오도록 처리 

    ```python
    def recursive_dfs(v, discovered=[]):
      discovered.append(v)
      for w in graph[v]:
        if w not in discovered:
          discovered = recursive_dfs(w, discovered)
      return discovered
    
    
    recursive_dfs(1)
    => [1, 2, 5, 6, 7, 3, 4]
    ```

    

- 스택을 이용한 반복 구조로 구현

  - 역순으로 방문

  - 수도코드: 스택을 이용해 모든 인접 간선을 추출하고 다시 도착 점인 정점을 스택에 삽입하는 구조

    ```python
    #수도코드
    DFS-iterative(G, v)
    	let S be a stack
    	S.push(v)
    	while S is not empty do
    		v = S.pop()
    		if v is not labeled as discovered then
    			label v as discovered
    			for all edges from v to w in G.adjacentEdges(v) do
    				S.push(w)
    ```

  - 파이썬 코드: 좀 더 직관적이라 이해하기 훨씬 쉽고, 실행속도도 빠른 편

    ```python
    def iterative_dfs(start_v):
    	discovered = []
    	stack = [start_v]
    	while stack:
    		v = stack.pop()
    		if v not in discovered:
    			discovered.append(v)
    			for w in graph[v]:
    				stack.append(w)
    	return discovered
    
    
    iterative_dfs(1)
    => [1, 4, 3, 5, 7, 6, 2]
    ```

  

- 똑같은 DFS인데 순서가 다른 이유?

  - 재귀 DFS는 사전식 순서로 방문한 데 반해 반복 DFS(스택)는 역순으로 방문함.
  - 스택으로 구현하다 보니 가장 마지막에 삽입된 노드부터 꺼내서 반복, 이 경우 인접 노드에서 가장 최근에 담긴 노드, 즉 가장 마지막부터 방문하기 때문.
    - 인접 노드를 한꺼번에 추가하는 형태이기 때문에, 자칫 BFS가 아닌가 하고 헷갈릴 수 있지만, 깊이 우선으로 탐색한다는 점에서 DFS가 맞다.

- 연습문제

  - [[리트코드] 200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
  
  - [[백준] 1260. DFS와 BFS](https://www.acmicpc.net/problem/1260)
  
  - [][백준] [[백준] 2606. 바이러스](https://www.acmicpc.net/problem/2606)
  
    



#### 너비 우선 탐색(Breadth-First Search, BFS)

*써티에서는 이게 더 중요, 완벽 이해 필수

- 핵심 아이디어: 인접한 가까운 정점을 모두 방문한 뒤에 먼 정점을 순회한다.

- keyword: 반복 수행(iterative), 

  큐(Queue)

  - 큐의 선입선출
    - 방문할꺼 큐에다 넣고 꺼내서 방문 표시하고 인접 점정을 방문할 거라고 큐에다가 넣는다

- DFS에 비해 구현이 다소 복잡

- iterative: 선후 관계 있을 때, 재귀호출(선후 관계 없을 때) - 병렬연산 장점

- 가중치 없는 그래프에서 목표 노드 사이의 최단 거리를 알고 싶을 때 BFS를 사용

- 방문확인을 위한 정점 배열이 필요하다는 것을 기억할 것 (방문 체크 꼭 처리)

- Dijkstra, Prim 알고리즘과 유사 (써티 advanced에서 Dijstra가 끝판왕)

*** 예시

\#정점의 수, 간선의 수, 시작점 주어짐 // weight, 방향성 추가로 주어지는 경우도 있음

무방향성: 간선수 *2개만큼의 엣지

\#정점의 수, 간선의수

10 10

1 2

1 3

1 4

2 5

2 6

5 9

6 10

3 7

4 8

\#최단 경로 문제 → 이런걸로 문제 대부분 나옴

- 최단 경로 문제의 정의
  - 가장 짧은 경로에서 두 꼭지점을 찾는 문제로 그래프의 형태와 문제의 특징에 따라 최적의 알고리즘이 달라짐
  - **비가중치 그래프 - BFS**
  - 양의 가중치만 가지는 그래프
    - 하나의 정점에서 다른 모든 점정까지의 최단 거리를 구하는 문제 → **다익스트라(Dijkstra) 알고리즘**
- 최단 경로 문제의 특징
  - 최단 경로 문제는 optimal substructure의 속성을 가지고 있다.
    - 최단 경로의 부분 경로도 최단 경로이다
    - 이 속성이 중요한 이유는 문제 해결 기법의 **탐욕법(greedy algorithm)**이나 **동적계획법(dp, dynamic programming)**을 적용할 수 있는 근거이기 때문
  - 최단 경로 알고리즘은 Edge relacation을 기본 연산으로 한다.

- 그래프의 최단 경로 문제 (예: 다익스트라 알고리즘) 등에서 유용하게 쓰임

- 큐를 이용한 반복 구조로 표현 (**재귀는 불가능**)

  - 수도코드: 모든 인접 간선을 추출하고 도착점인 정점을 큐에 삽입

    ```python
    BFS(G, start_v)
    	let Q be a queue
    	label start_v as discovered
    	Q.enqueue(start_v)
    	while Q is not empty do
    		v := Q.dequeue()
    		if v is the goal then
    			return v
    		for all edges from v to w in G,adjacentEdges(v) do
    			if w is not labeled as discovered then
    				label w as discovered
    				w.parent := v
    				Q.enqueue(w)
    ```

  - 파이썬 코드: 리스트 자료형을 사용했지만 pop(0)과 같은 큐의 연산만을 사용했다. 따라서 큐를 사용하는 것과 사실상 동일

    - 최적화 → 데크같은 자료형 사용

    ```python
    def iterative_bfs(start_v):
      discovered = [start_v]
      queue = [start_v]
      while queue:
        v = queue.pop(0)
        for w in graph[v]:
          if w not in discovered:
            discovered.append(w)
            queue.append(w)
      return discovered
    
    
    iterative_bfs(1)
    => [1, 2, 3, 4, 5, 6, 7]
    ```

- 연습문제

  - [[백준] 1260. DFS와 BFS](https://www.acmicpc.net/problem/1260)




### 백트래킹

백트래킹은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(백트랙 Backtrack)해 정답을 찾아가는 범용적인 알고리즘, 제약 충족 문제(Constraint Satisfaction Problems)에 특히 유용

- 백트래킹은 DFS와 같은 방식으로 탐색하는 모든 방법
- DFS는 백트래킹의 골격을 이루는 알고리즘
- 주로 재귀로 구현
- 가보고 되돌아 오고를 반복
- 브루트 포스와 유사
  - 하지만 한번 방문 후 가능성이 없는 경우에는 즉시 후보를 포기한다는 점에서 매번 같은 경로를 반복하는 브루트 포스 보다는 더 우아한 방식
- 불필요한 부분을 일찍 포기한다면 탐색을 최적화 할 수 있기 때문에, 가지치기는 트리의 탐색 최적화 문제와도 관련이 깊음
- 연습문제



### 제약 충족 문제

제약 충족 문제란 수많은 제약 조건(Contraints)을 충족하는 상태(States)를 찾아내는 수학 문제



## 최단 경로 문제

*교육

- 최단 경로 문제의 정의
  - 가장 짧은 경로에서 두 꼭지점을 찾는 문제로 그래프의 형태와 문제의 특징에 따라 최적의 알고리즘이 달라짐
  - **비가중치 그래프 - BFS**
  - 양의 가중치만 가지는 그래프
    - 하나의 정점에서 다른 모든 점정까지의 최단 거리를 구하는 문제 → **다익스트라(Dijkstra) 알고리즘**
- 최단 경로 문제의 특징
  - 최단 경로 문제는 optimal substructure의 속성을 가지고 있다.
    - 최단 경로의 부분 경로도 최단 경로이다
    - 이 속성이 중요한 이유는 문제 해결 기법의 **탐욕법(greedy algorithm)**이나 **동적계획법(dp, dynamic programming)**을 적용할 수 있는 근거이기 때문
  - 최단 경로 알고리즘은 Edge relacation을 기본 연산으로 한다.

------

최단 경로 문제는 각 간선의 가중치 합이 최소가 되는 두 정점(또는 노드) 사이의 경로를 찾는 문제

- 최단 경로 알고리즘
  - 다익스트라(Dijkstra) 알고리즘
    - 항상 노드 주변의 최단 경로만을 택하는 그리디 알고리즘 중 하나, 단순할 뿐 아니라 실행 속도 또한 빠름.
    - 노드 주변을 탐색할 때 BFS(너비 우선 탐색) 이용
    - 가중치가 음수인 경우는 처리 불가
    - 연습문제



## 트리



## 힙





## 트라이





# 알고리즘
## 다익스트라(Dijkstra)

**거리 가중치가 양인 그래프에서 하나의 정점에서 출발해서 모든 정점까지의 최소 경로를 계산한다**

- 인접한 정점들까지의 거리를 먼저 갱신하고, 최단 거리의 정점을 BFS로 탐색한다는 것을 잊지 말자!
- 가중치가 음수인 경우는 최단 거리를 보장할 수 없다
  - 가중치가 음수인 그래프에 대해 써야 한다면, 간선의 최소값을 모든 간선에 빼서 양수로 만들고 계산한 후에, 다시 지나간 간선의 회수와 간선 최소값을 고려해 최종 거리를 보정하는 식으로 할 수는 있다
- 다익스트라 알고리즘을 우선순위 큐로 구현하면, 시간 복잡도는 O로 개선되나 꽤 복잡해진다
  - 우선순위 큐 == max que (pro 레벨)
  - BFS랑 닮음, 구현이 쉬움





*내용 출처

[파이썬 알고리즘 인터뷰 (박상길)](https://www.yes24.com/Product/Goods/91084402)
