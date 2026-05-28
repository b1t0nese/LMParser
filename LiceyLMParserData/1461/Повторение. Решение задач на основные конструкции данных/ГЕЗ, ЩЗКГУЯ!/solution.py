text = input()
k = int(input())

encrypt_text = ""
reversed_encrypt_text = ""
for i in range(len(text)):
    encrypt_text += text[(i + k) % len(text)]
    reversed_encrypt_text += text[(i - k) % len(text)]

print(encrypt_text)
print(text)
print(reversed_encrypt_text)