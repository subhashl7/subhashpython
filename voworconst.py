#subbu#vowel or consonant:
yy=raw_input()
if((yy>='a' and yy<='z') or (yy>='A' and yy<='Z')):
         if (yy in ['a','e','i','o','u','A','E','I','O','U']):
                 print('Vowel')
         else:
                 print('Consonant')
else:
	print('invalid')
  
