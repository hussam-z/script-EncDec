#Created by : Mohammad Hussam Alzeyyat
#Facebook :  https://www.facebook.com/muhammedhusam.alzeyyat.9
#Running on python3
#For execute script use this command in terminal 'python3 Z-EnDeC.py' not './Z-EnDeC.py'
#can execute on linux and windows machine



def banner():
	print('''



              ███████╗      ███████╗███╗   ██╗██████╗ ███████╗ ██████╗
               ╚══███╔╝      ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔════╝
                 ███╔╝ █████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██║     
                ███╔╝  ╚════╝██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██║     
             ███████╗      ███████╗██║ ╚████║██████╔╝███████╗╚██████╗
            ╚══════╝      ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝ ╚═════╝



                                                               [+] Z-EnDeC [+]
                                                    [+] Encryption & Decryption [+]

                                                                  Created By :
                                                    Mohammad Hussam Alzeyyat

                                                                  Facebook :
                            https://www.facebook.com/muhammedhusam.alzeyyat.9


                            
''')

banner()

print("#"*40)
print("if you want encryption press '1' ")
print("if you want decryption press '2' ")
print("if you want go out press '0' ")
print("#"*40)

enc_dec_i = input("please enter your choose : ")

def my_md5():

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        from hashlib import md5 
        word_i = input("please enter a text : ")
    
        word = md5(word_i.encode()).hexdigest()
        print(word)
    elif we_i == "e2":
        from hashlib import md5
        file_i = input("please enter a text file : ")
        with open(file_i,mode='r')as f:
            for new_line in f:
                line= md5(new_line.encode()).hexdigest()
                print(line)

def my_sha1():

    from hashlib import sha1
    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        
        word_i = input("please enter a text : ")

        word = sha1(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i,mode='r')as f:
            for new_line in f:
                line= sha1(new_line.encode()).hexdigest().strip()
                print(line)

def my_sha224():

    from hashlib import sha224
    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")
    if we_i == "w1":
        word_i = input("please enter a text : ")

        word = sha224(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i,mode='r')as f:
            for new_line in f:
                line= md5(new_line.encode()).hexdigest().strip()
                print(line)
def my_sha256():

    from hashlib import sha256
    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")
    if we_i == "w1":
        word_i = input("please enter a text : ")

        word = sha256(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i,mode='r')as f:
            for new_line in f:
                line= md5(new_line.encode()).hexdigest().strip()
                print(line)

def my_sha384():

    from hashlib import sha384
    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")
    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = sha384(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i,mode='r')as f:
            for new_line in f:
                line = sha384(new_line.encode()).hexdigest().strip()
                print(line)

def my_sha512():
    
    from hashlib import sha512
    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = sha512(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i=input("please enter a text file : ")

        with open(file_i,mode='r'):
            for new_line in f:
                line= sha512(new_line.encode()).hexdigest().strip()
                print(line)


def my_sha3_224():

    from hashlib import sha3_224

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = sha3_224(word_i.encode()).hexdigest()
        print(word)
        
    elif we_i == "e2":
        with open(file_i,mode='r')as f:
            file_i = input("please enter a text file : ")
            for new_line in f:
                line = sha3_224(new_line.encode()).hexdigest().strip()
                print(line)
                
def my_sha3_256():

    from hashlib import sha3_256

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = sha3_256(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i,mode='r')as f:
            for new_lin in f:
                line = sha3_256(new_line.encode()).hexdigest().strip()
                print(line)
            

def my_sha3_384():

    from hashlib import sha_384

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose :")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = sha3_384(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i,mode='r')as f:
            for new_line in f:
                line = sha3_384(new_lin.encode()).hexdigest().strip()
                print(line)
        

def my_sha3_512():

    from hashlib import sha3_512

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = sha3_512(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i =input("please enter a text file : ")
        with opne(file_i,mode='r')as f:
            for new_line in f:
                line = sha3_512(new_line.encode()).hexdigest().strip()
                print(line)

def my_blake2b():

    from hashlib import blake2b

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = blake2b(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i , mode='r')as f:
            for new_line in f:
                line = blake2b(new_line.encode()).hexdigest().strip()
                print(line)

def my_blake2s():

    from hashlib import blake2s

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = blake2s(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i, mode='r')as f:
            for new_line in f:
                line= blake2s(line.encode()).hexdigest().strip()
                print(line)

def my_shake_128():

    from hashlib import shake_128

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = shake128(word_i.encode()).hexdigest()
        print(word)

    elif we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i , mode='r')as f:
            for new_line in f:
                line = shake_128(new_line.encode()).hexdigest().strip()
                print(line)
            

def my_shake_256():

    from hashlib import shake_256

    print("if you want write a text enter 'w1' ")
    print("if you want enter a text file enter 'e2' ")

    we_i = input("please enter your choose : ")

    if we_i == "w1":
        word_i = input("please enter a text : ")
        word = shake_256(word_i.encode()).hexdigest()
        print(word)

    elif  we_i == "e2":
        file_i = input("please enter a text file : ")

        with open(file_i,mode='r')as f:
            for new_line in f :
                line = shake_256(new_line.encode()).hexdigest().strip()
                print(line)

def encryption() :

    print("= "*20)
    print("** Encryption Types **")
    print("- "*5)
    print("1- md5 ")
    print("- "*5+"\n")

    print("- "*5)
    print("2- sha1")   # Encryption Types
    print("3- sha224")
    print("4- sha256")
    print("5- sha384")
    print("6- sha512")
    print("7- sha3_224")
    print("8- sha3_256")
    print("9- sha3_384")
    print("10- sha3_512")
    print("- "*5+"\n")

    print("- "*5)
    print("11- blake2b")
    print("12- blake2s")
    print("- "*5+"\n")

    print("- "*5)
    print("13- shake_128")
    print("14- shake_256")
    print("- "*5+"\n")

    print("if you want go out press '0'")
    print("= "*20)

    type_i = input("please enter type number : ")

    if type_i == "1":
        my_md5()

    elif type_i == "2":
        my_sha1()

    elif type_i == "3":
        my_sha224()

    elif type_i == "4":
        my_sha256()

    elif type_i == "5":
        my_sha384()

    elif type_i == "6":
        my_sha512()

    elif type_i == "7":
        my_sha3_224()

    elif type_i == "8":
        my_sha3_256()

    elif type_i == "9":
        my_sha3_384()

    elif type_i == "10":
        my_sha3_512()

    elif type_i == "11":
        my_blake2b()

    elif type_i == "12":
        my_blake2s()

    elif type_i == "13":
        my_shake_128()

    elif type_i == "14":
        my_shake_256()

    elif type_i == "0":
        print(">> Good Buy <<")
        exit


def my_dec_md5():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import md5
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if md5(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_sha1():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha1
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha1(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_sha224():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha224
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha224(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_sha256():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha256
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha256(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_sha384():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sh384
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha384(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_sha512():
    
    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha512
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha512(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        


def my_de_sha3_224():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha3_224
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha3_224(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        
               
def my_dec_sha3_256():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha3_256
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha3_256(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        
      

def my_dec_sha3_384():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha3_384
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha3_384(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        
 

def my_dec_sha3_512():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import sha3_512
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if sha3_512(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_blake2b():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import blacke2b
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if blacke2b(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_blake2s():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import blacke2s
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if blacke2s(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        

def my_dec_shake_128():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import shake_128
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if shake_128(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)

        
            

def my_dec_shake_256():

    hash_i = input("please enter a hash : ")
    file_i = input("please enter a data file : ")

    from hashlib import shake_256
    with open(file_i, mode='r')as f:
        for dec_hash in f:
            dec_hash=dec_hash.strip()
            if shake_256(dec_hash.encode()).hexdigest() == hash_i :
                print("hash is cracked : ",dec_hash)


def decryption():

    print("= "*20)
    print("** Decryption Types **") 
    print("- "*5)
    print("1- md5 ")
    print("- "*5+"\n")

    print("- "*5)
    print("2- sha1")   # Dncryption Types
    print("3- sha224")
    print("4- sha256")
    print("5- sha384")
    print("6- sha512")
    print("7- sha3_224")
    print("8- sha3_256")
    print("9- sha3_384")
    print("10- sha3_512")
    print("- "*5+"\n")

    print("- "*5)
    print("11- blake2b")    
    print("12- blake2s")
    print("- "*5+"\n")

    print("- "*5)
    print("13- shake_128")
    print("14- shake_256")
    print("- "*5+"\n")

    print("if you want go out press '0'")
    print("= "*20)

    type_i = input("please enter type number : ")
    
    if type_i == "1":
        my_dec_md5()

    elif type_i == "2":
        my_dec_sha1()

    elif type_i == "3":
        my_dec_sha224()

    elif type_i == "4":
        my_dec_sha256()

    elif type_i == "5":
        my_dec_sha384()

    elif type_i == "6":
        my_dec_sha512()

    elif type_i == "7":
        my_dec_sha3_224()

    elif type_i == "8":
        my_dec_sha3_256()

    elif type_i == "9":
        my_dec_sha3_384()

    elif type_i == "10":
        my_dec_sha3_512()

    elif type_i == "11":
        my_dec_blake2b()

    elif type_i == "12":
        my_dec_blake2s()

    elif type_i == "13":
        my_dec_shake_128()

    elif type_i == "14":
        my_sdec_hake_256()

    elif type_i == "0":
        print(">> Good Buy <<")
        exit






if enc_dec_i == "1":
    encryption()

elif enc_dec_i == "2":
    decryption()

elif enc_dec_i == "0":
    print(">> Good Buy <<")
    exit

else:
    print("I'm Soory")
    exit



