def search_replace(my_list, search, replace):
    newlist = list.copy(my_list)
    for x in range(0, len(my_list)):
        if newlist[x] == search:
            newlist[x] = replace
    return newlist
