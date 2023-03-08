import csv
import os
import time
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, 'rows_300.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['№', 'Дата и время', 'Секунда', 'Микросекунда'])
    
    for i in range(1, 301):
        now = datetime.now()
        sec = now.second
        microsec = now.microsecond
        
        writer.writerow([i, now, sec, microsec])
        time.sleep(0.01)

        
csvfile.close()