score = int(input())
total_a = 0
total_b = 0

while score != -1:
    score = int(input())
    if a > b:
        total_a += 1
        winner = "A"
    elif a == b:
        total_a += 1
        total_b += 1 
        winner = "Tie"
    else:
        total_b += 1
        winner = "B"

    score = int(input())

print(total_a)
print(total_b)
print(winner)
