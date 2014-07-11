import sys
import json

def hw(sent_file, tweet_file):
    token_score = {}
    for line in sent_file:
        token, score = line.split("\t")
        token_score[token] = int(score)

    for line in tweet_file:
        j = json.loads(line)
        if not j.has_key('text'):
            continue

        text = j['text']
        score = 0
        for word in text.split(" "):
            if token_score.has_key(word):
                score += token_score[word]
        print score

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
