# Generates heading (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("instruction", "-")

    print('''
To use this program simply enter an integer between 1 to 200. The program will show the factors of your chosen integer.
\nIt will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square
\nTo exit the program, please type 'xxx'.
    ''')


#Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")