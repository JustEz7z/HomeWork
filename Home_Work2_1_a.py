def findText(some_text,find_text):
    result = some_text.count(find_text)
    print(result)

text = input("Enter text: ")
findtext = input("Some text what u want to find in the text: ")
# indFindText = findtext.split()
findText(text,findtext)
