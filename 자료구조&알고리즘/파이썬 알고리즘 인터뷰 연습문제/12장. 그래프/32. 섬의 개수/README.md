# 풀이

### 책 해설

- 반드시 그래프 모양이 아니더라도 그래프형으로 변환해서 풀이할 수 있음을 확인해보는 좋은 문제.

- 입력값이 정확히 그래프는 아니지만 사실상 동서남북이 모두 연결된 그래프로 가정, 동일한 형태로 처리할 수 있으며 네 방향 각각 DFS 재귀를 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수를 파악할 수 있다.

- 행렬(Matrix) 입력값인 grid의 행, 열 단위로 육지(1)인 곳을 찾아 진행하다가 육지를 발견하면 그때부터 self.dfs()를 호출해 탐색 시작

  ```python
  for i in range(len(grid)):
  	for i in range(len(grid[0])):
  		if grid[i][j] == '1':
  			self.dfs(grid, i, j)
  			...
  ```

- DFS 탐색을 하는 dfs() 함수는 동서남북을 모두 탐색하면서 재귀호출.

  - 함수 상단에는 육지가 아닌 곳은 return으로 종료 조건을 설정.
  - 이렇게 재귀 호출이 백트래킹으로 모두 빠져 나오면 섬 하나를 발견한 것으로 간주.
  - 이때 이미 방문했던 곳은 1이 아닌 값으로 마킹.
  - 육지(1)를 더 이상 육지가 아닌 것으로 만들기. (다음에 다시 계산 못하도록, 가지치기)
    - 여기서는 grid[i][j]=’0’

  ```python
  def dfs(self, grid, i, j):
  # 더 이상땅이아닌경우종료
  	if i < 0 or i = len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
  		return
  	
  	grid[i][j] = '0'
  
  	# 동서남북 탐색
  	self.dfs(grid, i+1, j)
  	self.dfs(grid, i-1, j)
  	self.dfs(grid, i, j+1)
  	self.dfs(grid, i, j-1)
  ```

- dfs() 함수를 빠져 나온 후에는 해당 위치에서 탐색할 수 있는 모든 육지를 탐색한 것이므로, 카운트를 1 증가시킨다. (섬을 하나 발견한 것)

  ```python
  ...
  self.dfs(grid, i, j)
  count += 1
  ```

- 입력값이 비어 있는 경우에 대해 예외 처리를 포함한 전체 코드

- \#1에서 dfs()함수를 호출할 때마다 self.dfs(grid, i+1, j)와 같은 형태로 grid 변수를 매번 넘기는 것을 확인할 수 있다.

  ```python
  class Solution:
  	def dfs(self, grid: List[List[str]], i: int, j: int):
  			# 더 이상 땅이 아닌 경우 종료
  			if i<0 or j>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != '1':
  				return
  		
  			grid[i][j]='0'
  
  			# 동서남북 탐색
  			self.dfs(grid, i+1, j)      #1
  			self.dfs(grid, i-1, j)
  			self.dfs(grid, i, j+1)
  			self.dfs(grid, i, j-1)
  
  	def numIslands(self, grid: List[List[str]]) -> int:
  		# 예외 처리
  		if not grid:
  			return 0
  
  		count = 0
  
  		for i in range(len(grid)):
  			for j in range(len(grid[0])):
  				if grid[i][j] == '1':
  					self.dfs(grid, i, j)
  					# 모든 육지 탐색 후 카운트 1 증가
  					count += 1
  		return count
  ```

- 파이썬의 중첩함수 기능을 활용

  ```	python
  def numIslands(self, grid: List[List[str]]) -> int:
  	def dfs(i, j)
  		# 더 이상 땅이 아닌 경우 종료
  		if i<0 or j>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != '1':
  				return
  
  		grid[i][j]='0'
  
  		# 동서남북 탐색
  		dfs(i+1, j)
  		dfs(i-1, j)
  		dfs(i, j+1)
  		dfs(i, j-1)
  	
  	count = 0
  
  	for i in range(len(grid)):
  		for j in range(len(grid[0])):
  			if grid[i][j] == '1':
  				dfs(i, j)
  				# 모든 육지 탐색 후 카운트 1 증가
  				count += 1
  	
  		return count
  ```

  