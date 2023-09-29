#In English, every sentence ends with a period. You will use this to divide the paragraph into different sentences. Using the split method to split the text into sentences by searching for the string. (a period followed by a space). Store the result in a variable called sentences. Print the result.

sentences = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

sentence_list = sentences.split('. ')

for sentence in sentence_list:
    if 'temperature' in sentence:
            print(sentence)
