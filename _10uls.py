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

#17
adri=2
summ=0
for i in range(1,10):
    summ=adri*i
    print(f'{adri} * {i} = {summ}')
print()

#15
from difflib import SequenceMatcher


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

