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
- [x] WSL environment with VSCode integration
- [x] Virtual environment with clang bindings (clang==16.0.6)
- [x] System clang/libclang-dev installation
- [x] README.md documentation with comprehensive project overview
- [x] Basic project files (.gitignore, requirements.txt)
- [x] **Placeholder main.py with CLI argument parsing**
- [x] **File validation logic (C/C++ extensions, file existence)**
- [x] **Basic project package structure (analyzer/ module)**
- [x] **Placeholder analyzer class with analyze_file method**
- [x] **Sample vulnerable.c test file with 3 different vulnerability types**

## 🔧 Core Implementation Tasks - NEXT STEPS

### 1. Rules Engine (`analyzer/rules.py`) - **START HERE**
- [ ] **Define Vulnerability class to represent found issues**
- [ ] **Create VulnerabilityRule base class structure**
- [ ] **Implement DangerousFunctionRule (gets, strcpy, sprintf, etc.)**
- [ ] **Add BufferOverflowRule detection patterns**
- [ ] **Create UseAfterFreeRule patterns**
- [ ] Add format string vulnerability rules
- [ ] Add rule severity levels (HIGH, MEDIUM, LOW)
- [ ] Implement rule metadata (description, remediation suggestions)

### 2. AST Parser & Analyzer (`analyzer/analyzer.py`) - **PHASE 2**
- [ ] **Replace placeholder with real libclang AST traversal setup**
- [ ] **Implement basic function call detection using clang.cindex**
- [ ] **Apply rules to detected function calls and patterns**
- [ ] **Create Vulnerability objects and return them from analyze_file**
- [ ] Add variable declaration and usage tracking
- [ ] Create buffer size analysis for arrays
- [ ] Implement pointer arithmetic vulnerability detection
- [ ] Add basic data flow tracking for tainted variables
- [ ] Handle multiple file analysis

### 3. Main CLI Interface (`main.py`) - **ENHANCE EXISTING**
- [x] Basic command-line argument parsing ✅
- [x] File/directory input validation ✅
- [x] Basic error handling for invalid files ✅
- [ ] **Improve vulnerability output formatting**
- [ ] Add output format options (JSON, detailed console)
- [ ] Add verbose/quiet mode options
- [ ] Add progress reporting for large codebases
- [ ] Handle directory scanning (not just single files)

### 4. Package Initialization (`analyzer/__init__.py`) - **SIMPLE TASK**
- [x] Empty file exists ✅
- [ ] Export main analyzer classes
- [ ] Define package version
- [ ] Set up logging configuration

## 🧪 Testing & Validation - **CONTINUOUS**

### 5. Test Cases (`test/vulnerable.c`)
- [x] **Basic vulnerable C code with 3 vulnerability types** ✅
  - [x] gets() dangerous function ✅
  - [x] strcpy() buffer overflow ✅  
  - [x] Use-after-free scenario ✅
- [ ] **Verify your analyzer detects these 3 existing vulnerabilities**
- [ ] Add more buffer overflow test cases
- [ ] Include format string vulnerability examples
- [ ] Add edge cases and false positive tests

### 6. Additional Test Files - **LATER**
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
