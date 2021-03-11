def reverse_string(word):
    reversed = ''
    for i in word:
        reversed = i + reversed
    print(reversed)

def reverse(string):
    string = string[::-1]
    print(string)

reverse_string('anne')
reverse('anne')