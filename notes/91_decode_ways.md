### Question

![alt text](Question91.PNG)

### [Initial idea](91_decode_ways.md#appendix)

Loop through the string and look for possible ways of decoding:
  - if digit > 2: only one possible way of decoding
  - if digit = 2: one possibility if the following digit is 0 or >= 7; two possibilities if the following digit is 1 ~ 6 
  - if digit = 1: one possibility if the follwoing digit is 0; two possibilities otherwise
  - if digit = 0: unless 0 is following 1 or 2, we should return 0 as there's no way of decoding
  
Can ultilize recursion to calculate number of possibilities for the rest of the string.

**Issue**

 - It's hard to stop when we encounter invalid "0"s in betweeen.
 - Recursion is not necessary / feasible to implemented since the whole string can be invalid

### Improved idea

We will use string with length equals to `len(s) + 1` to keep counting the possibilities. 


### Appendix

Python code for the initial idea:

```Python
class Solution:
    def numDecodings(self, s):
        if "0" in s:
            idx = s.index("0")
            if idx == 0 or s[idx-1] == "0" or s[idx-1] > "2":
                return(0)
        
        if len(s) < 1 or s[0] == "0":
            return(0)
        elif len(s) == 1:
            return(1)
        elif len(s) == 2:
            if s < "27" and s != "10" and s != "20":
                return(2)
            else:
                return(1)
        else:
            answer = 0
            if s[0] == "0":
                answer = self.numDecodings(s[1:])
            elif s[0] == "1":
                if s[1] == "0":
                    answer += self.numDecodings(s[2:])
                else:
                    answer += self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            elif s[0] == "2":
                if s[1] == "0":
                    answer += self.numDecodings(s[2:])
                elif s[1] < "7":
                    answer += self.numDecodings(s[1:]) + self.numDecodings(s[2:])
                elif s[1] >= "7":
                    answer += self.numDecodings(s[1:])
            else:
                answer += self.numDecodings(s[1:])
            return(answer)
```
