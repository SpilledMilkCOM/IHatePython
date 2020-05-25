import sys


f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
    # print(line) # adds a new line
    sys.stdout.write(line)      # does NOT add a new line
f.close()