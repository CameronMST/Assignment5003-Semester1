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
        
        Input1 = int(self.EntryP.get())
        Input2 = int(self.EntryQ.get())
    
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