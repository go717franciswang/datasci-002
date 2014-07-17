.PHONY: wordcount, inverted_index, join

wordcount: 
	python wordcount.py data/books.json | diff - solutions/wordcount.json

inverted_index: 
	python inverted_index.py data/books.json | diff - solutions/inverted_index.json | head

join:
	python join.py data/records.json | diff - solutions/join.json | head
