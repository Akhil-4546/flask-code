document.addEventListener("DOMContentLoaded", loadBooks);

function loadBooks() {
    fetch('/books')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("book-list");
            list.innerHTML = '';
            data.forEach(book => {
                const li = document.createElement("li");
                li.textContent = `${book.title} - ${book.available ? 'Available' : 'Borrowed'}`;
                list.appendChild(li);
            });
        });
}

function borrowBook() {
    const title = document.getElementById("borrow-book").value;
    fetch('/borrow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadBooks();
    });
}

function returnBook() {
    const title = document.getElementById("return-book").value;
    fetch('/return', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadBooks();
    });
}
