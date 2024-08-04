burger, cola, hotdog, sandwishes = "","","",""
print("Type 'y' for order confirmation; if not, type 'n'.")
burger=input("Do you want a burger? :")
cola=input("Do you want a cola? :")
hotdog=input("Do you want a hotdog? :")
sandwishes=input("Do you want a sandwishes? :")

if burger=='y' and cola=='n' and hotdog=='n' and sandwishes=='n':
    print("50% discount")

elif burger=='y' and cola=='n' and hotdog=='y' and sandwishes=='n':
    print("30% discount")

elif burger=='y' and cola=='n' and hotdog=='n' and sandwishes=='y':
    print("10% discount")

else:
    print("no discount")