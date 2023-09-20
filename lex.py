from tabulate import tabulate

def clean_seperators(text: str) -> list[list[str], list[str]]:
# [[stores all seperators], [updated text without seperators]]
    bank = [[], []]
    seps = ['(', ')', '{', '}', ';']
    start = 0
    i = 0
    new_s = ''

    while i <= len(text) - 1:
        if text[i] in seps:
            bank[0].append(text[i])
        else:
            new_s += text[i]
        i += 1
    
    bank[1].append(new_s)

    return bank


def clean_quotes(text: str) -> list[list[str], list[str]]:
# [[stores all strings], [updated text without strings and seperators]]
    bank = [[], []]
    new_s = ''
    start = 0
    i = 0

    while i <= len(text) - 1:
        if text[i] == "\"" and start == 0:
            start = i + 1
        elif text[i] == '\"' and start > 0:
            bank[0].append(text[start:i])
            start = 0
        else:
            new_s += text[i]
        i += 1

    bank[1].append(new_s)
    return bank


def clean_operators(text: str) -> list[list[str], list[str]]:
# [[stores all operators], [updated text without operators, strings and serperators]]
    bank = [[], []]
    ops = ['&', '<', '>', '<=', '>=', '=', '==', '*', '+', '-', '%', '/']
    new_s = ''
    i = 0

    while i <= len(text) - 1:
        if text[i] in ops:
            bank[0].append(text[i])
        else:
            new_s += text[i]

        i += 1

    bank[1].append(new_s)
    return bank


def clean_keywords(text: str) -> list[list[str], list[str]]:
# [[stores all keywords], [updated text without operators, strings and serperators]]
    bank = [[], []]
    new_s = ''
    keys = ['while', 'for', 'if', 'else']

    for word in text.split():
        if word in keys:
            bank[0].append(word)
        else:
            new_s += word + ' '
    
    bank[1].append(new_s)
    return bank

def clean_nums_and_identifiers(text: str) -> list[list[str], list[str]]: 
# [[stores all numbers], [stores all identifiers]]
    bank = [[], []]
    
    for word in text.split():
        try:
            bank[0].append(float(word))
        except:
            bank[1].append(word)

    return bank


def main(file_name: str) -> dict:

    text_file = open(file_name)
    text = text_file.read()
    text_file.close()
    ans = {}

    
    no_seps = clean_seperators(text)
    ans["Seperators"] = no_seps[0] if no_seps[0] else None

    no_str = clean_quotes(no_seps[1][0])
    ans["Strings"] = no_str[0] if no_str[0] else None

    no_ops = clean_operators(no_str[1][0])
    ans['Operators'] = no_ops[0] if no_ops[0] else None

    no_keywords = clean_keywords(no_ops[1][0])
    ans['Keywrods'] = no_keywords[0] if no_keywords[0] else None

    no_nums_and_ids = clean_nums_and_identifiers(no_keywords[1][0])
    ans["Real"] = no_nums_and_ids[0]
    ans["Identifiers"] = no_nums_and_ids[1]

    #print out the result into two columns
    table = []
    for k,v in ans.items():
        if v is not None:
            if isinstance(v, list):
                for item in v:
                    table.append([k, item])
            else:
                table.append([k, v])

    print(tabulate(table, headers=["Token", "Lexeme"], tablefmt="grid"))

main('nput_scode.txt')
