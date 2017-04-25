from config import environments
import pyodbc
import MeCab
import json

tagger = MeCab.Tagger('mecabrc')

def parse_arr(row):
    if row == None:
        return []
    else:
        keywords = []
        message = row.split('\n')
        for column in message:
            if bool(column):
                mecab_result = tagger.parse(column)
                info_of_words = mecab_result.split('\n')
                for info in info_of_words:
                    if not(info == 'EOS' or info == ''):
                        info_elems = info.split(',')
                        keywords.append(info_elems[0])
    return keywords

def write_json(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

if __name__ == '__main__':
    server = environments.SERVER()
    database = environments.DATABASE()
    table = environments.TABLE()
    username = environments.USERNAME()
    password = environments.PASSWORD()
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM " + table + ";")
    row = cursor.fetchone()
    des_ = {}
    act_ = {}
    ID = 1
    while row:
        arr_des_jap = parse_arr(row[0]) # Description
        arr_act_jap = parse_arr(row[1]) # Activity Body
        des_[ID] = arr_des_jap
        act_[ID] = arr_act_jap
        ID += 1
        row = cursor.fetchone()
    des_path = 'data/raw_data/Description.json'
    act_path = 'data/raw_data/Activity_Body.json'
    write_json(des_, des_path)
    write_json(act_, act_path)
