#Write a function that for 2 given dictionaries find their common keys.

def common_keys(a, b):
    for c in a.keys():
        for d in b.keys():
            if c ==d:
                print('Common key is', c)
    return c
#students' marks in school subjects:
student_1 = {'Math':11, 'History':9, 'Biology':5, 'Chemistry':10, 'English':12}
student_2 = {'Sport':8, 'Ukrainian':10, 'English':3, 'Literature':7,'Math':4}
common_keys(student_1,student_2)
