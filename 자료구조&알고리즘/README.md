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




#### 너비 우선 탐색(Breadth-First Search, BFS)

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



### 백트래킹

- 









*내용 출처

[파이썬 알고리즘 인터뷰 (박상길)](https://www.yes24.com/Product/Goods/91084402)
