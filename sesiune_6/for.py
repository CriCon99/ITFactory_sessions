'''
o bucla for este folosita pentru a itera peste o secventa (lista, tuplu, dictionar, set sau string)
'''

for i in range(10):
    print(i)
print(20 * '-')
for i in range(5, 10):
    print(i)
print(20 * '-')
for i in range(5, 10, 2):
    print(i)

print(20 * '-')
l =[1,2,3,4,5]
for i in range(len(l)):
    print(l[i])

print(20 * '-')
# for each

fructe = ['mere', 'pere', 'banane']

for x in fructe:
    print(x)


print(20 * '-')
for x in 'ana are mere':
    print(x)


print(20 * '-')
d = {
    'a':1,
    'b':2
}
for x in d:  # iterarea in dictionar se face implicit prin chei
    print(x)

for x, value in d.items():
    print(x,value)

print(20 * '-')
# break
for x in fructe:
    if x == 'banane':
        break
    print(x)
print(20 * '-')
#continue

for x in fructe:
    if x == 'mere':
        continue
    print(x)
print(20 * '-')
# for + else

for x in fructe:
    print(x)
else:
    print('sunt in else')
print(20 * '-')
# else + break

for x in fructe:
    if x == 'pere':
        break
    print(x)
else:
    print('sunt in else')

print(20 * '-')
# nested for

adj = ['rosii', 'mari', 'delicioase']

for x in fructe:
    for y in adj:
        print(x,y)

print(20 * '-')
# pass

for x in range(100_000_000):
    pass
print('gata')