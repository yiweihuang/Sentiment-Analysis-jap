import json
from jNlp.jSentiments import *

jp_wn = 'dict/wnjpn-all.tab'
en_swn = 'dict/SentiWordNet_3.0.0.txt'

def p_or_n(pScore, nScore):
    if pScore == nScore:
        return 'Text is Neural or Cannot Determine'
    if pScore > nScore:
        return 'Positive'
    else:
        return 'Negative'

def write_json(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii = False)

if __name__ == '__main__':
    des_filter_path = 'data/filter_speech/Description.json'
    act_filter_path = 'data/filter_speech/Activity_Body.json'
    senti_path = 'data/Sentiment_Analysis/Sentiment_Analysis_done.json'
    classifier = Sentiment()
    classifier.train(en_swn, jp_wn)
    with open(des_filter_path) as des_file:
        des_ = json.load(des_file)
    with open(act_filter_path) as act_file:
        act_ = json.load(act_file)
    dict_ = {}
    for ID in des_:
        temp_dict = {}
        temp_arr = []
        # Description
        if des_[ID]:
            des_pScore, des_nScore = classifier.polarScores_text(des_[ID])
            temp_dict['Problem'] = 'YES'
            temp_dict['des_pScore'] = des_pScore
            temp_dict['des_nScore'] = des_nScore
            temp_dict['Description'] = p_or_n(des_pScore, des_nScore)
        else:
            temp_dict['Problem'] = 'We can not find nouns and verbs.'
        # Activity_Body
        if act_[ID]:
            act_pScore, act_nScore = classifier.polarScores_text(act_[ID])
            temp_dict['Reply'] = 'YES'
            temp_dict['act_pScore'] = act_pScore
            temp_dict['act_nScore'] = act_nScore
            temp_dict['Activity_Body'] = p_or_n(act_pScore, act_nScore)
        else:
            temp_dict['Reply'] = 'NO'
        dict_[int(ID)] = temp_dict
    write_json(dict_, senti_path)
