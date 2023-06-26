class Solution:
    def romanToInt(self, s: str) -> int:
        nums = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
#        s = str(input('Type Roman numerals:'))
        eye = s.find('I')
        x = s.find('X')
        cee = s.find('C')
        count = 0
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
 #       for x in s:
   #         repeat = s.count(x)
        if 'C' in s and 'M' in s:
            if s.find('C',s.index('C')) - s.find('M',s.index('C')) == -1:
                count += 900
                s.replace('CM','',1)
        elif 'C' in s and 'D' in s:
            if s.find('C',index('C')) - s.find('D',s.index('C')) == -1:
                count += 400
                s.replace('CD','',1)
        elif 'X' in s and 'C' in s:
            if s.index('X') - s.find('C',s.index('X')) == -1:
                count += 90
                s.replace('XC','',1)
        elif 'X' in s and 'L' in s:
            if s.index('X') -s.find('L',s.index('X')) == -1:
                count += 40
                s.replace('XL','',1)
        elif 'I' in s and 'X' in s:
            if s.index('I') - s.find('X',s.index('I')) == -1:
                count += 9
                s.replace('IX',"",1)                                               
        elif 'I' in s and 'V' in s:
            if s.index('I') - s.find('V',s.index('I')) == -1:
                count += 4
                s.replace('IV',"",1)
        for i in s:
            if i in roman:
                count += roman[i]
                s = list(s)
                s.remove(i)
                elem = enumerate(s)
                print(elem)
        if len(s) <= 1 or len(s) >= 15:
            print('too long input')
        for val in s:
            if val in nums:
                return true
            return False
        if count >= 3999 or count <1:
            print('your numeral is too high, has to be between 1 and 3999')
        return count
