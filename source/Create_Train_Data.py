
from konlpy.tag import Twitter
from File_IO import *

pos_tagger = Twitter()

def extract_features(words):
    return dict([(word, True) for word in words])

def Make_train_Model(name):
 pos = []
 neg = []
 nomal = []
 str2 = ""
 list1 = []
 train_docs = read_train_data(name)
 print("학습데터의 수 : ", len(train_docs))
 for i in train_docs:
    list2 = []
    list2.append(i[0])
    for j in range(1, len(i)):
        str2 = str2 + i[j] + " "
    list2.append(str2)
    str2 = ""
    list1.append(list2)
 for test in list1:
    if test[0] == '1' or test[0] == '2' or test[0] == '3':
        neg.append(test[1])
    elif test[0] == '4' or test[0] == '5' or test[0] == '6' or test[0] == '7':
        nomal.append(test[1])
    elif test[0] == '8' or test[0] == '9' or test[0] == '10':
        pos.append(test[1])

 print("긍정데이터 :", len(pos))
 print("중립데이터 :", len(nomal))
 print("부정데이터 :", len(neg))

 features_pos = [(extract_features(pos_tagger.nouns(f)), 'Positive') for f in pos]
 features_neg = [(extract_features(pos_tagger.nouns(f)), 'Negative') for f in neg]
 features_nomal = [(extract_features(pos_tagger.nouns(f)), 'Nomal') for f in nomal]

 threshold = 0.8
 num_pos = int(threshold * len(features_pos))
 num_neg = int(threshold * len(features_neg))
 num_nom = int(threshold * len(features_nomal))

 features_train = features_pos[:num_pos] + features_neg[:num_neg] + features_nomal[:num_nom]
 features_test = features_pos[num_pos:] + features_neg[num_neg:] + features_nomal[num_nom:]

 write_pickle(features_train, 'features_train.txt')
 write_pickle(features_test, 'features_test.txt')

