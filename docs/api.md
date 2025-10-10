# PowerScript API Documentation

**Complete API reference for PowerScript built-in functions, classes, and modules**

> **Version**: 2.0 | **Status**: Production Ready | **Updated**: October 2025

## Table of Contents

1. [Console API](#console-api)
2. [File System API](#file-system-api)
3. [String API](#string-api)
4. [Array API](#array-api)
5. [Object API](#object-api)
6. [Math API](#math-api)
7. [Date and Time API](#date-and-time-api)
8. [JSON API](#json-api)
9. [Regular Expressions API](#regular-expressions-api)
10. [HTTP Client API](#http-client-api)
11. [Async Utilities API](#async-utilities-api)
12. [Type Validation API](#type-validation-api)

## Console API

### `console` Object

The global console object provides methods for outputting information to the terminal or debugging interface.

#### Methods

##### `console.log(...args: any[]): void`
Outputs a message to the console with normal priority.

```powerscript
console.log("Hello, World!")
console.log("User:", user.name, "Age:", user.age)
console.log(f"Welcome {name}!")
```

##### `console.error(...args: any[]): void`
Outputs an error message to the console.

```powerscript
console.error("Something went wrong!")
console.error(f"Failed to load user {userId}")
```

##### `console.warn(...args: any[]): void`
Outputs a warning message to the console.

```powerscript
console.warn("Deprecated function usage")
console.warn(f"Low memory: {memoryUsage}MB remaining")
```

##### `console.info(...args: any[]): void`
Outputs an informational message to the console.

```powerscript
console.info("Application started successfully")
console.info(f"Processing {itemCount} items")
```

##### `console.debug(...args: any[]): void`
Outputs a debug message to the console (only visible when debug mode is enabled).

```powerscript
console.debug("Debug information:", debugData)
console.debug(f"Variable state: {JSON.stringify(state)}")
```

##### `console.dir(obj: any): void`
Displays an interactive list of the properties of the specified object.

```powerscript
const user = { name: "John", age: 30, preferences: { theme: "dark" } }
console.dir(user)
```

##### `console.table(data: any[]): void`
Displays tabular data as a table.

```powerscript
const users = [
    { name: "John", age: 30, role: "admin" },
    { name: "Jane", age: 25, role: "user" }
]
console.table(users)
```

##### `console.time(label?: string): void`
Starts a timer with the specified label.

```powerscript
console.time("data-processing")
// ... processing code ...
console.timeEnd("data-processing")
```

##### `console.timeEnd(label?: string): void`
Stops the timer with the specified label and outputs the elapsed time.

## File System API

### `File` Class

Represents a file in the file system with methods for reading, writing, and manipulation.

#### Constructor

```powerscript
const file = new File(path: string)
```

#### Properties

- `path: string` - The absolute path to the file
- `name: string` - The filename with extension
- `extension: string` - The file extension
- `size: number` - The file size in bytes
- `exists: boolean` - Whether the file exists

#### Methods

##### `read(): string`
Reads the entire file content as a string.

```powerscript
const file = new File("./data.txt")
const content = file.read()
console.log(content)
```

##### `readLines(): string[]`
Reads the file content as an array of lines.

```powerscript
const file = new File("./data.txt")
const lines = file.readLines()
for (const line of lines) {
    console.log(line)
}
```

##### `write(content: string): void`
Writes content to the file, overwriting existing content.

```powerscript
const file = new File("./output.txt")
file.write("Hello, World!")
```

##### `append(content: string): void`
Appends content to the end of the file.

```powerscript
const file = new File("./log.txt")
file.append(f"{new Date().toISOString()}: Application started\n")
```

##### `copy(destination: string): void`
Copies the file to the specified destination.

```powerscript
const source = new File("./data.txt")
source.copy("./backup/data.txt")
```

##### `move(destination: string): void`
Moves the file to the specified destination.

```powerscript
const file = new File("./temp.txt")
file.move("./archive/temp.txt")
```

##### `delete(): void`
Deletes the file from the file system.

```powerscript
const file = new File("./temp.txt")
file.delete()
```

### `Directory` Class

Represents a directory in the file system.

#### Constructor

```powerscript
const dir = new Directory(path: string)
```

#### Properties

- `path: string` - The absolute path to the directory
- `name: string` - The directory name
- `exists: boolean` - Whether the directory exists

#### Methods

##### `create(): void`
Creates the directory and any necessary parent directories.

```powerscript
const dir = new Directory("./data/temp")
dir.create()
```

##### `list(): string[]`
Returns an array of file and directory names in this directory.

```powerscript
const dir = new Directory("./src")
const items = dir.list()
console.log("Items:", items)
```

##### `listFiles(): File[]`
Returns an array of File objects for all files in this directory.

```powerscript
const dir = new Directory("./documents")
const files = dir.listFiles()
files.forEach(file => console.log(file.name, file.size))
```

##### `listDirectories(): Directory[]`
Returns an array of Directory objects for all subdirectories.

```powerscript
const dir = new Directory("./src")
const subdirs = dir.listDirectories()
subdirs.forEach(subdir => console.log(subdir.name))
```

##### `delete(): void`
Deletes the directory and all its contents.

```powerscript
const dir = new Directory("./temp")
dir.delete()
```

### File System Functions

#### `fileExists(path: string): boolean`
Checks if a file exists at the specified path.

```powerscript
if (fileExists("./config.json")) {
    const config = JSON.parse(new File("./config.json").read())
}
```

#### `directoryExists(path: string): boolean`
Checks if a directory exists at the specified path.

```powerscript
if (!directoryExists("./logs")) {
    new Directory("./logs").create()
}
```

#### `getAbsolutePath(path: string): string`
Returns the absolute path for the given relative path.

```powerscript
const absolutePath = getAbsolutePath("./data.txt")
console.log(absolutePath)
```

#### `joinPath(...parts: string[]): string`
Joins path components using the appropriate path separator.

```powerscript
const dataPath = joinPath(".", "data", "users.json")
const file = new File(dataPath)
```

## String API

### String Methods

These methods are available on all string values:

#### `length: number`
Returns the length of the string.

```powerscript
const text = "Hello, World!"
console.log(text.length)  // 13
```

#### `toUpperCase(): string`
Returns the string in uppercase.

```powerscript
const text = "hello"
console.log(text.toUpperCase())  // "HELLO"
```

#### `toLowerCase(): string`
Returns the string in lowercase.

```powerscript
const text = "HELLO"
console.log(text.toLowerCase())  // "hello"
```

#### `trim(): string`
Removes whitespace from both ends of the string.

```powerscript
const text = "  hello world  "
console.log(text.trim())  // "hello world"
```

#### `substring(start: number, end?: number): string`
Returns a substring from start to end (exclusive).

```powerscript
const text = "Hello, World!"
console.log(text.substring(0, 5))  // "Hello"
console.log(text.substring(7))     // "World!"
```

#### `split(separator: string): string[]`
Splits the string into an array using the separator.

```powerscript
const text = "apple,banana,orange"
const fruits = text.split(",")  // ["apple", "banana", "orange"]
```

#### `replace(search: string, replacement: string): string`
Replaces the first occurrence of search with replacement.

```powerscript
const text = "Hello, World!"
const newText = text.replace("World", "PowerScript")  // "Hello, PowerScript!"
```

#### `replaceAll(search: string, replacement: string): string`
Replaces all occurrences of search with replacement.

```powerscript
const text = "foo bar foo"
const newText = text.replaceAll("foo", "baz")  // "baz bar baz"
```

#### `startsWith(prefix: string): boolean`
Checks if the string starts with the given prefix.

```powerscript
const text = "Hello, World!"
console.log(text.startsWith("Hello"))  // true
```

#### `endsWith(suffix: string): boolean`
Checks if the string ends with the given suffix.

```powerscript
const text = "Hello, World!"
console.log(text.endsWith("World!"))  // true
```

#### `includes(substring: string): boolean`
Checks if the string contains the given substring.

```powerscript
const text = "Hello, World!"
console.log(text.includes("World"))  // true
```

#### `indexOf(substring: string): number`
Returns the index of the first occurrence of substring, or -1 if not found.

```powerscript
const text = "Hello, World!"
console.log(text.indexOf("World"))  // 7
console.log(text.indexOf("foo"))    // -1
```

#### `lastIndexOf(substring: string): number`
Returns the index of the last occurrence of substring, or -1 if not found.

```powerscript
const text = "Hello, World! Hello!"
console.log(text.lastIndexOf("Hello"))  // 14
```

### String Utilities

#### `padStart(targetLength: number, padString?: string): string`
Pads the string from the start to reach the target length.

```powerscript
const num = "5"
console.log(num.padStart(3, "0"))  // "005"
```

#### `padEnd(targetLength: number, padString?: string): string`
Pads the string from the end to reach the target length.

```powerscript
const text = "Hello"
console.log(text.padEnd(10, "!"))  // "Hello!!!!!"
```

#### `repeat(count: number): string`
Returns a string with the original string repeated count times.

```powerscript
const text = "Ha"
console.log(text.repeat(3))  // "HaHaHa"
```

## Array API

### Array Methods

#### `length: number`
Returns the number of elements in the array.

```powerscript
const numbers = [1, 2, 3, 4, 5]
console.log(numbers.length)  // 5
```

#### `push(...items: T[]): number`
Adds one or more elements to the end of the array and returns the new length.

```powerscript
const numbers = [1, 2, 3]
const newLength = numbers.push(4, 5)  // numbers = [1, 2, 3, 4, 5], newLength = 5
```

#### `pop(): T | undefined`
Removes and returns the last element of the array.

```powerscript
const numbers = [1, 2, 3]
const last = numbers.pop()  // last = 3, numbers = [1, 2]
```

#### `unshift(...items: T[]): number`
Adds one or more elements to the beginning of the array and returns the new length.

```powerscript
const numbers = [2, 3]
const newLength = numbers.unshift(1)  // numbers = [1, 2, 3], newLength = 3
```

#### `shift(): T | undefined`
Removes and returns the first element of the array.

```powerscript
const numbers = [1, 2, 3]
const first = numbers.shift()  // first = 1, numbers = [2, 3]
```

#### `slice(start?: number, end?: number): T[]`
Returns a shallow copy of a portion of the array.

```powerscript
const numbers = [1, 2, 3, 4, 5]
const slice1 = numbers.slice(1, 3)  // [2, 3]
const slice2 = numbers.slice(2)     // [3, 4, 5]
```

#### `splice(start: number, deleteCount?: number, ...items: T[]): T[]`
Changes the array by removing/replacing existing elements and/or adding new elements.

```powerscript
const numbers = [1, 2, 3, 4, 5]
const removed = numbers.splice(1, 2, 10, 20)  // removed = [2, 3], numbers = [1, 10, 20, 4, 5]
```

#### `concat(...arrays: T[][]): T[]`
Returns a new array with the elements of this array followed by the elements of the given arrays.

```powerscript
const arr1 = [1, 2]
const arr2 = [3, 4]
const combined = arr1.concat(arr2)  // [1, 2, 3, 4]
```

#### `join(separator?: string): string`
Joins all elements into a string using the separator.

```powerscript
const fruits = ["apple", "banana", "orange"]
const text = fruits.join(", ")  // "apple, banana, orange"
```

#### `reverse(): T[]`
Reverses the array in place and returns it.

```powerscript
const numbers = [1, 2, 3]
numbers.reverse()  // numbers = [3, 2, 1]
```

#### `sort(compareFn?: (a: T, b: T) => number): T[]`
Sorts the array in place and returns it.

```powerscript
const numbers = [3, 1, 4, 1, 5]
numbers.sort()  // numbers = [1, 1, 3, 4, 5]

// Custom sorting
const people = [{name: "John", age: 30}, {name: "Jane", age: 25}]
people.sort((a, b) => a.age - b.age)  // Sort by age
```

### Array Iteration Methods

#### `forEach(callback: (item: T, index: number, array: T[]) => void): void`
Executes a function for each array element.

```powerscript
const numbers = [1, 2, 3]
numbers.forEach((num, index) => {
    console.log(f"Item {index}: {num}")
})
```

#### `map<U>(callback: (item: T, index: number, array: T[]) => U): U[]`
Creates a new array with the results of calling a function for every array element.

```powerscript
const numbers = [1, 2, 3]
const doubled = numbers.map(num => num * 2)  // [2, 4, 6]
```

#### `filter(callback: (item: T, index: number, array: T[]) => boolean): T[]`
Creates a new array with all elements that pass the test.

```powerscript
const numbers = [1, 2, 3, 4, 5]
const evens = numbers.filter(num => num % 2 === 0)  // [2, 4]
```

#### `reduce<U>(callback: (accumulator: U, item: T, index: number, array: T[]) => U, initialValue: U): U`
Executes a reducer function on each element, resulting in a single output value.

```powerscript
const numbers = [1, 2, 3, 4, 5]
const sum = numbers.reduce((acc, num) => acc + num, 0)  // 15
```

#### `find(callback: (item: T, index: number, array: T[]) => boolean): T | undefined`
Returns the first element that satisfies the testing function.

```powerscript
const numbers = [1, 2, 3, 4, 5]
const found = numbers.find(num => num > 3)  // 4
```

#### `findIndex(callback: (item: T, index: number, array: T[]) => boolean): number`
Returns the index of the first element that satisfies the testing function.

```powerscript
const numbers = [1, 2, 3, 4, 5]
const index = numbers.findIndex(num => num > 3)  // 3
```

#### `includes(searchElement: T): boolean`
Determines whether the array includes the search element.

```powerscript
const numbers = [1, 2, 3]
console.log(numbers.includes(2))  // true
console.log(numbers.includes(4))  // false
```

#### `indexOf(searchElement: T): number`
Returns the first index at which the element can be found, or -1 if not present.

```powerscript
const numbers = [1, 2, 3, 2]
console.log(numbers.indexOf(2))  // 1
console.log(numbers.indexOf(4))  // -1
```

#### `lastIndexOf(searchElement: T): number`
Returns the last index at which the element can be found, or -1 if not present.

```powerscript
const numbers = [1, 2, 3, 2]
console.log(numbers.lastIndexOf(2))  // 3
```

#### `some(callback: (item: T, index: number, array: T[]) => boolean): boolean`
Tests whether at least one element passes the test.

```powerscript
const numbers = [1, 2, 3, 4, 5]
const hasEven = numbers.some(num => num % 2 === 0)  // true
```

#### `every(callback: (item: T, index: number, array: T[]) => boolean): boolean`
Tests whether all elements pass the test.

```powerscript
const numbers = [2, 4, 6]
const allEven = numbers.every(num => num % 2 === 0)  // true
```

## Object API

### Object Static Methods

#### `Object.keys(obj: object): string[]`
Returns an array of the object's property names.

```powerscript
const person = { name: "John", age: 30, city: "New York" }
const keys = Object.keys(person)  // ["name", "age", "city"]
```

#### `Object.values(obj: object): any[]`
Returns an array of the object's property values.

```powerscript
const person = { name: "John", age: 30, city: "New York" }
const values = Object.values(person)  // ["John", 30, "New York"]
```

#### `Object.entries(obj: object): [string, any][]`
Returns an array of key-value pairs.

```powerscript
const person = { name: "John", age: 30 }
const entries = Object.entries(person)  // [["name", "John"], ["age", 30]]
```

#### `Object.assign(target: object, ...sources: object[]): object`
Copies properties from source objects to target object.

```powerscript
const target = { a: 1 }
const source = { b: 2, c: 3 }
const result = Object.assign(target, source)  // { a: 1, b: 2, c: 3 }
```

#### `Object.freeze(obj: object): object`
Freezes an object, preventing modifications.

```powerscript
const person = { name: "John", age: 30 }
Object.freeze(person)
// person.age = 31  // This will have no effect
```

#### `Object.seal(obj: object): object`
Seals an object, preventing addition/deletion of properties but allowing modification.

```powerscript
const person = { name: "John", age: 30 }
Object.seal(person)
person.age = 31  // This works
// person.city = "NYC"  // This won't work
```

#### `Object.hasOwnProperty(obj: object, prop: string): boolean`
Checks if object has the specified property as its own.

```powerscript
const person = { name: "John" }
console.log(Object.hasOwnProperty(person, "name"))  // true
console.log(Object.hasOwnProperty(person, "age"))   // false
```

## Math API

### Math Constants

```powerscript
Math.PI     // 3.141592653589793
Math.E      // 2.718281828459045
Math.LN2    // 0.6931471805599453
Math.LN10   // 2.302585092994046
Math.LOG2E  // 1.4426950408889634
Math.LOG10E // 0.4342944819032518
Math.SQRT2  // 1.4142135623730951
Math.SQRT1_2 // 0.7071067811865476
```

### Math Methods

#### Basic Operations

```powerscript
Math.abs(x: number): number      // Absolute value
Math.ceil(x: number): number     // Round up to nearest integer
Math.floor(x: number): number    // Round down to nearest integer
Math.round(x: number): number    // Round to nearest integer
Math.trunc(x: number): number    // Remove fractional part
Math.sign(x: number): number     // Sign of number (-1, 0, 1)
```

#### Min/Max Operations

```powerscript
Math.max(...values: number[]): number    // Maximum value
Math.min(...values: number[]): number    // Minimum value
Math.clamp(value: number, min: number, max: number): number  // Clamp value between min and max
```

#### Power and Root Operations

```powerscript
Math.pow(base: number, exponent: number): number  // base^exponent
Math.sqrt(x: number): number    // Square root
Math.cbrt(x: number): number    // Cube root
Math.exp(x: number): number     // e^x
Math.log(x: number): number     // Natural logarithm
Math.log10(x: number): number   // Base-10 logarithm
Math.log2(x: number): number    // Base-2 logarithm
```

#### Trigonometric Functions

```powerscript
Math.sin(x: number): number     // Sine
Math.cos(x: number): number     // Cosine
Math.tan(x: number): number     // Tangent
Math.asin(x: number): number    // Arcsine
Math.acos(x: number): number    // Arccosine
Math.atan(x: number): number    // Arctangent
Math.atan2(y: number, x: number): number  // Arctangent of y/x
```

#### Hyperbolic Functions

```powerscript
Math.sinh(x: number): number    // Hyperbolic sine
Math.cosh(x: number): number    // Hyperbolic cosine
Math.tanh(x: number): number    // Hyperbolic tangent
Math.asinh(x: number): number   // Inverse hyperbolic sine
Math.acosh(x: number): number   // Inverse hyperbolic cosine
Math.atanh(x: number): number   // Inverse hyperbolic tangent
```

#### Random Number Generation

```powerscript
Math.random(): number           // Random number between 0 and 1
Math.randomInt(min: number, max: number): number  // Random integer between min and max
Math.randomFloat(min: number, max: number): number // Random float between min and max
```

## Date and Time API

### `Date` Class

#### Constructor

```powerscript
const now = new Date()                    // Current date and time
const specific = new Date(2023, 9, 15)    // October 15, 2023
const fromString = new Date("2023-10-15") // From ISO string
const fromTimestamp = new Date(1697356800000) // From timestamp
```

#### Instance Methods

##### Getting Date Components

```powerscript
const date = new Date()

date.getFullYear(): number      // 4-digit year
date.getMonth(): number         // Month (0-11)
date.getDate(): number          // Day of month (1-31)
date.getDay(): number           // Day of week (0-6, Sunday = 0)
date.getHours(): number         // Hours (0-23)
date.getMinutes(): number       // Minutes (0-59)
date.getSeconds(): number       // Seconds (0-59)
date.getMilliseconds(): number  // Milliseconds (0-999)
date.getTime(): number          // Timestamp in milliseconds
```

##### Setting Date Components

```powerscript
const date = new Date()

date.setFullYear(year: number, month?: number, date?: number): void
date.setMonth(month: number, date?: number): void
date.setDate(date: number): void
date.setHours(hours: number, min?: number, sec?: number, ms?: number): void
date.setMinutes(min: number, sec?: number, ms?: number): void
date.setSeconds(sec: number, ms?: number): void
date.setMilliseconds(ms: number): void
date.setTime(timestamp: number): void
```

##### Formatting Methods

```powerscript
const date = new Date()

date.toString(): string                 // Full date string
date.toDateString(): string            // Date portion only
date.toTimeString(): string            // Time portion only
date.toISOString(): string             // ISO 8601 format
date.toLocaleDateString(): string      // Localized date
date.toLocaleTimeString(): string      // Localized time
date.toLocaleString(): string          // Localized date and time
```

#### Static Methods

```powerscript
Date.now(): number                     // Current timestamp
Date.parse(dateString: string): number // Parse date string to timestamp
Date.UTC(year: number, month: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number): number
```

### Date Utilities

```powerscript
// Date arithmetic
function addDays(date: Date, days: number): Date {
    const result = new Date(date)
    result.setDate(result.getDate() + days)
    return result
}

function addMonths(date: Date, months: number): Date {
    const result = new Date(date)
    result.setMonth(result.getMonth() + months)
    return result
}

function addYears(date: Date, years: number): Date {
    const result = new Date(date)
    result.setFullYear(result.getFullYear() + years)
    return result
}

// Date comparison
function isSameDay(date1: Date, date2: Date): boolean {
    return date1.getFullYear() === date2.getFullYear() &&
           date1.getMonth() === date2.getMonth() &&
           date1.getDate() === date2.getDate()
}

function daysBetween(date1: Date, date2: Date): number {
    const msPerDay = 24 * 60 * 60 * 1000
    return Math.floor((date2.getTime() - date1.getTime()) / msPerDay)
}
```

## JSON API

### JSON Object

#### `JSON.stringify(value: any, replacer?: (key: string, value: any) => any, space?: number): string`
Converts a JavaScript value to a JSON string.

```powerscript
const data = { name: "John", age: 30, active: true }
const jsonString = JSON.stringify(data)  // '{"name":"John","age":30,"active":true}'

// With formatting
const formatted = JSON.stringify(data, null, 2)
// {
//   "name": "John",
//   "age": 30,
//   "active": true
// }

// With replacer function
const filtered = JSON.stringify(data, (key, value) => {
    return key === "age" ? undefined : value
})
```

#### `JSON.parse(text: string, reviver?: (key: string, value: any) => any): any`
Parses a JSON string and returns the corresponding value.

```powerscript
const jsonString = '{"name":"John","age":30,"active":true}'
const data = JSON.parse(jsonString)  // { name: "John", age: 30, active: true }

// With reviver function
const parsed = JSON.parse(jsonString, (key, value) => {
    return key === "age" ? value + 1 : value
})
```

### JSON File Operations

```powerscript
// Read JSON file
function readJsonFile(path: string): any {
    const file = new File(path)
    const content = file.read()
    return JSON.parse(content)
}

// Write JSON file
function writeJsonFile(path: string, data: any): void {
    const file = new File(path)
    const jsonString = JSON.stringify(data, null, 2)
    file.write(jsonString)
}

// Usage
const config = readJsonFile("./config.json")
config.lastModified = new Date().toISOString()
writeJsonFile("./config.json", config)
```

## Regular Expressions API

### `RegExp` Class

#### Constructor

```powerscript
const regex1 = new RegExp("pattern", "flags")
const regex2 = /pattern/flags
```

#### Common Flags

- `g` - Global search (find all matches)
- `i` - Case-insensitive search
- `m` - Multiline search
- `s` - Dot matches newlines
- `u` - Unicode mode
- `y` - Sticky search

#### Methods

##### `test(string: string): boolean`
Tests if the pattern matches the string.

```powerscript
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
console.log(emailRegex.test("user@example.com"))  // true
console.log(emailRegex.test("invalid-email"))     // false
```

##### `exec(string: string): RegExpMatchArray | null`
Executes the search and returns match information.

```powerscript
const regex = /(\d{4})-(\d{2})-(\d{2})/
const result = regex.exec("Date: 2023-10-15")
if (result) {
    console.log("Full match:", result[0])    // "2023-10-15"
    console.log("Year:", result[1])          // "2023"
    console.log("Month:", result[2])         // "10"
    console.log("Day:", result[3])           // "15"
}
```

### String Regex Methods

#### `match(regexp: RegExp): RegExpMatchArray | null`
Returns match information for the string.

```powerscript
const text = "The year is 2023"
const match = text.match(/\d{4}/)
console.log(match[0])  // "2023"
```

#### `matchAll(regexp: RegExp): IterableIterator<RegExpMatchArray>`
Returns an iterator of all matches.

```powerscript
const text = "Phone: 123-456-7890, Fax: 098-765-4321"
const phoneRegex = /(\d{3})-(\d{3})-(\d{4})/g
for (const match of text.matchAll(phoneRegex)) {
    console.log(f"Number: {match[0]}")
}
```

#### `search(regexp: RegExp): number`
Returns the index of the first match, or -1 if not found.

```powerscript
const text = "Hello World"
const index = text.search(/World/)  // 6
```

#### `replace(searchValue: string | RegExp, replaceValue: string | ((match: string, ...args: any[]) => string)): string`
Returns a new string with matches replaced.

```powerscript
const text = "Hello World"
const newText = text.replace(/World/, "PowerScript")  // "Hello PowerScript"

// With function
const formatted = text.replace(/(\w+)/g, (match) => match.toUpperCase())
```

### Common Regex Patterns

```powerscript
// Email validation
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

// Phone number (US format)
const phoneRegex = /^\(\d{3}\)\s\d{3}-\d{4}$/

// URL validation
const urlRegex = /^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/

// Date (YYYY-MM-DD)
const dateRegex = /^\d{4}-\d{2}-\d{2}$/

// Credit card number
const creditCardRegex = /^\d{4}\s\d{4}\s\d{4}\s\d{4}$/

// Password (at least 8 chars, 1 uppercase, 1 lowercase, 1 number)
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$/
```

## HTTP Client API

### `fetch` Function

#### Basic Usage

```powerscript
// GET request
const response = await fetch("https://api.example.com/users")
const data = await response.json()

// POST request
const response = await fetch("https://api.example.com/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: "John Doe",
        email: "john@example.com"
    })
})
```

#### Response Object

```powerscript
interface Response {
    ok: boolean                    // true if status 200-299
    status: number                 // HTTP status code
    statusText: string             // HTTP status text
    headers: Headers               // Response headers
    url: string                    // Final URL after redirects
    
    text(): Promise<string>        // Response as text
    json(): Promise<any>           // Response as JSON
    blob(): Promise<Blob>          // Response as binary data
    arrayBuffer(): Promise<ArrayBuffer>  // Response as array buffer
}
```

#### Request Options

```powerscript
interface RequestInit {
    method?: string                // HTTP method
    headers?: HeadersInit          // Request headers
    body?: string | FormData | Blob // Request body
    mode?: "cors" | "no-cors" | "same-origin"
    credentials?: "omit" | "same-origin" | "include"
    cache?: "default" | "no-store" | "reload" | "no-cache" | "force-cache"
    redirect?: "follow" | "error" | "manual"
    referrer?: string
    integrity?: string
    signal?: AbortSignal           // For request cancellation
}
```

### HTTP Client Examples

```powerscript
// GET with error handling
async function getUser(id: number): Promise<User | null> {
    try {
        const response = await fetch(f"https://api.example.com/users/{id}")
        
        if (!response.ok) {
            throw new Error(f"HTTP {response.status}: {response.statusText}")
        }
        
        return await response.json()
    } catch (error) {
        console.error("Failed to fetch user:", error)
        return null
    }
}

// POST with JSON data
async function createUser(userData: CreateUserRequest): Promise<User> {
    const response = await fetch("https://api.example.com/users", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {getAuthToken()}"
        },
        body: JSON.stringify(userData)
    })
    
    if (!response.ok) {
        const error = await response.json()
        throw new Error(error.message)
    }
    
    return await response.json()
}

// File upload
async function uploadFile(file: File): Promise<UploadResponse> {
    const formData = new FormData()
    formData.append("file", file)
    
    const response = await fetch("https://api.example.com/upload", {
        method: "POST",
        body: formData
    })
    
    return await response.json()
}

// Request with timeout
async function fetchWithTimeout(url: string, timeout: number = 5000): Promise<Response> {
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), timeout)
    
    try {
        const response = await fetch(url, {
            signal: controller.signal
        })
        clearTimeout(timeoutId)
        return response
    } catch (error) {
        clearTimeout(timeoutId)
        throw error
    }
}
```

## Async Utilities API

### Promise Utilities

#### `Promise.all(promises: Promise[]): Promise<any[]>`
Waits for all promises to resolve.

```powerscript
const promises = [
    fetch("/api/users"),
    fetch("/api/posts"),
    fetch("/api/comments")
]

const [users, posts, comments] = await Promise.all(promises)
```

#### `Promise.race(promises: Promise[]): Promise<any>`
Returns the result of the first promise to settle.

```powerscript
const timeout = new Promise((_, reject) => 
    setTimeout(() => reject(new Error("Timeout")), 5000)
)
const request = fetch("/api/data")

const result = await Promise.race([request, timeout])
```

#### `Promise.allSettled(promises: Promise[]): Promise<PromiseSettledResult[]>`
Waits for all promises to settle (resolve or reject).

```powerscript
const promises = [
    fetch("/api/users"),
    fetch("/api/posts"),
    Promise.reject(new Error("Failed"))
]

const results = await Promise.allSettled(promises)
results.forEach((result, index) => {
    if (result.status === "fulfilled") {
        console.log(f"Promise {index} succeeded:", result.value)
    } else {
        console.log(f"Promise {index} failed:", result.reason)
    }
})
```

### Async Control Flow

#### Delay Function

```powerscript
function delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms))
}

// Usage
await delay(1000)  // Wait 1 second
console.log("Delayed execution")
```

#### Retry Function

```powerscript
async function retry<T>(
    operation: () => Promise<T>,
    maxAttempts: number = 3,
    delayMs: number = 1000
): Promise<T> {
    let lastError: Error
    
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
        try {
            return await operation()
        } catch (error) {
            lastError = error
            if (attempt < maxAttempts) {
                console.log(f"Attempt {attempt} failed, retrying in {delayMs}ms...")
                await delay(delayMs)
            }
        }
    }
    
    throw lastError
}

// Usage
const data = await retry(
    () => fetch("/api/unreliable-endpoint").then(r => r.json()),
    3,
    2000
)
```

#### Throttle and Debounce

```powerscript
function throttle<T extends (...args: any[]) => any>(
    func: T,
    limit: number
): (...args: Parameters<T>) => void {
    let inThrottle: boolean
    return function(...args: Parameters<T>) {
        if (!inThrottle) {
            func.apply(this, args)
            inThrottle = true
            setTimeout(() => inThrottle = false, limit)
        }
    }
}

function debounce<T extends (...args: any[]) => any>(
    func: T,
    delay: number
): (...args: Parameters<T>) => void {
    let timeoutId: number
    return function(...args: Parameters<T>) {
        clearTimeout(timeoutId)
        timeoutId = setTimeout(() => func.apply(this, args), delay)
    }
}

// Usage
const throttledLog = throttle(console.log, 1000)
const debouncedSearch = debounce(performSearch, 300)
```

## Type Validation API

### Built-in Type Checking

```powerscript
// Type checking functions
function isString(value: any): value is string {
    return typeof value === "string"
}

function isNumber(value: any): value is number {
    return typeof value === "number" && !isNaN(value)
}

function isBoolean(value: any): value is boolean {
    return typeof value === "boolean"
}

function isArray(value: any): value is any[] {
    return Array.isArray(value)
}

function isObject(value: any): value is object {
    return value !== null && typeof value === "object" && !Array.isArray(value)
}

function isFunction(value: any): value is Function {
    return typeof value === "function"
}

function isDate(value: any): value is Date {
    return value instanceof Date && !isNaN(value.getTime())
}

function isRegExp(value: any): value is RegExp {
    return value instanceof RegExp
}
```

### Runtime Type Validation

```powerscript
// Schema validation
interface UserSchema {
    name: string
    age: number
    email: string
    active?: boolean
}

function validateUser(data: any): data is UserSchema {
    if (!isObject(data)) return false
    if (!isString(data.name) || data.name.trim().length === 0) return false
    if (!isNumber(data.age) || data.age < 0 || data.age > 150) return false
    if (!isString(data.email) || !data.email.includes("@")) return false
    if (data.active !== undefined && !isBoolean(data.active)) return false
    
    return true
}

// Type assertion with validation
function assertUser(data: any): UserSchema {
    if (!validateUser(data)) {
        throw new Error("Invalid user data")
    }
    return data
}

// Usage
try {
    const userData = JSON.parse(userJsonString)
    const user = assertUser(userData)
    console.log(f"Valid user: {user.name}")
} catch (error) {
    console.error("Invalid user data:", error.message)
}
```

### Custom Validators

```powerscript
// Email validator
function isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(email)
}

// Password strength validator
function isStrongPassword(password: string): boolean {
    const minLength = 8
    const hasUpperCase = /[A-Z]/.test(password)
    const hasLowerCase = /[a-z]/.test(password)
    const hasNumbers = /\d/.test(password)
    const hasSpecialChars = /[!@#$%^&*(),.?":{}|<>]/.test(password)
    
    return password.length >= minLength &&
           hasUpperCase &&
           hasLowerCase &&
           hasNumbers &&
           hasSpecialChars
}

// URL validator
function isValidUrl(url: string): boolean {
    try {
        new URL(url)
        return true
    } catch {
        return false
    }
}

// Credit card validator (Luhn algorithm)
function isValidCreditCard(cardNumber: string): boolean {
    const cleaned = cardNumber.replace(/\D/g, "")
    if (cleaned.length < 13 || cleaned.length > 19) return false
    
    let sum = 0
    let isEven = false
    
    for (let i = cleaned.length - 1; i >= 0; i--) {
        let digit = parseInt(cleaned[i])
        
        if (isEven) {
            digit *= 2
            if (digit > 9) digit -= 9
        }
        
        sum += digit
        isEven = !isEven
    }
    
    return sum % 10 === 0
}
```

---

## Error Handling

All API functions follow consistent error handling patterns:

1. **Synchronous functions** throw exceptions for errors
2. **Asynchronous functions** return rejected promises
3. **Type validation functions** return boolean results
4. **File operations** throw `FileError` for file system issues
5. **Network operations** throw `NetworkError` for connectivity issues

### Common Error Types

```powerscript
// File system errors
class FileError extends Error {
    constructor(message: string, public path: string) {
        super(message)
        this.name = "FileError"
    }
}

// Network errors
class NetworkError extends Error {
    constructor(message: string, public status?: number) {
        super(message)
        this.name = "NetworkError"
    }
}

// Validation errors
class ValidationError extends Error {
    constructor(message: string, public field?: string) {
        super(message)
        this.name = "ValidationError"
    }
}

// Type errors
class TypeError extends Error {
    constructor(message: string, public expectedType: string, public actualType: string) {
        super(message)
        this.name = "TypeError"
    }
}
```

---

This completes the PowerScript API Documentation. For more information, see:

- [Language Reference](language-reference.md)
- [CLI Guide](cli.md)
- [VS Code Extension](vscode.md)
- [Tutorial](../powerscript/docs/tutorial.md)

**PowerScript: Complete API reference for modern Python development! 🐍✨**