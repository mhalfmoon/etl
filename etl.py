class etl():
    def transform(old):
        new_dict={}
        for key,val in old.items():
            print(key,val)
            print(new_dict)
            new_dict[val].extend(key)
            print(new_dict)
etl.transform({1: ['WORLD']})
