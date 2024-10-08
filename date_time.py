""""
Author:Abhirami
date:08-10-24
"""

from datetime import datetime
from http.cookiejar import cut_port_re

current_time=datetime.now()
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
format2=current_time.strftime("%m/%d/%Y")
format3=current_time.strftime("%A,%B %d,%Y")
format4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
format5=current_time.strftime("%a-%b-%d %H:%M:%S %Z %Y")
format6=current_time.strftime("%a-%b-%d %H:%M:%S %Z %Y")
format7=current_time.isoformat()
format8=current_time.strftime("%d")
format9=current_time.strftime("%H:%M:%S")
format10=current_time.strftime("%B")
format11=current_time.strftime("%Y")

print(format1)
print(format2)
print(format3)
print(format4)
print(format5)
print(format6)
print(format7)
print(format8)
print(format9)
print(format10)
print(format11)