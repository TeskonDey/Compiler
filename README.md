# Interactive Equation Compiler

This is a simple interactive compiler for evaluating arithmetic equations and assignments. It includes a custom lexer, parser, and code generator, and it also supports evaluating the result of expressions.

## 🧠 Features

- Lexical analysis using a custom `Lexer`
- Parsing to generate an Abstract Syntax Tree (AST)
- Code generation with virtual instructions
- Variable assignment and reuse
- Evaluation of expressions and display of results
- Interactive REPL-style interface
- Built-in help and variable display

## 🚀 Getting Started

### Prerequisites

- Python 3.7+

### Folder Structure

```
your-project/
├── main.py
├── lexer.py
├── parser.py
├── code_generator.py
└── README.md
```

### Run the Program

```bash
python main.py
```

## 💻 Usage

Once running, you can enter commands like:

```plaintext
> x = 5
> y = x + 2 * 3
> vars
> y + 10
> help
> exit
```

### Supported Operators

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`

### Variable Rules

- Variable names must start with a letter and can contain letters and digits.
- You can assign values and use them in expressions.

## 🧪 Example Session

```
Welcome to the Interactive Equation Compiler!
==================================================
Enter an equation (or command): x = 10
Compiling: x = 10
Generated Instructions:
MOV R1, 10
MOV R2, R1 ; Store into variable x
Evaluated Result: 10

Enter an equation (or command): x * 2 + 5
Compiling: x * 2 + 5
Generated Instructions:
... [custom virtual instructions here]
Evaluated Result: 25
```

## 📚 Commands

- `help` – Show help message
- `vars` – List all current variables and values
- `exit` – Exit the compiler

## 📦 TODO / Future Improvements

- Add support for parentheses and operator precedence
- Add support for floating point numbers
- Export compiled instructions to file
- Improve error handling and messages

## 📝 License

This project is licensed under the MIT License.
