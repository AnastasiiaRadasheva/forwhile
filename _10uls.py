#27
for A in range(10, 100):
    for B in range(10, 100):
        num1 = int(str(A) + str(B))
        num2 = int(str(B) + str(A)) 
        
        if num1 % 99 == 0 and num2 % 49 == 0:
            print(f"A = {A}, B = {B}")

#13
count = 0
total_sum = 0

for i in range(100, 1001):
    if i % 7 == 0:
        count += 1
        total_sum += i
print(f"Seitsmega jaguvate arvude arv: {count}")
print(f"Seitsmega jaguvate arvude summa: {total_sum}")
#7
veedi=int(input('sisesta K: '))
A=int(input('sisesta A: '))
B=int(input('sisesta B: '))
for i in range(A, B + 1):
    if i % veedi == 0:
        print(i)
#8
print('дюймы   см')
for i in range(1, 21):
    print(i,"     ", i * 2.5)

#9
euro = int(input("Sisesta eurode arv: "))
aasta = int(input("Sisesta aasta: "))
while aasta > 0:
    euro = (euro * 3)/100 + euro
    aasta -= 1
    print (round(euro, 2))
31
K = int(input("Sisesta kotlettide arv: "))
M = int(input("Sisesta kotlettide arv ühes pannil: "))

pants = K // M
remaining_cutlets = K % M

print(f"Täis panne: {pants}")
print(f"Viimasele pannile jäävad kotletid: {remaining_cutlets}")
#16
for i in range(1, 10):
    print("0" * (i - 1) + str(i) + "0" * (9 - i))

#21
numbrid = [abs(int(input(f"Sisesta arv {i+1}: "))) for i in range(10)]

print("Muudetud arvud:", numbrid)

#14
import random
numeeq=random.randint(1,100)
pip=1
while pip<=numeeq:
    try:
        ymnoj=pip*numeeq
        pip+=1
        print(f'{pip-1} * {numeeq} = {ymnoj}')
    except:
        break
#28 import random
num=random.randint(1,100)
while True:
    try:
        polz1=int(input('vvedite chislo: '))

        if num>polz1:
            print('chislo bolshe')
        elif num<polz1:
            print('chislo menshe')
        else: 
            print('vi ugadali!!!!')
            break
    except:
        print('nepravilnoe znachenie')

#18
for i in range(20, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
#19
print('19')
for i in range(20, 51):
    ref=i/7
    if ref==2 or ref==5 or ref==7:
        print(i)
#10 
for j in range(10):
    a1=float(input('esimese arv: '))
    a2=float(input('teine arv: '))
    if a1>a2:
        print('esimene arv on suurem')
    elif a1<a2:
        print('teine arv on suurem')
    else:
        print('arvud on võrdsed')
print()
#17
adri=2
summ=0
for i in range(1,10):
    summ=adri*i
    print(f'{adri} * {i} = {summ}')
print()

#15
for j in range(10):
    for i in range(10):
        print(i,end=' ')
    print()
print()
#6
N = int(input("sisesdta: "))
positive_count = 0
negative_count = 0
zero_count = 0
for i in range(N):
    number = int(input("arv: "))
    
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1
print(f"positiv: {positive_count}")
print(f"negativ: {negative_count}")
print(f"zero: {zero_count}")
#1
täisaa=0
for i in range(3):
    while True:
        try:
            arv=int(input(f'{i+1} arv '))
            break
        except ValueError:
            print('see pole täisaarv')
    if arv==int(arv): täisaa+=1
print(f'vot ctolko täisarvad {täisaa}')
#2
arv1=0
pip=int(input("do skolki täisarvad chitat"))
for i in range(1,pip):
        while True:
            try:
                arv=int(input(f'{i} arv '))
                arv1=arv1+arv
                print(arv1)
                break
            except ValueError:
                print('see pole täisaarv')
#3
arv2=1
for i in range(8):
        while True:
            try:
                arv=int(input(f'{i+1} arv '))
                if arv>0:
                    arv2=(arv*arv2)
                    print(f'summa {arv2}')
                    break
                else:
                    print('see on negativ arv')
                    print(f'summa {arv2}')
                    break
            except ValueError:
                print('see pole täisaarv')
#4
start = int(input("ot kakogo: "))
end = int(input("do kakogo: "))
for i in range(start, end + 1):
    print(f"kvadrat {i} raven {i**2}")
#5
summa=0
while True:
    try:
        N=int(input('sisest N:'))
        if N>=1:
            for i in range(1,N+1):
                arv=float(input(f'sisesta {i} arv '))
                if arv<0:
                    summa+=arv
            print(f'summa {summa}')
            break
        else:
            print('arv a üeab alema rohkem kui 1')
    except ValueError:
        print('bbebebebe')