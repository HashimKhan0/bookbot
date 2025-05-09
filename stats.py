def num_words(path_to_txt):
# txt is one long string of a book.  a textbook one may say
        words = path_to_txt.split()
        return len(words)

def num_characters(txt):
	words = txt.split()
	result = {}
	for w in words:
		for l in w:
			char = l.lower()
			if char not in result:
				result.setdefault(char,1)
			else:
				result[char] += 1
	return result


def report(dict,path,total_words):
	dict_sort = sorted(dict.items())
	print("============ BOOKBOT ============ \n"
	     f"Analyzing book found at {path}... \n"
	      "----------- Word Count ---------- \n"
	     f"Found {total_words} total words\n"
              "--------- Character Count -------\n")

	for key,value in dict_sort:
		if key.isalpha():
			print(f"{key}: {value}"),

	print("============= END ===============")


