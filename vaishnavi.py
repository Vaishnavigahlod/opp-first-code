#Create a class book

class Book:
      title=None
      author=None
      price=0
b=Book()
print("Enter book details:")
b.title=input("Enter title:")
b.author=input("Enter author:")
b.price=int(input("Enter price:"))
print("book details")
print(f"title :{b.title}")
print(f"author :{b.author}")
print(f"price :{b.price}")
