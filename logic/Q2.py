def count_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalnum(): 
            char = char.upper()  
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

if __name__=="__main__":
    text = "Hello welcome to Cathay 60th year anniversary"
    result = count_letters(text)
    for letter in sorted(result):
        print(f"{letter} {result[letter]}")
