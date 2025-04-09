from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample list of books
books = [
    {"title": "Harry Potter", "available": True},
    {"title": "The Hobbit", "available": True},
    {"title": "1984", "available": True},
    {"title":"python","available":True}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def get_books():
    return jsonify(books)

@app.route('/borrow', methods=['POST'])
def borrow_book():
    title = request.json.get('title', '').strip().lower()
    for book in books:
        if book['title'].lower() == title and book['available']:
            book['available'] = False
            return jsonify({"message": "Book borrowed successfully"})
    return jsonify({"message": "Book not available"}), 400

@app.route('/return', methods=['POST'])
def return_book():
    title = request.json.get('title', '').strip().lower()
    for book in books:
        if book['title'].lower() == title and not book['available']:
            book['available'] = True
            return jsonify({"message": "Book returned successfully"})
    return jsonify({"message": "Book not found or already available"}), 400

if __name__ == '__main__':
    app.run(debug=True)
