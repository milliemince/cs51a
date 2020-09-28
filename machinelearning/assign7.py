#millie mince
#cs51a
#assignment7
#oct 25 2019

#Data, Training, and Classifying----------------------------------------------

def get_file_counts(filename):
    """counts the number of times each word occurs in a file and stores this 
    data as key-value pairs in a dictionary"""
    new_file = open(filename, "r")
    d = dict()
    for line in new_file: 
        split_line = line.split()
        for word in split_line:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    new_file.close()
    return d

def counts_to_probs(some_dict, num):
    """"from an input dictionary, counts_to_probs creates a new dictionary
    that has the same keys as the original dictionary, but divides each
    value by the input parameter 'num'"""
    new_d = dict()
    for key in some_dict:
        value = some_dict[key]
        new_d[key] = value/num
    return new_d

def train_model(filename):
    """function calculates the probabilities of each word in a given file 
    by dividing the number of occurences of each word by the total number 
    of words and returns a dictionary with these probabilites"""
    counts = get_file_counts(filename)
    new_file = open(filename, "r")
    num_lines = 0
    for line in new_file:
        num_lines += 1 
        #number of lines in file
    return counts_to_probs(counts, num_lines)

def get_probability(some_dict, some_string):
    """returns the probility of some_string by multiplying the probabilities 
    of each word in some_string. The probabilities of each word are received 
    from the input some_dict that stores data of each word's probability. 
    If some_string contains an unknown word, the function assumes its 
    probability is close to zero."""
    lowercase_review = some_string.lower()
    split_review = lowercase_review.split()
    product = 1 
    for word in split_review:
        if word not in some_dict:
            probability = 0.00009
            #assigning unknown words a probability very close to zero
        else: 
            probability = some_dict[word]
        product *= probability
    return product

def classify(some_string, trained_pos, trained_neg):
    """given an input positive and negative data set, this function classifies
    if input some_string is more likely to be a positive of negative movie
    review by determining whether the positive or negative probability is
    higher."""
    pos_probability = get_probability(trained_pos, some_string)
    neg_probability = get_probability(trained_neg, some_string)
    if (pos_probability >= neg_probability):
        return "positive"
    elif pos_probability < neg_probability: 
        return "negative"
        
def sentiment_analyzer(pos_file, neg_file):
    """prompts user for an input statement, and then classifies if this 
    statement is more likely to be positive or negative. function continues
    to prompt user for an input statement until they enter a blank line."""
    print("Blank line terminates.")
    trained_pos = train_model(pos_file)
    trained_neg = train_model(neg_file)
    running = True 
    #using this boolean statement to keep function running until user inputs ""
    while running:
        sentiment = input("Enter a sentence: ") 
        if sentiment == "":
            running = False
        else: 
            analysis = classify(sentiment, trained_pos, trained_neg)
            print(analysis)
            
def average(x, y):
    """returns the average of two numbers"""
    #helper function for get_accuracy
    average = (x+y)/2 
    return average
            
def get_accuracy(pos_test, neg_test, pos_train, neg_train):
    """determines how many of the movie reviews in pos_test and neg_test are
    accurately predicted given the positive and negative train data. The 
    function prints the positive, negative, and overall accuracy"""
    pos_file = open(pos_test, "r")
    neg_file = open(neg_test, "r")
    trained_pos = train_model(pos_train)
    trained_neg = train_model(neg_train)
    pos_count = 0
    #keeps track of how many positive reviews are accurately predicted
    total_pos_reviews = 0 
    neg_count = 0
    #keeps track of how many negative reviews are accurately predicted
    total_neg_reviews = 0
    for review in pos_file:
        classification = classify(review, trained_pos, trained_neg)
        total_pos_reviews += 1
        if classification == "positive":
            pos_count += 1    
    positive_accuracy = pos_count/total_pos_reviews 
    for review in neg_file:
        classification = classify(review, trained_pos, trained_neg)
        total_neg_reviews += 1
        if classification == "negative":
            neg_count += 1  
    negative_accuracy = neg_count/total_neg_reviews 
    total_accuracy = average(positive_accuracy, negative_accuracy)
    print("Positive accuracy: " + str(positive_accuracy))
    print("Negative accuracy: " + str(negative_accuracy))
    print("Total accuracy: " + str(total_accuracy))

#Evaluation------------------------------------------------------------------

"""
The output of get_accuracy("test.positive", "test.negative", "train.positive", 
"train.negative") is 
Positive accuracy: 0.960431654676259
Negative accuracy: 0.7043795620437956
Total accuracy: 0.8324056083600273
This shows that our Naive Bayes model is 96% accurate when predicting positive
reviews and 70% accurate when predicting negative reviews. Our model predicts
correctly on positive movie reviews much more often than negative reviews.
By taking the average of the positive and negative accuracies, we see that our
model is 83% accurate overall.

An example of when our model incorrectly predicts a movie review as positive
is the statement "This movie is incredibly terrible." Our model identifies
this as a positive statement because the probability of "incredibly" occuring
in a positive review is 0.00205, while the probability of "terrible" occuring
in a positive review is 0.00109. Because the probability of "incredibly" is 
higher than that of "terrible," the computer associates this statement with
positive reviews. It is thrown off by the word "incredibly" when that word 
is actually describing how terrible the movie was.

An example of when our model incorrectly predicts a movie review as negative 
is the statement "This movie is not good." It is thrown off by the word "good." 
The probability of "good" occuring in a positive movie review is 0.0521, while
the probability of "good" occuring in a negative movie review is 0.0260. The 
computer is unable to associate the word "not" with "good" and understand 
that the movie reviewer is trying to negate "good." 

In general, our model is unable of understanding the nuances of English (ex.
it is unable to tell that "incredibly" is describing how terrible the movie 
was, and it is similarly unable to tell that "not" is describing "good.")
"""