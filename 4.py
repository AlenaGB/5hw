word = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
lines = []
with open('file4.txt', 'r') as f:
    for line in f:
        splitted_line = line.split(' — ')
        print(splitted_line)
        splitted_line[0] = word[splitted_line[0]]
        lines.append(splitted_line)
print(lines)

with open('file4_translated.txt', 'w') as f:
    for l in lines:
        f.write(' — '.join(l))