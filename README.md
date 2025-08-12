# vulnscan-cpp

# Static Analyzer for C/C++ Security Vulnerabilities

This tool statically analyzes C and C++ code to detect common security vulnerabilities such as buffer overflows, use-after-free, and unsafe function calls. It leverages Clang tooling to parse code into an Abstract Syntax Tree (AST) and applies rule-based detection and simple data flow tracking to flag insecure patterns.

---

## 🔍 Features

- Detects:
  - Buffer overflows
  - Use-after-free
  - Format string vulnerabilities
  - Dangerous function usage (e.g., `gets()`, `strcpy()`)
- AST traversal using Clang
- Basic data flow tracking for taint propagation
- CLI interface to scan `.c` or `.cpp` files
- Outputs results with vulnerability type, location, and remediation suggestions

---

## 🛠 Tech Stack

- Language: Python 3.x
- Parsing: Clang via `libclang` (Python bindings)
- Output: JSON or console printout (customizable)

---

## 📦 Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Ensure you have `libclang` installed and properly configured. On Ubuntu:

```bash
sudo apt install clang libclang-dev
```

3. Clone the repository and run the analyzer:

```bash
python3 main.py path/to/source.c
```

---

## 🧪 Example Usage

```bash
python3 main.py test/vulnerable.c
```

Sample output:
```
[WARNING] Use of unsafe function 'gets()' at line 12 in vulnerable.c
[WARNING] Potential buffer overflow at line 25 in vulnerable.c
```

---

## 📁 Project Structure

```
.
├── analyzer/
│   ├── __init__.py
│   ├── rules.py
│   └── analyzer.py
├── test/
│   └── vulnerable.c
├── main.py
├── README.md
└── requirements.txt
```

---

# Implementation Checklist for C/C++ Static Analyzer

## ✅ Completed
- [x] Project structure setup
- [x] Virtual environment with clang bindings
- [x] README.md documentation
- [x] Basic project files (.gitignore, requirements.txt)

## 🔧 Core Implementation Tasks

### 1. Rules Engine (`analyzer/rules.py`)
- [ ] Define vulnerability rule classes/data structures
- [ ] Implement buffer overflow detection rules
- [ ] Add use-after-free detection patterns
- [ ] Create format string vulnerability rules
- [ ] Define dangerous function blacklist (gets, strcpy, sprintf, etc.)
- [ ] Add rule severity levels (HIGH, MEDIUM, LOW)
- [ ] Implement rule metadata (description, remediation suggestions)

### 2. AST Parser & Analyzer (`analyzer/analyzer.py`)
- [ ] Set up libclang bindings and AST traversal
- [ ] Implement function call detection and analysis
- [ ] Add variable declaration and usage tracking
- [ ] Create buffer size analysis for arrays
- [ ] Implement pointer arithmetic vulnerability detection
- [ ] Add basic data flow tracking for tainted variables
- [ ] Create vulnerability reporting mechanism
- [ ] Handle multiple file analysis

### 3. Main CLI Interface (`main.py`)
- [ ] Implement command-line argument parsing
- [ ] Add file/directory input handling
- [ ] Create output formatting options (JSON, console, file)
- [ ] Add verbose/quiet mode options
- [ ] Implement error handling for invalid files
- [ ] Add progress reporting for large codebases

### 4. Package Initialization (`analyzer/__init__.py`)
- [ ] Export main analyzer classes
- [ ] Define package version
- [ ] Set up logging configuration

## 🧪 Testing & Validation

### 5. Test Cases (`test/vulnerable.c`)
- [ ] Create comprehensive vulnerable C code examples
- [ ] Add buffer overflow test cases
- [ ] Include use-after-free scenarios
- [ ] Add format string vulnerability examples
- [ ] Create dangerous function usage tests
- [ ] Add edge cases and false positive tests

### 6. Additional Test Files
- [ ] Create `test/safe.c` with secure coding examples
- [ ] Add `test/complex.c` with mixed vulnerable/safe patterns
- [ ] Include C++ specific test cases (`test/vulnerable.cpp`)

## 🚀 Advanced Features (Optional)

### 7. Enhanced Analysis
- [ ] Implement inter-procedural analysis
- [ ] Add control flow analysis
- [ ] Create more sophisticated data flow tracking
- [ ] Implement path-sensitive analysis
- [ ] Add support for custom rule definitions

### 8. Output & Reporting
- [ ] Create HTML report generation
- [ ] Add integration with popular IDEs
- [ ] Implement CI/CD pipeline integration
- [ ] Add baseline comparison features

## 📋 Implementation Priority Order

### Phase 1: Core Functionality
1. **Start with `analyzer/rules.py`**: Define basic rule structures
2. **Implement `analyzer/analyzer.py`**: Basic AST parsing and simple rules
3. **Create `main.py`**: Basic CLI to tie everything together
4. **Build `test/vulnerable.c`**: Simple test cases to validate

### Phase 2: Enhanced Detection
5. **Expand rules engine**: Add more sophisticated vulnerability patterns
6. **Improve analyzer**: Add data flow tracking
7. **Enhance testing**: Create comprehensive test suite

### Phase 3: Polish & Documentation
8. **Output formatting**: JSON/HTML reports
9. **Error handling**: Robust file processing
10. **Documentation**: Usage examples and API docs

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

Ivan Arredondo Mancilla  
*Security & Infrastructure Engineering Enthusiast*
