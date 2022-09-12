def sayhello():
    print("こんにちは")

sayhello()
sayhello()
sayhello()
    
def postTaxPrice(price):
    ans = price * 1.08
    return ans

print(postTaxPrice(100), "円")
print(postTaxPrice(128), "円")
print(postTaxPrice(980), "円")

def sayhello2(name):
    print("こんにちは、" + name + "さん。")
sayhello2("フタバ")

import random
def omikuji():
    kuji = ["大吉", "中吉", "小吉", "凶"]
    return random.choice(kuji)
kekka = omikuji()
print("結果は", kekka, "です。")
