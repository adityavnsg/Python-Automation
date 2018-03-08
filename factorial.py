import re
class Factorial:
    def facto(self):
        fac_num = input("enter any number")
        regex= '[a-zA-Z]'
        pattern=re.compile(regex)
        if(pattern.search(fac_num)):
          print("you entered string value\n")
        else:
          fac_num = int(fac_num)
        if(type(fac_num) is int):
            temp = fac_num
            sum=1
            for i in range(1,temp+1):
              sum=sum*i
            print(sum)
        else:
            print('enter only number\n')
           
FactObj = Factorial()
FactObj.facto()
