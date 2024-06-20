def calc_avg(query_name, student_marks):
    for name in student_marks:
        if name == query_name:
            avg = round(sum(student_marks[name]) / len(student_marks[name]), 2)
    return avg

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg_marks = calc_avg(query_name, student_marks)
    print(f"{avg_marks:.2f}")