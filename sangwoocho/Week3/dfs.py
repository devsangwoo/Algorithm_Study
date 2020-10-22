# 배열의 원소를 더하거나 빼서 타겟 값이 나오는 모든 경우의 수를 출력하는 문제
def solution(numbers, target):
    #최상위 노드(슈퍼노드)
    sup= [0]
    for i in numbers: # 1 1 1 1 1  = array, i = 1   // 각 레이어별로 루프 돌음
        sub = []
        for j in sup : 
            #[0+1] [0-1]=> [0+1+1] [0+1-1] , [0-1+1] [0-1-1]  [3 1 -1]
            sub.append(j+i)
            sub.append(j-i) # [1 -1   ==> 다음 값에 저장됨]
        print(sub)
        sup = sub
    #전체 저장된 리스트중에 타겟 넘버와 같은 녀석들의 수를 셈
    return sup.count(target) # 


print(solution([1, 1, 1, 1, 1], 3))


# DFS vs BFS
""" 
백트렉킹/ 그리디/ 쏘팅 
=> 무어의 법칙, 리그레션 모델링, 다직트라 패스

 백트래킹 한번간뒤에 다시는 돌아오지 않는다. 

DFS
Depth First Search
4n 트리가 기본, 
서치의 의미는 찾는것,
12개의 서치를 전부 서치를 하게됨

ex) 결과값을 찾고 불리언으로 찾아라 => DFS

BFS
Breadth First Search
각 층별로 가로로 먼저 봄.
ex) 경우의 수 DFS/BFS
자식이 2가지 케이스 

재귀함수를 쓸때는 기본 조건을 줌... 어떤 

슬라이싱으로 popping을 해줌.
 """



 def solution(numbers, target):
    #최상위 노드(슈퍼노드)
    sup= [0]
    for i in numbers: # 1 1 1 1 1  = array, i = 1   // 각 레이어별로 루프 돌음
        sub = []
        for j in sup : 
            #[0+1] [0-1]=> [0+1+1] [0+1-1] , [0-1+1] [0-1-1]  [3 1 -1]
            sub.append(j+i) # 합
            sub.append(j-i) # 차 [1 -1   ==> 다음 값에 저장됨]
        print(sub)
        sup = sub
    #전체 저장된 리스트중에 타겟 넘버와 같은 녀석들의 수를 셈
    return sup.count(target) # 


print(solution([1, 1, 1, 1, 1], 3))
 
 
 
"""
[1, -1]
[2, 0, 0, -2]
[3, 1, 1, -1, 1, -1, -1, -3]
[4, 2, 2, 0, 2, 0, 0, -2, 2, 0, 0, -2, 0, -2, -2, -4]

2의 5승 32개 케이스가 전부됨
[5, 3, 3, 1, 3, 1, 1, -1, 3, 1, 1, -1, 1, -1, -1, -3, 3, 1, 1, -1, 1, -1, -1, -3, 1, -1, -1, -3, -1, -3, -3, -5]


이중 포문은 괜찮지만 O^2,
count 메소드 자체가 루프가 있을 확률이 높음.
"""