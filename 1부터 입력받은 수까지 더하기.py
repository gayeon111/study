Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input("숫자를 입력하시오"))
숫자를 입력하시오100
>>> s=0
>>> for i in range(1,n):
	s=s+i

	
>>> prnt(s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    prnt(s)
NameError: name 'prnt' is not defined
>>> print(s)
4950
>>> 