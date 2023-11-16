n = input()
myList = list(map(int, input().split()))
mymax = max(myList)
sum = sum(myList)

# 점수가 A, B, C인 경우
# (A / M * 100 + B / M * 100 + C / M * 100) / 3 = (A + B + C) * 100 / M / 3
print(sum * 100 / mymax / int(n))