astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)
astr = '123'
try:
    istr = int("ee")
except Exception as e:
    print(e)
print('Second', istr)