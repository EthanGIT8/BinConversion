def look():
    print("#######################")

def denToBin(num1):
    if num1 > 1:
        denToBin(num1//2)
    print(num1 % 2, end= "")

def binToDen(num2):
    value = 0
    for i in range(len(num2)):
        digit = num2.pop()
        if digit == '1':
            value = value + pow(2, i)
    print("Denary Value = ", value)


def denToHex(num3):
    hexVal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    revNum = ""
    while num3 > 0:
        rem = num3 % 16
        num3 -= rem
        num3 //= 16
        revNum+= str(hexVal[rem])
    print("Hex Value = ", revNum[::-1])

def hexToDen(num4):
    c = count = i = 0
    global len
    len = len(num4) - 1
    while len>=0:
        if num4[len]>='0' and num4[len]<='9':
            rem = int(num4[len])
        elif num4[len]>='A' and num4[len]<='F':
            rem = ord(num4[len]) - 55
        elif num4[len]>='a' and num4[len]<='f':
            rem = ord(num4[len]) - 87
        else:
            c = 1
            break
        count = count + (rem * (16 ** i))
        len = len - 1
        i = i+1

    if c == 0:
        print("\nDenary Value = ", count)

look()
print("\nBinary and Hex Converter\n\n1. Denary to Binary\n2. Binary to Denary\n3. Denary to Hex\n4. Hex to Denary\n")
look()
select = int(input("\nPlease enter a number from the above list of options:\n"))

if select == 1:
    print("Denary to Binary")
    den1 = int(input("Enter a denary number: "))
    denToBin(den1)
elif select == 2: 
    print("Binary to Denary")
    binary = list(input("Enter 8 bit binary: "))
    binToDen(binary)
elif select == 3:
    print("Denary to Hex")
    den2 = int(input("Enter a denary number: "))
    denToHex(den2)
elif select == 4:
    print("Hex to Denary")
    hexadecimal = input("Enter a hex value: ")
    hexToDen(hexadecimal)