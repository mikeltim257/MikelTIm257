string1 = 'Небо красное пришло '
string2 = 'Море синее ушло '

print(string1.replace(string1[:2], string2[:2]) + string2.replace(string2[:2], string1[:2]))
