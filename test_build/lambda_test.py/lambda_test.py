from powerscript.runtime.builtins import *
add_two = lambda x: x + 2
console.log('Lambda result:', add_two(5))
multiply = lambda a, b: a * b
console.log('Multiply result:', multiply(4, 6))
is_even = lambda n: n % 2 == 0
console.log('Is 4 even?', is_even(4))
console.log('Is 7 even?', is_even(7))
console.log('Lambda expressions test completed!')