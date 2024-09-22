import sys

def name_verification(str):
    words = str.split(" ")
    count_true =0
    capitalized_words = [word[0].isupper() for word in words]
    for item in capitalized_words:
        if item == True:
            count_true += 1

    if count_true == len(capitalized_words):
        pass
    else:
        print("First Character of each word must be capital !")
        # sys.exit()




