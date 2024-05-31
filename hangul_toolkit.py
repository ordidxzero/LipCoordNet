import hgtk
from typing import List


# 초성 / 중성 / 종성을 유니코드로 변환하는 함수
# 빈 문자열이 들어오면 None을 반환
def __syllable_to_uni(c: str):
    c = c.strip()
    if c == "":
        return None
    return ord(c)


# 유니코드를 초성 / 중성 / 종성으로 변환하는 함수
# None이 들어오면 None을 반환
def __uni_to_syllable(c: int):
    if c == None:
        return None
    return chr(c)


# 하나의 한글 음절을 받아서 초성, 중성, 종성으로 분해 후 유니코드로 변환하는 함수
def decompose_hangul(c: str, return_unicode=True):
    if type(c) != str:
        raise TypeError("Input should be a string")

    c = c.strip()

    if len(c) != 1:
        raise ValueError("The input must have exactly one character.")

    decomposed = hgtk.letter.decompose(c)

    if return_unicode == True:
        return list(map(__syllable_to_uni, decomposed))
    else:
        return list(decomposed)


# 초성, 중성, 종성 유니코드를 받아서 하나의 한글 음절로 합치는 함수
def compose_hangul(syllables: List[int | None], input_unicode=True):

    if len(syllables) != 3:
        raise ValueError("The input must have exactly 3 elements.")

    if syllables[0] == None or syllables[1] == None:
        raise ValueError("cho and jung should not be None")

    if input_unicode == True:
        cho, jung, jong = list(map(__uni_to_syllable, syllables))
    else:
        cho, jung, jong = syllables

    return hgtk.letter.compose(cho, jung, jong)
