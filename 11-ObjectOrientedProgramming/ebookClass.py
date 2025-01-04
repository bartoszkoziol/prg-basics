class Ebook:
    def __init__(self, title, author, num_of_pages):
        self.title=title
        self.author=author
        self.num_of_pages=num_of_pages
        self.current_page=0
        self.is_open=False
        

    def open_book(self):
        self.is_open=True
        self.current_page=1

    def close_book(self):
        self.is_open=False
        self.current_page=0

    def next_page(self):
        if self.is_open and self.current_page<self.num_of_pages:
            self.current_page+=1
        elif not self.is_open:
            print("The book is closed. Open it first")
        elif self.current_page == self.num_of_pages:
            print("You are already on the last page")

    def previous_page(self):
        if self.is_open and self.current_page>1:
            self.current_page-=1
        elif not self.is_open:
            print("The book is closed. Open it first")
        elif self.current_page==1:
            print("You are already on the first page")

    def display_status(self):
        if self.is_open:
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Pages: {self.num_of_pages}")
            print(f"Current page: {self.current_page}")
        else:
            print("The book is closed")

