class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeoiuAEOIU'
        li = {}
        for i in range(len(s)):
            if s[i] in vowels:
                li[i] = s[i]
        newli = list(li.values())[::-1]
        new = dict(zip(li.keys(), newli))

        li_s = list(s)

        for i in range(len(li_s)):
            if i in new:
                li_s[i] = new[i]

        return "".join(li_s)
