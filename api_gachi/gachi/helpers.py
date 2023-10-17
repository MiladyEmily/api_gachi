GACHICLONE = {
    "асс" : "Ass",
    "трах" : "Трах",
    "вяч": "ВИЧ",
    "вич": "ВИЧ",
    "дип" : "Deep",
    "деп" : "Deep",
    "гей" : "Gay",
    "гий" : "Gay",
    "слава" : "Slave",
    "оргий" : "Orgy",
    "ксан" : "Cum",
    "кам" : "Cum",
    "ком" : "Cum",
    "кан" : "Cum",
    "ка" : "Cum",
    "дик" : "Dick",
    "семен" : "Semen",
    "семён" : "Semen",
    "семе" : "Semen",
    "сем" : "Semen",
    "сим" : "Semen",
    "сер" : "Sir",
    "вии" : "Wee",
    "вее" : "Wee",
    "ви" : "Wee",
    "ве" : "Wee",
    "орги" : "Orgy",
    "ас" : "Ass",
    "тах" : "Трах",
    "тра" : "Трах",
    "де" : "Deep",
    "ге" : "Gay",
    "ги" : "Gay",
    "слав" : "Slave",
    "анал" : "Anal",
    "ана" : "Anal",
    "ан" : "Cum",
    "АН" : "Anal",
    "иго" : "Nigga",
    }

TRANSLIT = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'yo',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'j',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'kh',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shh',
    'ъ': 'ie',
    'ы': 'y',
    'ь': '',
    'э': 'ei',
    'ю': 'u',
    'я': 'ia',
    ' ': '_',
    '-': '-'
}


# добавить, что если в конце ей или эй, то Ass
def gaching(word):
    return getGachi(word.lower())


def getGachi(word, start = 0):
    variants = []
    for gachi in GACHICLONE:
        start_letter = word.find(gachi, start)
        if start_letter < 0:
            continue
        end_letter = start_letter + len(gachi)
        gachied = word.replace(gachi, GACHICLONE[gachi])
        variants.append(gachied)
        if len(gachied) - end_letter > 1:
            variants += getGachi(gachied, end_letter)
    return variants

def translit_name(name):
    translit_name = ''
    for char in name:
        if char in TRANSLIT:
            translit_name += TRANSLIT[char]
    return translit_name
