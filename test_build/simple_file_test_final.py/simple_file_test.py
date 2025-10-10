from powerscript.runtime.builtins import *
message = 'Hello from PowerScript file handling!'
file_write('test.txt', message)
content = file_read('test.txt')
console.log('File content:', content)
if file_exists('test.txt'):console.log('File exists successfully!')
else:console.log('File does not exist')
file_delete('test.txt')
console.log('Test completed successfully!')