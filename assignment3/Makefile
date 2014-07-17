.PHONY: wordcount, inverted_index

wordcount: wordcount.py
	python wordcount.py data/books.json | diff - solutions/wordcount.json

inverted_index: 
	python inverted_index.py data/books.json | diff - solutions/inverted_index.json | head
