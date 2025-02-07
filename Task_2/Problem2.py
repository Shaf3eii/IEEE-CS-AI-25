# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()) )
    arr.sort()
    first = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] < first:
            print(arr[i])
            break