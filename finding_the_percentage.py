if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_means = {}
    for k,v in student_marks.items():
        scores_average = sum(v)/len(v)
        student_means[k] = scores_average 
    print("%.2f" % round(student_means[query_name], 2)) #Formato para que aparezca con dos decimales