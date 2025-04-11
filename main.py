from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator

def print_help():
    print("\n=== Interactive Equation Compiler ===")
    print("Commands:")
    print("  <expression>   Evaluate expression (e.g., '2 + 3 * 4')")
    print("  x = <value>    Assign variable (e.g., 'x = 5')")
    print("  SQUARE <value> Square a number (e.g., 'SQUARE 3')")
    print("  vars           Show all variables")
    print("  help           Show this help")
    print("  exit           Quit the program")
    print("\nOperators: +, -, *, /, ^, ()")
    print("Example: 'SQUARE(2 + 3) * x'")

def show_variables(generator):
    if not generator.variables:
        print("No variables defined.")
        return
    print("\nVariables:")
    for var, reg in generator.variables.items():
        value = generator.var_values.get(var, "?")
        print(f"  {var} (in {reg}) = {value}")

def main():
    print("Welcome to the Equation Compiler with SQUARE support!")
    print_help()
    
    generator = CodeGenerator()
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'help':
                print_help()
                continue
            elif user_input.lower() == 'vars':
                show_variables(generator)
                continue
            elif not user_input:
                continue
            
            # Process input
            lexer = Lexer(user_input)
            parser = Parser(lexer)
            ast = parser.parse()
            
            # Generate and show code
            generator.generate(ast)
            print("\nGenerated Instructions:")
            print("-" * 40)
            for instruction in generator.get_instructions():
                print(instruction)
            
            # Show result (stored in '_' for expressions)
            if ast['type'] == 'ASSIGNMENT':
                var_name = ast['name']
                value = generator.var_values.get(var_name, "?")
                print(f"\nResult: {var_name} = {value}")
            else:
                value = generator.var_values.get('_', "?")
                print(f"\nResult: {value}")
                
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Type 'help' for usage examples.")

if __name__ == "__main__":
    main()