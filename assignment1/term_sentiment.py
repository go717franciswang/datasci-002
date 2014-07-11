import sys
import json

def hw(sent_file, tweet_file):
    token_score = {}
    new_token_score_sum = {}
    new_token_score_count = {}
    for line in sent_file:
        token, score = line.split("\t")
        token_score[token] = int(score)

    for line in tweet_file:
        j = json.loads(line)
        if not j.has_key('text'):
            continue

        text = j['text']
        score = 0
        new_words = set()
        for word in text.split(" "):
            if token_score.has_key(word):
                score += token_score[word]
            else:
                new_words.add(word)

        for word in new_words:
            if not new_token_score_sum.has_key(word):
                new_token_score_sum[word] = 0.
                new_token_score_count[word] = 0
            new_token_score_sum[word] += score
            new_token_score_count[word] += 1

    for word, score in new_token_score_sum.items():
        print "%s %f" % (word, score / new_token_score_count[word])

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
