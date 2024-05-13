from tqdm import tqdm

from core.schemas import schemas

from datetime import datetime
import csv
import os

post_list = [
    "Yes", "yeah", "Affirmative", "indeed", "I agree", "I do agree", "I must agree", "I totally agree",
    "I tent to agree with you", "couldn't agree more", "It is true", "It could be", "That's true",
    "so true", "they do", "they did", "they sure do", "That's why", "that's true", "That's how I see",
    "That's how I feel", "That's exactly how I feel", "That is my position", "That's exactly my position",
    "That's just what I was thinking", "That's spot on", "That's a good point", "that's just it",
    "Tell me about it", "You are right", "I think so", "I do think so", "I believe so", "I guess so",
    "I suppose so", "I know it", "I knew it", "i can confirm this", "I have to side with you",
    "I have come to the same conclusion", "I hold the same opinion", "I hold exactly the same view",
    "I have no objection", "I see it that way, too", "I share your opinion", "I share your view",
    "I was just going to say that", "You have a point", "You've made a good point.", "We are of one mind",
    "We are of the same mind", "Fair enough", "of course", "I'm with you", "I'll go along with that",
    "You've hit the nail on the head", "I approve of it", "I feel the same", "might be right",
    "Just so", "No doubt", "Quite so", "quite true", "without doubt"
]

post_list = [x.lower() for x in post_list]

neg_list = [
    'Not exactly', 'Not really', 'I disagree', 'I do not agree', 'I must disagree', 'I totally disagree',
    'doubt that i agree', 'not sure I agree', 'of course not', 'I do not think so', 'I do not believe so',
    "I don't think so", "I don't believe so", "I don't agree with you", "I don't think so", "I don't believe so"
]

neg_list = [x.lower() for x in neg_list]



def evaluate_yes_no(expected_result, generated_result):
    if 'yes' in generated_result.lower().strip() and 'no' in generated_result.lower().strip():
        return 'fail'
    if expected_result.lower().strip() in generated_result.lower():
        return 'pass'
    if expected_result.lower().strip() == 'yes' and any(x in generated_result.lower() for x in post_list):
        return 'pass'
    if expected_result.lower().strip() == 'no' and any(x in generated_result.lower() for x in neg_list):
        return 'pass'
    if expected_result.lower().strip() == 'yes' and any(x in generated_result.lower() for x in neg_list):
        return 'fail'
    if expected_result.lower().strip() == 'no' and any(x in generated_result.lower() for x in post_list):
        return 'fail'
    if expected_result.lower().strip() == 'yes' and 'no' in generated_result.lower().strip():
        return 'fail'
    if expected_result.lower().strip() == 'no' and 'yes' in generated_result.lower().strip():
        return 'fail'
    return 'pass'


