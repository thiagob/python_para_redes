import psutil
import platform

import schedule
import time
from datetime import datetime

def log_hw_data():
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # Abre o arquivo
    file_object = open('hw_info.log', 'a')
 
    # Adiciona a hora atual no arquivo de texto
    file_object.write(datetime.now().strftime("%H:%M:%S"))
    file_object.write('\r')
 
    # Fecha o arquivo
    file_object.close()

# executa o método uma primeira vez
log_hw_data()

# depois executa o método a cada 10 segundos
schedule.every(10).seconds.do(log_hw_data)


# Mantém o programa execução, do contrário só executaria uma vez
while True:
    schedule.run_pending()
    time.sleep(1)