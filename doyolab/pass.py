import random
import string

print("=================================")
print("    PASSWORD GENERATOR")
print("=================================")

length = int(input("パスワードの長さ："))

characters = ""

if input("英字を使いますか？ (y/n)：") == "y":
    characters += string.ascii_letters

if input("数字を使いますか？ (y/n)：") == "y":
    characters += string.digits

if input("記号を使いますか？ (y/n)：") == "y":
    characters += string.punctuation

if characters == "":
    print("1種類以上選んでください！")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nあなたのパスワードはこちら！")
    print(password)