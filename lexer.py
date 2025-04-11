class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return ('INTEGER', self.integer())

            if self.current_char.isalpha() or self.current_char == '_':
                if self.text.startswith('SQUARE', self.pos):
                    self.pos += 6
                    self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                    return ('SQUARE', 'SQUARE')
                return ('VARIABLE', self.identifier())

            if self.current_char == '+':
                self.advance()
                return ('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return ('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return ('MULTIPLY', '*')

            if self.current_char == '/':
                self.advance()
                return ('DIVIDE', '/')

            if self.current_char == '(':
                self.advance()
                return ('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return ('RPAREN', ')')

            if self.current_char == '=':
                self.advance()
                return ('EQUALS', '=')

            raise Exception(f'Invalid character: {self.current_char}')

        return ('EOF', None)