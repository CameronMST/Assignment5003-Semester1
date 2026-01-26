Message = input("Enter a message or ciphertext, ciphers must be space-seperated integers: ")


def RSAAlgorithm():
    def power(base, exponent, m):
        result = 1
        base = base % m
        while exponent > 0:
            if exponent & 1:
                result = (result * base) % m
            base = (base * base) % m
            exponent = exponent // 2
        return result

    def isPrime(n):
        if n <= 1: 
            return False
        for i in range(2, n): 
            if n % i == 0: 
                return False; 
        return n; 

    def modInverse(e, phi):
        for d in range(2, phi):
            if (d * e) % phi == 1:
                return d
        return None

    def generateKeys(p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 0
        for e in range(2, phi):
            if gcd(e, phi) == 1:
                break
        d = modInverse(e, phi)
        return (e, n), (d, n)

    def gcd(inta, intb):
        while intb !=0:
            inta, intb = intb, inta % intb
        return inta
        
    def encrypt(pk, plaintext):
        key, n = pk
        cipher = [power(ord(char), key, n) for char in plaintext]
        return " ".join(map(str, cipher))

    def decrypt(pk, ciphertext):
        key, n = pk
        try:
            ciphertext = list(map(int, ciphertext.split()))
            plain = [chr(power(char, key, n)) for char in ciphertext]
            return ''.join(plain)
        except ValueError:
            print("Ciphertext is not valid!")
            return
    
    try:
        Input1 = int(input("Enter a prime number for p: "))
        Input2 = int(input("Enter a prime number for q: "))
    except ValueError:
        print("Please enter positive integers only.")
        return
    
    input3 = int(input("Type \"1\" for Encrypt and \"2\" for Decrypt: "))
    Message = input("Enter a message or ciphertext, ciphers must be space-seperated integers: ")
    
    if Input1 == Input2:
        print("p and q cannot be the same!")
        return

  
    if not isPrime(Input1) or not isPrime(Input2):
        print("One or both numbers are not prime!")
        return
  
    if Input1 < 17 or Input2 < 17:
        print("Enter a primes greater than 16.")
        return

    public, private = generateKeys(Input1, Input2)

    if input3 == 1:
        Encrypted_Message = encrypt(public, Message)
        print(f"Original Message: {Message}")
        print(f"Encrypted Message: {Encrypted_Message}")

    elif input3 == 2:
        Decrypted_Message = decrypt(private, Message)
        print(f"Encrypted Message: {Message}")
        print(f"Decrypted Message: {Decrypted_Message}")

    else:
        print("Invalid option selected.")


RSAAlgorithm()