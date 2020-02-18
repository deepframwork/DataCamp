'''
Counting words (II)
Once the vectorizer has been fit to the data, it can be used to transform the text to an array representing the word counts. This array will have a row per block of text and a column for each of the features generated by the vectorizer that you observed in the last exercise.

The vectorizer to you fit in the last exercise (cv) is available in your workspace.

Instructions 1/2
50 XP
1
Apply the vectorizer to the text_clean column.
Convert this transformed (sparse) array into a numpy array with counts.

2
Print the dimensions of this numpy array.

'''
SOLUTION 

1
# Apply the vectorizer
cv_transformed = CountVectorizer(speech_df['text_clean'])

# Print the full array
cv_array = cv.transform(speech_df['text_clean'])
print(cv_array)

2
# Apply the vectorizer
cv_transformed = cv.transform(speech_df['text_clean'])

# Print the full array
cv_array = cv_transformed.toarray()

# Print the shape of cv_array
print(cv_array.shape)