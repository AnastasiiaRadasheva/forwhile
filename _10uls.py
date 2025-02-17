# #1
# täisaa=0
# for i in range(3):
#     while True:
#         try:
#             arv=int(input(f'{i+1} arv '))
#             break
#         except ValueError:
#             print('see pole täisaarv')
#     if arv==int(arv): täisaa+=1
# print(f'vot ctolko täisarvad {täisaa}')
# #2
# arv1=0
# pip=int(input("do skolki täisarvad chitat"))
# for i in range(1,pip):
#         while True:
#             try:
#                 arv=int(input(f'{i} arv '))
#                 arv1=arv1+arv
#                 print(arv1)
#                 break
#             except ValueError:
#                 print('see pole täisaarv')
#3
arv2=0
for i in range(8):
        while True:
            try:
                arv=int(input(f'{i+1} arv '))
                if arv>0:
                    arv2=arv*arv2
                    print(f'summa {arv2}')
                    break
                else:
                    print('see on negativ arv')
                    print(f'summa {arv2}')
                    break
            except ValueError:
                print('see pole täisaarv')
#4
while True:
    try:
