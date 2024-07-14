def check_palindrome(text):
    reversed = text[::-1]
    if reversed == text:
        return "Palindrome text"
    else:
        return "Not a Palindrome text"
    
if __name__ == '__main__':
    text = input()
    check = check_palindrome(text)
    print(check)