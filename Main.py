from tkinter import *
from tkinter import ttk
import ctypes

class BaseWindow: #Setting up a BaseWindow, so other Windows will inherit the colouring and sizing.
    def WindowParameters(self, window):
        #Window Configuration
        self.title("Algorithm App")
        window.geometry("550x550")
        window.config(background="#1F1F1F", relief=SUNKEN, bd=5)
        window.resizable(False, False)
        #Taskbar & Taskbar Image
        window.iconbitmap(r"Winchester.ico")
        myappid = "mycompany.myproduct.subproduct.version"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(Tk, BaseWindow):
    def __init__(self): #Constructor
        super().__init__()
        self.WindowParameters(self)

        #Background Image & Text.
        image = PhotoImage(file=r"Winchester.png")  # Opens Image and Assigns it to variable
        self.photo = image
        banner_Label = Label(self, text="Algorithm App", font=('Arial', 20, 'bold'), fg='green', bg='#0A0A0A', image=self.photo, compound='top')
        banner_Label.place(anchor=N, rely=0, relx=0.5)

        # Drop Down Menu
        self.clicked = StringVar()
        self.clicked.set("Select Option")
        drop = OptionMenu(self, self.clicked, "RSA", "Bubble Sort", "Selection Sort", "Nth Fibonacci Solver", "Merge sort - Divide and Conquer", "Randomised Algorithm", "Recursion", "Search Algorithm", "Behavioural Pattern", "Creational Pattern", "Structural Pattern")  # Source - https://www.geeksforgeeks.org/python/tkinter-optionmenu-widget/
        drop.config(font='Arial', fg='white', bg='purple', activebackground='purple', activeforeground='white', bd=1, highlightthickness=0)
        drop.place(anchor=N, rely=0.7, relx=0.5)

        # Confirm Button
        confirm_Button = Button(self, text='Confirm!', width=12, fg='white', bg='purple', activebackground='purple', activeforeground='white', command=self.selected_algorithm)  # You can technically put everything that uses .config on the same line
        confirm_Button.config(state=ACTIVE)
        confirm_Button.place(anchor=N, rely=0.76, relx=0.5)

    #Switch statements, for opening new Windows
    def selected_algorithm(self):
        selected = self.clicked.get()
        match selected:
            case "RSA":
                RSAWindow(self)
            case "Bubble Sort":
                BubbleWindow(self)
            case "Selection Sort":
                SelectionWindow(self)
            case "Nth Fibonacci Solver":
                FibonacciWindow(self)
            case "Merge sort - Divide and Conquer":
                MergeSortWindow(self)
            case "Randomised Algorithm":
                RandomisedWindow(self)
            case  "Recursion":
                RecursionWindow(self)
            case "Search Algorithm":
                 SearchWindow(self)
            case "Behavioural Pattern":
                 BehaviouralWindow(self)
            case "Creational Pattern":
                 CreationalWindow(self)
            case "Structural Pattern":
                StructuralWindow(self)

    #Algorithm Window Initalisation
class RSAWindow(Toplevel, BaseWindow): #FIX THIS TO ENSURE BOTH NUMBERS ARE DISTINCT PRIMES.
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)
        self.EntryP = Entry(self, width = 21)
        self.EntryQ = Entry(self, width = 21)
        self.LabelP = Label(self, text="Enter prime number p:", fg='white', bg='#1F1F1F')
        self.LabelQ = Label(self, text="Enter prime number q:", fg='white', bg='#1F1F1F')

        self.LabelP.place(x=50, y=30)
        self.LabelQ.place(x=50, y=80)
        self.EntryP.place(x=50, y=50)
        self.EntryQ.place(x=50, y=100)
    
        RSAButton = Button(self, text="Generate Keys & Encrypt/Decrypt", command=self.RSAAlgorithm)
        RSAButton.place(x=50, y=150)

    def RSAAlgorithm(self):
        def power(base, expo, m):
            res = 1
            base = base % m
            while expo > 0:
                if expo & 1:
                    res = (res * base) % m
                base = (base * base) % m
                expo = expo // 2
            return res

        def isPrime(n): #Time complexity = O(n) and Space is O(1) - Very inefficient at large primes.
            if n <= 1: #Primes need two distinct integers.
                return False
            for i in range(2, n): #This will check between 2 until n, in the case of 2 it actually works because it will be an empty range, and it will return outside of the loop
                if n % i == 0: #Prime numbers cannot result in an remainder of 0
                    return False; #Will return false & halt function
            return n; #Only will run if the division does not result in a remainder of 0, meaning its prime.

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

        def gcd(a, b):
            while b !=0:
                a, b = b, a % b
            return a
            
        def encrypt(pk, plaintext):
            key, n = pk
            cipher = [power(ord(char), key, n) for char in plaintext]
            return cipher

        def decrypt(pk, ciphertext):
            key, n = pk
            plain = [chr(power(char, key, n)) for char in ciphertext]
            return ''.join(plain)

        Input1 = int(self.EntryP.get())
        Input2 = int(self.EntryQ.get())

        if not isPrime(Input1) or not isPrime(Input2):
            raise ValueError("Both inputs must be prime numbers!")

        public, private = generateKeys(Input1, Input2)

        Message = 'HI'
        Encrypted_Message = encrypt(public, Message)
        Decrypted_Message = decrypt(private, Encrypted_Message)

        print(f"Original Message: {Message}")
        print(f"Encrypted Message: {Encrypted_Message}")
        print(f"Decrypted Message: {Decrypted_Message}")


        #Encryption - Two large numbers, which are secret, calculate the product of multiplication between the primes
        #Decryption -

        #We need two key pairs a public and a private
        #We need to convert messages to ASCII
        #We need to pad the messages to make sure each ASCII representation is three digits.

        #Example if our keys are (5, 14) and our text is B or Ascii 2
        #We represent this as 2^5(mod 14) == 4 or Ciphertext D.

        #For decryption the modulus number remains the same 14
        #The second number will be for example 11 (11, 14) | The private keys are UNIQUE for encryption and decryption.

        # D -> 4 | 4^11(MOD 14) = 4194304(MOD 14) = 2 -> B The original text

        #---------------------------------------------

        #P = 2, P = 7 | Our two prime numbers
        #N = The product of the two primes | N = 14

        # fi function (Russian f) f(n) = Essentially we just get rid of every common factor of 14 exluding 1. | f(n) counts how many positive numbers up to n are relatively prime to 9 e.g 1, 2, 3 is not because 9 is divisible by 3, 4, 5, 7,8 are all relatively prime. | f(p) = p-1 when p is prime
        # These are our coprimes with 14 e.g in this case 1, 3, 5, 9, 11, 13 | 6 Numbers total
        #Coprime or relatively prime means the two numbers will have a GCD of 1.

        #We use a way to compute this number of 6 using this formula f(n) = (p-1)(q-1) e.g (2-1)(7-1) = (1)*(6) = 6

        # e (Encryption private key)  | Has to be between 1 and f(n) | Which in this case is 6.
        #Has to be coprime with N, f(N) so 14 and 6 so 2, 3, 4, 5 | We cannot use 3, because it is a common factor and 2, 4 are even and cannot be co-prime so we will use 5.

        #D - The decryption key | Has to follow one condition d*e(mod f(n) = 1 | d*5 x (MOD 6) = 1
        #Multiples of 5, will fit this pattern | 5, 10, 15, 20, 25, 30
        #5MOD 6 = 5 | 10MOD 6 = 4 ..... When we get to 25MOD 6 we will get 1 | 30 Will be 0 35 will start again from 5 MOD 6 numbers will always be remainder 0-5
        #D is the index of the Number that will equal to remainder 1 so 25 mod 5 is 1, but its index is index 5 (Non computing index)

        #We need to find the greatest common divisor of f(n) & e

        # Encryption
        # e = 5 | Private key
        # n = 14 | Public key


        #Decryption
        # d = 5
        # n = 14 | Public Key








class BubbleWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class SelectionWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class FibonacciWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class MergeSortWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class RandomisedWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class RecursionWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class SearchWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class BehaviouralWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class StructuralWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

class CreationalWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)


#Algorithms


#Produces Window
app = MainWindow()
app.mainloop()