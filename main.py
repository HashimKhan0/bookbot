from stats import num_words
from stats import num_characters
from stats import report
import sys

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():

	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]

	text = get_book_text(path)
	n = num_words(text)
	#print(f"{n} words found in the document",num_characters(text))
	dict = num_characters(text)
	report(dict,path,n)

if __name__ == "__main__":
	main()
