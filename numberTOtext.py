x = 'abcdefghijklmnopqrstuvwxyz'
tuplee = {}
num = 0
for i in x:
    tuplee[num +1] = i
    num += 1



def numberTOtext(num):
    encoded_text =  num
    encoded_text = encoded_text.split(' ')
    for i in encoded_text :
            if i.isdigit():
                print(tuplee[int(i)], end = '')
            else:
                print(i, end = '')

numberTOtext('16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }')



