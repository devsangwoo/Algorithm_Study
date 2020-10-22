# 배열의 원소를 더하거나 빼서 타겟 값이 나오는 모든 경우의 수를 출력하는 문제
def solution(numbers, target):
    #최상위 노드(슈퍼노드)
    sup= [0]
    for i in numbers:
        sub = []
        for j in sup : 
            #[0+1] [0-1]=> [0+1+1] [0+1-1] , [0-1+1] [0-1-1] 
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    #전체 저장된 리스트중에 타겟 넘버와 같은 녀석들의 수를 셈
    return sup.count(target)


print(solution([1, 1, 1, 1, 1], 3))