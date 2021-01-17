import sys
with open('file.txt', 'w') as f:
    for line in sys.stdin:
        if line == '0':
            break
        else:
            f.write(line)