words = input().split()
substr = input().lower()
    
for word in words:
    if substr in word.lower():
        print(word)
