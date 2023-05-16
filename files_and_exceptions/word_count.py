'''A function that counts the number of words in a file'''
def count_words(file_list):
    for file in file_list:
        with open(file) as f:
            content = f.read()
    num_count = len(content)        
    print(num_count)
