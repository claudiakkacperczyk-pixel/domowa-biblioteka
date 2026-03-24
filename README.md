# Domowa Biblioteka

Aplikacja do zarzadzania domowa biblioteka. Pozwala przechowywaC informacje o ksiazkach, autorach oraz wypozyczeniach.

## Technologie

- Python 3
- Flask
- SQLAlchemy (flask-sqlalchemy)
- flask-migrate
- SQLite

---

## Jak pobrac i uruchomić lokalnie

### 1. Sklonuj repozytorium z GitHub
```bash
git clone https://github.com/claudiakkacperczyk-pixel/domowa-biblioteka.git
cd domowa-biblioteka
```

### 2. Utworz wirtualne srodowisko

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Zainstaluj zaleznosci
```bash
pip install -r requirements.txt
```

### 4. Zainicjuj baze danych
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 5. Uruchom aplikacje
```bash
flask run
```

### 6. Uruchom konsole Flask
```bash
flask shell
```

Masz dostep do: db, Author, Book, Loan

Przyklad uzycia:
```python
a = Author(first_name="Andrzej", last_name="Sapkowski")
db.session.add(a)
db.session.commit()
```

---

## Jak uruchomic w Google Colab

### 1. Otworz Google Colab

Wejdz na https://colab.research.google.com

### 2. Sklonuj repozytorium
```python
!git clone https://github.com/claudiakkacperczyk-pixel/domowa-biblioteka.git
```

### 3. Zainstaluj zaleznosci
```python
!pip install flask flask-sqlalchemy flask-migrate
```

### 4. Uruchom notatnik

Otworz plik domowa_biblioteka_colab.ipynb i uruchom komorki po kolei.

---

## Struktura projektu
```
domowa_biblioteka/
├── app/
│   ├── __init__.py      # Inicjalizacja Flask, db, migrate
│   ├── models.py        # Modele: Author, Book, Loan
│   └── routes.py        # Trasy aplikacji
├── .flaskenv            # Konfiguracja zmiennych Flask
├── biblioteka.py        # Punkt wejscia aplikacji
├── config.py            # Konfiguracja aplikacji
├── requirements.txt     # Zaleznosci projektu
└── README.md
```
