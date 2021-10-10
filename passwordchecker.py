import requests
import hashlib


def passwordcheck(password):

    pwd = password.encode('utf-8')   # encode password in bytes
    hash_object = hashlib.sha1(pwd)  # hash the password using sha1 hashing

    # get the hex content of the hash and get first 5 characters
    hash_prefix = hash_object.hexdigest()[0:5].upper()
    hash_suffix = hash_object.hexdigest()[5:].upper()
    url = "https://api.pwnedpasswords.com/range/" + hash_prefix
    res = requests.get(url)          # send request
    result_dictionary = dict()

    if res.status_code == 200:
        # print(str(res.content))
        for line in res.text.split("\r\n"):
            pwd_key_value = line.split(":")
            result_dictionary[pwd_key_value[0]] = pwd_key_value[1]
            # print(line + '😊')
        # print(hash_prefix)
        if hash_suffix in result_dictionary:
            # print(f"The password '{password}' has been used {result_dictionary[hash_suffix]} times. "
            #       f"It seems rather unsafe.")
            return result_dictionary[hash_suffix]
        else:
            # print(f"It would seem the password {password} has not been used before. Go ahead.")
            return 0
    else:
        pass

    return -1
