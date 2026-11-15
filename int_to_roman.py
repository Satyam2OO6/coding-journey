roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
class Solution():
    def int_to_roman(self,num):
        result = ""
        for values,symbol in roman:
            while num>=values:
                result +=symbol
                num -=values


        return result


obj=Solution()
print(obj.int_to_roman(30))                