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


def sort_on(dict):
    return dict["num"]


def get_chars_report(chars_dict):
    chars_list = []
    for char, num in chars_dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": num})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
