import unittest
from src.stack import Stack


class TestStackExpression(unittest.TestCase):
    allowed_operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
        '=': None
    }

    def calculate(self, expr):
        result = Stack()
        elements = self.expr_to_stack(expr)

        while elements.size() > 0:
            element = elements.pop()

            # If passed operator "=", then we return value from result buffer
            if element == '=':
                return result.pop()

            # If passed number, then add it to result buffer
            if isinstance(element, int):
                result.push(element)

            # If passed another operator, then calculate
            if element in self.allowed_operators: # If size >= 2
                y = result.pop()
                x = result.pop()
                value = self.allowed_operators[element](x, y)  # Pass params in reverted direction
                result.push(value)

        return result.pop()

    def expr_to_stack(self, expr):
        stack = Stack()

        buf = ''
        idx = len(expr) - 1
        while idx >= 0:
            char = expr[idx]
            idx -= 1

            # If 0-9 then add to buffer (for multi-digit numbers)
            if char.isdigit():
                buf = char + buf
                continue

            # Convert value from buffer to integer and move to stack
            if buf != '':
                stack.push(int(buf))
                buf = ''

            # Add operators to stack
            if not char.isdigit() and char in self.allowed_operators.keys():
                stack.push(char)

        # Finally flush buffer into stack
        if buf != '':
            stack.push(int(buf))

        return stack

    def test_expression_to_stack(self):
        expr_chunks = ['1259', '736', '+', '3', '*', '9', '/', '184', '-', '=']
        stack = self.expr_to_stack(' '.join(expr_chunks))

        self.assertEqual(len(expr_chunks), stack.size())
        for chunk in expr_chunks:
            self.assertEqual(chunk, str(stack.pop()))

    def test_calculation(self):
        cases = {
            '1 2 + 3 *': 9,
            '5 5 * =': 25,
            '8 2 + 5 * 9 + =': 59,
            '81 9 / 3 * 8 + 15 -': 20,
            '1259 736 + 3 * 9 / 184 - =': 481,
        }

        for expr in cases:
            self.assertEqual(cases[expr], self.calculate(expr))

    def test_calculation_zero_division(self):
        self.assertRaises(ZeroDivisionError, self.calculate, '123 0 / =')


if __name__ == '__main__':
    unittest.main()
