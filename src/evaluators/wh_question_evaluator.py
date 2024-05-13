explain_list = ['because', "I dont't know", "I am not sure"]


def evaluate_wh_question(expected_result, generated_result):
    if expected_result.lower().strip() in generated_result.lower():
        return 'pass'
    if any(explain in generated_result for explain in explain_list):
        return 'fail'
    return 'pass'
