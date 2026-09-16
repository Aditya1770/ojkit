## ojkit: Online Judge Kit

A lightweight command-line toolkit for competitive programming.

`ojkit` lets you browse Codeforces problems by rating, create a ready-to-use C++ workspace, fetch sample test cases, and run your solution against them.

> **Alpha:** ojkit is currently under active development. Features and CLI behavior may change.

## Features

- Browse Codeforces problems by rating
- Fuzzy-search problems from the terminal
- Automatically create a C++ source file
- Automatically fetch sample test cases
- Compile solutions using `g++`
- Run solutions against all sample tests
- Simple `ojkit run` workflow
- Cross-platform Python CLI

## Installation

ojkit requires Python 3.10 or newer.

```bash
pip install --pre ojkit
```

A C++ compiler (`g++`) is currently required for running solutions.

## Usage

### Find a problem

```bash
ojkit
```

By default, ojkit searches for 800-rated Codeforces problems.

Specify another rating with:

```bash
ojkit -r 1200
```

Select a problem using the fuzzy finder and ojkit will create a workspace such as:

```text
~/codeforces/4/A/
├── A.cpp
└── tests/
    ├── input1.txt
    ├── output1.txt
    ├── input2.txt
    └── output2.txt
```

### Run a solution

Enter the generated problem directory:

```bash
cd ~/codeforces/4/A
```

Then run:

```bash
ojkit run
```

ojkit will compile the C++ solution using `g++` and run it against the downloaded sample test cases.

Example:

```text
✓ Compiled successfully
Test 1: PASS
Test 2: PASS
```

## Development

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ojkit.git
cd ojkit
```

Install it in editable mode:

```bash
pip install -e .
```

Changes to the Python source will then be reflected immediately when running:

```bash
ojkit
```

## Status

ojkit is currently in **alpha**.

Current version:

```text
0.1.0a1
```

The initial releases focus on Codeforces and C++ support. More online judges, languages, configuration options, and runner improvements may be added later.

## License

MIT Online Judge Kit
