
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
printtext = main()
length = []
length = printtext.split()
lower_text = printtext.lower()


def count(lower_text):
    text_dict = {}
    for char in lower_text:
        if char.isalpha():
            if char in text_dict:
                text_dict[char] += 1
            else: 
                text_dict[char] = 1

        
    return text_dict

resulting_chars = count(lower_text)

def sort_on(item):
    return item[1]

sorted_chars = sorted(resulting_chars.items(), key=sort_on, reverse=True)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(length)} words found in the document")
def printf():
    for char,count in sorted_chars:
        print(f"the '{char}' was found {count} times")

printf()
print("End of Report")



  



