# ex2) STRINGS

hello = "NOT-RAW: This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

print hello

# RAW string
hello = r"RAW: This is a rather long string containing\n\
several lines of text much as you would do in C."

print hello
print # carriage return

# concatenate strings
word = 'Help' + 'A'
print word
print '<' + word*5 + '>'

# not changeable strings
#word[0] = 'x' # error

# length
s = 'supercalifragilisticexpialidocious'
len(s)

# UNICODE strings
print 'UNICODE:'
unic = u'Hello\u0020World !'
print unic