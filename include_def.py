def descriptions_len_list(list_len):
    descript = []
    for text_in_list in list_len:
        if len(text_in_list) >= 6:
            descript.append(text_in_list)
    quantity_discription = {}
    for quantity in descript:
        if quantity not in quantity_discription.keys():
            quantity_discription[quantity] = 1
        else:
            quantity_discription[quantity] += 1
    return quantity_discription

def words_top(dict_quantity,):
    quantity = 1
    list_word = list()
    while quantity <= 10:
        words_name = None
        words_value = 0
        for word in dict_quantity.keys():
            if words_value < dict_quantity[word]:
                if word not in list_word:
                    words_name = word
                    words_value = dict_quantity[word]

        list_word.append(words_name)
        print('Слово "{}" занимает {} место и повторяется {} раза'.format(words_name, quantity, words_value))
        quantity += 1
