
class LibraryRecordManager:
    def __init__(self):
        self.library = {}

    def add_book(self, title, author, isbn=None, genre=None):
        self.library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'genre': genre,
            'borrowed': False
        }
        print(f'Book "{title}" by {author} added to the library.')

    def search_book(self, search_query):
        results = []
        for book in self.library.values():
            if search_query.lower() in book['title'].lower() or search_query.lower() in book['author'].lower() or search_query == book['isbn']:
                results.append(book)
        if results:
            print(f'Search results for "{search_query}":')
            for idx, book in enumerate(results, start=1):
                print(f"{idx}. '{book['title']}' by {book['author']}")
        else:
            print(f'No books found matching "{search_query}".')

    def mark_borrowed(self, isbn):
        if isbn in self.library:
            self.library[isbn]['borrowed'] = True
            print(f'Book "{self.library[isbn]["title"]}" marked as borrowed.')
        else:
            print(f'Book with ISBN {isbn} not found in the library.')

    def mark_returned(self, isbn):
        if isbn in self.library:
            if self.library[isbn]['borrowed']:
                self.library[isbn]['borrowed'] = False
                print(f'Book "{self.library[isbn]["title"]}" marked as returned.')
            else:
                print(f'Book "{self.library[isbn]["title"]}" is not currently borrowed.')
        else:
            print(f'Book with ISBN {isbn} not found in the library.')

    def delete_book(self, isbn):
        if isbn in self.library:
            del self.library[isbn]
            print(f'Book with ISBN {isbn} deleted from the library.')
        else:
            print(f'Book with ISBN {isbn} not found in the library.')

    def list_borrowed_books(self):
        borrowed_books = [book['title'] for book in self.library.values() if book['borrowed']]
        if borrowed_books:
            print('Books currently borrowed:')
            for book in borrowed_books:
                print(f'- {book}')
        else:
            print('No books are currently borrowed.')

    def start_chat(self):
        print('Welcome to Library Record Manager!')
        while True:
            print('\nWhat would you like to do?')
            print('1. Add a new book')
            print('2. Search for a book')
            print('3. Mark a book as borrowed')
            print('4. Mark a book as returned')
            print('5. List all borrowed books')
            print('6. Delete a book from the library')
            print('7. Exit')

            choice = input('Enter your choice (1-7): ')

            if choice == '1':
                title = input('Enter the title of the book: ')
                author = input('Enter the author of the book: ')
                isbn = input('Enter the ISBN of the book (optional): ')
                genre = input('Enter the genre of the book (optional): ')
                self.add_book(title, author, isbn, genre)

            elif choice == '2':
                search_query = input('Enter the title, author, or ISBN of the book: ')
                self.search_book(search_query)

            elif choice == '3':
                isbn = input('Enter the ISBN of the book to mark as borrowed: ')
                self.mark_borrowed(isbn)

            elif choice == '4':
                isbn = input('Enter the ISBN of the book to mark as returned: ')
                self.mark_returned(isbn)

            elif choice == '5':
                self.list_borrowed_books()

            elif choice == '6':
                isbn = input('Enter the ISBN of the book to delete: ')
                self.delete_book(isbn)

            elif choice == '7':
                print('Exiting Library Record Manager. Have a great day!')
                break

            else:
                print('Invalid choice. Please enter a number from 1 to 7.')

# Usage example
if __name__ == '__main__':
    library_manager = LibraryRecordManager()
    library_manager.start_chat()
