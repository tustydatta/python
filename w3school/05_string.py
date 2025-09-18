a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")

print("Expensive" not in txt)

# Slicing string
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

# Modify string
c = "   Hello, World! and Tusty"
print(c)
print(c.upper())
print(c.lower())
print(c.strip())
print(c.replace("o", "J"))
print(c.split(" "))

# String concatenation
d = "Hello"
e = "World"
f = d + e
print(f)
f = d + " " + e
print(f)

# String format
age = 22
txt = f"My name is Tusty, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)
txt = f"The price is {20 * price} dollars"
print(txt)

print("when we use single quote \' ,use backslash \\, use new line \n, use carriage return \r, use tab \t, use backspace\b , use fromfeed \f, use octal value \110, use hex value \x48")