class Library:
	def __init__(self, listofbook, libraryname):
		self.list_of_book = listofbook
		self.name = libraryname
		self.lended_book_dict ={}
	def display_book(self):
		i = 1
		for books in self.list_of_book:
			print(f"{i}.{books}")
			i +=1	
	def lend_book(self):
		user_input = input("Enter book name which you want to borrow:")	
		if user_input not in self.lended_book_dict.keys():
			person_name = input("Enter Your Name:")
			self.lended_book_dict.setdefault(user_input,person_name)
			self.list_of_book.remove(user_input)
			print("Book database has been updated..you can take book now.")
		else:
			print(f"Book borrowed by person name :{self.lended_book_dict.get(user_input)}")
	def add_book(self):
		self.list_of_book.append(input("Enter Book name Which you want to Donate :"))
		print("Thank you for Donating the Book.")
	def return_book(self):
		return_book_name = input("Enter Book name which you borrowed :")
		self.lended_book_dict.pop(return_book_name)
		self.list_of_book.append(return_book_name)
		print("Thank you...Come again")

if __name__ == '__main__':
	object_name = input("Enter your library Owner Name :")
	mylibraryname = input("Enter your library name:")
	books_of_mylibrary = []
	n = int(input("How many book do you have in library :"))
	for i in range(n):
		books_of_mylibrary.append(input("Enter list of book :"))
	object_name = Library(books_of_mylibrary, mylibraryname)
	print(f"\n_______Welcome to \"{mylibraryname}\" Library______\n")
	while(True):
		print("What do you want to do?\n Press 1 For Display Book\n Press 2 For Lend Book \n Press 3 For Add Book\n Press 4 For Return Book")
		a = input()
		if a not in ['1','2','3','4']:
			print("Please Enter valid input")
			continue
		else:
			a = int(a)
		if a == 1:
			object_name.display_book()
		elif a == 2:
			object_name.lend_book()
		elif a ==3:
			object_name.add_book()
		else:
			object_name.return_book()
		b = input("Please Enter 'c' to continue or 'q' to quit : ")
		while(b != "c" and b != "q"):
			if b == "c":
				continue
			elif b == "q":
				exit()
			
		
	