import random

aleatorio=random.randint(1,9)
aleatorio2=random.randint(1,9)

if aleatorio==4:
    print("ganaste un chupete")
elif aleatorio== 8:
    print("te ganaste un valon")
elif aleatorio ==3 and aleatorio2 ==7: 
    print("te ganaste nu televisor")
else:
    print("perdiste!!!!")