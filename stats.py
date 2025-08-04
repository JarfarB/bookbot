def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_dict_list(dico):
    liste = []
    for char, num in dico.items():
        entry = {"char": char, "num": num}
        liste.append(entry)
    liste.sort(key=lambda x: x["num"], reverse=True)
    return liste




