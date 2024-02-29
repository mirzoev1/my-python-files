# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:58:35 2024

@author: Shukurullo
"""
# savol = 'yaxshi ko\'rgan kitobingiz nomi?  '
# savol += 'Dasturni to\'xtashish uchun \'stop\' so\'zini yozing  '
# kitob = ''
# while kitob != 'stop':
#     kitob = input(savol)
# print("dastur tugadi")    


# savol =('Yoshingizni kirting   ')

# #qiymat = 'stop' or qiymat = 'quit'
# while True:
#     qiymat = input(savol)
#     if qiymat== 'exit' or qiymat == 'quit':
#           break
#     yosh = int(qiymat)  
#     if yosh <7:       
#         narx = 2    
#     elif  7<= yosh<=18:
#         narx = 3
#     elif 18<yosh<65:
#         narx = 10
#     else :
#         narx = 0     
#     if yosh ==0:
#       print("SIZGA KIRISH TEKIN")
#     else:
#       print(f"Siz ucun kirish {narx} s")
            
         
# savol =('Yoshingizni kirting   ')
#   #qiymat = 'stop' or qiymat = 'quit'
# flag = True  
# while True:
#     qiymat = input(savol)
#     if qiymat== 'exit' or qiymat == 'quit':
#           flag = False
#     yosh = int(qiymat)  
#     if yosh <7:       
#         narx = 2    
#     elif  7<= yosh<=18:
#         narx = 3
#     elif 18<yosh<65:
#         narx = 10
#     else :narx = 0
              
#     if narx ==0:
#                 print("SIZGA KIRISH TEKIN")
#     else:
#       print(f"Siz ucun kirish {narx} s")
             


print("quyidagi dastur siz kiritgan sonning\n ildizini chiqaradi\n")
savol = 'musbat son kiriting'
savol += ' dasturga \'exit\' deb yozmasangiz tuxtamaydi '
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
            ishora = False
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning  ildizi {ildiz} ga teng") 
print("DASTUR TUGADI")











