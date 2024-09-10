import requests
import hashlib
import sys


def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + \
        query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the api and try again")
    return res


def read_res(response):
    print(response.text)


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print(hashes)
    for h, count in hashes:
        if h == hash_to_check:
            # print(h, hash_to_check)
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    # it returns characters from 5th position
    response = request_api_data(first5_char)
    # print(first5_char, tail, response)
    return get_password_leak_count(response, tail)
    # return read_res(response)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should probably change your password.")
        else:
            print(f"{password} was not found, carry on!")
    return 'done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
