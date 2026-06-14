from dataclasses import dataclass
import ast
import re

from sympy import Matrix


@dataclass
class ParsedCommand:
    operation: str
    arguments: list
    raw_text: str


class CommandParser:
    def __init__(self) -> None:
        self.operation_aliases = {
            "det": "det",
            "wyznacznik": "det",

            "rank": "rank",
            "rzad": "rank",
            "rząd": "rank",

            "transpose": "transpose",
            "transpozycja": "transpose",

            "multiply": "multiply",
            "mnozenie": "multiply",
            "mnożenie": "multiply",

            "add": "add",
            "dodaj": "add",
            "dodawanie": "add",

            "subtract": "subtract",
            "odejmij": "subtract",
            "odejmowanie": "subtract",

            "scalar_multiply": "scalar_multiply",
            "mnozenie_przez_skalar": "scalar_multiply",
            "mnożenie_przez_skalar": "scalar_multiply",

            "power": "power",
            "potega": "power",
            "potęga": "power",

            "trace": "trace",
            "slad": "trace",
            "ślad": "trace",

            "inverse": "inverse",
            "odwrotna": "inverse",

            "eigenvalues": "eigenvalues",
            "wartosci_wlasne": "eigenvalues",
            "wartości_własne": "eigenvalues",

            "eigenvectors": "eigenvectors",
            "wektory_wlasne": "eigenvectors",
            "wektory_własne": "eigenvectors",

            "diagonalize": "diagonalize",
            "diagonalizacja": "diagonalize",

            "complex_eigenvalues": "complex_eigenvalues",
            "zespolone_wartosci_wlasne": "complex_eigenvalues",
            "zespolone_wartości_własne": "complex_eigenvalues",
        }
    
    def normalize_short_matrix_format(self, operation, arguments):
        """
        Obsługuje skrócony zapis macierzy dla operacji jednoargumentowych.

        Przykład:
        det([1, 2], [1, 6])

        zostanie potraktowane jak:
        det([[1, 2], [1, 6]])
        """

        one_matrix_operations = {
            "det",
            "rank",
            "transpose",
            "trace",
            "inverse",
            "eigenvalues",
            "eigenvectors",
            "diagonalize",
            "complex_eigenvalues"
        }

        if operation not in one_matrix_operations:
            return arguments

        if len(arguments) <= 1:
            return arguments

        rows = []

        for argument in arguments:
            if isinstance(argument, Matrix):
                if argument.rows == 1 or argument.cols == 1:
                    rows.append(list(argument))
                else:
                    return arguments

            elif isinstance(argument, (list, tuple)):
                if all(not isinstance(element, (list, tuple, Matrix)) for element in argument):
                    rows.append(list(argument))
                else:
                    return arguments

            else:
                return arguments

        row_lengths = [len(row) for row in rows]

        if len(set(row_lengths)) != 1:
            return arguments

        return [Matrix(rows)]
    


    def parse(self, command_text: str) -> ParsedCommand:
        command_text = command_text.strip()

        if not command_text:
            raise ValueError("Nie podano żadnej komendy.")

        operation_name, arguments_text = self._split_command(command_text)
        operation = self._normalize_operation(operation_name)

        raw_arguments = self._split_arguments(arguments_text)
        arguments = []

        for raw_argument in raw_arguments:
            parsed_argument = self._parse_argument(raw_argument)
            arguments.append(parsed_argument)

        arguments = self.normalize_short_matrix_format(operation, arguments)

        return ParsedCommand(
            operation=operation,
            arguments=arguments,
            raw_text=command_text,
        )

    def _split_command(self, command_text: str) -> tuple[str, str]:
        pattern = r"^([a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ_]+)\((.*)\)$"
        match = re.match(pattern, command_text)

        if not match:
            raise ValueError(
                "Niepoprawny format komendy. "
                "Użyj formatu: operacja(argumenty), np. det([[1,2],[3,4]])."
            )

        operation_name = match.group(1)
        arguments_text = match.group(2)

        return operation_name, arguments_text

    def _normalize_operation(self, operation_name: str) -> str:
        operation_name = operation_name.strip().lower()

        if operation_name not in self.operation_aliases:
            raise ValueError(f"Nieznana operacja: {operation_name}")

        return self.operation_aliases[operation_name]

    def _split_arguments(self, arguments_text: str) -> list[str]:
        arguments = []
        current_argument = []
        bracket_level = 0
        parenthesis_level = 0

        for character in arguments_text:
            if character == "[":
                bracket_level += 1
            elif character == "]":
                bracket_level -= 1
            elif character == "(":
                parenthesis_level += 1
            elif character == ")":
                parenthesis_level -= 1

            if (
                character == ","
                and bracket_level == 0
                and parenthesis_level == 0
            ):
                argument = "".join(current_argument).strip()
                if argument:
                    arguments.append(argument)
                current_argument = []
            else:
                current_argument.append(character)

        last_argument = "".join(current_argument).strip()

        if last_argument:
            arguments.append(last_argument)

        if not arguments:
            raise ValueError("Nie podano argumentów komendy.")

        return arguments

    def _parse_argument(self, argument_text: str):
        try:
            parsed_argument = ast.literal_eval(argument_text)
        except ValueError as error:
            raise ValueError(
                f"Nie można odczytać argumentu: {argument_text}"
            ) from error
        except SyntaxError as error:
            raise ValueError(
                f"Niepoprawna składnia argumentu: {argument_text}"
            ) from error

        if isinstance(parsed_argument, list):
            return Matrix(parsed_argument)

        if isinstance(parsed_argument, (int, float)):
            return parsed_argument

        raise ValueError(f"Nieobsługiwany typ argumentu: {argument_text}")