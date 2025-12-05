def filter_by_state(list_dictionary, state='EXECUTED'):
    list_dictionary_executed = []
    for dictionary in list_dictionary:
        if dictionary.get("state") == state:
            list_dictionary_executed.append(dictionary)
    return list_dictionary_executed


def sort_by_date (list_dictionary):
    sort_list_dictionary = sorted(list_dictionary, key=lambda i: i.get("date"), reverse=True)
    return sort_list_dictionary
