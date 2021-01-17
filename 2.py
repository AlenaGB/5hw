with open('file1.txt', 'r') as f:
    lines = f.readlines()
    for i, value in enumerate(lines):
        words = len(value.split())
        print('Line number {} has {} words.\n'.format(i + 1, words))