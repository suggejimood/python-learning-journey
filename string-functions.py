s = "Merhaba"

print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
s = "Merhaba Dünya"
print(s.strip())
print(s.replace("a", "q"))
print(s.find("a"))
print(s.startswith("Me"))
print(s.endswith("cs"))

name = "Mehmet"
surname = "TAN"

print(f"Ad: {name} Soyad: {surname}")
print("Ad: {} Soyad: {} Yaş: {}".format(name, surname, 27))

multi = """Bu bir çoklu satır denemesi.
Birden fazla satır böyle oluyor.
Güzel.
"""
print(multi)