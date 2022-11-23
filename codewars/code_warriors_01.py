
class SimplePigLatin:
    """ Simple Pig Latin
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

    Examples
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !

    """

    def trans(w):
        return w[1:] + w[0] + "ay" if w.isalpha() else w

    def pig_it(text):
        return " ".join([SimplePigLatin.trans(w) for w in text.split(" ") ])

    def __init__(self):

        # test
        assert SimplePigLatin.pig_it('Hello o !') == "elloHay oay !"
        assert SimplePigLatin.pig_it('Hello world !') == "elloHay orldway !"
        assert SimplePigLatin.pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
        assert SimplePigLatin.pig_it('This is my string') == 'hisTay siay ymay tringsay'

SimplePigLatin()

import collections
import re
class Anagrams:
    """ Where my anagrams at?

    What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
    For example:
        'abba' & 'baab' == true
        'abba' & 'bbaa' == true
        'abba' & 'abbba' == false
        'abba' & 'abca' == false

    Write a function that will find all the anagrams of a word from a list. 
    You will be given two inputs a word and an array with words.
    You should return an array of all the anagrams or an empty array if there are none

    """

    def anagrams(word, words):
        results = []
        c1 = collections.Counter(word)
        for w in words:
            if c1 == collections.Counter(w):
                results.append(w)
        return results

    def anagrams(word, words):
        s0 = sorted(word)
        return [w for w in words if s0 == sorted(w)]

    def __init__(self):
        assert Anagrams.anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
        assert Anagrams.anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']

Anagrams()


import string

class Pangram:
    """
    A pangram is a sentence that contains every single letter of the alphabet at least once.
    For example, the sentence
        "The quick brown fox jumps over the lazy dog" 
        is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

    Given a string, detect whether or not it is a pangram.
    Return True if it is, False if not. Ignore numbers and punctuation.

    """


    def is_pangram(text):
        letters = set()
        for t in text:
            if t.isalpha():
                letters.add(t.lower())
        return sorted(letters) == list(string.ascii_lowercase)
        
    def is_pangram(text):
        return sorted(set([t.lower() for t in text if t.isalpha()])) == list(string.ascii_lowercase)

    def is_pangram(text):
        ASCII_LOWERCASE_SET = set(string.ascii_lowercase)
        return ASCII_LOWERCASE_SET.issubset(text.lower())

        
    assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True

    assert is_pangram("1bcdefghijklmnopqrstuvwxyz") == False

Pangram()


class DeleteOccurrences:
    """ Delete occurrences of an element if it occurs more than n times

    Task
    Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
    For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
    With list [20,37,20,21] and number 1, the result would be [20,37,21].
    """

    def delete_nth(order,max_e):
        r = []
        c = {}
        for i in order:
            if i not in c.keys():
                c[i] = 0
            c[i] += 1
            if c[i] <= max_e:
                r.append(i)
        return r

    def delete_nth(order,max_e):
        ans = []
        for o in order:
            if ans.count(o) < max_e:
                ans.append(o)
        return ans

    print("DeleteOccurrences")
    assert delete_nth([20,37,20,21], 1) == [20,37,21]
    assert delete_nth([1,1,3,3,7,2,2,2,2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]

DeleteOccurrences()

import string
from operator import indexOf

class HighestScoringWord:
    """ Highest Scoring Word
    Given a string of words, you need to find the highest scoring word.

    Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

    You need to return the highest scoring word as a string.

    If two words score the same, return the word that appears earliest in the original string.

    All letters will be lowercase and all inputs will be valid.
    """



    ASCII_LOWERCASE = string.ascii_lowercase

    def get_score(word):
        return sum([1 + indexOf(HighestScoringWord.ASCII_LOWERCASE, l) for l in word])

    def high(text):
        max = -1
        for word in text.split(" "):
            score = HighestScoringWord.get_score(word)
            if score > max:
                max = score
                result = word
        return result

    def high(text):
        # ord("a") = 97 
        return max(text.split(), key=lambda word: sum(ord(letter) - 96 for letter in word))

    print("HighestScoringWord")
    assert high('man i need a taxi up to ubud') == 'taxi'
    assert high('what time are we climbing up the volcano') == 'volcano'
    assert high('take me to semynak') == 'semynak'
    assert high('aa b') == 'aa'
    assert high('b aa') == 'b'

HighestScoringWord()

class WhoLikesIt:
    """ Who likes it?
    You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
    We want to create the text that should be displayed next to such an item.

    Implement the function which takes an array containing the names of people that like an item. 
    It must return the display text as shown in the examples:

    []                                -->  "no one likes this"
    ["Peter"]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

    """
    def likes(names):
        likes = len(names)
        if likes == 0:
            r = "no one likes this"

        elif likes == 1:
            r = f"{names[0]} likes this"
        
        elif likes == 2:
            r = f"{names[0]} and {names[1]} like this"

        elif likes == 3:
            r = f"{names[0]}, {names[1]} and {names[2]} like this"
        
        else:
            r = f"{names[0]}, {names[1]} and {likes - 2 } others like this"

        #print(names, r)
        return r

    def likes(names):
        formats = {
                0: "no one likes this",
                1: "{} likes this",
                2: "{} and {} like this",
                3: "{}, {} and {} like this",
                4: "{}, {} and {n_others} others like this"
            }
        n_likes = len(names)
        text = formats[min(n_likes, 4)].format(*names, n_others=n_likes-2)
        # print(names, text)
        return text

    print("WhoLikesIt")
    assert likes([]) == 'no one likes this' 
    assert likes(['Peter']) == 'Peter likes this' 
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this' 
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this' 
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this' 

WhoLikesIt()



from operator import indexOf
from collections import OrderedDict


class RomanNumerals:
    """ Roman Numerals Helper
        Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
        It should follow the API demonstrated in the examples below
        Multiple roman numeral values will be tested for each helper method.

        Modern Roman numerals are written by expressing each digit separately starting with the left most digit
        and skipping any digit with a value of zero.
        In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
        2008 is written as 2000=MM, 8=VIII; or MMVIII.
        1666 uses each Roman sym in descending order: MDCLXVI.

        Input range : 1 <= n < 4000
    """

    ROMAN_VAL = OrderedDict({
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        "V̅":5000,
        "X̅":10000,
    }
    )

    ROMAN_LIST = list(ROMAN_VAL.keys())
    ROMAN_LIST_LIM = len(ROMAN_LIST) - 1

    MAX_VAL = ROMAN_VAL[ROMAN_LIST[-1]] * 4 - 1 

    VAL_ROMAN = {v: k for k, v in ROMAN_VAL.items()}

    def to_string(n, mag):
        sym = RomanNumerals.VAL_ROMAN[mag]
        sym_index = indexOf(RomanNumerals.ROMAN_LIST,  sym)

        next_s = RomanNumerals.ROMAN_LIST[min([sym_index + 1, RomanNumerals.ROMAN_LIST_LIM])]
        two_next_s = RomanNumerals.ROMAN_LIST[min([sym_index + 2, RomanNumerals.ROMAN_LIST_LIM])]
        formats = {
            0: "",
            1: f"{sym}",                    # I
            2: f"{sym}{sym}",               # II
            3: f"{sym}{sym}{sym}",          # III
            4: f"{sym}{next_s}",            # IV
            5: f"{next_s}",                 # V
            6: f"{next_s}{sym}",            # VI
            7: f"{next_s}{sym}{sym}",       # VII
            8: f"{next_s}{sym}{sym}{sym}",  # VIII
            9: f"{sym}{two_next_s}",        # IX
        }
        return formats[n]

    def to_roman_reversed(n):
        result = ""
        for exp in reversed(range(4)):
            val = int(n / 10 ** exp)
            n = n - 10 ** exp * val
            result += RomanNumerals.to_string(val, 10 ** exp)
        return result

    def to_roman_(n):
        result = ""
        for exp in range(4):
            val = n % (10 ** (exp + 1))
            n = n - val
            tmp = RomanNumerals.to_string(val / 10 ** exp, 10 ** exp)
            result = tmp + result
        return result

    def to_roman(n):
        # print("*"* 10, n)
        if n > RomanNumerals.MAX_VAL:
            print(f"val: {n} exceded MAX_VAL: {RomanNumerals.MAX_VAL}")
            return "?"
        result = ""
        for k, v in reversed(RomanNumerals.ROMAN_VAL.items()):
            if n == 0:
                break
            if str(v)[0] == "5":
                continue
            x = int(n / v)
            result += RomanNumerals.to_string(x, v)
            n = n - v * x
        return result

    def to_roman_old(n):
        remaing = n

        thousands = int(remaing / 10 ** 3)
        remaing = remaing - 10 ** 3 * thousands

        hundreds = int(remaing / 10 ** 2)
        remaing = remaing - 10 ** 2 * hundreds

        tens = int(remaing / 10 ** 1)
        remaing = remaing - 10 ** 1 * tens

        units = int(remaing / 10 ** 0)
        remaing = remaing - 10 ** 0 * units
        # print(f"final renaming: {remaing}   {remaing} == {0}")

        r = (
            RomanNumerals.to_string(thousands, 10 ** 3) +
            RomanNumerals.to_string(hundreds, 10 ** 2) +
            RomanNumerals.to_string(tens, 10 ** 1) +
            RomanNumerals.to_string(units, 10 ** 0) +
            ""
        )
        print(r)
        return r

    def from_roman(val_str):
        result = 0
        prev_val = 0
        for i in reversed(val_str):
            val = RomanNumerals.ROMAN_VAL.get(i, 0)
            if val < prev_val:
                val = -val
            prev_val = val
            result += val
        return result

    def to_roman_alternativs(num):
        conversions = OrderedDict([
                                ('X̅',10000),
                                ('MX̅',9000), ('V̅',5000),('MV̅',4000), ('M',1000),
                                ('CM',900), ('D', 500), ('CD',400), ('C',100),
                                ('XC',90), ('L',50), ('XL',40),('X',10),
                                ('IX',9), ('V',5), ('IV',4), ('I',1)])
        out = ''
        for key, value in conversions.items():
            while num >= value:

                out += key
                num -= value
        return out

    def __init__(self):
        print("test_RomanNumerals")
        self.test_RomanNumerals()

    def test_RomanNumerals(self):

        assert RomanNumerals.to_roman(1000) == 'M'
        assert RomanNumerals.to_roman(2000) == 'MM'
        assert RomanNumerals.to_roman(3000) == 'MMM'

        assert RomanNumerals.to_roman(4000) == 'MV̅'
        assert RomanNumerals.to_roman(5000) == 'V̅'
        assert RomanNumerals.to_roman(6000) == 'V̅M'
        assert RomanNumerals.to_roman(9000) == 'MX̅'


        assert RomanNumerals.to_roman(4) == 'IV' #  , '4 should == "IV"')
        assert RomanNumerals.to_roman(1) == 'I' #  , '1 should == "I"')
        assert RomanNumerals.to_roman(9) == 'IX' #  , '1 should == "I"')
        assert RomanNumerals.to_roman(1990) == 'MCMXC' #  , '1990 should == "MCMXC"')
        assert RomanNumerals.to_roman(2008) == 'MMVIII' #  , '2008 should == "MMVIII"')



        assert RomanNumerals.from_roman('XXI') == 21 #  , 'XXI should == 21')
        assert RomanNumerals.from_roman('I') == 1 #  , 'I should == 1')
        assert RomanNumerals.from_roman('IV') == 4 #  , 'IV should == 4')
        assert RomanNumerals.from_roman('MMVIII') == 2008 #  , 'MMVIII should == 2008')
        assert RomanNumerals.from_roman('MDCLXVI') == 1666 #  , 'MDCLXVI should == 1666')

RomanNumerals()

class HashtagGenerator:
    """ The Hashtag Generator
    Hashtag Generator!

    Here's the deal:

        It must start with a hashtag (#).
        All words must have their first letter capitalized.
        If the final result is longer than 140 chars it must return false.
        If the input or the result is an empty string it must return false
    """
    def __init__(self):
        print("HashtagGenerator")
        self.test_generate_hashtag()

    @staticmethod
    def generate_hashtag(text):
        return HashtagGenerator.get_hashtag(text)

    def get_hashtag_(text):
        result = "".join([w.strip().capitalize() for w in text.split()])
        if result == "" or len(result) > 140:
            return False
        return "#" + result
    
    def get_hashtag(text):
        result = "#"
        for w in text.split():
            result += w.strip().capitalize()
        if result == "#" or len(result) > 140:
            return False
        return result

    def test_generate_hashtag(self):
        assert self.generate_hashtag('Codewars') ==  '#Codewars' #  'Should handle a single word.')
        assert self.generate_hashtag('') == False #  'Expected an empty string to return False')
        assert self.generate_hashtag('Do We have A Hashtag')[0], '#' #  'Expeted a Hashtag (#) at the beginning.')
        assert self.generate_hashtag('    Codewars      ') ==  '#Codewars' #  'Should handle trailing whitespace.')
        assert self.generate_hashtag('Codewars      ') ==  '#Codewars' #  'Should handle trailing whitespace.')
        assert self.generate_hashtag('Codewars Is Nice') ==  '#CodewarsIsNice' #  'Should remove spaces.')
        assert self.generate_hashtag('codewars is nice') ==  '#CodewarsIsNice' #  'Should capitalize first letters of words.')
        assert self.generate_hashtag('CodeWars is nice') ==  '#CodewarsIsNice' #  'Should capitalize all letters of words - all lower case but the first.')
        assert self.generate_hashtag('c i n') ==  '#CIN' #  'Should capitalize first letters of words even when single letters.')
        assert self.generate_hashtag('codewars  is  nice') ==  '#CodewarsIsNice' #  'Should deal with unnecessary middle spaces.')
        assert self.generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False #  'Should return False if the final word is longer than 140 chars.')

HashtagGenerator()

class PrimeFactors:
    """
    A natural number is called k-prime if it has exactly k prime factors, 
    counted with multiplicity.
    A natural number is thus prime if and only if it is 1-prime.
    
    Examples:
        k = 2 -> 4, 6, 9, 10, 14, 15, 21, 22, …
        k = 3 -> 8, 12, 18, 20, 27, 28, 30, …
        k = 5 -> 32, 48, 72, 80, 108, 112, …

    Given an integer k and a list arr of positive integers the function consec_kprimes 
    returns how many times in the sequence arr numbers come up twice in a row with exactly k prime factors?

        consec_kprimes(4, arr) => 3 because 
        10005 - 10030 are consecutive 4-primes, 
        10030 - 10026 too as well 
        10028 - 10004 
        but 
        10008 - 10016 are 6-primes.
 
   
   """
    def prime_factors(n):
        primes_count = 0
        c = 2
        while n > 1:
            if not n % c: # n % c == 0
                primes_count += 1
                n //= c  # n = n / c
            else:
                c += 1
        return primes_count

    def consec_kprimes(k, arr):
        result = 0
        prev_count = 0
        for n in arr:
            primes_count = PrimeFactors.prime_factors(n)
            if prev_count == primes_count == k:
                result += 1
            prev_count = primes_count
        return result

    def consec_kprimes(k, arr):
        kprimes = [PrimeFactors.prime_factors(n) for n in arr]
        result = sum(k == kprimes[i] == kprimes[i+1] for i in range(len(arr)-1))
        result = sum(k == kprimes[i] == kprimes[i-1] for i in range(1, len(arr)))
        return result


    def __init__(self) -> None:
        print("TestPrimeFactors")
        self.test_prime_factors()
        self.test_consec_kprimes()
        pass

    def test_prime_factors(self):
        # Driver code
        assert PrimeFactors.prime_factors(2) == 1
        assert PrimeFactors.prime_factors(3) == 1
        assert PrimeFactors.prime_factors(4) == 2
        assert PrimeFactors.prime_factors(5) == 1
        assert PrimeFactors.prime_factors(6) == 2
        assert PrimeFactors.prime_factors(7) == 1
        assert PrimeFactors.prime_factors(8) == 3

        assert PrimeFactors.prime_factors(10005) == 4
        assert PrimeFactors.prime_factors(10030) == 4
        assert PrimeFactors.prime_factors(10026) == 4
        assert PrimeFactors.prime_factors(10008) == 6
        assert PrimeFactors.prime_factors(10016) == 6
        assert PrimeFactors.prime_factors(10028) == 4
        assert PrimeFactors.prime_factors(10004) == 4

    def test_consec_kprimes(self):
        assert PrimeFactors.consec_kprimes(4, [10005, 10030, 10026, 10008, 10016, 10028, 10004]) == 3
        assert PrimeFactors.consec_kprimes(3, [10158, 10182, 10184, 10172, 10179, 10168, 10156, 10165, 10155, 10161, 10178, 10170]) ==  5
        assert PrimeFactors.consec_kprimes(2, [10110, 10102, 10097, 10113, 10123, 10109, 10118, 10119, 10117, 10115, 10101, 10121, 10122]) ==  7
        assert PrimeFactors.consec_kprimes(2, [10123, 10122, 10132, 10129, 10145, 10148, 10147, 10135, 10146, 10134]) ==  2
        assert PrimeFactors.consec_kprimes(6, [10176, 10164]) ==  0
        assert PrimeFactors.consec_kprimes(1, [10182, 10191, 10163, 10172, 10178, 10190, 10177, 10186, 10169, 10161, 10165, 10181]) ==  0

PrimeFactors()


import collections
class Scramblies:
    """
    Complete the function scramble(str1, str2)
    that returns true if a portion of str1 characters can be rearranged to match str2,
    otherwise returns false.

    Notes:
    Only lower case letters will be used (a-z).
    No punctuation or digits will be included.
    Performance needs to be considered.
    """
    def scramble(s1, s2):
        # print(f"{s1=} {s2=}")
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)
        for letter, count2 in c2.items():
            count1 = c1[letter]
            # print(f"\t{letter=} {count1=} {count2=}")
            if count2 > count1:
                return False
        return True

    def scramble(s1, s2):
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)
        for letter, count2 in c2.items():
            if count2 > c1[letter]:
                return False
        return True

    def scramble(s1, s2):
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)

        fail = sum(1 for letter, count2 in c2.items() if count2 > c1[letter])
        return not fail

    def scramble(s1, s2):
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)
        x = c2 - c1
        print(x)
        print(len(x))
        return len(c2 - c1) == 0

    def scramble(s1, s2):
        # return     all(s1.count(x) >= s2.count(x) for x in set(s2))
        return not any(s1.count(x) <  s2.count(x) for x in set(s2))


    print("Scramblies")

    for s1, s2, expected in [
        
            ('rkqodlw', 'world', True),
            ('katas', 'steak', False),
            ('aa', 'aa', True),
            ('ax', 'aaa', False),
            ('hurmsujsxqdjin', 'jdsxxhrnqi', False),
            ('aaaabbbccc', 'abc', True),
            ('abc', 'cba', True),

            ('cedewaraaossoqqyt', 'codewars', True),
            ('scriptjava', 'javascript', True),
            ('scriptingjava', 'javascript', True)
    ]:
        assert scramble(s1, s2) == expected

Scramblies()

from itertools import combinations
class Travel1:
    """
    John and Mary want to travel between a few towns A, B, C ...
    Mary has on a sheet of paper a list of distances between these towns. 
    ls = [50, 55, 57, 58, 60]. 
    John is tired of driving and he says to Mary that 
    he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

    Which distances, hence which towns, 
    they will choose so that the sum of the distances is the biggest possible to please Mary and John?

    Example:
    With list ls and 3 towns to visit they can make a choice between:
    [50,55,57],
    [50,55,58],
    [50,55,60],
        [50,57,58],
        [50,57,60],
            [50,58,60],
    
    [55,57,58],[55,57,60],[55,58,60],[57,58,60].

    The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

    The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

    The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters
        t (maximum sum of distances, integer >= 0), 
        k (number of towns to visit, k >= 1) a
        nd ls (list of distances, all distances are positive or zero integers and this list has at least one element).
        
        The function returns the "best" sum ie the biggest possible sum of k distances 
        less than or equal to the given limit t, if that sum exists, 
        or otherwise nil, null, None, Nothing, depending on the language. 
        In that case with C, C++, D, Dart, Fortran, F#, Go, Julia, Kotlin, Nim, OCaml, Pascal, Perl, PowerShell, Reason, Rust, Scala, Shell, Swift return -1.

    Examples:
    ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

    xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)

    ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

    Notes:
    try not to modify the input list of distances ls
    in some languages this "list" is in fact a string (see the Sample Tests).
    """

    print("Travel1")
    def choose_best_sum(max_distance, num_towns, ls_dist):
        best_dist = 0
        combinations_k = combinations(ls_dist, num_towns)
        for combination_k in combinations_k:
            dist = sum(combination_k)
            if dist <= max_distance and dist > best_dist:
                best_dist = dist
        if best_dist == 0:
            return None
        return best_dist

    def choose_best_sum(max_distance, num_towns, ls_dist):
        x = max((sum(d) for d in combinations(ls_dist, num_towns) if sum(d) <= max_distance), default=None)
        x = max((s for s in (sum(d) for d in combinations(ls_dist, num_towns)) if s <= max_distance), default=None)
        # print(x)
        return x
 
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

    assert choose_best_sum(2333, 1, xs) == 2333
    assert choose_best_sum(2433, 2, xs) == 2433
    assert choose_best_sum(230, 4, xs) == 230
    assert choose_best_sum(430, 5, xs) == 430
    assert choose_best_sum(430, 8, xs) == None

Travel1()

from collections import Counter
import re
class MostFrequentlyWords:
    """
    DESCRIPTION:
    Write a function that, given a string of text (possibly with punctuation and line-breaks),
    returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

    Assumptions:
    - A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
    - Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
    - Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
    - Matches should be case-insensitive, and the words in the result should be lowercased.
    - Ties may be broken arbitrarily.
    - If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
    
    Examples:

    top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
    # => ["e", "ddd", "aa"]

    top_3_words("  //wont won't won't")
    # => ["won't", "wont"]

    Bonus points (not really, but just for fun):
    Avoid creating an array whose memory footprint is roughly as big as the input text.
    Avoid sorting the entire array of unique words.
    """

    def top_3_words(text):
        words = re.findall(r"[a-z']+", text.lower())
        counts = Counter(words)
        to_remove = [word for word in counts.keys() if len(re.findall(r"[a-z]+", word)) == 0]
        [counts.pop(word) for word in to_remove]
        top_words = [word for word, _ in counts.most_common(3)]
        return top_words

    def top_3_words(text):
        # words = re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower()))
        words = re.findall(r"'*[a-z][a-z']*", text.lower())
        counts = Counter(words)
        top_words = [word for word, _ in counts.most_common(3)]
        return top_words
    
    print("MostFrequentlyWords")
    assert top_3_words("  //wont     won't     won't ") ==  ["won't", "wont"]
    assert top_3_words("y'l'owmiw   t'amadfs") == ["y'l'owmiw", "t'amadfs"]
    assert top_3_words("E") ==  ["e"]
    assert top_3_words("  , e   .. ") ==  ["e"]
    assert top_3_words("  ...  ") ==  []
    assert top_3_words("  '  ") ==  []
    assert top_3_words("  '''  ") ==  []

MostFrequentlyWords()

class RangeExtraction:
    """
    Range Extraction

    A format for expressing an ordered list of integers is to use a comma separated list of either individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.

    The range includes all integers in the interval including both endpoints.
    It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

    Complete the solution so that it takes a list of integers in increasing order
    and returns a correctly formatted string in the range format.
    solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
    Example:
    """

    def get_range_01(args_raw):
        elements = []
        range_count = 0
        args = sorted(args_raw)
        args.append(args_raw[0] - 1) # add an element at the end that will break any range
        for i in range(len(args) -1):
            #print(f"\t {i=} p={args[i-1]} n={args[i]}")
            if args[i+1] - args[i] == 1:
                #print(f"\t\t  increment")
                if range_count == 0:
                    start_range_k = args[i]
                range_count += 1
            else:
                #print(f"\t\t  no increment")
                if range_count > 1: 
                    elements.append(f"{start_range_k}-{args[i]}")
                    #print(f"\t\t\t  finish range add: {elements[-1]}")
                else:
                    if range_count == 1:
                        elements.append(f"{args[i-1]}")
                        #print(f"\t\t\t  i-1 add: {elements[-1]}")
                    elements.append(f"{args[i]}")
                    #print(f"\t\t\t   add: {elements[-1]}v********")
                range_count = 0

        return ",".join(elements)

    def get_range_02(args_raw):
        elements = []
        start_range_i = 0
        args = sorted(args_raw)
        args.append(None) # add an element at the end that will break any range
        # print(args)
        for i in range(len(args) -1):
            #print(f"\t{i}: {args[i+1]} {args[i]}   {args[start_range_i]}")
            if args[i+1] != args[i] + 1:
                #rint(f"\t\t  no increment", end=" ")
                if i - start_range_i > 1:
                    #elements.append(f"{args[i+1]}")
                    #print(f"\t\t\t  finish range add: {elements[-1]}")
                    #print("range")
                    elements.append(f"{args[start_range_i]}-{args[i]}")
                else:
                    #print("simple", end=" ")
                    if i - start_range_i == 1:
                        #print("add prev")
                        elements.append(f"{args[start_range_i]}")
                    elements.append(f"{args[i]}")
                    #print()
                    #print(f"\t\t\t   add: {elements[-1]}v********")
                start_range_i = i + 1


        return ",".join(elements)

    def get_range_03(arr):
        elements = []
        b = arr[0] # inital element
        a = arr[0] # start_range_k
        #for n in arr[1:] + [b -1]:
        for n in arr[1:] + [None]:
            if n != b + 1:
            #if n - b != 1:  # break range
                e = f"{b}" if a == b else "{}{}{}".format(a, "," if a+1 == b else "-", b)
                if a == b: # simple
                    e = f"{b}"
                    pass
                else:
                    if a + 1 == b:
                        e = f"{a},{b}"
                    else:
                        e = f"{a}-{b}"
                    pass 
                elements.append(e)
                a = n # start a new range
            b = n
        return ",".join(elements)

    def test_range_extraction():
        print("RangeExtraction test")
        test_data = {
            "1-3": [1, 2, 3],
            "1,3,5": [1, 3, 5],
            "1-3,5": [1, 2, 3, 5],
            "1,3-5": [1, 3, 4, 5],
            "1-3": [1, 2, 3],
            '-6,-3-1': [-6,-3,-2,-1,0,1],
            "-3--1,2,10,15,16,18-20": [-3,-2,-1,2,10,15,16,18,19,20],
            '-6,-3-1,3-5,7-11,14,15,17-20': [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20],
        }
        get_range_fun_list = [
            RangeExtraction.get_range_01,
            RangeExtraction.get_range_02,
            RangeExtraction.get_range_03,
        ]
        for get_range_fun in get_range_fun_list:
            # print(f"{get_range_fun}")
            for expected, input in test_data.items():
                result = get_range_fun(input)
                if expected != result:
                    print(f"  result: {result}")
                    print(f"expected: {expected}")
                assert expected == result

RangeExtraction.test_range_extraction()

class HumanReadableDurationFormat:
    """
   function which formats a duration, given as a number of seconds, in a human-friendly way.

    The function must accept a non-negative integer. 
    If it is zero, it just returns "now". 
    Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

    It is much easier to understand with an example:

        * For seconds = 62   return  "1 minute and 2 seconds"
        * For seconds = 3662 return  "1 hour, 1 minute and 2 seconds"
    """

    def format_01(seconds):
        if seconds == 0:
            return "now"

        time_elem = [
            ("year", 365 * 24 * 60 * 60),
            ("day", 24 * 60 * 60),
            ("hour", 60 * 60),
            ("minute", 60),
            ("second", 1),
        ]

        elements = []
        for name, value in time_elem:
            qty = seconds // value
            if qty == 0:
                continue
            # seconds = seconds % value
            seconds -= value * qty
            elements.append(f"{qty} {name}" + ("s" if qty > 1 else ""))

        if len(elements) == 1:
            result = f"{elements[-1]}"
        else:
            result = f", ".join(e for e in elements[0:-1]) +  f" and {elements[-1]}"

        return result

    def test():
        print("HumanReadableDurationFormat test")
        data = {
            0: "now",
            1: "1 second",
            2: "2 seconds",
            60: "1 minute",
            3600: "1 hour",
            62: "1 minute and 2 seconds",
            120: "2 minutes",
            3662: "1 hour, 1 minute and 2 seconds",
            86400: "1 day",
            2 * 86400: "2 days",
            365 * 24 * 60 * 60: "1 year",
        }
        format_fun_list = [
            HumanReadableDurationFormat.format_01,
            #HumanReadableDurationFormat.format_02,
        ]

        for format_fun in format_fun_list:
            for input, expected in data.items():
                result = format_fun(input)
                if result != expected:
                    print(f"{input=}")
                    print(f"{result=}")
                    print(f"{expected=}")
                assert result == expected

HumanReadableDurationFormat.test()


class CountTheDigit:

    def nb_dig(n, d):
        from collections import Counter
        r = 0
        for k in range(n + 1):
            count = Counter(str(k ** 2))
            r += count[str(d)]
        return r

    def nb_dig_01(n, d):
        return sum(str(k ** 2).count(str(d)) for k in range(n+1))

    def testCountTheDigit():

        functions_list = [
            CountTheDigit.nb_dig,
            CountTheDigit.nb_dig_01,
        ]

        test_data = [
            [(10, 1), 4],
            [(25, 1), 11],
            [(5750, 0), 4700],
            [(11011, 2), 9481],
            [(12224, 8), 7733],
            [(11549, 1), 11905],
        ]

        for fun in functions_list:
            for input, expected in test_data:
                result = fun(*input)
                if result != expected:
                    print(input, expected, result)
                assert result == expected

        print("CountTheDigit tested")

CountTheDigit.testCountTheDigit() 

class countSheeps:

    def count_sheeps_01(sheep_array):
        # return sum(1 for ship in sheep_array if ship is True)
        return sheep_array.count(True)


    def test():
        function_list  = [
            countSheeps.count_sheeps_01,
        ]

        test_data = [
            [0, [False]],
            [0, [False, None]],
            [0, [False, False]],
            [1, [True]],
            [1, [True, False]],
            [2, [True, True]],
            [2, [True, True]],
            [2, [True, True, False]],
            [2, [True, True, False, False]],
        ]

        for fun in function_list:
            for expected, input in test_data:
                result = fun(input)
                assert result == expected
        print("countSheeps tested")

countSheeps.test()

class ReverseWords:
    """
    Reverse every other word in a given string, then return the string. 
    Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. 
    Punctuation marks should be treated as if they are a part of the word in this kata.
    """
    def reverse_alternate_01(input):
        words = []
        reverse = False
        for w in input.split():
            if reverse:
                w = w[::-1]
            words.append(w)
            reverse = not reverse
        return " ".join(words)

    def reverse_alternate_02(input):
        words = input.split()
        for i in range(1, len(words) + 1, 2):
            words[i] = words[i][::-1]
        # iterator[start:stop:step]
        # words[1::2] = [word[::-1] for word in words[1::2]]
        return " ".join(words)


    def reverse_alternate_03(input):
        # words = []
        # for i, w in enumerate(input.split()):
        #     w = w[::-1] if i % 2 else w
        #     words.append(w)
        # return " ".join(words)
        return " ".join([w[::-1] if i % 2 else w for i, w in enumerate(input.split())])

    def test():
        function_list  = [
            ReverseWords.reverse_alternate_01,
            ReverseWords.reverse_alternate_02,
            ReverseWords.reverse_alternate_03,
        ]

        # for input, expected 
        test_data = [
            ("123 123 abc abc", "123 321 abc cba"),
            ("Reverse this string, please!", "Reverse siht string, !esaelp"),
            ("I really don't like reversing strings!","I yllaer don't ekil reversing !sgnirts"),
        ]

        for fun in function_list:
            for input, expected in test_data:
                result = fun(input)
                if not result == expected:
                    print(result)
                    print(expected)
                assert result == expected
        
        # map try 1: simple, one function, many imputs
        # result = map(ReverseWords.reverse_alternate_01, test_data)
        # doesn't work because test_data[i] = (input, expected)
        # not so clear if there will be a mismatch since the assert is in a list
        inputs = [val[0] for val in test_data]
        expected_values = [val[1] for val in test_data]
        for fun in function_list:
            results = list(map(fun, inputs))
        assert expected_values == results

        print("ReverseWords tested")

ReverseWords.test()

class SudokuValidator:

    def valid_solution_01(input):
        valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for row in input:
            if valid != sorted(row):
                return False

        for col in zip(*input):
            if valid != sorted(col):
                return False

        # validate blocks  
        for x in range(3):
            three_rows = input[x * 3 : 3 + x * 3 ]
            for y in range(3):
                block = [row[y * 3 : 3 + y * 3] for row in three_rows]
                flat_block = [item for sublist in block for item in sublist]

                # block1 = []
                # for row in three_rows:
                #     block1 += row[y * 3 : 3 + y * 3]

                if valid != sorted(flat_block):
                    return False
    
        return True

    def valid_solution_02(input):
        """ using np
        """
        import numpy as np
        input_np = np.array(input)

        valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # validate blocks  
        i = 0
        for x in range(3):
            for y in range(3):
                # validate blocks
                if not valid == sorted(input_np[3 * x: 3 * (x +1) , 3 * y: 3 * (y +1)].flatten()):
                    return False

                # validate col
                if not valid == sorted(input_np[i, :]):
                    return False

                 # validate rows
                if not valid == sorted(input_np[:, i]):
                    return False

                i += 1

        return True

    def valid_solution_03(input):
        valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
        
            # validate rows
            row = input[i][:]
            if valid != sorted(row):
                return False


            # validate columns
            col = [row[i] for row in input]
            if valid != sorted(col):
                return False

        # validate blocks  
        for x in range(3):
            three_rows = input[0 + 3 * x : 3 + 3 * x]
            for y in range(3):
                block = [row[0 + 3 * y: 3 + 3 * y] for row in three_rows]
                flat_block = [item for sublist in block for item in sublist]
                if valid != sorted(flat_block):
                    return False
    
        return True

    def test_validator():
        print("SudokuValidator test")

        funtion_list = [
            SudokuValidator.valid_solution_01,
            SudokuValidator.valid_solution_02,
            SudokuValidator.valid_solution_03,
        ]
    
        test_data = (
            (True, [
                [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ]),

            (False, [
                [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 0, 3, 4, 9],
                [1, 0, 0, 3, 4, 2, 5, 6, 0],
                [8, 5, 9, 7, 6, 1, 0, 2, 0],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 0, 1, 5, 3, 7, 2, 1, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 0, 0, 4, 8, 1, 1, 7, 9],
            ]),
    
            (True, [
                [1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]
            ]),

            (False, [
                 [1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]
            ]),

            (False, [
                [1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 0, 3, 7, 5]
                ,[7, 0, 6, 3, 8, 0, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 0, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 0, 8, 4, 6]
                ,[9, 8, 0, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 0, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 0, 6, 4, 2, 1, 3, 5]
            ]),

            (False, [
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
                ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
                ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
                ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
                ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
                ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
                ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
                ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
                ,[9, 1, 2, 3, 4, 5, 6, 7, 8]
            ]),
        )

        for funtion in funtion_list:
            for expected, input in test_data:
                result = funtion(input)
                if result != expected:
                    print(f"{result=} {expected=}")
                    [print(l) for l in input]
                assert result == expected

SudokuValidator.test_validator()


class MSE:
    """ Mean Square Error
    """

    def solution01(array_a, array_b):
        # s = 0
        # for a, b in zip(array_a, array_b):
        #     s += (a - b) ** 2
        # r =  s / len(array_a)
        # return r
        return sum((a - b) ** 2 for a, b in zip(array_a, array_b)) / len(array_a)

    def solution02(array_a, array_b):
        from statistics import mean
        return mean((a - b) ** 2 for a, b in zip(array_a, array_b))
  
    def solution03(array_a, array_b):
        from statistics import mean
        return mean((array_a[i] - array_b[i]) ** 2 for i in range(len(array_a)))

    def solution11(array_a, array_b):
        import numpy as np
        # return (np.square(np.array(array_a) - np.array(array_b))).mean()
        # return np.square(np.subtract(array_a, array_b)).mean()
        # return ((np.array(array_a) - np.array(array_b)) **2 ).mean()
        return (np.subtract(array_a, array_b) ** 2).mean()

    def solution21(array_a, array_b):
        import pandas as pd
        return ((pd.DataFrame(array_a) - pd.DataFrame(array_b)) ** 2).mean()[0]

    def test():
        test_data = [
            (9, ([1,2,3], [4,5,6])),
            (16.5, ([10, 20, 10, 2], [10, 25, 5, -2])),
            (1, ([0, -1], [-1, 0])),
            (0, ([10, 10], [10, 10])),
            ]

        functions = [
            MSE.solution01,
            MSE.solution02,
            MSE.solution03,
            MSE.solution11,
            MSE.solution21,
        ]

        for funtion in functions:
            for data in test_data:
                expected, arrays = data
                result = funtion(*arrays)
                if expected != result:
                    print(f"{result=} {expected=} {arrays=}")
                assert expected == result

        print("MSE test")


MSE.test()