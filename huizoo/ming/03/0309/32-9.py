card = list(input())
card.sort(reverse=True)
n = int(input())
card = card[:n]
print(max(card, key=lambda x: card.count(x)))
