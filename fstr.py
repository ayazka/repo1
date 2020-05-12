ipaddr = '10.1.1.1'
oct1, oct2, oct3, oct4 = ipaddr.split('.')
print(f'{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}')
