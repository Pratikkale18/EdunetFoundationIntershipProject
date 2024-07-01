# app.py

from flask import Flask, render_template, request, jsonify
from library_record_manager import LibraryRecordManager

app = Flask(__name__)
library_manager = LibraryRecordManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    bot_response = process_message(user_message)
    return jsonify({'bot_response': bot_response})

def process_message(message):
    if message.lower() == 'exit':
        return 'Exiting Library Record Manager. Have a great day!'
    
    elif message.isdigit() and 1 <= int(message) <= 7:
        return handle_choice(message)

    elif message.startswith('add book'):
        return 'Please enter book details in the format: add book title, author, [isbn], [genre]'
    
    elif message.startswith('add book'):
        return 'Please enter book details in the format: add book title, author, [isbn], [genre]'
    
    elif message.startswith('add book '):
        params = message.split('add book ')[1].split(', ')
        if len(params) < 2 or len(params) > 4:
            return 'Invalid format. Please enter book details in the format: add book title, author, [isbn], [genre]'
        
        title = params[0].strip()
        author = params[1].strip()
        isbn = params[2].strip() if len(params) > 2 else None
        genre = params[3].strip() if len(params) > 3 else None

        success, response = library_manager.add_book(title, author, isbn, genre)
        return response

    elif message.startswith('search book'):
        search_query = message.split('search book ')[1].strip()
        results = library_manager.search_book(search_query)
        if results:
            response = f'Search results for "{search_query}":\n'
            for idx, book in enumerate(results, start=1):
                response += f"{idx}. '{book['title']}' by {book['author']}\n"
            return response
        else:
            return f'No books found matching "{search_query}".'

    elif message.startswith('borrow book '):
        isbn = message.split('borrow book ')[1].strip()
        success, response = library_manager.mark_borrowed(isbn)
        return response

    elif message.startswith('return book '):
        isbn = message.split('return book ')[1].strip()
        success, response = library_manager.mark_returned(isbn)
        return response

    elif message.startswith('delete book '):
        isbn = message.split('delete book ')[1].strip()
        success, response = library_manager.delete_book(isbn)
        return response

    elif message.lower() == 'list borrowed books':
        borrowed_books = library_manager.list_borrowed_books()
        if borrowed_books:
            response = 'Books currently borrowed:\n'
            for idx, book in enumerate(borrowed_books, start=1):
                response += f"{idx}. {book}\n"
            return response
        else:
            return 'No books are currently borrowed.'

    else:
        return 'Invalid command. Please enter a valid command or type "exit" to quit.'

def handle_choice(choice):
    # Implement handling for choices (1-7) if necessary
    pass

if __name__ == '__main__':
    app.run(debug=True)
