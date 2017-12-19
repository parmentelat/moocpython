# -*- coding: utf-8 -*-
"""
Chiffrage de Vigenère dans le cadre du FUN MOOC Python 3
"""
import collections, time
from string import ascii_lowercase as abc, ascii_uppercase as ABC

class Vigenere:
    def __init__(self, key):
        "Initialize"
        assert isinstance(key, str)
        self.key = key
        
    def encode(self, text):
        "Encode text"
        assert isinstance(text, str)
        return self._cypher_(text, mode = 1)
        
    def decode(self, coded):
        "Decode coded"
        assert isinstance(coded, str)
        return self._cypher_(coded, mode = -1)
        
    def _cypher_(self, string, mode):
        "Shared methode to encode or decode"
        assert isinstance(string, str)
        assert isinstance(mode, int)
        assert mode in (1, -1)
        return ''.join((
                abc[(abc.index(c) + mode*self._get_key_idx(i)) % len(abc)] if c in abc else
                ABC[(ABC.index(c) + mode*self._get_key_idx(i)) % len(ABC)] if c in ABC else c
                for i, c in enumerate(string)))
    
    def _get_key_idx(self, idx):
        "Returns a upper or lower case caracter index corresponding to the input caracter position in the key word"
        c = self.key[idx % len(self.key)]
        return abc.index(c) if c in abc else ABC.index(c)
    
def test_vigenere(encode, decode):
    assert isinstance(encode, collections.Callable)
    assert isinstance(decode, collections.Callable)
    
    not_coded = "j'adorE écouter la radio toute la journee"
    coded = "v'slelI éuwknid di lepcg jiyfy tq naojvuy"
    
    t = time.process_time()
    coded_test = encode(not_coded)
    elapsed_time = time.process_time() - t
    if coded_test == coded:
        print(f"encode function OK ({t} ms): {coded_test}")
    else:
        print(f"encode function KO:\nexpected: {coded}\nobtained: {coded_test}")
    
    t = time.process_time()
    decoded_test = decode(coded)
    elapsed_time = time.process_time() - t
    if decoded_test == not_coded:
        print(f"decode function OK ({t} ms): {decoded_test}")
    else:
        print(f"decode function KO: expected:\n{not_coded}\nobtained: {decoded_test}")
    

if __name__ == "__main__":
    codec = Vigenere("mUsique")
    test_vigenere(codec.encode, codec.decode)
