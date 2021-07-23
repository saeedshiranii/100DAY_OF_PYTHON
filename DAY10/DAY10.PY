# task: change the format of word to title case
# i wanna use title method
def format_name2(f_name, l_name):

    f_name = f_name.title()
    l_name = l_name.title()

    return f"formated name is : {f_name} {l_name} . "


print(format_name2("jack","ana"))