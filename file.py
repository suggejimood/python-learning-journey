# Yazma
with open("output.txt", "w") as f:
    f.write("Deneme\n")

# Ekleme
with open("output.txt", "a") as f:
    f.write("Yeni satir\n")

# Okuma
with open("output.txt", "r") as f:
    content = f.read()
    print(content)