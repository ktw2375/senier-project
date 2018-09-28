from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from File_IO import *
from  Create_Train_Data import *
import matplotlib.pyplot as plt

def Analtsis_Movie(Movie_Reple):
    positive_count = 0
    negative_count = 0
    nomal_count = 0
    features_train=read_pickle('features_train.txt')
    features_test=read_pickle('features_test.txt')
    print('\n학습데이터의 수:', len(features_train))
    print('테스트 데이터의 수: ', len(features_test))

    classifier = NaiveBayesClassifier.train(features_train)
    print('\n정확도 :', nltk_accuracy(
        classifier, features_test))

    N = 15
    print('\nTop ' + str(N) + ' 결정적인 단어 :')
    for i, item in enumerate(classifier.most_informative_features()):
        print(str(i + 1) + '. ' + item[0])
        if i == N - 1:
            break

    input_reviews = read_review(Movie_Reple)

    print("\n영화 리뷰 예측:")

    review_list = []

    for review in input_reviews:

        probabilities = classifier.prob_classify(extract_features(pos_tagger.nouns(review)))
        # Pick the maximum value
        predicted_sentiment = probabilities.max()

        print("\n리뷰 :", review)

        print("예측된 감정:", predicted_sentiment)
        print("정확도 :", round(probabilities.prob(predicted_sentiment), 2))
        if predicted_sentiment == 'Positive':
               positive_count +=1
        elif predicted_sentiment == "Negative":
               negative_count +=1
        elif predicted_sentiment == 'Nomal':
               nomal_count +=1

    print('긍정적인 비율 : ', positive_count/(positive_count+negative_count+nomal_count))
    print('부정적인 비율 : ', negative_count/(positive_count+negative_count+nomal_count))
    print('중립의 비율 : ',nomal_count/(positive_count+negative_count+nomal_count))
    print('총 개수 : ', positive_count+negative_count+nomal_count)

    num = [positive_count, nomal_count, negative_count]
    vec = ['postive', 'nomal', 'negative']

    plt.pie(num,
            labels=vec,
            colors=['steelblue', 'lightskyblue', 'salmon'],
            startangle=90,
            shadow=True,
            autopct='%1.1f%%')
    plt.show()