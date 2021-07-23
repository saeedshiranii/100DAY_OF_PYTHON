list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
                 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']


# this is my finnal version of caeser cipher


def caeser(shift, text, mod):
    p = ""
    shift = int(shift % 26)
    for i in text:
        position = list_alphabet.index(i)
        if mod == "encode":
            n_position = position + shift
            p += list_alphabet[n_position]


        elif mod == "decode":
            position = list_alphabet.index(i)
            n_position = position - shift
            p += list_alphabet[n_position]
    print(f"your text got {mod} and it is : {p}")


n_text = input("enter your text : ").lower()
n_shift = int(input("enter your shift number : "))
n_mod = input("encode or decode ? ").lower()

caeser(text=n_text, shift=n_shift, mod=n_mod)