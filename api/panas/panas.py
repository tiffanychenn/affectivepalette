import unittest

POSITIVE_EMOTIONS = ["interested", "alert", "attentive", "excited", "enthusiastic", "inspired", "proud", "strong", "determined", "active"]
NEGATIVE_EMOTIONS = ["upset", "jittery", "nervous", "distressed", "guilty", "ashamed", "hostile", "irritable", "scared", "afraid"]

def get_affective_state_from_panas(panas_scores):
    """
    Gets the affective state from PANAS-20. 

    Parameters:
    panas_scores(dict): Dictionary with the PANAS scores for each mood.

    Returns:
    (x, y), where x is the positive affective state from 0 to 1 and y is the negative affective state from 0 to 1

    Raises:
    ValueError: when any emotions are missing from panas_scores, or if a panas score is not an integer between 1 and 5
    """
    if type(panas_scores) != dict:
        raise ValueError("incorrect input: expected dict")

    if len(panas_scores.keys()) != 20:
        raise ValueError("incorrect input: length of given dict is not 20")
    
    for e in POSITIVE_EMOTIONS + NEGATIVE_EMOTIONS:
        if e not in panas_scores:
            raise ValueError("incorrect input: missing " + e)
        if type(panas_scores[e]) != int:
            raise ValueError("incorrect input: value for " + e + " not integer") 
        if panas_scores[e] < 1 or panas_scores[e] > 5:
            raise ValueError("incorrect input: value for " + e + " not between 1 and 5") 

    positive_score = sum([panas_scores[e] for e in panas_scores if e in POSITIVE_EMOTIONS])
    negative_score = sum([panas_scores[e] for e in panas_scores if e in NEGATIVE_EMOTIONS])

    return ((positive_score - 10) / 40, (negative_score - 10) / 40)


class TestPanas(unittest.TestCase):
    def test_min_negative_min_positive(self):
        panas_scores = {
            "interested": 1, 
            "alert": 1,
            "attentive": 1, 
            "excited": 1, 
            "enthusiastic": 1, 
            "inspired": 1, 
            "proud": 1, 
            "strong": 1, 
            "determined": 1, 
            "active": 1,
            "upset": 1,
            "jittery": 1,
            "nervous": 1, 
            "distressed": 1, 
            "guilty": 1, 
            "ashamed": 1, 
            "hostile": 1, 
            "irritable": 1, 
            "scared": 1, 
            "afraid": 1
        }
        positive_score, negative_score = get_affective_state_from_panas(panas_scores)
        self.assertEqual(positive_score, 0)
        self.assertEqual(negative_score, 0)

    def test_min_negative_max_positive(self):
        panas_scores = {
            "interested": 5, 
            "alert": 5,
            "attentive": 5, 
            "excited": 5, 
            "enthusiastic": 5, 
            "inspired": 5, 
            "proud": 5, 
            "strong": 5, 
            "determined": 5, 
            "active": 5,
            "upset": 1,
            "jittery": 1,
            "nervous": 1, 
            "distressed": 1, 
            "guilty": 1, 
            "ashamed": 1, 
            "hostile": 1, 
            "irritable": 1, 
            "scared": 1, 
            "afraid": 1
        }
        positive_score, negative_score = get_affective_state_from_panas(panas_scores)
        self.assertEqual(positive_score, 1)
        self.assertEqual(negative_score, 0)

    def test_max_negative_min_positive(self):
        panas_scores = {
            "interested": 1, 
            "alert": 1,
            "attentive": 1, 
            "excited": 1, 
            "enthusiastic": 1, 
            "inspired": 1, 
            "proud": 1, 
            "strong": 1, 
            "determined": 1, 
            "active": 1,
            "upset": 5,
            "jittery": 5,
            "nervous": 5, 
            "distressed": 5, 
            "guilty": 5, 
            "ashamed": 5, 
            "hostile": 5, 
            "irritable": 5, 
            "scared": 5, 
            "afraid": 5
        }
        positive_score, negative_score = get_affective_state_from_panas(panas_scores)
        self.assertEqual(positive_score, 0)
        self.assertEqual(negative_score, 1)

    def test_max_negative_max_positive(self):
        panas_scores = {
            "interested": 5, 
            "alert": 5,
            "attentive": 5, 
            "excited": 5, 
            "enthusiastic": 5, 
            "inspired": 5, 
            "proud": 5, 
            "strong": 5, 
            "determined": 5, 
            "active": 5,
            "upset": 5,
            "jittery": 5,
            "nervous": 5, 
            "distressed": 5, 
            "guilty": 5, 
            "ashamed": 5, 
            "hostile": 5, 
            "irritable": 5, 
            "scared": 5, 
            "afraid": 5
        }
        positive_score, negative_score = get_affective_state_from_panas(panas_scores)
        self.assertEqual(positive_score, 1)
        self.assertEqual(negative_score, 1)

    def test_case_from_proposal(self):
        panas_scores = {
            "interested": 1, 
            "alert": 5,
            "attentive": 2, 
            "excited": 3, 
            "enthusiastic": 1, 
            "inspired": 3, 
            "proud": 3, 
            "strong": 3, 
            "determined": 1, 
            "active": 1,
            "upset": 5,
            "jittery": 5,
            "nervous": 4, 
            "distressed": 4, 
            "guilty": 2, 
            "ashamed": 4, 
            "hostile": 4, 
            "irritable": 2, 
            "scared": 5, 
            "afraid": 4
        }
        positive_score, negative_score = get_affective_state_from_panas(panas_scores)
        self.assertEqual(positive_score, 0.325)
        self.assertEqual(negative_score, 0.725)

    def test_invalid_input_size(self):
        self.assertRaises(ValueError, lambda: get_affective_state_from_panas({}))

    def test_invalid_input_type(self):
        self.assertRaises(ValueError, lambda: get_affective_state_from_panas(5))
        
    def test_invalid_input_value_type(self):
        panas_scores = {
            "interested": 1, 
            "alert": 5,
            "attentive": 2, 
            "excited": 3, 
            "enthusiastic": 1, 
            "inspired": 3, 
            "proud": 3, 
            "strong": 3, 
            "determined": 1, 
            "active": 1,
            "upset": 5,
            "jittery": 5,
            "nervous": 4, 
            "distressed": 4, 
            "guilty": "yes", 
            "ashamed": 4, 
            "hostile": 4, 
            "irritable": 2, 
            "scared": 5, 
            "afraid": 4
        }
        self.assertRaises(ValueError, lambda: get_affective_state_from_panas(panas_scores))

    def test_invalid_input_value_value(self):
        panas_scores = {
            "interested": 1, 
            "alert": 5,
            "attentive": 2, 
            "excited": 3, 
            "enthusiastic": 1, 
            "inspired": 3, 
            "proud": 3, 
            "strong": 3, 
            "determined": 1, 
            "active": 1,
            "upset": 5,
            "jittery": 5,
            "nervous": 4, 
            "distressed": 4, 
            "guilty": 3, 
            "ashamed": 4, 
            "hostile": 4, 
            "irritable": 10, 
            "scared": 5, 
            "afraid": 4
        }
        self.assertRaises(ValueError, lambda: get_affective_state_from_panas(panas_scores))
        
if __name__ == '__main__':
    unittest.main()