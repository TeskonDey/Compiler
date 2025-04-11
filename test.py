from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator

def test_square():
    equation = "SQUARE 5"
    lexer = Lexer(equation)
    parser = Parser(lexer)
    ast = parser.parse()
    generator = CodeGenerator()
    generator.generate(ast)
    instructions = generator.get_instructions()
    print("Generated Instructions:")
    for instruction in instructions:
        print(instruction)
    print(f"Result: {generator.var_values.get('_', 'No result')}")

if __name__ == "__main__":
    test_square()