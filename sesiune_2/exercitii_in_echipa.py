# daca conditia prima conditie x se intruneste programul ruleaza un set de instructiuni, altfel o va rula pe cea dea doua


x = 10
y = 10
# 2
if x >= 0:
    print("numarul este natural")
# 3
if x > 0:
    print('x este numar pozitiv')
elif x == 0:
    print('numarul este neutru')
else:
    print('numarul este negativ')
# 4
print(-2 < x < 13)

# 5
print(x - y < 5)

# 6
print(not 5 <= x <= 27)

# 7
if x == y:
    print('x si y sunt egale')
else:
    if x > y:
        print('x este mai mare')
    else:
        print('y este mai mare')
