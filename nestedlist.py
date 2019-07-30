if __name__ == '__main__':
    students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        students.append([name,score])
    students.sort()
    scores = list(scores)
    scores.sort()
    second = scores[1]
    for student in students:
        if student[1] == second:
            print(student[0])

