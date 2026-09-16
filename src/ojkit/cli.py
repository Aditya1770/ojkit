import argparse
from InquirerPy.prompts import fuzzy
from InquirerPy.base.control import Choice
from rich.console import Console
from pathlib import Path

from ojkit import api
from ojkit import contest
from ojkit import runner

console = Console()


def selectProblem(problems):

    choices = []

    for problem in problems:
        choices.append(
            Choice(
                value=problem,
                name=(
                    f"{problem['rating']} {problem['contestId']}{problem['index']} - {problem['name']}"
                ),
            )
        )

    selected = fuzzy.FuzzyPrompt(
        message="Select a problem: ", choices=choices
    ).execute()

    return selected


def runProblem():
    folder = Path.cwd()

    cpp_files = list(folder.glob("*.cpp"))
    test_folder = folder / "tests"

    if len(cpp_files) != 1 or not test_folder.is_dir():
        console.print("[red]Error:[/red] Not an ojkit problem folder")
        return

    cpp_file = cpp_files[0]
    index = cpp_file.stem

    with console.status(f"Compiling {cpp_file.name}..."):
        executable, error = runner.compileCpp(folder, index)

    if error:
        console.print("[red]✗ Compilation failed[/red]")
        console.print(error)
        return

    console.print("[green]✓[/green] Compiled successfully")

    runner.runTests(folder, executable)

def runCli():
    parser = argparse.ArgumentParser(prog="ojkit", description="Online Judge Kit")
    
    parser.add_argument(
            "command",
            nargs="?",
            choices=["run"]
        )

    parser.add_argument(
            "-r",
            "--rating",
            type=int,
            default=800,
            help="Search problems by rating"
            )

    args = parser.parse_args()
    
    if args.command == "run":
        runProblem()
        return

    rating = args.rating

    with console.status("Getting problems..."):
        problems = api.getProblem(rating)

    problem = selectProblem(problems)

    with console.status("Fetching test cases..."):
        test_cases = api.getTestCases(problem)

    console.print(f"[green]✓[/green] Found {len(test_cases)} test cases")

    with console.status("Creating problem..."):
        problem_folder = contest.createProblem("~/codeforces/", problem)

        contest.createTestCases(problem_folder, test_cases)

    console.print(f"[green]✓[/green] Created {problem_folder}")


def main():
    try:
        runCli()
    except KeyboardInterrupt:
        console.print("\n[dim]Cancelled.[/dim]")


if __name__ == "__main__":
    main()
