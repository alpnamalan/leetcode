### JULY 27, 2025 -- P12: INTEGER TO ROMAN ###

class Solution:
    def intToRoman(self, num: int) -> str:
        # CLEAN VERSION USING HASH TABLE
        M  = ["", "M", "MM", "MMM"] # 1000-3999
        C  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 100-999
        X  = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 10-99
        I  = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1-9

        s = M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
        return s

        # final = ""

        # 1000-3999

        # while num > 999:
        #     final += "M"
        #     num -= 1000

        # 100-999

        # if num > 899:
        #     final += "CM"
        #     num -= 900
        # elif num > 499:
        #     final += "D"
        #     num -= 500
        # elif num > 399:
        #     final += "CD"
        #     num -= 400
        # while num > 99:
        #     final += "C"
        #     num -= 100

        # 10-99

        # if num > 89:
        #     final += "XC"
        #     num -= 90
        # elif num > 49:
        #     final += "L"
        #     num -= 50
        # elif num > 39:
        #     final += "XL"
        #     num -= 40
        # while num > 9:
        #     final += "X"
        #     num -= 10

        # 1-9

        # if num == 9:
        #     final += "IX"
        #     num -= 9
        # elif num > 4:
        #     final += "V"
        #     num -= 5
        # elif num == 4:
        #     final += "IV"
        #     num -= 4
        # while num > 0:
        #     final += "I"
        #     num -= 1
        
        # return final
