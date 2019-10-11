"""
Copyright (c) 2019 dark0bserver, https://medium.com/@dark0bserver

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import csv
import os


class AnewScorer:

    def __init__(
            self,
            score_path=os.path.join(os.path.dirname(__file__), 'anew/'),
            labels=['all', 'female', 'male']):
        self.score_ref = dict()
        self.labels = labels
        self.vocabulary = set()

        for label in self.labels:
            with open(f'{score_path}{label}.csv', 'r') as score_file:
                self.score_ref[label] = dict()
                reader = csv.DictReader(score_file)
                for row in reader:
                    scores = dict()
                    word = row.pop('Description')
                    self.vocabulary.add(word)
                    scores['Word Frequency'] = row.pop('Word Frequency')
                    for k in row:
                        scores[k] = float(row[k])
                    self.score_ref[label][word] = scores

    def __get_word_score__(self, word, label, axis):
        return self.score_ref[label][word][axis]

    def vad_score_words_to_dict(self, words, zero_missing_words):
        """Function to return a VAD score matrix for a group of tokenized words

        (Valence, Arousal, and Dominance) X (all, female, male)

        """
        # TODO extend this, it only returns mean values at the moment
        results = dict()
        num_words = 0

        for label in self.labels:
            results[label] = dict()

            # Valence Mean,Valence SD,
            # Arousal Mean,Arousal SD,
            # Dominance Mean,Dominance SD
            for axis in ['Valence Mean', 'Arousal Mean', 'Dominance Mean']:
                total = 0
                for word in words:
                    if word in self.vocabulary:
                        total += self.__get_word_score__(word, label, axis)
                        num_words += 1
                    elif zero_missing_words:
                        num_words += 1

                if 0 < num_words:
                    results[label][axis] = total/num_words
                else:
                    results[label][axis] = 0

        return results

    def vad_score_words(self, words, zero_missing_words=False):
        """Get dictionary describing average scores for words in the
        scoring corpus.
        """
        dscores = self.vad_score_words_to_dict(words, zero_missing_words)
        scores = dict()

        for label in dscores:
            for axis in dscores[label]:
                scores[f"{label}.{axis}"] = dscores[label][axis]

        return scores
