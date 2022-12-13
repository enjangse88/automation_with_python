def replacewordinfile():
    openFile = open("string.txt", "r")

    data = openFile.read()

    occurences = data.count("Lorem")

    print(f'Number of occurrences of the word: {occurences}')

replacewordinfile()
