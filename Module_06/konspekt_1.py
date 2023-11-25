fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)  # 6
fh.close()


fh = open('test.txt', 'w+')
fh.write('Maks!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'Ma'

fh.close()


a = 'hello python'
print(a[-2:2:-2])