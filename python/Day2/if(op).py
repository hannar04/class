'''name = "Chan Pyae"

if name=="Chan Pyae":
    print(f"Hello {name}")
else:
    print("You are not Chan Pyae")
-----------------------------------'''
is_adult=True

if is_adult:
    print("is adult")

age = 17

if age>=18:
    print("adult")
else:
    print("Not an adult")
'''------------------------------------
have_coupon=True
is_student=False
if is_student:
    if have_coupon:
        print("You can get a discount")
    else:
        print("You don't have a coupon")
else:
    print("You can't get a discount")
------------------------------------
have_coupon=False
is_student=False

if is_student:
    print("You can get a discount because you are a student.")
elif have_coupon:
    print("You can get a discount because you have a coupon.")
else:
    print("You can't a discount")
------------------------------------
brown_suger_milktea=False
choco_milktea=False
macha=False

if brown_suger_milktea:
    print("brown_suger_milktea")
elif choco_milktea:
    print("choco_milktea")
elif macha:
    print("macha")
else:
    print("None")
------------------------------------
action=input("Type 'b' for Brown suger milktea \n Type 'c' for Choco milktea \n Type 'm' for Macha")

if action == 'b':
    print("Brown suger milktea")
elif action == 'c':
    print("Choco milktea")
elif action == 'm':
    print("Macha")
else:
    print("None")'''