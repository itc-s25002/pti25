import random
kuji = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]

def omikuzi():
    #print(random.choice(kuji))
    return random.choice(kuji)

omikuzi()
print("結果は" + omikuzi() + "です")
