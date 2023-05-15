def unir_dict(list_dic):
    final_dic = {}
    for dics in list_dic:
        for key, value in dics.items():
            if key in final_dic:
                final_dic[key] = [final_dic[key], value]
            else:
                final_dic[key] = value
    return final_dic


PEOPLE = [{'first': 'Reuven', 'email': 'reuven@lerner.co.il'},
          {'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', }]

print(unir_dict(PEOPLE))
