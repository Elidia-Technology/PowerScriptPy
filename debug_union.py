import traceback
from powerscript.compiler.lexer import Lexer
from powerscript.compiler.parser import Parser
from powerscript.compiler.transpiler import Transpiler

try:
    code = """
function test(value: string | number) {
    console.log("Value:", value);
}
"""
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    transpiler = Transpiler()
    python_ast = transpiler.transpile(ast)
    
    print("Success!")
    
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()