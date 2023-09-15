text = "std::cout << \"Hello World\"; "

def read_str(text: str) -> str:
    bank = []
    start = 0
    i = 0
    while i <= len(text) - 1:
        if text[i] == "\"" and start == 0:
            start = i + 1
        elif text[i] == '\"' and start > 0:
            bank.append(text[start:i])
            start = 0

        i += 1

    return bank






def lexeme(file_name: str) -> dict:
    d = {'keyword': ['while', 'for', 'if', 'else'], 
         'seperator': ['(', ')', '{', '}', ';'], 'operator': ['<', '>', '<=', '>=', '=', '==', '*', '+', '-', '%', '/']}
    text_file = open(file_name)
    text = text_file.read()
    text_file.close()


print(read_str(text))
