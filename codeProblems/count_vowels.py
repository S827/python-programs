def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for a in text:
        if a in vowels:
            count += 1
    return count

if __name__ == '__main__':
    text = input()
    count = count_vowels(text)
    print(count)