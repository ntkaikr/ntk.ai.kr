# apps/nickgen/nonsense.py
import random

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
VOWELS = 'aeiou'
CONSONANTS = ''.join(c for c in ALPHA if c not in VOWELS)

def gibberish_en(min_len=3, max_len=10):
    target = random.randint(min_len, max_len)
    out = []
    last_vowel = random.random() < 0.5
    while len(''.join(out)) < target:
        if last_vowel:
            out.append(random.choice(CONSONANTS))
        else:
            out.append(random.choice(VOWELS))
        last_vowel = not last_vowel
    return ''.join(out)[:target].capitalize()

CHO = [0x1100,0x1102,0x1103,0x1105,0x1106,0x1107,0x1109,0x110B,0x110C,0x110E,0x110F,0x1110,0x1111,0x1112]
JUNG = [0x1161,0x1162,0x1165,0x1166,0x1167,0x1168,0x1169,0x116D,0x116E,0x1172,0x1173,0x1175]
JONG = [0x0000,0x11A8,0x11AB,0x11AE,0x11AF,0x11B7,0x11BA,0x11BC]

BASE = 0xAC00

def syllable(cp_cho, cp_jung, cp_jong=0):
    def idx(lst, cp):
        return lst.index(cp)
    ci = idx(CHO, cp_cho)
    vi = idx(JUNG, cp_jung)
    ji = JONG.index(cp_jong) if cp_jong else 0
    code = (ci*21 + vi)*28 + ji + BASE
    return chr(code)

def gibberish_ko(min_syll=2, max_syll=4):
    n = random.randint(min_syll, max_syll)
    out = []
    for _ in range(n):
        ch = syllable(random.choice(CHO), random.choice(JUNG), random.choice(JONG))
        out.append(ch)
    return ''.join(out)
