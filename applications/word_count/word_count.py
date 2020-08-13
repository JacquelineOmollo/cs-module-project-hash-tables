def word_count(s):
    cache = {}  
   
#  Case should be ignored
#  Output keys must be lowercase.
#  Split the strings into words on any whitespace
#  ignore each of the following characters:" : ; , . - + = / \ | [ ] { } ( ) * ^ &

    lowercase = s.lower()
    ignore = '" : ; , . - + = / \ | [ ] {} ( ) * ^ &"'.split(" ")

    for i in ignore:
        lowercase = lowercase.replace(i, "")
    for word in lowercase.split():
        print(word)
        if word == "":
            return word
        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1
    
    return cache
   


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))