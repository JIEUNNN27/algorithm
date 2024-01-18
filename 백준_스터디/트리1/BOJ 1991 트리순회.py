# https://www.acmicpc.net/problem/1991
# https://blog.naver.com/inpink_/222944239048

import sys
input = sys.stdin.readline

N = int(input())

# tree = [[] for _ in range(N)]
# tree -> 딕셔너리로 표현
tree = {}

for i in range(N):
    a, b, c = map(str, input().split())
    tree[a] = [b, c]

#print(tree)

# 전위 순회
pre = []
def preorder(a):
    # '.'이면 방문 안함
    if a != ".":
        #print(a)
        pre.append(a)
        preorder(tree[a][0]) # 왼
        preorder(tree[a][1]) # 오

# 중위 순회
ino = []
def inorder(a):
    if a != ".":
        inorder(tree[a][0]) # 왼
        #print(a)
        ino.append(a)
        inorder(tree[a][1]) # 오

# 후위 순회
post = []
def postorder(a):
    if a != ".":
        postorder(tree[a][0]) # 왼
        postorder(tree[a][1]) # 오
        #print(a)
        post.append(a)

preorder('A')
print(*pre, sep="")
inorder('A')
print(*ino, sep="")
postorder('A')
print(*post, sep="")