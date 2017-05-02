import json

def write_json(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii = False)

if __name__ == '__main__':
    des_path = 'data/filter_speech/Description.json'
    act_path = 'data/filter_speech/Activity_Body.json'
    senti_path = 'data/Sentiment_Analysis/Sentiment_Analysis_done.json'
    analysis_path = 'data/analysis/Positive_Negative.json'
    P_to_N_path = 'data/analysis/P_to_N.json'
    N_to_N_path = 'data/analysis/N_to_N.json'
    P_to_N_word_path = 'data/analysis/P_to_N_word.json'
    with open(senti_path) as senti_file:
        senti_ = json.load(senti_file)
    temp_P_to_N = []
    temp_N_to_N = []
    p_to_p = 0
    n_to_p = 0
    p_to_n = 0
    n_to_n = 0
    neural = 0
    dist_ = {}
    P_to_N_dist = {}
    N_to_N_dist = {}
    for ID in senti_:
        if senti_[ID]['Problem'] == 'YES' and senti_[ID]['Reply'] == 'YES':
            if senti_[ID]['Description'] == 'Positive' and senti_[ID]['Activity_Body'] == 'Positive':
                p_to_p += 1
            elif senti_[ID]['Description'] == 'Negative' and senti_[ID]['Activity_Body'] == 'Positive':
                n_to_p += 1
            elif senti_[ID]['Description'] == 'Positive' and senti_[ID]['Activity_Body'] == 'Negative':
                p_to_n += 1
                temp_P_to_N.append(ID)
            elif senti_[ID]['Description'] == 'Negative' and senti_[ID]['Activity_Body'] == 'Negative':
                n_to_n += 1
                temp_N_to_N.append(ID)
            else:
                neural += 1
    dist_['p_to_p'] = p_to_p
    dist_['n_to_p'] = n_to_p
    dist_['p_to_n'] = p_to_n
    dist_['n_to_n'] = n_to_n
    dist_['neural'] = neural
    # write_json(dist_, analysis_path)

    with open(des_path) as des_file:
        des_ = json.load(des_file)
    with open(act_path) as act_file:
        act_ = json.load(act_file)

    # P_to_N
    # for id_ in temp_P_to_N:
    #     temp_dist = {}
    #     temp_dist['Description'] = des_[id_]
    #     temp_dist['Activity_Body'] = act_[id_]
    #     P_to_N_dist[id_] = temp_dist
    # write_json(P_to_N_dist, P_to_N_path)

    # N_to_N
    # for id_ in temp_N_to_N:
    #     temp_dist = {}
    #     temp_dist['Description'] = des_[id_]
    #     temp_dist['Activity_Body'] = act_[id_]
    #     N_to_N_dist[id_] = temp_dist
    # write_json(N_to_N_dist, N_to_N_path)

    # find word
    # with open(P_to_N_path) as P_to_N_file:
    #     P_to_N = json.load(P_to_N_file)
    #
    # word_dict = {}
    # Description_arr = []
    # Activity_Body_arr = []
    # for id_ in P_to_N:
    #     d_arr_word = P_to_N[id_]['Description'].split('、')
    #     for d_word in d_arr_word:
    #         if d_word not in Description_arr:
    #             Description_arr.append(d_word)
    #     a_arr_word = P_to_N[id_]['Activity_Body'].split('、')
    #     for a_word in a_arr_word:
    #         if a_word not in Activity_Body_arr:
    #             Activity_Body_arr.append(a_word)
    # word_dict['Description'] = Description_arr
    # word_dict['Activity_Body'] = Activity_Body_arr
    # write_json(word_dict, P_to_N_word_path)

    # Sentiment
    des_tfidf_path = 'data/analysis/des_tfidf_n_3.json'
    act_tfidf_path = 'data/analysis/act_tfidf_n_3.json'
    with open(act_tfidf_path) as des_tfidf_file:
        des_tfidf = json.load(des_tfidf_file)
    temp_str = '、'.join(list(des_tfidf.keys()))
    print(temp_str)
