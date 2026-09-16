import argparse
from InquirerPy.prompts import fuzzy
from InquirerPy.base.control import Choice
from rich.console import Console

import api
import contest
import runner

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

def main():
    rating = 800

    with console.status("Getting problems..."):
        problems = api.getProblem(rating)

    problem = selectProblem(problems)

    with console.status("Fetching test cases..."):
        test_cases = api.getTestCases(problem)

    console.print(
            f"[green]✓[/green] Found {len(test_cases)} test cases"
        )

    with console.status("Creating problem..."):
        problem_folder = contest.createProblem(
                "~/codeforces/",
                problem
            )

        contest.createTestCases(
                problem_folder,
                test_cases
            )

    console.print(
            f"[green]✓[/green] Created {problem_folder}"
        )

if __name__ == "__main__":
    main()
