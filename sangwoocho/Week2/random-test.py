def solution(answers):
    
    # 1번, 2번, 3번 학생의 답안지
    student_answers = []
    student_answers.append([1,2,3,4,5]) # 1번 학생
    student_answers.append([2,1,2,3,2,4,2,5]) # 2번 학생
    student_answers.append([3,3,1,1,2,2,4,4,5,5]) # 3번 학생
    
    # 1번, 2번, 3번 학생의 정답 개수
    count = [0,0,0]
    
    # 각 학생에 대해서, 하나씩 정답을 확인하며 맞춘 개수를 카운트
    for i in range(3):
        for j in range(len(answers)):
            # 각 문제의 번호를 학생의 답안지의 길이로 나눈 나머지를 인덱스로 이용
            if student_answers[i][j%len(student_answers[i])] == answers[j]:
                count[i] += 1
            
    # 가장 많이 맞춘 학생들의 번호를 반환
    answer = []
    for i in range(3):
        if count[i] == max(count):
            answer.append(i + 1)
    
    return answer