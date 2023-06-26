class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if len(s) < 1 or len(s) > 15:
            return False
        if 'C' in s and 'M' in s:
            if s.find('C',s.index('C')) - s.find('M',s.index('C')) == -1:
                count += 900
                s = s.replace('CM','',1)
        if 'C' in s and 'D' in s:
            if s.index('C') - s.find('D',s.index('C')) == -1:
                count += 400
                s = s.replace('CD','',1)
        if 'X' in s and 'C' in s:
            if s.index('X') - s.find('C',s.index('X')) == -1:
                count += 90
                s = s.replace('XC','',1)
        if 'X' in s and 'L' in s:
            if s.index('X') -s.find('L',s.index('X')) == -1:
                count += 40
                s = s.replace('XL','',1)
        if 'I' in s and 'X' in s:
            if s.index('I') - s.find('X',s.index('I')) == -1:
                count += 9
                s = s.replace('IX',"",1)                                               
        if 'I' in s and 'V' in s:
            if s.index('I') - s.find('V',s.index('I')) == -1:
                count += 4
                s = s.replace('IV',"",1)
        for i in s:
            if i in roman:
                count += roman[i]
        for val in s:
            if val not in roman:
                return False
        if count > 3999 or count < 1:
            print('your numeral is too high, has to be between 1 and 3999')
            return False
        return count
            return False
        if count >= 3999 or count <1:
            print('your numeral is too high, has to be between 1 and 3999')
        return count
