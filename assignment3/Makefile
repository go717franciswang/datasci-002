SHELL=/bin/bash

.PHONY: wordcount inverted_index join friend_count asymmetric_friendships

wordcount: 
	python wordcount.py data/books.json | diff - solutions/wordcount.json

inverted_index: 
	python inverted_index.py data/books.json | diff - solutions/inverted_index.json | head

join:
	python join.py data/records.json | diff - solutions/join.json | head

friend_count:
	python friend_count.py data/friends.json | diff - solutions/friend_count.json | head

asymmetric_friendships:
	comm -13 \
		<(python asymmetric_friendships.py data/friends.json | sort) \
		<(sort solutions/asymmetric_friendships.json)
