# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    grades = []
    lowest_grade = 10321.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
        lowest_grade = min(lowest_grade, score)
        
    grades.sort(key=lambda x: x[1])
    second_lowest = None
    for name, score in grades:
        if score > lowest_grade:
            second_lowest = score
            break
                
    names = sorted([name for name, score in grades if score == second_lowest])
    for name in names:
        print(name)