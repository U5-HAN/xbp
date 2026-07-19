import random
import string

print("=================================")
print("    PASSWORD GENERATOR")
print("=================================")

# パスワードの長さを入力
length = int(input("パスワードの長さを入力してください："))

# 使用する文字
characters = string.ascii_letters + string.digits + string.punctuation

# パスワード生成
password = ""
for i in range(length):
    password += random.choice(characters)

print("\n生成されたパスワード")
print("-----------------------------")
print(password)
print("-----------------------------")