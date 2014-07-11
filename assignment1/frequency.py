import json, sys

def main():
    tweet_file = open(sys.argv[1])
    freq = {}
    total = 0.
    for line in tweet_file:
        j = json.loads(line)
        if not j.has_key('text'):
            continue

        text = j['text']
        for word in text.split():
            total += 1
            if not freq.has_key(word):
                freq[word] = 0
            freq[word] += 1

    for word, count in freq.items():
        print "%s %f" % (word, count / total)

if __name__ == '__main__':
    main()
