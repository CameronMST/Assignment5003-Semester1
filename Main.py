import time
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
        drop = OptionMenu(self, self.clicked, "RSA", "Bubble Sort", "Selection Sort", "Nth Fibonacci Solver", "Merge sort - Divide and Conquer", "Randomised Algorithm", "Recursion", "Search Algorithm", "Palindrome" ,"Behavioural Pattern", "Creational Pattern", "Structural Pattern")  # Source - https://www.geeksforgeeks.org/python/tkinter-optionmenu-widget/
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
            case "Palindrome":
                PalindromeWindow(self)

    #Algorithm Window Initalisation
class RSAWindow(Toplevel, BaseWindow): #FIX THIS TO ENSURE BOTH NUMBERS ARE DISTINCT PRIMES.
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)
        self.EntryP = Entry(self, width = 21)
        self.EntryQ = Entry(self, width = 21)
        self.EntryString = Entry(self, width = 21)
        self.LabelP = Label(self, text="Enter prime number p:", fg='white', bg='#1F1F1F')
        self.LabelQ = Label(self, text="Enter prime number q:", fg='white', bg='#1F1F1F')
        self.EnteredString = Label(self, text="Enter a string to Encrypt / Decrypt:", fg='white', bg='#1F1F1F')
        
        self.LabelEncryptDecrypt = Text(self, fg='black', bg='white', width=40, height=5)
        self.LabelEncryptDecrypt.place(x=50, y=230)

        self.LabelP.place(x=50, y=30)
        self.LabelQ.place(x=50, y=80)
        self.EntryP.place(x=50, y=50)
        self.EntryQ.place(x=50, y=100)
        self.EntryString.place(x=50, y=150)
        self.EnteredString.place(x=50, y=130)

        Encrypt = Button(self, text="Encrypt", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda:self.RSAAlgorithm(True))
        Encrypt.place(x=50, y=200)

        Decrypt = Button(self, text="Decrypt", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda:self.RSAAlgorithm(False))
        Decrypt.place(x=150, y=200)

    def RSAAlgorithm(self, EncryptDecrypt):
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
            ciphertext = list(map(int, ciphertext.split()))
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

        Message = self.EntryString.get()

        if EncryptDecrypt == True:
            Encrypted_Message = encrypt(public, Message)
            self.LabelEncryptDecrypt.delete("1.0", "end")
            self.LabelEncryptDecrypt.insert("1.0", Encrypted_Message)

        else:
            Decrypted_Message = decrypt(private, Message)
            self.LabelEncryptDecrypt.delete("1.0", "end")
            self.LabelEncryptDecrypt.insert("1.0", Decrypted_Message)

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

        ShuffleDeck = Button(self, text="Shuffle Deck", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=self.Shuffle_Deck)
        ShuffleDeck.place(x=50, y=80)
        
        self.TextRa = Text(self, fg='black', bg='white')
        self.TextRa.place(x=50, y=120, width= 300, height = 400)


    def Shuffle_Deck(self):
        import random #Importing Random, because you cannot "Randomise" without it, it would be shuffled but not randomised otherwise
        Type = ['Heart', 'Diamond', 'Club', 'Spade']
        Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        deck = [(Type, Rank) for Type in Type 
                for Rank in Ranks] #(Portfolio Courses, 2023)

        seed = random.randint(1, 1000)
        random.seed(seed)

        for i in range(len(deck)):
            j = random.randint(0, len(deck) - 1)
            deck[i], deck[j] = deck[j], deck[i]

        self.TextRa.config(state=NORMAL)
        self.TextRa.delete(1.0, END)
        self.TextRa.insert(END, f"The shuffled deck is Deck is:\n\n")
        for Type, Rank in deck:
            self.TextRa.insert(END, f"{Rank} of {Type}\n")
        self.TextRa.config(state=DISABLED)

class RecursionWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

        self.RecursionText = Entry(self, width = 35)
        self.RecursionText.place(x=50, y=50)
        self.RecursionLabel = Label(self, text="Enter an integer:", fg='white', bg='#1F1F1F')
        self.RecursionLabel.place(x=50, y=30)
        self.LabelResult = Label(self, text="", fg='white', bg='#1F1F1F')
        self.LabelResult.place(x=50, y=180)
        
        FactorialButton = Button(self, text="Generate Factorial", command=self.run_factorial)
        FactorialButton.place(x=50, y=150)

    def run_factorial(self):
        number = int(self.RecursionText.get())
        def factorial(number):
            return 1 if number <= 1 else number * factorial(number-1)
        self.LabelResult.config(text=f"The factorial of {number} is {factorial(number)}")
        




class SearchWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

        self.Search = Entry(self, width = 35)
        self.Search.place(x=50, y=50)
        self.SearchLabel = Label(self, text="Enter numbers seperated by whitespace:", fg='white', bg='#1F1F1F')
        self.SearchLabel.place(x=50, y=30)

        SearchButton = Button(self, text="Press for Statistics", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=self.run_search)
        SearchButton.place(x=150, y=80)

    def run_search(self):
        list_input = self.Search.get()
        my_list = list(map(int, list_input.split()))

        TextBox = Text(self, fg='black', bg='white', width=40, height=10)
        TextBox.place(x=50, y=120)
        TextBox.delete("1.0", "end")

        def selection_sort(my_list):
            for iter in range(0, len(my_list)-1):
                min = iter
                for i in range(iter + 1, len(my_list)):
                    if my_list[i] < my_list[min]:
                        min = i
                my_list[iter], my_list[min] = my_list[min], my_list[iter]
            return my_list
        
        sorted_list = selection_sort(my_list)

        def Statistical_Search(sorted_list):
            
            #Smallest & Largest
            smallest = sorted_list[0]
            largest = sorted_list[-1]
            #Median
            if len(sorted_list) % 2 == 1:
                median = sorted_list[len(sorted_list)//2]
            else:
                median = (sorted_list[len(sorted_list)//2 - 1] + sorted_list[len(sorted_list)//2]) / 2.
            
            #Inter Quartile
            n = len(sorted_list)
            LowerIQF = sorted_list[n // 4]
            UpperIQF = sorted_list[(3 * n) // 4]

            #Mode
            max_count = 0
            modes = []
            for item in sorted_list:
                count = sorted_list.count(item)
                if count > max_count:
                    max_count = count
                    modes = [item]
                elif count == max_count and item not in modes:
                    modes.append(item) #(GeeksforGeeks, 2018)

            TextBox.insert("1.0", f"Smallest Number: {smallest}\n")
            TextBox.insert("2.0", f"Largest Number: {largest}\n")
            TextBox.insert("3.0", f"Median: {median}\n")
            TextBox.insert("4.0", f"Lower Inter Quartile Factor: {LowerIQF}\n")
            TextBox.insert("5.0", f"Upper Inter Quartile Factor: {UpperIQF}\n")
            TextBox.insert("6.0", f"Mode(s): {modes[:]}\n")
            TextBox.configure(state=DISABLED)

        Statistical_Search(sorted_list)

        


class PalindromeWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

        self.Palindrome = Entry(self, width = 35)
        self.Palindrome.place(x=50, y=50)
        self.PalindromeLabel = Label(self, text="Enter a string:", fg='white', bg='#1F1F1F')
        self.PalindromeLabel.place(x=50, y=30)

        PalindromeButton = Button(self, text="Press for Palindrome Count", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=self.run_palindrome)
        PalindromeButton.place(x=150, y=80)

        self.LabelResult = Label(self, text="", fg='white', bg='#1F1F1F')
        self.LabelResult.place(x=50, y=150)

    def run_palindrome(self):
        InputString = self.Palindrome.get()
        
        def countPS(InputString):
            string_length = len(InputString)
            
            memo = [[-1 for i in range(string_length)] for i in range(string_length)]

            count = 0
            for i in range(string_length):
                for j in range(i + 1, string_length):
                    
                    if isPalindrome(i, j, InputString, memo) == True:
                        count += 1
            return count
        def isPalindrome(left_index, right_index, InputString, memo):                            
            if left_index == right_index:
                return True
            
            if right_index == left_index + 1 and InputString[left_index] == InputString[right_index]:
                return True
            
            if memo[left_index][right_index] != -1:
                return memo[left_index][right_index]
            
            if InputString[left_index] == InputString[right_index] and isPalindrome(left_index + 1, right_index - 1, InputString, memo) == True:
                memo[left_index][right_index] = True
            else:
                memo[left_index][right_index] = False
            
            return memo[left_index][right_index]
        
        self.LabelResult.config(text=f"Total palindromic substrings are: {countPS(InputString)}")

class BehaviouralWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

        BehaviouralButton = Button(self, text="Run Iterator Pattern", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=self.run_iterator_pattern)
        BehaviouralButton.place(x=50, y=80)

    def run_iterator_pattern(self):

        class Song:
            def __init__(self, title):
                self.title = title
                self.next_song = 0

        class Playlist:
            def __init__(self, first_song):
                self.first_song = first_song
                self.current_song = None
            
            def __iter__(self):
                self.current_song = self.first_song
                return self

            def __next__(self):
                if self.current_song:
                    title_to_return = self.current_song.title
                    self.current_song = self.current_song.next_song
                    return title_to_return
                else:
                    raise StopIteration
            
        song1 = Song("Bohemian Rhapsody")
        song2 = Song("Stairway to Heaven")
        song3 = Song("Hotel California")            
                    
        song1.next_song = song2
        song2.next_song = song3

        my_playlist = Playlist(song1)

        self.outputLabel = Label(self, text="", fg='white', bg='#1F1F1F')
        self.outputLabel.place(x=50, y=120)

        for song_title in my_playlist: #(NeetCode, 2023)
            self.outputLabel.config(text=f"Now playing: {song_title}", fg='white', bg='#1F1F1F')
            time.sleep(1)
            self.update()
        time.sleep(2)
        self.outputLabel.config(text="Playlist ended.") 



    





class StructuralWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)

        DropboxLabel = Label(self, text="Select a Song", fg='white', bg='#1F1F1F')
        DropboxLabel.place(x=50, y=30)

        self.OutputLabel = Label(self, text="", fg='white', bg='#1F1F1F')
        self.OutputLabel.place(x=50, y=120)

        selected_song = StringVar() 
        dropdown = ttk.Combobox(
            self, 
            textvariable=selected_song,
            values=["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
            state="readonly"
        )

        dropdown.place(x=50, y=50)
        dropdown.current(0)

        StructuralButton = Button(self, text="Play Song",fg='white', bg='purple', activebackground='purple', activeforeground='white', command=lambda: self.run_adapter_pattern(selected_song))
        StructuralButton.place(x=50, y=80)


    def run_adapter_pattern(self, selected_song):
        #This is harder to demonstrate than my other patterns.

        #Old System
        class SimpleMusicPlayer:
            def __init__(self, output_label):
                self.output_label = output_label

            def playSongByTitle(self, songTitle):
                self.output_label.config(text=f"Playing song: {songTitle}")

        #New System
        class AdvancedMusicPlayer:
            def __init__(self, output_label):
                self.output_label = output_label

            def playSongById(self, song_id):
                self.output_label.config(text=f"Playing song with ID: {song_id}")

        #Adapter
        class TitleToIdAdapter(SimpleMusicPlayer):
            def __init__(self, advancedPlayer, output_label):
                super().__init__(output_label)
                self.advancedPlayer = advancedPlayer
                self.master = master

                self.songLibrary = {
                    "Bohemian Rhapsody": 12455122,
                    "Stairway to Heaven": 99887766,
                    "Hotel California": 55443322
                }

            def playSongByTitle(self, songTitle):
                self.output_label.config(text=f"Adapter: Translating '{songTitle}' to ID...")
                self.master.update()
                time.sleep(1)

                song_id = self.songLibrary.get(songTitle)

                if song_id:
                    self.advancedPlayer.playSongById(song_id)
                else:
                    self.output_label.config(text=f"Error: '{songTitle}' not found in library.") #(NeetCode, 2023)

        master = self
        advanced_player = AdvancedMusicPlayer(self.OutputLabel)
        adapter = TitleToIdAdapter(advanced_player, self.OutputLabel)
        adapter.playSongByTitle(selected_song.get())








class CreationalWindow(Toplevel, BaseWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.WindowParameters(self)


        self.LabelCPU = Label(self, text="Enter CPU Model", fg='white', bg='#1F1F1F')
        self.LabelGPU = Label(self, text="Enter GPU Model", fg='white', bg='#1F1F1F')
        self.LabelMotherboard = Label(self, text="Enter Motherboard Model", fg='white', bg='#1F1F1F')
        self.LabelPSU = Label(self, text="Enter PSU Model", fg='white', bg='#1F1F1F')
        self.LabelStorage = Label(self, text="Enter Storage", fg='white', bg='#1F1F1F')
        self.LabelMemory = Label(self, text="Enter Memory", fg='white', bg='#1F1F1F')

        self.EntryCPU = Entry(self, width = 21)
        self.EntryGPU = Entry(self, width = 21)
        self.EntryMotherboard = Entry(self, width = 21)
        self.EntryPSU = Entry(self, width = 21)
        self.EntryStorage = Entry(self, width = 21)
        self.EntryMemory = Entry(self, width = 21)
        self.EntryCPU.place(x=50, y=50)
        self.EntryGPU.place(x=50, y=100)
        self.EntryMotherboard.place(x=50, y=150)
        self.EntryPSU.place(x=50, y=200)
        self.EntryStorage.place(x=50, y=250)
        self.EntryMemory.place(x=50, y=300)

        self.LabelCPU.place(x=50, y=30)
        self.LabelGPU.place(x=50, y=80)
        self.LabelMotherboard.place(x=50, y=130)
        self.LabelPSU.place(x=50, y=180)
        self.LabelStorage.place(x=50, y=230)
        self.LabelMemory.place(x=50, y=280)

        BuilderButton = Button(self, text="Build Computer", fg='white', bg='purple', activebackground='purple', activeforeground='white', command=self.run_builder_pattern)
        BuilderButton.place(x=50, y=350)

    def run_builder_pattern(self):
        CPUInput = self.EntryCPU.get()
        GPUInput = self.EntryGPU.get()
        MotherboardInput = self.EntryMotherboard.get()
        PSUInput = self.EntryPSU.get()
        StorageInput = self.EntryStorage.get()
        MemoryInput = self.EntryMemory.get()

        TextBox = Text(self, fg='black', bg='white', width=40, height=15)
        TextBox.place(x=200, y=50)
        TextBox.delete("1.0", "end")

        class Computer:
            def __init__(self):
                self.CPU = None
                self.GPU = None
                self.Motherboard = None
                self.PSU = None
                self.Storage = None
                self.Memory = None

            def setCPU(self, CPUStyle):
                self.CPU = CPUStyle

            def setGPU(self, GPUStyle):
                self.GPU = GPUStyle

            def setMotherboard(self, MotherboardStyle):
                self.Motherboard = MotherboardStyle

            def setPSU(self, PSUStyle):
                self.PSU = PSUStyle

            def setStorage(self, StorageStyle):
                self.Storage = StorageStyle

            def setMemory(self, MemoryStyle):
                self.Memory = MemoryStyle

        class ComputerBuilder:
            def __init__(self):
                self.computer = Computer()

            def setCPU(self, CPUStyle):
                self.computer.setCPU(CPUStyle)
                return self

            def setGPU(self, GPUStyle):
                self.computer.setGPU(GPUStyle)
                return self

            def setMotherboard(self, MotherboardStyle):
                self.computer.setMotherboard(MotherboardStyle)
                return self
            
            def setPSU(self, PSUStyle):
                self.computer.setPSU(PSUStyle)
                return self

            def setStorage(self, StorageStyle):
                self.computer.setStorage(StorageStyle)
                return self    

            def setMemory(self, MemoryStyle):
                self.computer.setMemory(MemoryStyle)
                return self
            
            def build(self):
                return self.computer
            
        computer = ComputerBuilder() \
                    .setCPU(CPUInput) \
                    .setGPU(GPUInput) \
                    .setMotherboard(MotherboardInput) \
                    .setPSU(PSUInput) \
                    .setStorage(StorageInput) \
                    .setMemory(MemoryInput) \
                    .build() #(NeetCode, 2023)
        TextBox.insert("1.0", f"\nComputer Specifications:\n{computer.CPU}\n{computer.GPU}\n{computer.Motherboard}\n{computer.PSU}\n{computer.Storage}\n{computer.Memory}\n")
        TextBox.configure(state=DISABLED)

app = MainWindow()
app.mainloop()