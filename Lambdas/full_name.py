def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))