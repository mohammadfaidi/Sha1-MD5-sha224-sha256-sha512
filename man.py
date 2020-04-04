import hashlib
while 1:
    hashvalue = input("Enter the string:")

    hashvalue2 = hashlib.md5()
    print(hashvalue)
    # <md5 HASH object @ ox00ce3f10>

    hashvalue2.update(hashvalue.encode())
    print(hashvalue2.hexdigest())

    hashvalue3 = hashlib.sha1()
    hashvalue3.update(hashvalue.encode())
    print(hashvalue3.hexdigest())

    hashvalue4 = hashlib.sha224()
    hashvalue4.update(hashvalue.encode())
    print(hashvalue4.hexdigest())

    hashvalue5 = hashlib.sha256()
    hashvalue5.update(hashvalue.encode())
    print(hashvalue5.hexdigest())

    hashvalue6 = hashlib.sha512()
    hashvalue6.update(hashvalue.encode())
    print(hashvalue6.hexdigest())






