# Kalkulator-Macierzy

Aplikacja okienkowa służąca do wykonywania podstawowych i bardziej zaawansowanych operacji na macierzach. Program będzie umożliwiał m.in. mnożenie macierzy, wyznaczanie rzędu, obliczanie macierzy odwrotnej, transpozycji, wartości i wektorów własnych oraz diagonalizację.

Projekt tworzony jest w języku Python z wykorzystaniem bibliotek SymPy oraz PySide6.

Instrukcja dla systemu windows: 

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Instrukcja dla systemu Linux/MacOs:

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Aby uruchomic aplikacje, w głownym folderze projektu trzeba w terminalu wpisac:

python main.py

Testy można uruchomić z poziomu Visual Studio Code przez moduł testowania albo z terminala poleceniem:

python -m unittest discover -s tests -p "test_*.py" -v

UWAGA: program obługuje dwa formaty podawania macierzy

1: np det([1,2],[1,2])

2: det([[1,2],[1,2]])