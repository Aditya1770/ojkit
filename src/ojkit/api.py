import requests
import json

from bs4 import BeautifulSoup


def getProblem(rating: int, api_key=None) -> list:

    url = "https://codeforces.com/api/problemset.problems"

    parameters = {}

    res = requests.get(url).json()

    problems = res["result"]["problems"]

    rated_problems = [problem for problem in problems if "rating" in problem]

    problems_b = [problem for problem in rated_problems if problem["rating"] == rating]

    return problems_b


def getTestCases(problem):
    contestId = problem["contestId"]
    index = problem["index"]

    url = f"https://codeforces.com/contest/{contestId}/problem/{index}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers, timeout=10)
    res.raise_for_status()

    if "Just a moment..." in res.text:
        print("Codeforces blocked the request with Cloudflare")
        return []

    htmlParse = BeautifulSoup(res.text, "html.parser")

    inputs = htmlParse.select(".sample-test .input pre")
    outputs = htmlParse.select(".sample-test .output pre")

    test_cases = []

    for inp, out in zip(inputs, outputs):
        test_cases.append({
            "input": inp.get_text("\n"),
            "output": out.get_text("\n")
        })

    return test_cases
