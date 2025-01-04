from ebookClass import Ebook

def main():
    book=Ebook("The Great Gatsy", "F. Scott", 180)

    book.open_book()#2
    book.display_status()#3

    book.next_page()#4
    book.next_page()

    book.display_status()#5

    book.close_book()#6

    book.next_page()#7

main()