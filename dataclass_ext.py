from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    review: list

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

    def calculate_review(self):
        reviewTotal = sum(self.review)
        reviewAverage = reviewTotal / len(self.review)

        return reviewAverage

def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", review = [5,5,4,5])
    book2 = Book("To Kill a Mockingbird", "Harper Lee", review = [4,3,4,5])

    book1.display_info()
    print(f"Average review: {book1.calculate_review()} pages\n")

    book2.display_info()
    print(f"Average review: {book2.calculate_review()} pages")

if __name__ == '__main__':
    main()