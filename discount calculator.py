import time
gh=1
print("hello and wellcome to atharva's discount calculator")
while(gh<10):
 gh=gh+1
 time.sleep(3)
 amount=input("please enter amount: ")
 amount=int(amount)
 time.sleep(1)
 discont=input("please enter discount percentage: ")
 discont=int(discont)
 time.sleep(1)
 total=amount*discont/100
 result=amount-total
 print(result)
 time.sleep(3)                                                                                                     
