def find_difference(marks):
    unique_marks = list(set(marks))  

    if len(unique_marks) < 3:
        return
    
    unique_marks.sort(reverse=True)
    second_highest = unique_marks[1]
    third_highest = unique_marks[2]
    print(second_highest - third_highest)

marks = list(map(int, input().split()))
find_difference(marks)
