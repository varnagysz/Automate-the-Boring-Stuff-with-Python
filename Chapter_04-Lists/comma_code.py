'''Say you have a list value like this:


spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string
with all the items separated by a comma and a space, with and inserted before
the last item. For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'. But your function should be
able to work with any list value passed to it.'''

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(some_parameter):
    string_word = ''
    for i in range(len(some_parameter)-1):
        string_word += some_parameter[i] + ', '
    string_word += 'and ' + some_parameter[-1]
    return string_word

spam_comma = comma_code(spam)
print(spam_comma)
