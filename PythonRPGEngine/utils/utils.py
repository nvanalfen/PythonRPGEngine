def string_to_dict(text, key_converter, value_converter, dict_sep=","):
    text = text.replace("{","").replace("}","").strip()
    components = text.split(dict_sep)
    result = {}

    for pairs in components:
        key, value = pairs.split(":")
        result[ key_converter(key.strip()) ] = value_converter(value.strip())

    return result

def string_to_tuple(text, converters):
    text = text.replace("(","").replace(")","").strip()
    components = text.split(",")
    result = tuple( [ converters[i]( components[i].strip() ) for i in range(len(components)) ] )

    return result

def string_to_list(text, converter=str):
    text = text.replace("[","").replace("]","").strip()
    return [ converter( el.strip() ) for el in text.split(",") ]