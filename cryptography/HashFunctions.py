"""
A simple summary of basic Hash function combinations. Use these by comprehensive names!
by Sziller

File checksum for python. Use any file, get its hash.
For single sha256, you can check the results here:
https://emn178.github.io/online-tools/sha256_checksum.html
"""

import hashlib
import json


def single_sha256_byte2byte(preimage: bytes) -> bytes:
    """=== Function name: single_sha256_byte2byte ======================================================================
    Totally simple sha256 hashfunction.
    :param preimage: bytes - data you want to hash
    :return: bytes - the hash
    ============================================================================================== by Sziller ==="""
    return hashlib.sha256(preimage).digest()


def double_sha256_byte2byte(preimage: bytes) -> bytes:
    """=== Function name: single_sha256_byte2byte ======================================================================
    Double sha256 hashfunction. As used in Bitcoin most of the time.
    :param preimage: bytes - data you want to hash
    :return: bytes - the hash
    ============================================================================================== by Sziller ==="""
    return hashlib.sha256(hashlib.sha256(preimage).digest()).digest()


def generate_hashlist(hxstr_list, hash_procedure=single_sha256_byte2byte):
    """=== Function name: generate_hashlist ============================================================================
    Function turns a list's entries into hashses"""
    byte_list = [bytes.fromhex(_) for _ in hxstr_list]
    return json.dumps([hash_procedure(preimage=_).hex() for _ in byte_list])


if __name__ == "__main__":
    pass
    print(single_sha256_byte2byte(preimage=b'aa11hh').hex())
