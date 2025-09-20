def list_min_item_length(in_list:list)->int:
    """get the max length from list """
    list_len = len(in_list[0])
    for idx in range(1,len(in_list)):
        if len(in_list[idx]) < list_len:
            list_len = len(in_list[idx])
    return list_len

def list_max_item_length(in_list:list)->int:
    """get the max length from list """
    list_len = 0
    for idx in range(len(in_list)):
        if len(in_list[idx]) > list_len:
            list_len = len(in_list[idx])
    return list_len


def lol_nested_items(lol_input:list[list],positon:int = 0):
    """
    get all items at specified position for each nested list in list of lists
    return all as single list
    """
    return_list=[]
    for nested_list in lol_input:
        return_list.append(nested_list[positon])
    return return_list


def key_value_lists_to_dict(key_list:list,value_list:list)->dict:
    """convert two lists of keys and values into dictionary using position"""
    return_dict = {}
    for idx in range(len(key_list)):
        return_dict[key_list[idx]] = value_list[idx]
    return return_dict


def lol_to_lod(key_names:list[str], list_of_lists:list[list]) ->list[dict]:
    """
    convert a list of lists to a single dictionary,
    uses additional input list for the keys to assign each value based on matched position
    """
    return_list = []
    for idx in range(list_max_item_length(list_of_lists)):
        return_list.append(key_value_lists_to_dict(key_names,lol_nested_items(list_of_lists,idx)))
    return return_list







