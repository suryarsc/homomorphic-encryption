# custom module for code
import paillier
import bfv, ckks

print("\n\033[1mHOMOMORPHIC ENCRYPTION\033[0m")
print("""Homomorphic encryption is a cryptographic technique which allows computations (operations) to be performed 
on encrypted data without the need to decrypt it, thus enabling privacy preservation.\n""")

while True:
    print()
    print('''\033[1mHomomorphic Encryption Algorithms Menu\033[0m
\033[3mEach algorithm is designed to perform specific operations on certain datatypes only\033[0m
\033[1m1. Paillier\033[0m
   ╵---> \033[3mSupports addition, subtraction, and scalar multiplication of integers only\033[0m
\033[1m2. BFV\033[0m
   ╵---> \033[3mSupports addition, subtraction, and multiplication of integers only\033[0m
\033[1m3. CKKS\033[0m
   ╵---> \033[3mSupports addition, subtraction, and multiplication of floating-point numbers only\033[0m
\033[1m4. Exit\033[0m\n''')

    algo_choice = int(input("Choose Algorithm: "))
    print()
    if algo_choice == 1: 
        # Paillier Algorithm
        paillier_object = paillier.MyPaillier
        # take two integers input
        num1, num2 = input('Enter Two Integers To Use Paillier Algorithm: ').split()
        num1, num2 = int(num1), int(num2)
        paillier_object.number1, paillier_object.number2 = paillier_object.public_key.encrypt(num1),paillier_object.public_key.encrypt(num2)
        print()

        menu_choice = 0
        while True:
            menu_choice = paillier_object.paillier_menu(paillier_object)
            # break when "Change Algorithm"
            if menu_choice == 4: break

            # menu_choice to process menu_choice of user
            paillier_object.process_choice(paillier_object, menu_choice)
            # to exit program from paillier_menu()
            if menu_choice == 5: exit(0)
    elif algo_choice == 2: 
        # BFV Algorithm
        # keys generated when object created, bfv_object has HE object
        bfv_object = bfv.MyBfv

        # take two integers input, encrypt first ever input of 2 numbers
        num1, num2 = input('Enter Two Integers To Use BFV Algorithm: ').split()
        num1, num2 = int(num1), int(num2)
        bfv_object.number1 = bfv_object.HE.encrypt(num1)
        bfv_object.number2 = bfv_object.HE.encrypt(num2)8
        print()

        menu_choice = 0
        while True:
            menu_choice = bfv_object.bfv_menu(bfv_object)
            # break when "Change Algorithm"
            if menu_choice == 4: break
            # menu_choice to process menu_choice of user
            bfv_object.process_choice(bfv_object, menu_choice)
            # to exit program from bfv_menu()
            if menu_choice == 5: exit(0)

    elif algo_choice == 3: 
        # CKKS Algorithm
        # keys generated when object created, bfv_object has HE object
        ckks_object = ckks.MyCkks

        # take two integers input, encrypt first ever input of 2 numbers
        num1, num2 = input('Enter Two Floating-Point Numbers To Use CKKS Algorithm: ').split()
        num1, num2 = float(num1), float(num2)
        ckks_object.number1 = ckks_object.HE.encrypt(num1)
        ckks_object.number2 = ckks_object.HE.encrypt(num2)
        print()

        menu_choice = 0
        while True:
            menu_choice = ckks_object.ckks_menu(ckks_object)
            # break when "Change Algorithm"
            if menu_choice == 4: break
            # menu_choice to process menu_choice of user
            ckks_object.process_choice(ckks_object, menu_choice)
            # to exit program from ckks_menu()
            if menu_choice == 5: exit(0)

    elif algo_choice == 4:
        print("Exiting The Program...\n")
        break

    else: 
        print("Enter A Valid Choice!\n")