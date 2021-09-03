def add():
    sam = 0
    var = True
    while var:
        new_number = input('enter number: ').lower()
        if new_number == "end":
            var = False
        else:
            sam += int(new_number)

    print(sam)

add()
