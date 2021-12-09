with open('../inputs/input8.txt')as f:
    files = f.read().splitlines()

import re

signals = []
digits = []

for f in files:
    line = re.findall('[a-z]+', f)
    signals.append(line[:10])
    digits.append(line[-4:])

# part 1

sum4 = 0
display4 = []
for d in digits:
    l = [dd for dd in d if len(dd) in [2, 4, 3, 7]]
    sum4 += len(l)
    display4.append(l)
print(sum4)

# part 2
def decode(toy_signals, toy_digits):

    output = []
    dict_digits = {}
    dict_char = {}
    dict_convert = {}
    
    for d,o in zip(toy_signals, toy_digits): 
        for dd in d:   
            if len(dd)==2:
                dict_digits['1'] = ''.join(dd)
            elif len(dd) == 4:
                dict_digits['4'] = ''.join(dd)
            elif len(dd) == 3:
                dict_digits['7'] = ''.join(dd)
            elif len(dd) == 7:
                dict_digits['8'] = ''.join(dd)

        
        new_str = ''.join(d)

        for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            dict_char[c] = new_str.count(c)

        for i,j in dict_char.items():        
            if j == 9:
                dict_convert['f'] = i
            elif j == 4:
                dict_convert['e'] = i
            elif j == 6:
                dict_convert['b'] = i
                
        dict_convert['a'] = list(set(dict_digits['7']) - set(dict_digits['1']))[0]
        dict_convert['c'] = list(set(dict_digits['1']) - set(dict_convert['f']))[0]
        dict_convert['d'] = list(set(dict_digits['4']) - set(dict_convert['f']) - set(dict_convert['b']) - set(dict_convert['c']))[0]
        dict_convert['g'] = list(set(dict_digits['8']) - set(dict_digits['4']) - set(dict_convert['a']) - set(dict_convert['e']))[0]
        dict_digits['6'] = ''.join(list(set(dict_digits['8']) - set(dict_convert['c'])))
        dict_digits['9'] = ''.join(list(set(dict_digits['8']) - set(dict_convert['e'])))
        dict_digits['0'] = ''.join(list(set(dict_digits['8']) - set(dict_convert['d'])))
        dict_digits['5'] = ''.join(list(set(dict_digits['8']) - set(dict_convert['c']) - set(dict_convert['e'])))
        dict_digits['3'] = ''.join(list(set(dict_digits['8']) - set(dict_convert['b']) - set(dict_convert['e'])))
        dict_digits['2'] = ''.join(list(set(dict_digits['8']) - set(dict_convert['b']) - set(dict_convert['f'])))
        
        decoder = {}
        for i,j in dict_digits.items():
            dict_digits[i] = ''.join(sorted(j))
            decoder[dict_digits[i]] = i

        o = [''.join(sorted(i)) for i in o]
        out = ''.join([decoder[i] for i in o])
        output.append(int(out))

    return output
        
print(sum(decode(signals, digits)))
    
    