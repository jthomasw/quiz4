from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    book1.display_info()
    book2.display_info()

if __name__ == '__main__':
    main()