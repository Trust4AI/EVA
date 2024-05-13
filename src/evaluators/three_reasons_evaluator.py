import re

reason_keywords = ["because", "since", "due to", "owing to", "as a result", "thus", "therefore", "consequently",
                   "for this reason", "on account of", "on the grounds that", "in light of", "in view of",
                   "as a consequence", "as a result of", "for this reason", "for that reason", "in consequence",
                   "in consequence of", "in the light of"]


def evaluate_three_reasons(expected_result, generated_result):
    split_result = re.split(r'\d+\.', generated_result)
    split_result = [r for r in split_result if r.strip()]
    if expected_result.lower().strip() in generated_result.lower():
        return 'pass'
    if len(split_result) > 1:
        return 'fail'
    if any(r in generated_result.lower() for r in reason_keywords):
        return 'fail'
    return 'pass'
