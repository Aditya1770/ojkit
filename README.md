# ojkit

A lightweight CLI toolkit for competitive programming on Codeforces.

ojkit lets you quickly find or import Codeforces problems, create a C++ workspace, fetch sample test cases, and run your solution against them — all from the terminal.

## Features

- Browse Codeforces problems by rating
- Fuzzy-search problems directly from the terminal
- Import problems directly from a Codeforces URL
- Supports problemset and contest problem URLs
- Automatically creates a C++ workspace
- Fetches sample test cases
- Compiles C++ solutions using `g++`
- Runs solutions against all sample tests
- Works on Linux

## Installation

```bash
pip install ojkit
```

Requires Python 3.10+.

A C++ compiler is required to use `ojkit run`.

## Usage

### Find a problem

Run:

```bash
ojkit
```

By default, ojkit shows problems rated 800.

To search for a specific rating:

```bash
ojkit -r 1200
```

Select a problem using the fuzzy finder and ojkit will create a workspace and download its sample tests.

### Import a problem from a URL

You can import a Codeforces problem directly:

```bash
ojkit https://codeforces.com/problemset/problem/2264/F
```

Contest URLs work too:

```bash
ojkit https://codeforces.com/contest/2264/problem/F
```

This is especially useful during contests — just copy the problem URL and pass it to ojkit.

## Workspace

Problems are created inside your Codeforces directory:

```text
~/codeforces/
└── 2264/
    └── F/
        ├── F.cpp
        └── tests/
            ├── input1.txt
            ├── output1.txt
            ├── input2.txt
            └── output2.txt
```

ojkit will not overwrite an existing solution file.

## Running Tests

Enter the problem directory:

```bash
cd ~/codeforces/2264/F
```

Then run:

```bash
ojkit run
```

ojkit will compile your C++ solution and run it against the downloaded sample tests.

Example:

```text
✓ Compiled successfully
Test 1: PASS
Test 2: PASS
```

If a test fails, ojkit displays the expected and actual output.

## Development

Clone the repository:

```bash
git clone https://github.com/Aditya1770/ojkit.git
cd ojkit
```

Install it in editable mode:

```bash
pip install -e .
```

Changes to the source code will then be reflected immediately when running:

```bash
ojkit
```

## Requirements

- Python 3.10+
- `g++`
- Internet connection for fetching Codeforces problems

## License

ojkit is licensed under the MIT License.
