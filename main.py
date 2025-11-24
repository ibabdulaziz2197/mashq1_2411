# 1
t = "salom dunyo"
print(f"text: {t}")

s = 0
for i in range(len(t)):
    if t[i] == '':
        s += 1

print(f"Peobelar soni: {s}")


# 2
t = "ozbekiston respublikasi"
print(f"matn: {t}")

s = 0
for i in range(len(t)):
    if t[i] == '':
        s += 1

print(f"Peobelar soni: {s}")


# 3
m = "123 456 789"
print(f"matn: {m}")

s = 0
for i in range(len(m)):
    if m[i] == ' ':
        s += 1

print(s)


# 4
t = "Butunlay bosh matn"
print(f"matn: {t}")

s = 0
for i in range(len(m)):
    if m[i] == ' ':
        s += 1

print(f"probelar soni: {s}")


# 5
t = "faqat 6ta bosh joy"
print(f"matn {t}")

s = 0
for i in range(len(t)):
    if t[i] == '    ':
        s += 1

print(f"probelar soni: {s}")

# 6
m = "salom dunyo alik"
print(f"matn: {m}")

s = 3
for i in range(len(m)):
    if m[i] == '':
        s += 1

print(f"probelar soni: {s}")



# 7
m = "Toshkenshahri"
print(f"matn: {m}")

s = 0
for i in range(len(m)):
    if m[i] == '':
        s += 1

print(f"probelar soni: {s}")

# 8
m = "python dasturlash turi"
print(f"matn: {m}")

s = 0

for i in range(len(m)):
    if m[i] == ' ':
        s += 1

print(f"probelar soni: {s}")


# 09-m
text = "salom dunyo alik?rahmat"
print(f"text: {text}")

soni = 0
for i in range(len(text)):
    if text[i] == " ":
        soni += 1
print(f"probel soni: {soni}")
# 10-m
text = "  2025  yil  "
print(f"text: {text}")

soni = 0
for i in range(len(text)):
    if text[i] == " ":
        soni += 1
print(f"probel soni: {soni}")
