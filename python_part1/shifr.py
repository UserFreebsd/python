def main():
    import string

    alphabet_l = string.ascii_lowercase
    alphabet_u = string.ascii_uppercase
    offset = 13
    input_s = "Hello, world"

    for char in input_s:        # для каждого символа сделай то что мы напишем в input_s (Hello, world)
        if char in alphabet_l:  #если символ char находится в alphabet_1
            pos = alphabet_l.find(char)
            pos+=offset
            output_s

    # входная_строка = "Hello, world"
    # print(входная_строка)
    # import string
    # string.ascii_letters

main()
