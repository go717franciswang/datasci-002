import json, sys

def main():
    tweet_file = open(sys.argv[1])
    freq = {}
    total = 0.
    for line in tweet_file:
        j = json.loads(line)
        if not j.has_key('entities') or not j['entities'].has_key('hashtags'):
            continue

        hashtags = j['entities']['hashtags']
        for info in hashtags:
            hashtag = info['text']
            total += 1
            if not freq.has_key(hashtag):
                freq[hashtag] = 0
            freq[hashtag] += 1

    descending_hastags = sorted(freq, key=freq.__getitem__, reverse=True)
    for hashtag in descending_hastags[:10]:
        print "%s %f" % (hashtag, freq[hashtag])

if __name__ == '__main__':
    main()
