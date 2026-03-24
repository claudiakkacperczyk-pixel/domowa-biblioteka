from datetime import datetime
from app import db

# Tabela pomocnicza dla relacji wiele-do-wielu: ksiazka <-> autor
book_authors = db.Table(
    "book_authors",
    db.Column("book_id", db.Integer, db.ForeignKey("book.id")),
    db.Column("author_id", db.Integer, db.ForeignKey("author.id")),
)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    books = db.relationship("Book", secondary=book_authors, backref="authors")

    def __str__(self):
        return f"<Author {self.first_name} {self.last_name}>"

    def __repr__(self):
        return f"Author(id={self.id}, name={self.first_name} {self.last_name})"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(20), unique=True)
    year = db.Column(db.Integer)
    loans = db.relationship("Loan", backref="book", lazy="dynamic")

    @property
    def is_available(self):
        # Sprawdza czy ksiazka nie ma aktywnego wypozyczenia
        active_loan = self.loans.filter_by(returned=False).first()
        return active_loan is None

    def __str__(self):
        status = "dostepna" if self.is_available else "wypozyczona"
        return f"<Book '{self.title}' status={status}>"

    def __repr__(self):
        return self.__str__()


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    borrower_name = db.Column(db.String(200), nullable=False)
    loaned_at = db.Column(db.DateTime, default=datetime.utcnow)
    returned_at = db.Column(db.DateTime, nullable=True)
    returned = db.Column(db.Boolean, default=False)

    def __str__(self):
        status = "zwrocona" if self.returned else "wypozyczona"
        return f"<Loan book_id={self.book_id} borrower={self.borrower_name} status={status}>"

    def __repr__(self):
        return self.__str__()
