secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
#char = secret[0]
#print(ord('Z'))
#print(chr(68))
#print(chr((ord(char))))
for i in range(0, len(secret)):
    for char in secret:
        if char.upper() == True:
            print(char)
