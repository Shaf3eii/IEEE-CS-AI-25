# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    array = []
    N = int(input())
    for _ in range(N):
        command = input().split()
        operation = command[0]
        if operation == 'append':
            value = int(command[1])
            array.append(value)
        elif operation == 'insert':
            pos = int(command[1])
            value = int(command[2])
            array.insert(pos, value)
        elif operation == 'remove':
            value = int(command[1])
            array.remove(value)
        elif operation == 'pop':
            array.pop()
        elif operation == 'reverse':
            array.reverse()
        elif operation == 'sort':
            array.sort()
        else:
            print(array)
            