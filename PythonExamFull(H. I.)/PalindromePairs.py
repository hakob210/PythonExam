class Solution(object):
  def palindromePairs(self, words):
      """
      :type words: List[str]
      :rtype: List[List[int]]
      """
      def is_palindrome(s, start, end):
          while start < end:
              if s[start] != s[end]:
                  return False
              start += 1
              end -= 1
          return True
  
      word_dict = {}
      result = []
  
      for idx in range(len(words)):
          word_dict[words[idx]] = idx
  
      for idx in range(len(words)):
          if words[idx] == "":
              for j in range(len(words)):
                  if idx != j and is_palindrome(words[j], 0, len(words[j]) - 1):
                      result.extend([[idx, j], [j, idx]])
              continue
  
          reversed_word = ''.join(reversed(words[idx]))
  
          if reversed_word in word_dict:
              matching_idx = word_dict[reversed_word]
              if matching_idx != idx:
                  result.append([idx, matching_idx])
  
          for j in range(1, len(reversed_word)):
              if is_palindrome(reversed_word, 0, j - 1) and reversed_word[j:] in word_dict:
                  result.append([idx, word_dict[reversed_word[j:]]])
  
              if is_palindrome(reversed_word, j, len(reversed_word) - 1) and reversed_word[:j] in word_dict:
                  result.append([word_dict[reversed_word[:j]], idx])
  
      return result