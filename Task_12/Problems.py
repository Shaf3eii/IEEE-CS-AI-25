import numpy as np

# problem 1
task1 = np.eye(3) * 9
print(task1)

print()
print()




# problem 2
task2 = np.arange(2, 33, 2).reshape((4, 4))

mean = task2.mean()
deviation = task2.std()

lower = mean - deviation * .5
upper = mean + deviation * .5

ans = task2[(task2 >= lower) & (task2 <= upper)]
print(ans)

print()
print()



#problem 3
# task3 = np.eye(9) * 0
task3 = np.zeros((9, 9), dtype=int)
print(task3)

print()
print()



# problem 4
n = int(input("Enter the n: "))
task4 = np.ones((n, 1)) * np.arange(1, n + 1)

print(task4)

print()
print()



# problem 5
numberOfCards = int(input())
cards = list(map(int, input().split()))

arr = np.array(cards)

sereja, dima = 0, 0
l, r = 0, numberOfCards - 1
currentTurn = True # True for sereja, False for dima

while l <= r:
    if arr[l] >= arr[r]:
        sereja += arr[l] * currentTurn
        dima += arr[l] * (not currentTurn)
        l += 1
    else:
        sereja += arr[r] * currentTurn
        dima += arr[r] * (not currentTurn)
        r -= 1

    currentTurn ^= True


print(sereja, dima)


print()
print()



# problem 6
rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

arr = np.array(matrix)

white = np.count_nonzero(arr == 'W')
black = np.count_nonzero(arr == 'B')
grey = np.count_nonzero(arr == 'G')

print("#Black&White" if white + black + grey == rows * cols else "#Color")