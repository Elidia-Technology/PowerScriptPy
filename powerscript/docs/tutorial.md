# PowerScript Tutorial: Building AI Applications

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript

# Install dependencies
pip install -r requirements.txt

# Install PowerScript CLI tools
pip install -e .
```

### Your First PowerScript Program

Create a file called `hello.ps`:

```powerscript
// hello.ps
function greet(name: string): void {
    console.log(`Hello, ${name}! Welcome to PowerScript.`);
}

greet("World");
```

Compile and run:

```bash
# Compile to Python
powerscriptc hello.ps -o build/

# Run the compiled Python
python build/hello.py

# Or run directly
ps-run hello.ps
```

## Tutorial 1: Basic Syntax and Types

### Variables and Types

```powerscript
// Variables
let message: string = "PowerScript is awesome!";
let count: number = 42;
let isActive: boolean = true;
let items: Array<string> = ["apple", "banana", "cherry"];

// Constants
const PI: number = 3.14159;
const APP_NAME: string = "MyApp";

// Optional types and null coalescing
let optional: string? = null;
let result: string = optional ?? "default value";

console.log(`Message: ${message}`);
console.log(`Count: ${count}`);
console.log(`Active: ${isActive}`);
console.log(`Items: ${items.join(", ")}`);
console.log(`Result: ${result}`);
```

### Functions

```powerscript
// Basic function
function add(a: number, b: number): number {
    return a + b;
}

// Arrow function
let multiply = (x: number, y: number): number => x * y;

// Function with optional parameters
function greet(name: string, title?: string): string {
    if (title) {
        return `Hello, ${title} ${name}!`;
    }
    return `Hello, ${name}!`;
}

// Usage
console.log(add(5, 3));
console.log(multiply(4, 6));
console.log(greet("Alice"));
console.log(greet("Bob", "Dr."));
```

## Tutorial 2: Object-Oriented Programming

### Classes and Inheritance

```powerscript
// Base class
class Animal {
    protected name: string;
    protected species: string;
    
    constructor(name: string, species: string) {
        this.name = name;
        this.species = species;
    }
    
    public speak(): void {
        console.log(`${this.name} makes a sound`);
    }
    
    public getInfo(): string {
        return `${this.name} is a ${this.species}`;
    }
}

// Derived class
class Dog extends Animal {
    private breed: string;
    
    constructor(name: string, breed: string) {
        super(name, "dog");
        this.breed = breed;
    }
    
    public speak(): void {
        console.log(`${this.name} barks: Woof! Woof!`);
    }
    
    public getBreed(): string {
        return this.breed;
    }
}

// Usage
let myDog = new Dog("Buddy", "Golden Retriever");
myDog.speak();
console.log(myDog.getInfo());
console.log(`Breed: ${myDog.getBreed()}`);
```

### Access Modifiers

```powerscript
class BankAccount {
    private balance: number;
    protected accountNumber: string;
    public ownerName: string;
    
    constructor(owner: string, accountNumber: string, initialBalance: number = 0) {
        this.ownerName = owner;
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }
    
    public deposit(amount: number): void {
        if (amount > 0) {
            this.balance += amount;
            console.log(`Deposited $${amount}. New balance: $${this.balance}`);
        }
    }
    
    public withdraw(amount: number): boolean {
        if (amount > 0 && amount <= this.balance) {
            this.balance -= amount;
            console.log(`Withdrew $${amount}. New balance: $${this.balance}`);
            return true;
        }
        console.log("Insufficient funds or invalid amount");
        return false;
    }
    
    public getBalance(): number {
        return this.balance;
    }
}

let account = new BankAccount("Alice Johnson", "ACC123", 1000);
account.deposit(500);
account.withdraw(200);
console.log(`Current balance: $${account.getBalance()}`);
```

## Tutorial 3: Async Programming

### Async Functions and Promises

```powerscript
// Simulate async operations
async function fetchUserData(userId: number): Promise<any> {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    return {
        id: userId,
        name: `User ${userId}`,
        email: `user${userId}@example.com`
    };
}

async function fetchUserPosts(userId: number): Promise<Array<any>> {
    await new Promise(resolve => setTimeout(resolve, 800));
    
    return [
        { id: 1, title: "First Post", content: "Hello World!" },
        { id: 2, title: "Second Post", content: "PowerScript is great!" }
    ];
}

// Sequential execution
async function getUserDataSequential(userId: number): Promise<void> {
    console.log("Fetching user data sequentially...");
    
    let user = await fetchUserData(userId);
    console.log("User:", user);
    
    let posts = await fetchUserPosts(userId);
    console.log("Posts:", posts);
}

// Parallel execution
async function getUserDataParallel(userId: number): Promise<void> {
    console.log("Fetching user data in parallel...");
    
    let [user, posts] = await Promise.all([
        fetchUserData(userId),
        fetchUserPosts(userId)
    ]);
    
    console.log("User:", user);
    console.log("Posts:", posts);
}

// Error handling
async function safeAsyncOperation(): Promise<void> {
    try {
        let result = await fetchUserData(1);
        console.log("Success:", result);
    } catch (error) {
        console.log("Error:", error);
    }
}
```

## Tutorial 4: Generics and Advanced Types

### Generic Functions and Classes

```powerscript
// Generic function
function identity<T>(arg: T): T {
    return arg;
}

function wrapInArray<T>(item: T): Array<T> {
    return [item];
}

// Generic class
class Box<T> {
    private contents: T;
    
    constructor(contents: T) {
        this.contents = contents;
    }
    
    public getContents(): T {
        return this.contents;
    }
    
    public setContents(contents: T): void {
        this.contents = contents;
    }
}

// Usage
let stringBox = new Box<string>("Hello");
let numberBox = new Box<number>(42);
let booleanBox = new Box<boolean>(true);

console.log(stringBox.getContents());
console.log(numberBox.getContents());
console.log(booleanBox.getContents());

// Generic utility class
class Pair<T, U> {
    constructor(public first: T, public second: U) {}
    
    public swap(): Pair<U, T> {
        return new Pair<U, T>(this.second, this.first);
    }
}

let pair = new Pair<string, number>("age", 25);
let swapped = pair.swap();
console.log(`Original: ${pair.first}, ${pair.second}`);
console.log(`Swapped: ${swapped.first}, ${swapped.second}`);
```

## Tutorial 5: AI and Machine Learning Integration

### Data Processing with NumPy and Pandas

```powerscript
// data_analysis.ps
import numpy as np;
import pandas as pd;

class DataAnalyzer {
    private data: pd.DataFrame;
    
    constructor(csvPath: string) {
        this.data = pd.read_csv(csvPath);
    }
    
    public summary(): void {
        console.log("Dataset Info:");
        console.log(`Shape: ${this.data.shape}`);
        console.log("Columns:", this.data.columns.tolist());
        console.log("\nBasic Statistics:");
        console.log(this.data.describe());
    }
    
    public cleanData(): void {
        // Remove missing values
        let initialRows = this.data.shape[0];
        this.data = this.data.dropna();
        let finalRows = this.data.shape[0];
        
        console.log(`Removed ${initialRows - finalRows} rows with missing values`);
    }
    
    public normalize(columns: Array<string>): void {
        for (let col of columns) {
            let mean = this.data[col].mean();
            let std = this.data[col].std();
            this.data[col] = (this.data[col] - mean) / std;
        }
        console.log(`Normalized columns: ${columns.join(", ")}`);
    }
    
    public correlationMatrix(): pd.DataFrame {
        return this.data.corr();
    }
}

// Machine Learning Model
class MLModel {
    private model: any;
    
    constructor() {
        // This would import sklearn in real implementation
        // from sklearn.ensemble import RandomForestClassifier;
        // this.model = new RandomForestClassifier();
    }
    
    public async train(X: pd.DataFrame, y: pd.Series): Promise<void> {
        console.log("Training model...");
        // Simulate training time
        await new Promise(resolve => setTimeout(resolve, 2000));
        console.log("Model training completed!");
    }
    
    public predict(X: pd.DataFrame): Array<number> {
        console.log("Making predictions...");
        // Simulate predictions
        return Array.from({length: X.shape[0]}, () => Math.random() > 0.5 ? 1 : 0);
    }
    
    public evaluate(y_true: Array<number>, y_pred: Array<number>): number {
        let correct = 0;
        for (let i = 0; i < y_true.length; i++) {
            if (y_true[i] === y_pred[i]) correct++;
        }
        return correct / y_true.length;
    }
}
```

### Async Training Pipeline

```powerscript
// training_pipeline.ps
class TrainingPipeline {
    private analyzer: DataAnalyzer;
    private model: MLModel;
    
    constructor(dataPath: string) {
        this.analyzer = new DataAnalyzer(dataPath);
        this.model = new MLModel();
    }
    
    public async run(): Promise<void> {
        console.log("Starting training pipeline...");
        
        // Step 1: Analyze data
        this.analyzer.summary();
        
        // Step 2: Clean and preprocess
        this.analyzer.cleanData();
        this.analyzer.normalize(["feature1", "feature2", "feature3"]);
        
        // Step 3: Show correlations
        let correlations = this.analyzer.correlationMatrix();
        console.log("\nCorrelation Matrix:");
        console.log(correlations);
        
        // Step 4: Train model (async)
        // In real implementation, you'd split the data
        // let [X_train, X_test, y_train, y_test] = this.splitData();
        // await this.model.train(X_train, y_train);
        
        console.log("\nPipeline completed successfully!");
    }
}

// Usage
async function main(): Promise<void> {
    let pipeline = new TrainingPipeline("data/dataset.csv");
    await pipeline.run();
}

main().catch(console.error);
```

## Tutorial 6: Working with Modules

### Creating and Using Modules

**math_utils.ps:**
```powerscript
// math_utils.ps
export class MathUtils {
    public static add(a: number, b: number): number {
        return a + b;
    }
    
    public static multiply(a: number, b: number): number {
        return a * b;
    }
    
    public static factorial(n: number): number {
        if (n <= 1) return 1;
        return n * MathUtils.factorial(n - 1);
    }
}

export function isPrime(n: number): boolean {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

export const PI = 3.14159265359;
export const E = 2.71828182846;
```

**main.ps:**
```powerscript
// main.ps
import { MathUtils, isPrime, PI } from "./math_utils";

function demo(): void {
    console.log(`5 + 3 = ${MathUtils.add(5, 3)}`);
    console.log(`4 * 7 = ${MathUtils.multiply(4, 7)}`);
    console.log(`5! = ${MathUtils.factorial(5)}`);
    console.log(`Is 17 prime? ${isPrime(17)}`);
    console.log(`PI = ${PI}`);
}

demo();
```

## Tutorial 7: Project Structure and Best Practices

### Recommended Project Structure

```
my_ai_project/
├── src/
│   ├── main.ps              # Entry point
│   ├── models/
│   │   ├── base_model.ps    # Base ML model class
│   │   └── neural_net.ps    # Neural network implementation
│   ├── data/
│   │   ├── processor.ps     # Data processing utilities
│   │   └── loader.ps        # Data loading utilities
│   ├── utils/
│   │   ├── math.ps          # Math utilities
│   │   └── helpers.ps       # Helper functions
│   └── types/
│       └── interfaces.ps    # Type definitions
├── tests/
│   ├── test_models.ps       # Model tests
│   └── test_utils.ps        # Utility tests
├── data/
│   ├── raw/                 # Raw datasets
│   └── processed/           # Processed datasets
├── build/                   # Compiled Python code
├── powerscript.toml         # Project configuration
└── requirements.txt         # Python dependencies
```

### Creating a New Project

```bash
# Create a new PowerScript project
ps-create my_ai_project

# Navigate to the project
cd my_ai_project

# Start development
code .  # Open in VS Code

# Compile and run
powerscriptc src/ -o build/
python build/main.py

# Or run directly
ps-run src/main.ps
```

## Next Steps

1. **Explore Examples**: Check out the `examples/` directory for more complex projects
2. **Read the Language Spec**: Dive deeper into PowerScript features
3. **Set up VS Code**: Install the PowerScript extension for full IDE support
4. **Build AI Projects**: Use PowerScript for your machine learning workflows
5. **Contribute**: Help improve PowerScript by contributing to the project

## Common Patterns

### Error Handling
```powerscript
async function safeOperation(): Promise<any> {
    try {
        let result = await riskyOperation();
        return result;
    } catch (error) {
        console.error("Operation failed:", error);
        return null;
    } finally {
        console.log("Cleanup completed");
    }
}
```

### Configuration Management
```powerscript
class Config {
    private static instance: Config;
    private settings: Map<string, any>;
    
    private constructor() {
        this.settings = new Map();
        this.loadDefaults();
    }
    
    public static getInstance(): Config {
        if (!Config.instance) {
            Config.instance = new Config();
        }
        return Config.instance;
    }
    
    private loadDefaults(): void {
        this.settings.set("debug", false);
        this.settings.set("timeout", 5000);
        this.settings.set("retries", 3);
    }
    
    public get(key: string): any {
        return this.settings.get(key);
    }
    
    public set(key: string, value: any): void {
        this.settings.set(key, value);
    }
}
```

This tutorial covers the essential features of PowerScript and shows how to build AI applications effectively. Continue exploring and building amazing projects!