import Pyfhel


class MyCkks:
    HE = Pyfhel(
        context_params={'scheme': 'CKKS',
                        'n': 16384,
                        'qi_sizes': [30, 30, 30, 30, 30],
                        'scale': 2 ** 30},
        key_gen=True,
    )

    # store encrypted Number1 and Number2
    number1, number2 = 0, 0

    def ckks_menu(self):
        while True:
            menu_choice = int(input('''\033[1mCurrent Algothim: CKKS\033[0m
\033[1m1. Show Current Numbers Being Used\033[0m
   ╵---> \033[3mSee Number1 and Number2 which are user entered floating-point numbers which will be used for operations\033[0m
\033[1m2. Change Numbers To Use\033[0m
   ╵---> \033[3mChange the floating-point numbers on which the operations will be performed on\033[0m
\033[1m3. Perform Operations\033[0m
   ╵---> \033[3mPerform addition, substraction, and multiplication on encrypted floating-point numbers\033[0m
\033[1m4. Change Algorithm\033[0m
   ╵---> \033[3mChange the algorithm to use\033[0m
\033[1m5. Exit\033[0m\n\nYour Choice: '''))
            print()

            if menu_choice >= 1 and menu_choice <= 5:
                return menu_choice
            else:
                print("Enter A Valid Choice!\n\n")

    def process_choice(self, menu_choice):
        if menu_choice == 1:
            # show current numbers
            print(
                f"\033[1mCurrent Floating-Point Numbers Being Used:\033[0m {self.HE.decrypt(self.number1)[0]}, {self.HE.decrypt(self.number2)[0]}\n")
            print("Encryption Completed Successfully!\n")
            print(f'\033[1mEncrypted Numbers\033[0m')
            print(f'\033[1mNumber 1:\033[0m {self.number1}\n')
            print(f'\033[1mNumber 2:\033[0m {self.number2}\n\n')
        elif menu_choice == 2:
            # take updated numbers input
            a, b = input('Enter Two Floating-Point Numbers To Encrypt: ').split()
            a, b = float(a), float(b)
            # after encryption datatype: <Pyfhel Ciphertext at 0x103568d60, scheme=bfv, size=2/2, noiseBudget=45>
            self.number1, self.number2 = self.HE.encrypt(a), self.HE.encrypt(b)

            print(f'{self.HE.decrypt(self.number1)[0]} is encrypted as: {self.number1}')
            print()
            print(f'{self.HE.decrypt(self.number2)[0]} is encrypted as: {self.number2}')
            print()
            print(
                f"\033[1mCurrent Floating-Point Numbers Being Used:\033[0m {self.HE.decrypt(self.number1)[0]}, {self.HE.decrypt(self.number2)[0]}\n")
            print(f"Updated The Floating-Point Numbers And They Were Encrypted Successfully!\n")
            print(f'\033[1mEncrypted Numbers\033[0m')
            print(f'\033[1mNumber 1:\033[0m {self.number1}\n')
            print(f'\033[1mNumber 2:\033[0m {self.number2}\n\n')
        # Perform Operations
        elif menu_choice == 3:
            while True:
                print("\033[1mOperations Menu\033[0m")
                choice = int(input("""\033[1m1. Addition\033[0m
   ╵---> \033[3mEncrypted Number1 and Number2 Will Be Added To Give Encrypted Result\033[0m
\033[1m2. Substraction\033[0m
   ╵---> \033[3mEncrypted Number1 and Number2 Will Be Substracted To Give Encrypted Result\033[0m
\033[1m3. Multiplication\033[0m
   ╵---> \033[3mEncrypted Number1 And Number2 Will Be Multiplied To Give Encrypted Result\033[0m
\nEnter Your Choice: """))
                print()

                if choice == 1:
                    result = self.number1 + self.number2
                    print('\033[1mEncrypted Addition Result is:\033[0m', result, '\n')
                    print('\033[1mDecrypted Addition Result is:\033[0m', self.HE.decrypt(result)[0], '\n')
                    print('Addition Operation Performed Successfully!\n')
                    break
                elif choice == 2:
                    result = self.number1 - self.number2
                    print('\033[1mEncrypted Substraction Result is:\033[0m', result, '\n')
                    print('\033[1mDecrypted Substraction Result is:\033[0m', self.HE.decrypt(result)[0], '\n')
                    print('Substraction Operation Performed Successfully!\n')
                    break
                elif choice == 3:
                    # multiplication of 2 encrypted numbers
                    result = self.number1 * self.number2
                    print('\033[1mEncrypted Multiplication Result is::\033[0m', result, '\n')
                    print('\033[1mDecrypted Multiplication Result is:\033[0m', self.HE.decrypt(result)[0], '\n')
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
