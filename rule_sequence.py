def zero(str):
    if str[0] == '0':
        return str[1:]

def one(str):
    if str[0] == '1':
        return str[1:]

def rule_sequence(str, rules):
    length = len(str)
    counter = 0
    for rule in rules:
        s = rule(str[counter:length])
        if s == None:
            break
        counter += 1
    return s

def declrative_rule_sequence(str, rules):
    if str == None or not rules:
        return str
    else:
        return declrative_rule_sequence(rules[0](str), rules[1:])


