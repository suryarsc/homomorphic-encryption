import phe


class MyPaillier:
    # key generation
    public_key, private_key = phe.generate_paillier_keypair()
    # store encrypted Number1 and Number2
    number1, number2 = 0, 0

    def paillier_menu(self):
        while True:
            menu_choice = int(input('''\033[1mCurrent Algothim: Paillier\033[0m
\033[1m1. Show Generated Keys, Current Numbers Being Used\033[0m
   ╵---> \033[3mGenerated keys includes a public key (used for encryption) and a private key (used for decryption)
         See Number1 and Number2 which are user wentered integers which will be used for operations\033[0m
\033[1m2. Change Numbers To Use\033[0m
   ╵---> \033[3mChange the integers on which the operations will be performed on\033[0m
\033[1m3. Perform Operations\033[0m
   ╵---> \033[3mPerform addition, substraction, and scalar multiplication on encrypted integers\033[0m
\033[1m4. Change Algorithm\033[0m
   ╵---> \033[3mChange the algorithm to use\033[0m
\033[1m5. Exit\033[0m\n\nYour Choice: '''))
            print()

            if menu_choice >= 1 and menu_choice <= 5:
                return menu_choice
            else:
                print("Enter A Valid Choice!\n\n")

    def process_choice(self, menu_choice):
        # show keys
        if menu_choice == 1:
            print('\033[1mPublic Key(n):\033[0m', self.public_key.n, '\n')
            print('\033[1mPrivate Key(p):\033[0m', self.private_key.p, '\n')
            print('\033[1mPrivate Key(q):\033[0m', self.private_key.q)
            print()
            print(
                f"\033[1mCurrent Integers Being Used:\033[0m {self.private_key.decrypt(self.number1)}, {self.private_key.decrypt(self.number2)}\n")
            print("Encryption Completed Successfully!\n")
            print(f'\033[1mEncrypted Numbers\033[0m')
            print(f'\033[1mNumber 1:\033[0m {self.number1.ciphertext()}\n')
            print(f'\033[1mNumber 2:\033[0m {self.number2.ciphertext()}\n\n')
        elif menu_choice == 2:
            # take updated numbers input
            a, b = input('Enter Two Numbers To Encrypt: ').split()
            a, b = int(a), int(b)
            # encrypt and store
            # after encryption datatype: <class 'phe.paillier.EncryptedNumber'>
            self.number1, self.number2 = self.public_key.encrypt(a), self.public_key.encrypt(b)

            print(f'{self.private_key.decrypt(self.number1)} is encrypted as: {self.number1.ciphertext()}')
            print()
            print(f'{self.private_key.decrypt(self.number2)} is encrypted as: {self.number2.ciphertext()}')
            print()
            print(
                f"\033[1mCurrent Integers Being Used:\033[0m {self.private_key.decrypt(self.number1)}, {self.private_key.decrypt(self.number2)}\n")
            print(f"Updated The Numbers And They Were Encrypted Successfully!\n")
            print(f'\033[1mEncrypted Numbers\033[0m')
            print(f'\033[1mNumber 1:\033[0m {self.number1.ciphertext()}\n')
            print(f'\033[1mNumber 2:\033[0m {self.number2.ciphertext()}\n\n')
        # Perform Operations
        elif menu_choice == 3:
            while True:
                print("\033[1mOperations Menu\033[0m")
                choice = int(input("""\033[1m1. Addition\033[0m
   ╵---> \033[3mEncrypted Number1 and Number2 Will Be Added To Give Encrypted Result\033[0m
\033[1m2. Substraction\033[0m
   ╵---> \033[3mEncrypted Number1 and Number2 Will Be Substracted To Give Encrypted Result\033[0m
\033[1m3. Scalar Multiplication\033[0m
   ╵---> \033[3mEncrypted Number1 And A Scalar (Number3) Will Be Multiplied To Give Encrypted Result\033[0m
\nEnter Your Choice: """))
                print()

                if choice == 1:
                    result = self.number1 + self.number2
                    print('\033[1mEncrypted Addition Result is:\033[0m', result.ciphertext(), '\n')
                    print('\033[1mDecrypted Addition Result is:\033[0m', self.private_key.decrypt(result), '\n')
                    print('Addition Operation Performed Successfully!\n')
                    break
                elif choice == 2:
                    result = self.number1 - self.number2
                    print('\033[1mEncrypted Substraction Result is:\033[0m', result.ciphertext(), '\n')
                    print('\033[1mDecrypted Substraction Result is:\033[0m', self.private_key.decrypt(result), '\n')
                    print('Substraction Operation Performed Successfully!\n')
                    break
                elif choice == 3:
                    # scalar multiplication needs second number (b) to be decrypted and first number (a) in encrypted form
                    num3 = int(input('Enter A Scalar (Number3) i.e., An Integer: '))
                    print()
                    result = self.number1 * num3
                    print('\033[1mEncrypted Multiplication Result is::\033[0m', result.ciphertext(), '\n')
                    print('\033[1mDecrypted Multiplication Result is:\033[0m', self.private_key.decrypt(result), '\n')
                    print('Multiplication Operation Performed Successfully!\n')
                    break
                else:
                    print('Enter A Valid Choice!\n\n')

            print()
        # Change Algorithm
        elif menu_choice == 4:
            return
        # Exit
        else:
            print("Exiting The Program...\n")
            return
