import os

os.chdir(os.path.dirname(__file__))

def letter_percentages(filename):
    letter_count = {}
    total_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        inp = f.read().lower()
        for line in inp:
            for letter in line:
                if letter.isalpha():
                    if letter in letter_count:
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1
                    total_count += 1
    percentages = {letter: count/total_count*100 for letter, count in letter_count.items() if count != 0}
    sorted_percentages = {k: v for k, v in sorted(percentages.items(), key=lambda item: item[1], reverse=True)}
    return sorted_percentages

file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

percentages1 = letter_percentages(file1)
percentages2 = letter_percentages(file2)

print(f"{'file1':<10}{'file2':<10}")
for letter in sorted(set(list(percentages1.keys()) + list(percentages2.keys()))):
    col1 = f"{letter}: {percentages1.get(letter, 0):.1f}%" if letter in percentages1 else ""
    col2 = f"{letter}: {percentages2.get(letter, 0):.1f}%" if letter in percentages2 else ""
    print(f"{col1:<10}{col2:<10}")
