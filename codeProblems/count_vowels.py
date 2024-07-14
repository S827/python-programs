def count_vowels(text):
    count = 0
    for a in text:
        if a == 'a' or a == 'i' or a == 'o' or a == 'e' or a == 'u':
            count += 1
    return count

if __name__ == '__main__':
    text = input()
    count = count_vowels(text)
    print(count)