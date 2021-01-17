# Option 1
names = []
employees = []
with open('file3.txt', 'r') as f:
    for line in f:
        splitted_line = line.split(' ')
        employee = {
           'name': splitted_line[0],
            'salary': int(splitted_line[1])
        }
        employees.append(employee)

print(employees)
avg_salary = 0
for el in employees:
    if el['salary'] < 20:
        names.append(el['name'])
    avg_salary += el['salary']
print(names, round(avg_salary/len(employees), 2))

# Option 2
# через цикл