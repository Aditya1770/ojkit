import subprocess
from pathlib import Path


def compileCpp(folder, index):
    problem_folder = Path(folder)

    source = problem_folder / f"{index}.cpp"
    Exec = problem_folder / index

    result = subprocess.run(
        ["g++", str(source), "-std=c++17", "-O2", "-o", str(Exec)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return None, result.stderr

    return Exec, None


def runTests(folder, executable):
    problem_folder = Path(folder)
    test_folder = problem_folder / "tests"

    input_files = sorted(test_folder.glob("input*.txt"))

    for i, input_file in enumerate(input_files, start=1):
        output_file = test_folder / f"output{i}.txt"

        input_data = input_file.read_text()
        expected_output = output_file.read_text()

        result = subprocess.run(
            [str(executable)],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=2,
        )

        actual_output = result.stdout

        if actual_output.strip() == expected_output.strip():
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print(f"Expected: {expected_output.strip()}")
            print(f"Got: {actual_output.strip()}")

