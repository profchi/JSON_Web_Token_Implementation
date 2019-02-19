# -*- coding: utf-8 -*-
"""

The script contains a 2 primary methods

get_token is used to generate an encrypted token 

verify_token is used to decrypt and validate the token

The script also contains test for both methods


External libraries

PyJWT : pip install pyjwt

Cryptography : pip install cryptograph


Created on Fri Jan 18 12:34:18 2019

@author: CHINEDU ISAIAH


"""

# for encoding and decoding tokens
import jwt

# test library
import unittest

# for encyption
import cryptography.fernet
from cryptography.fernet import Fernet

import datetime
import time

# Key used to sign the token
signature_key = '0389icpdmtionwFiilon40.#$$58CPAJJRHXKM'

# Key generated for encryption
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

# The method returns a payload which is used to generate the token
# This could be gotten from the database 
def get_payload():
    payload = {'sub' : 'JWT Research',
               'iss' : 'Chinedu Isaiah',
               'admin' : 'false',
               'user' : '2ndUser',
               'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds= 20)
               }
    return payload

# The method generates and encrypts the token
def get_token():
    # generate token
    payload = get_payload()
    token = jwt.encode(payload, signature_key, algorithm= 'HS256')
    #encrypt token
    encrypted_token = cipher.encrypt(token)
    return encrypted_token

# The method decrypts and then validates the token
# Returns true if properly validated otherwise returns false
def verify_token(token):
    result = True
    try:
        #decrypt toke
        decrypted_token = cipher.decrypt(token)
        #validate decrypted token
        jwt.decode(decrypted_token, signature_key, algorithms = 'HS256')
    except (KeyError, jwt.DecodeError, jwt.ExpiredSignature,
            cryptography.fernet.InvalidToken):
        # returns false if one of the exceptions is thrown
        result = False
    return result


 # Contains test cases for the implemented methods
# Tokens used were obtained from online jwt debugger( https://jwt.io/)   
class TestJwtMethods(unittest.TestCase):

    def test_get_and_verify_token(self):
        # generates token and then check if it would be verified
        generated_token = get_token()
        self.assertTrue(verify_token(generated_token))
        
    def test_verify_token(self):
        # checks if a token generated with the same signature would be validated
        token = b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikp1ZGUgRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.x0mW0-GHsoxCeCra9tJ2NRPCy8wWUzdUbbfwl3mogOQ'
        self.assertFalse(verify_token(token))
        
        # encrypts the token and then checks if it would then be validated
        encrypted_token = cipher.encrypt(token)
        self.assertTrue(verify_token(encrypted_token))
        
    def test_verify_expired_token(self):
        # generates token and then check if it would be verified
        generated_token = get_token()
        self.assertTrue(verify_token(generated_token))
        
        # Delay for 21 seconds and checks if token expires
        time.sleep(21)
        self.assertFalse(verify_token(generated_token))
        
if __name__ == '__main__':
    # call the test methods
    unittest.main()
