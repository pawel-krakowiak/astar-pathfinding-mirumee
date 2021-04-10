def flatten(dictionary, lkey=''):
    if all(type(v) is str for v in dictionary.values()):
        return dictionary
    D = {}
    for key in dictionary.keys():
        if type(dictionary[key]) is str:
            D[key] = dictionary[key]
        elif len(dictionary[key])==0:
            D[key] = ''
        else:
            E = flatten(dictionary[key])
            for keyE in E:
                D[key+'/'+keyE] = E[keyE]
    return D
