print("Caesar Cipher Game")
st="yes"
while st=="yes":
    en=input("En or De ").strip().lower()
    msg=input("Msg ").strip()       
    num=int(input("Number "))
    res=""
    if en=="encode":
        for let in msg:
            if let.isalpha() and let.isupper(): res+=chr((ord(let)+num-65)%26+65)
            elif let.isalpha() and let.islower(): res+=chr((ord(let)+num-97)%26+97)
            else:
                res+=let
    elif en=="decode":
        for let in msg:
            if let.isalpha() and let.isupper(): res+=chr((ord(let)-num-65)%26+65)
            elif let.isalpha() and let.islower(): res+=chr((ord(let)-num-97)%26+97)
            else:
                res+=let
    print("Result ",res)
    st=input("Continue or Not ").strip().lower()
