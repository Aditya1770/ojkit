from pathlib import Path

TEMPLATE = Path(__file__).parent / "templates" / "default.cpp"

def createProblem(folder, problem):
    folder = Path(folder).expanduser()
    folder.mkdir(parents=True, exist_ok=True)
    
    contestId = str(problem["contestId"])
    index = problem["index"]

    problem_folder = folder / contestId / index
    problem_folder.mkdir(parents=True, exist_ok=True)

    cpp_file = problem_folder / f"{index}.cpp"
    
    if not cpp_file.exists():
        template = TEMPLATE.read_text()
        cpp_file.write_text(template)

    return problem_folder
    

def createTestCases(folder, test_cases):
    test_folder = folder / "tests"
    test_folder.mkdir(parents=True, exist_ok=True)

    for i, test in enumerate(test_cases, start=1):
        input_file = test_folder / f"input{i}.txt"
        output_file = test_folder / f"output{i}.txt"

        input_file.write_text(test["input"])
        output_file.write_text(test["output"])
