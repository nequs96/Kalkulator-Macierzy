from core.parser import CommandParser, ParsedCommand
import core.basic_matrix_operations as basic_operations
import core.advanced_matrix_operations as advanced_operations


class CommandDispatcher:
    def __init__(self) -> None:
        self.expected_arguments_count = {
            "det": 1,
            "rank": 1,
            "transpose": 1,
            "trace": 1,
            "inverse": 1,
            "eigenvalues": 1,
            "eigenvectors": 1,
            "diagonalize": 1,
            "complex_eigenvalues": 1,

            "add": 2,
            "subtract": 2,
            "multiply": 2,
            "scalar_multiply": 2,
            "power": 2,
        }

    def dispatch(self, command: ParsedCommand):
        self._validate_arguments_count(command)

        operation = command.operation
        arguments = command.arguments

        if operation == "det":
            return basic_operations.matrix_determinant(arguments[0])

        if operation == "rank":
            return basic_operations.matrix_rank(arguments[0])

        if operation == "transpose":
            return basic_operations.transponent_matrix(arguments[0])

        if operation == "trace":
            return basic_operations.matrix_trace(arguments[0])

        if operation == "add":
            return basic_operations.matrix_addition(
                arguments[0],
                arguments[1],
            )

        if operation == "subtract":
            return basic_operations.matrix_subtraction(
                arguments[0],
                arguments[1],
            )

        if operation == "multiply":
            return basic_operations.matrix_by_matrix_multiplying(
                arguments[0],
                arguments[1],
            )

        if operation == "scalar_multiply":
            return self._dispatch_scalar_multiply(arguments)

        if operation == "power":
            return basic_operations.matrix_exponentiation(
                arguments[0],
                arguments[1],
            )

        if operation == "inverse":
            return advanced_operations.inverse_matrix(arguments[0])

        if operation == "eigenvalues":
            return advanced_operations.matrix_eigenvalues(arguments[0])

        if operation == "eigenvectors":
            return advanced_operations.matrix_eigenvectors(arguments[0])

        if operation == "diagonalize":
            return advanced_operations.diagonalize_matrix(arguments[0])

        if operation == "complex_eigenvalues":
            return advanced_operations.has_complex_eigenvalues(arguments[0])

        raise ValueError(f"Nieobsługiwana operacja: {operation}")

    def _validate_arguments_count(self, command: ParsedCommand) -> None:
        expected_count = self.expected_arguments_count.get(command.operation)

        if expected_count is None:
            raise ValueError(f"Nieobsługiwana operacja: {command.operation}")

        actual_count = len(command.arguments)

        if actual_count != expected_count:
            raise ValueError(
                f"Operacja '{command.operation}' wymaga "
                f"{expected_count} argumentów, otrzymano: {actual_count}."
            )

    def _dispatch_scalar_multiply(self, arguments: list):
        first_argument = arguments[0]
        second_argument = arguments[1]

        if self._is_matrix(first_argument):
            matrix = first_argument
            scalar = second_argument
        elif self._is_matrix(second_argument):
            matrix = second_argument
            scalar = first_argument
        else:
            raise ValueError(
                "Operacja mnożenia przez skalar wymaga jednej macierzy "
                "i jednej liczby."
            )

        return basic_operations.scalar_multiplying(matrix, scalar)

    def _is_matrix(self, value) -> bool:
        return hasattr(value, "rows") and hasattr(value, "cols")


def execute_command(command_text: str):
    parser = CommandParser()
    dispatcher = CommandDispatcher()

    parsed_command = parser.parse(command_text)

    return dispatcher.dispatch(parsed_command)