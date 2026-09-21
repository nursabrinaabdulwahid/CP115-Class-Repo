num_rounds = int(input())

final_score = 0.0
rounds_processed = num_rounds

for round in range (num_rounds):
    score = float(input())
    if score > 100:
        score += score * 0.2
    final_score += score
    
print(f"{final_score:.1f}")
print(rounds_processed)
