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

## 📄 License

MIT License

---

## 🙋‍♂️ Author

Ivan Arredondo Mancilla  
*Security & Infrastructure Engineering Enthusiast*
