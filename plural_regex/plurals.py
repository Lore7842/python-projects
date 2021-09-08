import re


def func_builder(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern,word)
    def apply_rule(word):
        return re.sub(search,replace,word)
    return (matches_rule, apply_rule)


patterns = [
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('(qu | [^aeiou])y$', 'y$', 'ies'),
    ('$', '$', 's')
]
rules = [func_builder(pattern, search, replace) for (pattern, search, replace) in patterns]

def plural(word):
    for matches_rule, apply_rule in rules:
        if matches_rule(word):
            return apply_rule(word)


output = open('C:\\Users\\lollo\\Desktop\\python project\\plural_regex\\plurals.txt', 'r+')

with open('C:\\Users\\lollo\\Desktop\\python project\\plural_regex\\words.txt' ,'r+') as f:
    for line in f:
        plurale = plural(line.split('\n')[0])
        output.write(plurale +'\n')


output.close()
