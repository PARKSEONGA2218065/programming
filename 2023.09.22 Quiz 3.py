# 학생들의 점수 리스트
student_scores = [90, 45, 64, 9, 17, 29]

# 학생들의 각 학점을 저장할 리스트
results = []

# 학점 변환을 수행하는 반복문
for score in student_scores:
    if score >= 71:
        grade = 'A'
    elif score >= 41:
        grade = 'B'
    elif score >= 11:
        grade = 'C'
    else:
        grade = 'D'

    # 학점을 결과 리스트에 추가
    results.append(grade)

# 결과 출력
print(results)
