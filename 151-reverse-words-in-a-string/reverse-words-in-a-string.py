class Solution:
    def reverseWords(self, s: str) -> str:
      new = " ".join(s.split())
      
      again = new.split()
      again = again[::-1]

      st = ""
      for i in range(len(again)):
        if i == len(again) - 1:
          st += again[i]
        else:
          st = st + again[i] + " "
      return st