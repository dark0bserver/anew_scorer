import unittest
from anew_scorer.scorer import AnewScorer


class TestAnewScorer(unittest.TestCase):

    def setUp(self):
        self.scorer = AnewScorer()
        self.test_text_one = "happy happy hug foo".split(' ')

        self.test_text_one_scores = {
            'all.Valence Mean': 8.14,
            'all.Arousal Mean': 3.0549999999999997,
            'all.Dominance Mean': 2.1166666666666667,
            'female.Valence Mean': 2.045833333333333,
            'female.Arousal Mean': 1.176,
            'female.Dominance Mean': 1.0666666666666667,
            'male.Valence Mean': 1.150952380952381,
            'male.Arousal Mean': 0.8145833333333333,
            'male.Dominance Mean': 0.6937037037037037}

        self.test_text_one_scores_zero_missing = {
            'all.Valence Mean': 6.105,
            'all.Arousal Mean': 2.29125,
            'all.Dominance Mean': 1.5875000000000001,
            'female.Valence Mean': 1.5343749999999998,
            'female.Arousal Mean': 0.882,
            'female.Dominance Mean': 0.7999999999999999,
            'male.Valence Mean': 0.8632142857142858,
            'male.Arousal Mean': 0.6109375,
            'male.Dominance Mean': 0.5202777777777778}

        self.test_text_two = """foo baz""".split(' ')

        self.test_text_two_scores = {
            'all.Valence Mean': 0,
            'all.Arousal Mean': 0,
            'all.Dominance Mean': 0,
            'female.Valence Mean': 0,
            'female.Arousal Mean': 0,
            'female.Dominance Mean': 0,
            'male.Valence Mean': 0,
            'male.Arousal Mean': 0,
            'male.Dominance Mean': 0}

        self.test_word = "hug"

        self.test_word_score = 5.79

    def test_score_word(self):
        self.assertEqual(
            self.test_word_score,
            self.scorer.__get_word_score__(
                self.test_word, 'all', 'Dominance Mean'))

    def test_score_words(self):
        self.assertScoreAlmostEqual(
            self.test_text_one_scores,
            self.scorer.vad_score_words(self.test_text_one))
        self.assertScoreAlmostEqual(
            self.test_text_two_scores,
            self.scorer.vad_score_words(self.test_text_two))

    def test_score_words_zero_missind_words(self):
        self.assertScoreAlmostEqual(
                self.test_text_one_scores_zero_missing,
                self.scorer.vad_score_words(self.test_text_one, True))
        self.assertScoreAlmostEqual(
                self.test_text_two_scores,
                self.scorer.vad_score_words(self.test_text_two, True))

    def assertScoreAlmostEqual(self, s1, s2):
        for k in s1:
            self.assertAlmostEqual(s1[k], s2[k])


if __name__ == '__main__':
    unittest.main()
    print("testing!")
