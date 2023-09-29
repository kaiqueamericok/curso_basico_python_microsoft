# In English each sentence ends with a period. You will use this to break the paragraph into difference sentences. Using the split method to split the text into sentences by looking for the string .  (a period followed by a space). Store the result in a variable named sentences. Print the result.

text = ['Interesting facts about the Moon', "The Moon is Earth's only satellite", 'There are several interesting facts about the Moon and how it affects life here on Earth', '\nOn average, the Moon moves 4cm away from the Earth every year', 'This yearly drift is not significant enough to cause immediate effects on Earth', 'The highest daylight temperature of the Moon is 127 C.']

sentences = '.'.join(text).split('. ')
print(sentences)