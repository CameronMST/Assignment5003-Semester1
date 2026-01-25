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
        return cipher

    def decrypt(pk, ciphertext):
        key, n = pk
        plain = [chr(power(char, key, n)) for char in ciphertext]
        return ''.join(plain)
    
    Input1 = int(input("Enter a prime number for p: "))
    Input2 = int(input("Enter a prime number for q: "))
  
    if not isPrime(Input1) or not isPrime(Input2):
        raise ValueError("Both inputs must be prime numbers!")
  
    if Input1 < 17 or Input2 < 17:
        print("Primes smaller than 17, cannot encrypt all characters correctly.")
        return

    public, private = generateKeys(Input1, Input2)

    Message = 'HI'
    Encrypted_Message = encrypt(public, Message)
    Decrypted_Message = decrypt(private, Encrypted_Message)

    print(f"Original Message: {Message}")
    print(f"Encrypted Message: {Encrypted_Message}")
    print(f"Decrypted Message: {Decrypted_Message}")


RSAAlgorithm()