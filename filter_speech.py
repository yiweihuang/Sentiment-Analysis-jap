import json
import re

def filter_sp(read_data):
    dict_ = {}
    for ID in read_data:
        filter_arr = []
        # ID is string ; des_[ID] is list ; 名詞,動詞
        filter_arr = []
        for content_speech in read_data[ID]:
            try:
                content, speech = content_speech.split('\t')
                if (speech == '名詞' or speech == '動詞' or speech == '副詞' or speech == '形容詞') and content.isalpha():
                    filter_arr.append(content)
            except ValueError:
                pass
        temp_str = '、'.join(filter_arr)
        dict_[int(ID)] = temp_str
    return dict_

def filter_classifier(read_data):
    dict_ = {}
    for ID in read_data:
        filter_arr = []
        # ID is string ; des_[ID] is list ; 名詞,動詞
        filter_arr = []
        for content_speech in read_data[ID]:
            try:
                content, speech = content_speech.split('\t')
                if (speech == '名詞' or speech == '動詞' or speech == '副詞' or speech == '形容詞') and content.isalpha():
                    filter_arr.append(content)
            except ValueError:
                pass
        temp_str = ' '.join(filter_arr)
        dict_[int(ID)] = temp_str
    return dict_

def write_json(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii = False)

if __name__ == '__main__':
    des_path = 'data/raw_data/Description.json'
    act_path = 'data/raw_data/Activity_Body.json'
    des_filter_path = 'data/filter_speech/Description.json'
    act_filter_path = 'data/filter_speech/Activity_Body.json'
    des_classifier_path = 'data/classifier/Description.json'
    act_classifier_path = 'data/classifier/Activity_Body.json'
    with open(des_path) as des_file:
        des_ = json.load(des_file)
    with open(act_path) as act_file:
        act_ = json.load(act_file)
    # write_json(filter_sp(des_), des_filter_path)
    # write_json(filter_sp(act_), act_filter_path)
    write_json(filter_classifier(des_), des_classifier_path)
    write_json(filter_classifier(act_), act_classifier_path)
