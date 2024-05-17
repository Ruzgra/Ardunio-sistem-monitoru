try:
    import serial
except ImportError:
    print('\n\npyserial paketi bulunamadı\n\n')
else:
    from time import sleep
    try:
        from psutil import cpu_percent, virtual_memory, cpu_freq, disk_usage
    except ImportError:
        print('\n\npsutil paketi bulunamadı\n\n')
    try:
        import WinTmp, string
    except ImportError:
        print('WinTmp yok') 
    try:
        from serial import Serial, SerialException
    except ImportError:
        print('serial exept') 
 
    print("Serial port numararsını gir.\n")
    port = str(input('Port numarası: COM'))
    try:
        s = Serial('COM'+port, 9600)
        print('Şuanda çalışıyor'),
        
        while True:
        
            string = 'CPU:' + str(int(cpu_percent())) + '%' ' ' + 'RAM:' + str(int(virtual_memory()[2])) + '%'
            string += '                          '
            string += 'CPU ' + str(int(WinTmp.CPU_Temp())) + 'C' ' '+ 'GPU ' + str(int(WinTmp.GPU_Temp())) + 'C'
            
            string = string.strip()
            s.write(string.encode())
            sleep(1)

    except SerialException:
        print('Serial portu:"' + port + '" bu port bulunamadı veya rededildi.')
        sleep(1)
