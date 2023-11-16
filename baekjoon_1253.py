N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

count = 0
for i in range(N):
    target = numbers[i]
    left, right = 0, N - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        current_sum = numbers[left] + numbers[right]

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            count += 1
            break

print(count) 