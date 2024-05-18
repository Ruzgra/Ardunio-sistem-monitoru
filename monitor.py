import sys
import time

try:
    import serial
except ImportError:
    print('Import error: pyserial paketi bulunamadı\n')
    sys.exit(1)

from time import sleep

try:
    from psutil import cpu_percent, virtual_memory, cpu_freq, disk_usage
except ImportError:
    print('Import error: psutil\n')
    sys.exit(1)

try:
    import WinTmp
except ImportError:
    print('Import error: WinTmp\n')
    sys.exit(1)

try:
    from serial import Serial, SerialException
except ImportError:
    print('Import error: Serial, SerialException\n')
    sys.exit(1)

# Define the pages as functions

# Define the row length of the display

row_length = 20 # Constant and known

def System_Info_Page():
    string = f'CPU: {int(cpu_percent())}% RAM: {int(virtual_memory().percent)}%'
    string += ' ' * (row_length - len(string))  # Adjust spaces to align the display
    string += f'CPU {int(WinTmp.CPU_Temp())}C GPU {int(WinTmp.GPU_Temp())}C'
    return string.strip()

def CPU_Freq_Page():
    return f'CPU Frekans: {int(cpu_freq().current)} MHz'.strip()

# Setup
print("Serial port numarasını gir.\n")
port = input('Port numarası: COM')

try:
    s = Serial(f'COM{port}', 9600)
    print('Şuanda çalışıyor')

    # Timer setup
    duration = 5
    start_time = time.time()
    current_page = 0

    # List of page functions
    pages = [System_Info_Page, CPU_Freq_Page]  # Add more functions as needed

    # Program loop
    while True:
        elapsed_time = time.time() - start_time

        if elapsed_time >= duration:
            start_time = time.time()
            current_page = (current_page + 1) % len(pages)

        # Get the current page string and write to serial
        page_string = pages[current_page]()
        s.write(page_string.encode())
        
        sleep(1)

except SerialException:
    print(f'Serial portu: "COM{port}" bu port bulunamadı veya rededildi.')
    sleep(1)
