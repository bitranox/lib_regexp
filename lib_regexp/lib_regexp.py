import re


class ClassRegexExecute(object):
    """
    Führe eine regexp Suche oder Match durch
    Die Suche wird vorkompiliert abgespeichert.

    diese Klasse steht ganz oben in der Bibliothek, damit wir die vordefinierten Suchen in späteren Klassen verwenden können.

    Initialisierung:
    my_regexp=CRegex_execute(s_regexp)


    Parameter :     s_regexp            : ein Regexp String der die zu enthaltenden Zeichen beschreibt, z.Bsp: "[^a-z0-9.-]"
                                          die Suche ist Case Sensitive, somit würde ein Großbuchstabe ein unerlaubter Character sein
    Returns   :     mysearch            : ein Suchobjekt

    s_regexp Beispiele :
    [^a-z0-9.-]                         : Suche Zeichen die NICHT (^) a-z. 0-9,.,- enthalten
    \d                                  : Suche erste Ziffer
    (?:aaa|bbb)                         : Suche String aaa,bbb in Searchstring

                                          Bsp. s_regext aus einer Liste mit Strings erzeugen :
                                          s_regexp = '(?:%s)' % '|'.join(ls_searchstrings)

    Methoden:

    SEARCH :
    n_position,s_found=my_regexp.search(s_string)

    Parameter :    s_string             : der zu durchsuchende String
    Returns   :    n_position           : die Position an welcher der erste Character gefunden wurde der hier nicht sein sollte, oder None
                   s_found              : der Character der nicht enthalten sein sollte, oder None

    MATCH:
    n_position,s_found=my_regexp.match(s_string)

    >>> # Characters finden die nicht enthalten sein dürfen
    >>> my_regexp=ClassRegexExecute('[^a-z0-9.-]')
    >>> my_regexp.search('sadfkjhstr1kljhsadfstr2')
    (None, None)
    >>> my_regexp.search('blkmnÜat1')
    (5, 'Ü')
    >>> my_regexp.search('sadfkjhstTrxkljhsadfstry')
    (9, 'T')

    >>> # Liste of Strings in einem String finden (erstes vorkommen)
    >>> s_regexp='(?:%s)' % '|'.join(['str1','str2'])
    >>> my_regexp.set_s_regexp(s_regexp)
    >>> my_regexp.search('sadfkjhstr1kljhsadfstr2')
    (7, 'str1')
    >>> my_regexp.search('sadfkjhstrxkljhsadfstry')
    (None, None)
    >>> s_regexp='(?:%s)' % '|'.join(['.jpg','.tif','\.bat'])
    >>> my_regexp.set_s_regexp(s_regexp)
    >>> my_regexp.search('sadfkjhstr.jpgxkljhsadfstry')
    (10, '.jpg')
    >>> my_regexp.search('sadfkjhstrjp.batxkljhsadfstry')
    (12, '.bat')

    >>> # erstes Vorkommen einer Ziffer finden
    >>> my_regexp.set_s_regexp('\d')
    >>> my_regexp.search('sadfkjhstr1kljhsadfstr2')
    (10, '1')
    >>> my_regexp.search('bat1')
    (3, '1')
    >>> my_regexp.search('sadfkjhstrxkljhsadfstry')
    (None, None)

    """

    def __init__(self, s_regexp=None, flags=0):
        if bool(s_regexp):
            self.my_regexp = re.compile(s_regexp, flags=flags)
        else:
            self.my_regexp = None

    def set_s_regexp(self, s_regexp):
        self.my_regexp = re.compile(s_regexp)

    def search(self, s_string):
        result = self.my_regexp.search(s_string)
        if result is None:
            return None, None
        else:
            return result.start(), result.group()

    def match(self, s_string):
        result = self.my_regexp.match(s_string)
        if result is None:
            return None, None
        else:
            return result.start(), result.group()

    def findall(self, s_string):
        result = self.my_regexp.findall(s_string)
        return result

    def replace(self, s_string):
        result = self.my_regexp.replace(s_string)
        return result

    def sub(self, replace_with, s_input, count=0):
        result = self.my_regexp.sub(replace_with, s_input, count)
        return result


# VORDEFINIERTE REGEXP SUCHEN

# erstes Vorkommen einer Ziffer finden
regexp_ziffernsuche = ClassRegexExecute('\d')                                  # Ziffernsuche Instanz erzeugen, damit ist die Suche vorkompiliert

# Character finden a-z (case sensitive)
regexp_check_chars_az = ClassRegexExecute('[a-z]')                             # Instanz erzeugen, damit ist die Suche vorkompiliert
regexp_check_chars_azAZ = ClassRegexExecute('[a-zA-Z]')                        # Instanz erzeugen, damit ist die Suche vorkompiliert

# Alle Characters finden die nicht a-z,0-9,.,- sind (case sensitive)
regexp_check_chars_not_az09pointdash = ClassRegexExecute('[^a-z0-9.-]')        # Instanz erzeugen, damit ist die Suche vorkompiliert

# ^ = NOT
# \w = Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore
# \s = Matches Unicode whitespace characters (which includes [ \t\n\r\f\v], and also many other characters, for example the non-breaking spaces mandated by typography rules in many languages
# regexp_non_standard_unicode_characters = ClassRegexExecute(r'[^\w\s\^°!"§$%&/\'\(\)\[\]{}\~€@\+\-\*\|\=\?\>\<,;\.:#²³©®¼½¾ª™øØ\\]', flags=re.UNICODE)
regexp_non_standard_unicode_characters = ClassRegexExecute(r'[^\w\s\^°!"§$%&/\'\(\)\[\]{}\~€@\+\-\*\|\=\?\>\<,;\.:#`²³©®¼½¾ª™øØ\\]', flags=re.UNICODE)


def test_regexp(s_input):
    """

    # bad‌​string  <-- ungültige (unsichtbare) unicode characters befinden in diesem string !!! diese sollen entfernt werden.
    >>> test_regexp('bad‌​string^°!"§$%&/\\'()[]{}~€@öäüÖÄÜß+-*µ|><=?,;.:_ #²³©®¼½¾ª™øØ\\\\')
    ('badstring^°!"§$%&/\\'()[]{}~€@öäüÖÄÜß+-*µ|><=?,;.:_ #²³©®¼½¾ª™øØ\\\\', ['\\u200c', '\\u200b'])

    result = regexp_is_alphabetic_or_numeric.sub(input)
    return result


    """
    result = regexp_non_standard_unicode_characters.sub('', s_input)
    found = regexp_non_standard_unicode_characters.findall(s_input)
    return result, found
