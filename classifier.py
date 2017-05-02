import json
import csv
# from sklearn import svm
# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn import feature_selection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import numpy as np

def write_json(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii = False)

if __name__ == '__main__':
    des_filter_path = 'data/classifier/Description.json'
    act_filter_path = 'data/classifier/Activity_Body.json'
    senti_path = 'data/Sentiment_Analysis/Sentiment_Analysis_done.json'
    # des_tfidf_path = 'data/analysis/des_tfidf_n_3.json'
    des_tfidf_path = 'data/analysis/des_tfidf_n_1.json'
    # act_tfidf_path = 'data/analysis/act_tfidf_n_3.json'
    act_tfidf_path = 'data/analysis/act_tfidf_n_1.json'
    with open(des_filter_path) as des_file:
        des_ = json.load(des_file)
    with open(act_filter_path) as act_file:
        act_ = json.load(act_file)
    with open(senti_path) as senti_file:
        senti_ = json.load(senti_file)

    # TFIDF
    des_tfidf = []
    act_tfidf = []
    des_tfidf_dict = {}
    act_tfidf_dict = {}

    des_label = []
    act_label = []
    for ID in des_:
        # if des_[ID]:
        #     des_tfidf.append(des_[ID])
        #     if senti_[ID]['Description'] == 'Positive':
        #         des_label.append('pos')
        #     elif senti_[ID]['Description'] == 'Negative':
        #         des_label.append('neg')
        #     else:
        #         des_label.append('neural')
        if act_[ID]:
            act_tfidf.append(act_[ID])
            if senti_[ID]['Activity_Body'] == 'Positive':
                act_label.append('pos')
            elif senti_[ID]['Activity_Body'] == 'Negative':
                act_label.append('neg')
            else:
                act_label.append('neural')

    # Create feature vectors
    # vectorizer = TfidfVectorizer(min_df=5,
    #                              max_df = 0.8,
    #                              sublinear_tf=True,
    #                              use_idf=True)
    vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')

    train_vectors = vectorizer.fit_transform(act_tfidf)

    # Perform classification with SVM, kernel=linear
    classifier_liblinear = svm.LinearSVC()
    classifier_liblinear.fit(train_vectors, act_label)
    # 0 is neg ; 1 is neural ; 2 is pos ---- Description
    # 0 is neg ; 1 is neural ; 2 is pos ---- Activity_Body

    # Description
    # des_neg_feature_path = 'data/analysis/des_pos_feature_1.csv'
    # des_feature_names = vectorizer.get_feature_names()
    # labelid = 2 # this is the coef we're interested in.
    # svm_coef = classifier_liblinear.coef_
    # writer = csv.writer(open(des_neg_feature_path, 'w'))
    # topn = sorted(zip(svm_coef[labelid], des_feature_names), reverse=True)[:30]
    # for coef, feat in topn:
    #     writer.writerow([feat.encode('utf-8'), coef])


    # Activity_Body
    act_pos_feature_path = 'data/analysis/act_neg_feature_1.csv'
    act_feature_names = vectorizer.get_feature_names()
    labelid = 0 # this is the coef we're interested in.
    svm_coef = classifier_liblinear.coef_
    writer = csv.writer(open(act_pos_feature_path, 'w'))
    topn = sorted(zip(svm_coef[labelid], act_feature_names), reverse=True)[:30]
    for coef, feat in topn:
        writer.writerow([feat.encode('utf-8'), coef])


    #tag cloud
    # tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
    # tfidf_matrix =  tf.fit_transform(des_tfidf)
    # feature_names = tf.get_feature_names()
    # dense = tfidf_matrix.todense()
    # episode = dense[0].tolist()[0]
    # phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]
    # sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    # for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
    #     print('{0: <20} {1}'.format(phrase, score))
