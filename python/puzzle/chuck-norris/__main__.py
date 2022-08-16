import sys
import math


# ================== FUNCTIONS

def binEncode(message):
    '''Note on zfill:
    zfill(7) has been added to comply with codingame challenge for the '%' char test.

    > The final expected encoding is indeed : "00 0 0 0 00 00 0 0 00 0 0 0"
      which represents the binary 0b0100101 encoded over 7 bits
      converted to int this is : 37 (chr '%')

    > if the binary of 37 is NOT encoded over 7 bits,
      the binary encoding of 37 is : 0b100101, which is encoded over 6bits.
      The unaire encoding would hence be :  "0 0 00 00 0 0 00 0 0 0".
      That would fail '%' test in codingame.
    '''
    for charac in message:
        chrToBinStr = bin(ord(charac))[2:].zfill(7)
        yield chrToBinStr


def unaireSeqValidation(f):
    def hasOnlyBinaries(seq):
        binCount = seq.count('0') + seq.count('1')
        return len(seq) == binCount

    def wrapped(seq):
        if not hasOnlyBinaries(seq):
            raise ValueError('seq does not contain only binaries')
        r = f(seq)
        return r
    return wrapped


@unaireSeqValidation
def unaireSeq(message):
    unaireSeq = message[0]
    for i in message[1:]:
        if i == unaireSeq[0]:
            unaireSeq += i
        else:
            yield unaireSeq
            unaireSeq = i
    yield unaireSeq


def seqValidation(f):
    def getCharCount(seq):
        return {i: seq.count(i) for i in ['0', '1']}

    def hasUniqueValue(seq):
        return 0 in getCharCount(seq).values()

    def wrapped(seq):
        if type(seq) != str:
            raise TypeError("seq argument is not of type string")
        if not hasUniqueValue(seq):
            raise ValueError(
                "Only '0' OR '1' are accepted in sequence {}".format(seq))
        r = f(seq)
        return r
    return wrapped


@seqValidation
def unaireEncode(unaireSeq):
    result = '0 ' if unaireSeq[0] == '1' else '00 '
    result += '0' * len(unaireSeq)
    return result


# ================== MAIN

message = input()

binMessage = "".join(
    eachBinEncodedChar for eachBinEncodedChar in binEncode(message)
)

unaireMessage = " ".join(
    unaireEncode(eachUnaireSeq) for eachUnaireSeq in unaireSeq(binMessage)
)

print(unaireMessage)
