g = {
"a1" : "-",
"a2" : "-",
"a3": "-",
"b1" : "-",
"b2" : "-",
"b3" : "-",
"c1" : "-",
"c2" : "-",
"c3" : "-",
}

def tic_toe():
    print(f"""
       a | b | c
    1  {g["a1"]} | {g["b1"]} | {g["c1"]}
      ---|---|---
    2  {g["a2"]} | {g["b2"]} | {g["c2"]}
      ---|---|---
    3  {g["a3"]} | {g["b3"]} | {g["c3"]}
    """)

def check_symbol():
    global symbol_list
    symbol = input('Your Symbol X/O:')
    if not symbol_list or symbol != symbol_list[-1]:
        symbol_list.append(symbol)

    else:
        print("Incorrect symbol.")
        check_symbol()

def check_result():
    if g["a1"] == g["b1"] == g["c1"] or g["a1"] == g["a2"] == g["a3"] or g["a1"] == g["b2"] == g["c3"]:
        print(f"{g['a1']} Win!")
        return True



symbol_list = []
is_end = False
while len(symbol_list) < 9 and is_end == False:
    tic_toe()
    position = input('Enter the position that you want to mark: ')
    if g[position] != '-':
        print("Position has already been marked. Choose another one.")
    else:
        check_symbol()
        g[position] = symbol_list[-1]
    if check_result():
        is_end = True


