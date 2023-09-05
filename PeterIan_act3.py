name= input ('Type your name:')
math= input ('Input your Math grade:')
sci= input ('Input your Science grade:')
eng= input ('Input your English grade:')
ave= (float(math)+float(sci)+float(eng))/3
print ('Math:',math +' Science:',sci +' English:',eng +' Your average is:', ave)
if ave>=75:
    print('Congratulations',name +', You passed:',ave)
elif ave<=74:
    print('Unfortunately',name + ', You failed:',ave