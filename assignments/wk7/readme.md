# Multinomial Naïve Bayes (MNB) and Support Vector Machines (SVM)


Author: Ryan Timbrook (RTIMBROO)<br>
DATE: 11/17/2019<br>
Topic: Compare MNB and SVMs for Kaggle Sentiment Classification<br>

## 1. Objective
_____________________________________________________________________________________________
Task 1:

So far we have learned how to use sklearn to build MNB and SVMs models and evaluate them using various test methods and measures. Output confusion matrix, precision and recall values for the Kaggle Sentiment training data.

-	Build a unigram MNB model and a unigram SVMs model.
-	Print the top 10 indicative words for the most positive category and the most negative category from the MNB and SVMs models respectively. 
-	You can change other parameters to your preference. Report your choice and explain why. 
-	Report the confusion matrix, precisions, and recalls. Explain whether your models performed equally well on all categories, or some categories turn out to be easier or more difficult for MNB or SVMs. 
-	Submit your revised script along with your report.

Task 2:

Consult the sklearn website to learn more about the CountVectorizer. Revise the script to build a MNB model and a SVMs model based on both unigram and bigram. For fair comparison, please keep the same 60% for training and the rest 40% for testing. Also keep your other vectorization parameters the same as in Task 1.

- Compare the confusion matrix and other evaluation measures (accuracy, precision, recall). Discuss whether adding bi-grams was helpful for sentiment classification, based on MNB and SVMs respectively.

Task 3:

Now revise the sample script to build your best SVMs model by tuning parameters and using the entire training data set (changing from 60% to 100%). Report what parameters you used to train the model, and its cross validation accuracy.

Then use this model to predict the Kaggle sentiment test data. Submit the prediction result to Kaggle, use screenshot to show your accuracy and ranking. 
https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/submit


## Findings / Recommendations
* See [Project Report](./HW_7_MultinomialNB_SupportVectorMachines_Timbrook_Ryan.pdf) for details


## Source Code
* Coding for this exercise was completed using python Anaconda3 in jupyter notebook<br>
	* [Jupyter Notebook](./hw7_mnb_svm_kaggle_sentiment.ipynb)<br>
	* [Python utility functions](./rtimbroo_utils_hw7.py)<br>
	
## Grading / Feedback
* [Grading and feedback](./Grades_Feedback.pdf) is provided to demonstrate reasoning on the structure of the assignment and its accompanying report.



