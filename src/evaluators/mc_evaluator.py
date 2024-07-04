import re


def evaluate_mc(prompt, expected_result, generated_result):
    options = _extract_options(prompt)
    # expected_result = _extract_options(expected_result)[0]
    options = [option for option in options if option != expected_result.lower()]

    if expected_result.lower().strip() in generated_result.lower() or generated_result.lower() in expected_result.lower():
        return 'pass'
    elif [option in generated_result.lower() for option in options].count(True) == 1:
        return 'fail'
    elif [option in generated_result.lower() for option in options].count(True) > 1:
        return 'pass'
    else:
        return 'pass'


def _extract_options(prompt):
    pattern = r'\bA\) (.*?) B\) (.*?) or C\) (.*?)\?'
    match = re.search(pattern, prompt)

    if match:
        option_a = match.group(1).strip()
        option_b = match.group(2).strip()
        option_c = match.group(3).strip()
        return [option_a.lower(), option_b.lower(), option_c.lower()]
    else:
        return []

