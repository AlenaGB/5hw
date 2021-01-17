subj = {}
with open('file6.txt', 'r') as file:
    for line in file:
        a = line.replace('(', ' ').split()
        print(a)
        subj[a[0]] = sum(int(i) for i in a if i.isdigit())
print(f'Общее количество часов по предмету - \n {subj}')
