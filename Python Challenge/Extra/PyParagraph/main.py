

""" PYTHON Homework 3 (Extra) -PyParagraph """


''' Opening and Reading a text files '''

#filename = "PyParagraph_raw_data_paragraph_1.txt"
filename = "PyParagraph_raw_data_paragraph_2.txt"
f = open(filename,'r')
text = f.read()


''' Counting words in Paragraph '''
word_count = 0
words = text.split()
for each in words:
	word_count = word_count + 1
	
#print(word_count)


''' Counting number of sentences/lines in Paragraph and Average Sentence Length in words '''
sentence_count = 0
word_count_per_line = 0
paragraph = open(filename).readlines()
for line in paragraph:
	if line != '\n':
		sentence_count = sentence_count + 1
		words_list = line.split()
		average_sentence_length = len(words_list)
		
#print(sentence_count)
#print(average_sentence_length)



''' Average Letter Count per word '''
word_length = 0
for word in words:
	word_length = word_length + len(word)

Average_lenth_words = word_length / len(words)	
#print(Average_lenth_words)



''' Printing result to Terminal'''
print(f"\nFilename : {filename}")
output1 = "\nPARAGRAPH ANALYSIS"		
print(output1)	
print("-"*20)
output = "Approximate Word Count: {} \nApproximate Sentence Count: {} \nAverage Letter Count (per word): {} \nAverage Sentence Length (in words): {} \n"
print(output.format(word_count,sentence_count, Average_lenth_words, average_sentence_length))



