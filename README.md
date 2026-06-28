# Kalkulator-Macierzy

Aplikacja okienkowa służąca do wykonywania podstawowych i bardziej zaawansowanych operacji na macierzach. Program będzie umożliwiał m.in. mnożenie macierzy, wyznaczanie rzędu, obliczanie macierzy odwrotnej, transpozycji, wartości i wektorów własnych oraz diagonalizację.

Projekt tworzony jest w języku Python z wykorzystaniem bibliotek SymPy oraz PySide6.

---

## 1. Cel projektu

Celem projektu jest stworzenie prostej aplikacji graficznej, która pozwala użytkownikowi wykonywać obliczenia na macierzach bez konieczności ręcznego wpisywania kodu w interpreterze Pythona.

Projekt został wybrany, ponieważ działania na macierzach często pojawiają się na zajęciach z algebry liniowej, matematyki, informatyki oraz w różnych zastosowaniach technicznych. Aplikacja ma ułatwiać szybkie sprawdzanie wyników podstawowych i bardziej zaawansowanych operacji macierzowych.

Program działa w trybie graficznym. Użytkownik wpisuje komendę w oknie aplikacji, a program analizuje polecenie, wykonuje odpowiednie obliczenie i wyświetla wynik.

---

## 2. Wykorzystane technologie i biblioteki

Projekt został napisany w języku Python.

W projekcie wykorzystano następujące biblioteki:

- `PySide6` — biblioteka użyta do stworzenia graficznego interfejsu użytkownika,
- `SymPy` — biblioteka użyta do obliczeń symbolicznych i działań na macierzach,
- `unittest` — moduł standardowy Pythona użyty do testów jednostkowych,
- `pytest` — biblioteka dostępna w środowisku projektu, pomocna przy uruchamianiu testów.

Lista wymaganych bibliotek znajduje się w pliku:

requirements.txt