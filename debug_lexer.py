from powerscript.compiler.lexer import Lexer

# Test lexer with simple function
code = "function test() {}"
lexer = Lexer(code)
tokens = lexer.tokenize()

for token in tokens:
    print(f"{token.type}: '{token.value}' at {token.location}")