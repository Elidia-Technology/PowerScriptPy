# PowerScript Language Reference

**Complete language specification for PowerScript programming language**

> **Version**: 2.0 | **Status**: Production Ready | **Updated**: October 2025

## Table of Contents

1. [Overview](#overview)
2. [Syntax Fundamentals](#syntax-fundamentals)
3. [Data Types](#data-types)
4. [Variables and Constants](#variables-and-constants)
5. [Functions](#functions)
6. [Classes and Objects](#classes-and-objects)
7. [Control Flow](#control-flow)
8. [Modern Features](#modern-features)
9. [Error Handling](#error-handling)
10. [Modules and Imports](#modules-and-imports)
11. [Built-in Functions](#built-in-functions)
12. [Type System](#type-system)

## Overview

PowerScript is a modern programming language that transpiles to Python, combining Python's powerful ecosystem with contemporary language design patterns inspired by JavaScript, TypeScript, and other modern languages.

### Key Characteristics

- **Static Typing**: Optional type annotations with runtime validation
- **Modern Syntax**: ES6+ features like arrow functions, template literals, and destructuring
- **Python Compatibility**: Seamless integration with Python libraries and frameworks
- **Performance**: Direct Python AST generation for optimal execution speed
- **Safety**: Comprehensive error handling and type checking

## Syntax Fundamentals

### Comments

```powerscript
// Single-line comment

/*
Multi-line comment
supports multiple lines
*/

/**
 * Documentation comment
 * Used for API documentation
 */
```

### Identifiers

- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive
- Cannot be reserved keywords

```powerscript
// Valid identifiers
let userName = "john"
let _private = true
let API_VERSION = "2.0"
let user123 = {}

// Invalid identifiers
// let 123user = ""     // Cannot start with number
// let class = ""       // Reserved keyword
```

## Data Types

### Primitive Types

```powerscript
// String
let name: string = "PowerScript"
let message: string = 'Hello World'

// Number (integers and floats)
let count: number = 42
let price: number = 19.99
let scientific: number = 1.5e10

// Boolean
let isActive: boolean = true
let isComplete: boolean = false

// Null and undefined
let empty: null = null
let notSet: undefined = undefined
```

### Collection Types

```powerscript
// Arrays
let numbers: Array<number> = [1, 2, 3, 4, 5]
let names: string[] = ["Alice", "Bob", "Charlie"]
let mixed: any[] = [1, "hello", true, null]

// Objects (dictionaries)
let person: object = {
    name: "John Doe",
    age: 30,
    isEmployed: true
}

// Maps and Sets
let userMap: Map<string, number> = new Map()
let uniqueNumbers: Set<number> = new Set([1, 2, 3])
```

## Variables and Constants

### Variable Declarations

```powerscript
// Mutable variables
let counter = 0
let userName: string = "admin"
let isReady: boolean = false

// Constants (immutable)
const PI = 3.14159
const API_URL: string = "https://api.example.com"
const CONFIG: object = { debug: true, version: "1.0" }

// Type inference
let inferredString = "Hello"        // string
let inferredNumber = 42             // number
let inferredBoolean = true          // boolean
```

### Scope Rules

```powerscript
// Global scope
let globalVar = "accessible everywhere"

function example() {
    // Function scope
    let functionVar = "only in function"
    
    if (true) {
        // Block scope
        let blockVar = "only in block"
        console.log(globalVar)      // ✅ Accessible
        console.log(functionVar)    // ✅ Accessible
        console.log(blockVar)       // ✅ Accessible
    }
    
    // console.log(blockVar)        // ❌ Error: not accessible
}
```

## Functions

### Function Declarations

```powerscript
// Basic function
function greet(name: string): string {
    return f"Hello, {name}!"
}

// Function with default parameters
function createUser(name: string, age: number = 18, role: string = "user"): object {
    return {
        name: name,
        age: age,
        role: role,
        created: Date.now()
    }
}

// Function with optional parameters
function processData(data: Array<number>, options?: object): Array<number> {
    const multiplier = options?.multiplier || 1
    return data.map(x => x * multiplier)
}

// Function with rest parameters
function sum(first: number, ...rest: number[]): number {
    return rest.reduce((acc, num) => acc + num, first)
}
```

### Arrow Functions

```powerscript
// Single parameter, single expression
const double = x => x * 2

// Multiple parameters
const add = (a, b) => a + b

// With type annotations
const multiply = (a: number, b: number): number => a * b

// Multi-line arrow functions
const complexOperation = (numbers: number[]) => {
    const filtered = numbers.filter(x => x > 0)
    const doubled = filtered.map(x => x * 2)
    return doubled.reduce((acc, x) => acc + x, 0)
}

// Using with array methods
const numbers = [1, 2, 3, 4, 5]
const squared = numbers.map(x => x * x)
const evens = numbers.filter(x => x % 2 === 0)
```

### Function Overloading

```powerscript
// Multiple function signatures
function format(value: string): string
function format(value: number): string
function format(value: boolean): string
function format(value: any): string {
    if (typeof value === "string") {
        return `"${value}"`
    } else if (typeof value === "number") {
        return value.toString()
    } else if (typeof value === "boolean") {
        return value ? "true" : "false"
    }
    return String(value)
}
```

## Classes and Objects

### Class Definitions

```powerscript
// Basic class
class Person {
    // Properties with access modifiers
    private name: string
    protected age: number
    public email: string
    
    // Constructor
    constructor(name: string, age: number, email: string) {
        this.name = name
        this.age = age
        this.email = email
    }
    
    // Public method
    public introduce(): string {
        return f"Hi, I'm {this.name}, {this.age} years old"
    }
    
    // Private method
    private validateEmail(email: string): boolean {
        return email.includes("@")
    }
    
    // Protected method
    protected updateAge(newAge: number): void {
        if (newAge > 0) {
            this.age = newAge
        }
    }
    
    // Getter
    public get displayName(): string {
        return this.name.toUpperCase()
    }
    
    // Setter
    public set displayName(value: string) {
        this.name = value.toLowerCase()
    }
}

// Class inheritance
class Employee extends Person {
    private jobTitle: string
    private salary: number
    
    constructor(name: string, age: number, email: string, jobTitle: string, salary: number) {
        super(name, age, email)
        this.jobTitle = jobTitle
        this.salary = salary
    }
    
    public introduce(): string {
        return f"{super.introduce()}, I work as a {this.jobTitle}"
    }
    
    // Method overriding
    public getDetails(): string {
        return f"Employee: {this.displayName}, Title: {this.jobTitle}"
    }
}
```

### Interfaces and Abstract Classes

```powerscript
// Interface definition
interface Drawable {
    draw(): void
    getArea(): number
}

interface Movable {
    move(x: number, y: number): void
    getPosition(): {x: number, y: number}
}

// Abstract class
abstract class Shape implements Drawable {
    protected x: number
    protected y: number
    
    constructor(x: number, y: number) {
        this.x = x
        this.y = y
    }
    
    // Abstract method (must be implemented by subclasses)
    abstract getArea(): number
    
    // Concrete method
    public draw(): void {
        console.log(f"Drawing shape at ({this.x}, {this.y})")
    }
}

// Implementation
class Circle extends Shape {
    private radius: number
    
    constructor(x: number, y: number, radius: number) {
        super(x, y)
        this.radius = radius
    }
    
    public getArea(): number {
        return Math.PI * this.radius * this.radius
    }
}
```

## Control Flow

### Conditional Statements

```powerscript
// If-else statements
let score = 85

if (score >= 90) {
    console.log("Grade: A")
} else if (score >= 80) {
    console.log("Grade: B")
} else if (score >= 70) {
    console.log("Grade: C")
} else {
    console.log("Grade: F")
}

// Ternary operator
const status = score >= 60 ? "Pass" : "Fail"
const message = score >= 90 ? "Excellent!" : score >= 70 ? "Good job!" : "Keep trying!"
```

### Switch Statements

```powerscript
// Basic switch
function getDayName(dayNumber: number): string {
    switch (dayNumber) {
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6, 7:
            return "Weekend"
        default:
            return "Invalid day"
    }
}

// Switch with multiple cases
function getSeasonalActivity(month: string): string {
    switch (month.toLowerCase()) {
        case "december", "january", "february":
            return "Winter activities"
        case "march", "april", "may":
            return "Spring activities"
        case "june", "july", "august":
            return "Summer activities"
        case "september", "october", "november":
            return "Fall activities"
        default:
            return "Unknown season"
    }
}
```

### Loops

```powerscript
// For loops
for (let i = 0; i < 10; i++) {
    console.log(f"Iteration {i}")
}

// For-in loop (object properties)
const person = { name: "John", age: 30, city: "New York" }
for (let key in person) {
    console.log(f"{key}: {person[key]}")
}

// For-of loop (arrays)
const numbers = [1, 2, 3, 4, 5]
for (let num of numbers) {
    console.log(f"Number: {num}")
}

// While loop
let count = 0
while (count < 5) {
    console.log(f"Count: {count}")
    count++
}

// Do-while loop
let input: string
do {
    input = prompt("Enter 'quit' to exit:")
} while (input !== "quit")

// Break and continue
for (let i = 0; i < 10; i++) {
    if (i === 3) {
        continue  // Skip iteration
    }
    if (i === 7) {
        break     // Exit loop
    }
    console.log(i)
}
```

## Modern Features

### String Interpolation

```powerscript
// F-strings (Python-style)
const name = "PowerScript"
const version = "2.0"
const message = f"Welcome to {name} version {version}!"

// Complex expressions
const user = { name: "John", age: 30 }
const greeting = f"Hello {user.name}, you are {user.age} years old"
const calculation = f"Result: {2 + 3 * 4} = {2 + (3 * 4)}"
```

### Template Literals

```powerscript
// JavaScript-style template literals
const name = "PowerScript"
const multiLineTemplate = `
    Welcome to ${name}!
    
    This is a multi-line template
    with embedded expressions: ${2 + 3}
    
    Current date: ${new Date().toLocaleDateString()}
`

// Template functions
function html(strings, ...expressions) {
    let result = ""
    for (let i = 0; i < strings.length; i++) {
        result += strings[i]
        if (i < expressions.length) {
            result += String(expressions[i])
        }
    }
    return result
}

const title = "My Page"
const content = "Hello World"
const htmlTemplate = html`
    <html>
        <head><title>${title}</title></head>
        <body><h1>${content}</h1></body>
    </html>
`
```

### Destructuring

```powerscript
// Array destructuring
const numbers = [1, 2, 3, 4, 5]
const [first, second, ...rest] = numbers
// first = 1, second = 2, rest = [3, 4, 5]

// Object destructuring
const person = { name: "John", age: 30, city: "New York" }
const { name, age, city } = person

// Destructuring with renaming
const { name: fullName, age: currentAge } = person

// Destructuring with defaults
const { name, country = "USA" } = person

// Function parameter destructuring
function greetPerson({ name, age }: { name: string, age: number }): string {
    return f"Hello {name}, you are {age} years old"
}
```

### Spread Operator

```powerscript
// Array spread
const arr1 = [1, 2, 3]
const arr2 = [4, 5, 6]
const combined = [...arr1, ...arr2]  // [1, 2, 3, 4, 5, 6]

// Object spread
const baseConfig = { debug: true, version: "1.0" }
const devConfig = { ...baseConfig, environment: "development" }

// Function calls with spread
function sum(a: number, b: number, c: number): number {
    return a + b + c
}

const numbers = [1, 2, 3]
const result = sum(...numbers)
```

## Error Handling

### Try-Catch-Finally

```powerscript
// Basic error handling
try {
    const result = riskyOperation()
    console.log(f"Success: {result}")
} catch (error) {
    console.error(f"Error occurred: {error.message}")
} finally {
    console.log("Cleanup operations")
}

// Specific error types
try {
    const data = JSON.parse(jsonString)
} catch (error) {
    if (error instanceof SyntaxError) {
        console.error("Invalid JSON format")
    } else if (error instanceof TypeError) {
        console.error("Type error in parsing")
    } else {
        console.error(f"Unknown error: {error}")
    }
}

// Custom error throwing
function validateAge(age: number): void {
    if (age < 0) {
        throw new Error("Age cannot be negative")
    }
    if (age > 150) {
        throw new Error("Age seems unrealistic")
    }
}
```

### Custom Error Classes

```powerscript
// Custom error class
class ValidationError extends Error {
    public field: string
    
    constructor(message: string, field: string) {
        super(message)
        this.name = "ValidationError"
        this.field = field
    }
}

// Usage
function validateUser(user: any): void {
    if (!user.email) {
        throw new ValidationError("Email is required", "email")
    }
    if (!user.name) {
        throw new ValidationError("Name is required", "name")
    }
}

// Handling custom errors
try {
    validateUser({ name: "John" })  // Missing email
} catch (error) {
    if (error instanceof ValidationError) {
        console.error(f"Validation failed for {error.field}: {error.message}")
    }
}
```

## Modules and Imports

### Export Declarations

```powerscript
// Named exports
export const PI = 3.14159
export const E = 2.71828

export function calculateArea(radius: number): number {
    return PI * radius * radius
}

export class MathUtils {
    static square(x: number): number {
        return x * x
    }
    
    static cube(x: number): number {
        return x * x * x
    }
}

// Export list
const API_VERSION = "2.0"
const DEBUG_MODE = true

export { API_VERSION, DEBUG_MODE }

// Export with aliases
export { calculateArea as getCircleArea }

// Default export
export default class Calculator {
    add(a: number, b: number): number {
        return a + b
    }
    
    subtract(a: number, b: number): number {
        return a - b
    }
}
```

### Import Declarations

```powerscript
// Named imports
import { PI, calculateArea, MathUtils } from "./math-utils"

// Import with aliases
import { calculateArea as getArea } from "./math-utils"

// Import all as namespace
import * as MathLib from "./math-utils"

// Default import
import Calculator from "./calculator"

// Mixed imports
import Calculator, { PI, calculateArea } from "./math-utils"

// Import for side effects only
import "./polyfills"

// Dynamic imports (async)
async function loadModule() {
    const module = await import("./heavy-module")
    return module.processData()
}
```

## Built-in Functions

### Console Operations

```powerscript
// Logging
console.log("Information message")
console.error("Error message")
console.warn("Warning message")
console.info("Info message")
console.debug("Debug message")

// Formatted output
console.log(f"User {name} has {count} items")

// Object inspection
console.dir(complexObject)
console.table(arrayOfObjects)
```

### String Functions

```powerscript
// String manipulation
const text = "Hello World"
const length = text.length                    // 11
const upper = text.toUpperCase()              // "HELLO WORLD"
const lower = text.toLowerCase()              // "hello world"
const substring = text.substring(0, 5)        // "Hello"
const replaced = text.replace("World", "JS")  // "Hello JS"
const split = text.split(" ")                 // ["Hello", "World"]

// String checking
const startsWith = text.startsWith("Hello")   // true
const endsWith = text.endsWith("World")       // true
const includes = text.includes("llo")         // true
```

### Array Functions

```powerscript
const numbers = [1, 2, 3, 4, 5]

// Transformations
const doubled = numbers.map(x => x * 2)       // [2, 4, 6, 8, 10]
const evens = numbers.filter(x => x % 2 === 0) // [2, 4]
const sum = numbers.reduce((acc, x) => acc + x, 0) // 15

// Searching
const found = numbers.find(x => x > 3)        // 4
const index = numbers.findIndex(x => x > 3)   // 3
const includes = numbers.includes(3)          // true

// Modification
numbers.push(6)                               // [1, 2, 3, 4, 5, 6]
const last = numbers.pop()                    // 6
numbers.unshift(0)                            // [0, 1, 2, 3, 4, 5]
const first = numbers.shift()                 // 0
```

### Math Functions

```powerscript
// Basic operations
Math.abs(-5)        // 5
Math.max(1, 5, 3)   // 5
Math.min(1, 5, 3)   // 1
Math.round(4.7)     // 5
Math.floor(4.7)     // 4
Math.ceil(4.2)      // 5

// Power and roots
Math.pow(2, 3)      // 8
Math.sqrt(16)       // 4
Math.cbrt(27)       // 3

// Trigonometry
Math.sin(Math.PI / 2)    // 1
Math.cos(0)              // 1
Math.tan(Math.PI / 4)    // 1

// Random numbers
Math.random()            // 0.0 to 1.0
Math.floor(Math.random() * 10)  // 0 to 9
```

## Type System

### Basic Type Annotations

```powerscript
// Primitive types
let name: string = "John"
let age: number = 30
let isActive: boolean = true
let data: any = { key: "value" }

// Array types
let numbers: number[] = [1, 2, 3]
let names: Array<string> = ["Alice", "Bob"]
let mixed: (string | number)[] = ["hello", 42]

// Object types
let person: { name: string, age: number } = {
    name: "John",
    age: 30
}
```

### Union and Intersection Types

```powerscript
// Union types
type StringOrNumber = string | number
type Status = "loading" | "success" | "error"

function process(value: StringOrNumber): string {
    if (typeof value === "string") {
        return value.toUpperCase()
    } else {
        return value.toString()
    }
}

// Intersection types
type Person = { name: string, age: number }
type Employee = { jobTitle: string, salary: number }
type PersonWithJob = Person & Employee

const worker: PersonWithJob = {
    name: "John",
    age: 30,
    jobTitle: "Developer",
    salary: 75000
}
```

### Generic Types

```powerscript
// Generic functions
function identity<T>(value: T): T {
    return value
}

const stringResult = identity<string>("hello")
const numberResult = identity<number>(42)

// Generic classes
class Container<T> {
    private value: T
    
    constructor(value: T) {
        this.value = value
    }
    
    getValue(): T {
        return this.value
    }
    
    setValue(value: T): void {
        this.value = value
    }
}

const stringContainer = new Container<string>("hello")
const numberContainer = new Container<number>(42)

// Generic constraints
interface Lengthwise {
    length: number
}

function logLength<T extends Lengthwise>(arg: T): T {
    console.log(f"Length: {arg.length}")
    return arg
}
```

### Type Aliases and Interfaces

```powerscript
// Type aliases
type Point = { x: number, y: number }
type EventHandler = (event: Event) => void
type UserRole = "admin" | "user" | "guest"

// Interface definitions
interface User {
    id: number
    name: string
    email: string
    role: UserRole
    readonly createdAt: Date
    preferences?: UserPreferences
}

interface UserPreferences {
    theme: "light" | "dark"
    notifications: boolean
    language: string
}

// Interface extension
interface AdminUser extends User {
    permissions: string[]
    lastLogin: Date
}
```

### Utility Types

```powerscript
// Built-in utility types
type UserUpdate = Partial<User>          // All properties optional
type UserDisplay = Pick<User, "name" | "email">  // Only selected properties
type UserWithoutId = Omit<User, "id">    // Exclude specified properties
type UserKeys = keyof User               // Union of property names

// Custom utility types
type NonNullable<T> = T extends null | undefined ? never : T
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never
```

---

## Best Practices

### Code Organization

```powerscript
// Use consistent naming conventions
const API_BASE_URL = "https://api.example.com"  // Constants: UPPER_SNAKE_CASE
class UserService { }                           // Classes: PascalCase
function getUserData() { }                      // Functions: camelCase
let userCount = 10                             // Variables: camelCase

// Group related functionality
namespace MathUtils {
    export const PI = 3.14159
    export function calculateArea(radius: number): number {
        return PI * radius * radius
    }
}
```

### Error Handling

```powerscript
// Always handle potential errors
async function fetchUserData(id: number): Promise<User | null> {
    try {
        const response = await fetch(f"/api/users/{id}")
        if (!response.ok) {
            throw new Error(f"HTTP {response.status}: {response.statusText}")
        }
        return await response.json()
    } catch (error) {
        console.error(f"Failed to fetch user {id}:", error)
        return null
    }
}
```

### Type Safety

```powerscript
// Use type annotations for better code clarity
function processUser(user: User): UserDisplay {
    return {
        name: user.name,
        email: user.email
    }
}

// Prefer interfaces over any
interface ApiResponse<T> {
    data: T
    status: number
    message: string
}

async function apiCall<T>(url: string): Promise<ApiResponse<T>> {
    // Implementation
}
```

---

This completes the PowerScript Language Reference. For more information, see:

- [API Documentation](api.md)
- [CLI Guide](cli.md)
- [VS Code Extension](vscode.md)
- [Tutorial](../powerscript/docs/tutorial.md)

**PowerScript: Where Python meets modern language design! 🐍✨**