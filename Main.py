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
    
        RSAButton = Button(self, text="Generate Keys & Encrypt/Decrypt", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=self.RSAAlgorithm)
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

        self.Selection = Entry(self, width = 35)
        self.Selection.place(x=50, y=50)
        self.LabelSe = Label(self, text="Enter numbers seperated by whitespace:", fg='white', bg='#1F1F1F')
        self.LabelSe.place(x=50, y=30)

        AscSortButton = Button(self, text="Sort Ascending", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda: self.RunBubbleSort('+'))
        AscSortButton.place(x=150, y=80)

        DesSortButton = Button(self, text="Sort Descending", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda: self.RunBubbleSort('-'))
        DesSortButton.place(x=50, y=80)

    def RunBubbleSort(self, equality):
        list_input = self.Selection.get()
        my_list = list(map(int, list_input.split()))

        def bubblesort(my_list):
            for iter in range(len(my_list)-1):
                    for i in range(len(my_list)-iter-1):

                        if equality == '-':
                            if my_list[i] < my_list[i+1]:
                                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                        #Descending - Placed at top for default Ascending if any other option is entered
                        else:
                            if my_list[i] > my_list[i+1]:
                                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                        #Ascending
            return my_list
                    
        print(bubblesort(my_list))

class SelectionWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

        self.Selection = Entry(self, width = 35)
        self.Selection.place(x=50, y=50)
        self.LabelSe = Label(self, text="Enter numbers seperated by whitespace:", fg='white', bg='#1F1F1F')
        self.LabelSe.place(x=50, y=30)

        AscSortButton = Button(self, text="Sort Ascending", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda: self.Run_Selection_Sort('+'))
        AscSortButton.place(x=150, y=80)

        DesSortButton = Button(self, text="Sort Descending", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda: self.Run_Selection_Sort('-'))
        DesSortButton.place(x=50, y=80)


    def Run_Selection_Sort(self, equality):

        list_input = self.Selection.get()
        my_list = list(map(int, list_input.split()))

        def selection_sort(my_list):
            for iter in range(0, len(my_list)-1):
                min = iter
                for i in range(iter + 1, len(my_list)):
                    
                    if equality == '-':
                        if my_list[i] > my_list[min]:
                            min = i
                    #Descending - Placed at top for default Ascending, if anyother option is entered.
                    else:
                        if my_list[i] < my_list[min]:
                            min = i
                    #Descending
                my_list[iter], my_list[min] = my_list[min], my_list[iter]
            return my_list

        print(selection_sort(my_list)) # (W3Schools, n.d)

class FibonacciWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)
        self.Fibonacci = Entry(self, width = 21)
        self.Fibonacci.place(x=50, y=50)
        self.LabelFib = Label(self, text="Enter a positive integer:", fg='white', bg='#1F1F1F')
        self.LabelFib.place(x=50, y=30)

        FibonacciButton = Button(self, text="Generate the Nth term", command=self.run_fib_memo)
        FibonacciButton.place(x=50, y=150)

    def run_fib_memo(self):
        def fib_memo(n, mem={}):
            if n in mem:
                return mem[n]
            if n <=1:
                mem[n] = n
            else:
                mem[n] = fib_memo(n-1, mem) + fib_memo(n-2, mem)
            return mem[n]

        print(fib_memo(int(self.Fibonacci.get())))

class MergeSortWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

        self.Selection = Entry(self, width = 35)
        self.Selection.place(x=50, y=50)
        self.LabelSe = Label(self, text="Enter numbers seperated by whitespace:", fg='white', bg='#1F1F1F')
        self.LabelSe.place(x=50, y=30)

        AscSortButton = Button(self, text="Sort Ascending", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda: self.Run_Merge_Sort('+'))
        AscSortButton.place(x=150, y=80)

        DesSortButton = Button(self, text="Sort Descending", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda: self.Run_Merge_Sort('-'))
        DesSortButton.place(x=50, y=80)

    def Run_Merge_Sort(self, equality):
        list_input = self.Selection.get()
        my_list = list(map(int, list_input.split()))

        def Merge_Sort(my_list):
            if len(my_list) > 1:
                mid = len(my_list) // 2
            
                
                left_half = my_list[:mid]
                right_half = my_list[mid:]

                Merge_Sort(left_half)
                Merge_Sort(right_half)

                left_index, right_index, main_index = 0, 0, 0

                while left_index < len(left_half) and right_index < len(right_half):
                    
                    #Descending Order
                    if equality == '-':
                        if left_half[left_index] > right_half[right_index]:
                            my_list[main_index] = left_half[left_index]
                            left_index += 1
                            main_index += 1
                    
                        else:
                            my_list[main_index] = right_half[right_index]
                            right_index += 1
                            main_index += 1
                    #Ascending Order, Placed Below for Defaulting.
                    else:
                        if left_half[left_index] < right_half[right_index]:
                            my_list[main_index] = left_half[left_index]
                            left_index += 1
                            main_index += 1

                        else:
                            my_list[main_index] = right_half[right_index]
                            right_index += 1
                            main_index += 1    

                while left_index < len(left_half):
                    my_list[main_index] = left_half[left_index]
                    left_index += 1
                    main_index += 1

                while right_index < len(right_half):
                    my_list[main_index] = right_half[right_index]
                    right_index += 1
                    main_index += 1 #(Tutorialspoint, 2019)

            return my_list

        print(Merge_Sort(my_list))        

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