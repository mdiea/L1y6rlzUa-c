# 
# git clone https://github.com/mdiea/L1y6rlzUa-c.git
# cd L1y6rlzUa-c
# git clone https://github.com/mdiea/jds6600_python.git
#
from jds6600_python.jds6600 import jds6600
import time

j = jds6600('COM12')

j.getAPIinfo_version()
j.getAPIinfo_release()

j.getinfo_devicetype()
j.getinfo_serialnumber()

j.getinfo_waveformlist()

j.setfrequency(1,0,0)
j.setfrequency(1,0.0,0)
j.setchannelenable(True,False)
time.sleep(5)
j.setfrequency(1,0.499929,0)
time.sleep(10)
j.setfrequency(1,0.509929,0)
time.sleep(10)

j.setfrequency(1,1.500000,0)
time.sleep(10)
j.setfrequency(1,1.510000,0)
time.sleep(10)

j.setfrequency(1,9.50000,0)
time.sleep(10)
j.setfrequency(1,10.510000,0)
time.sleep(10)

j.setfrequency(1,99.50000,0)
time.sleep(10)
j.setfrequency(1,100.510000,0)
time.sleep(10)

j.setfrequency(1,990.50000,0)
time.sleep(10)
j.setfrequency(1,1000.510000,0)
time.sleep(10)

j.setfrequency(1,9900.50000,0)
time.sleep(10)
j.setfrequency(1,10000.510000,0)
time.sleep(10)

j.setfrequency(1,99000.50000,0)
time.sleep(10)
j.setfrequency(1,100000.510000,0)
time.sleep(10)

j.setfrequency(1,990000.50000,0)
time.sleep(10)
j.setfrequency(1,1000000.510000,0)
time.sleep(5)


j.setfrequency(1,5000000,0)
time.sleep(5)
j.setfrequency(1,5200000,0)
time.sleep(5)
j.setfrequency(1,5400000,0)
time.sleep(5)
j.setfrequency(1,5600000,0)
time.sleep(5)
j.setfrequency(1,5800000,0)
time.sleep(5)
j.setfrequency(1,6000000,0)
time.sleep(5)
j.setfrequency(1,6100000,0)
time.sleep(5)
j.setfrequency(1,6200000,0)
time.sleep(5)
j.setfrequency(1,6300000,0)
time.sleep(5)
j.setfrequency(1,6400000,0)
time.sleep(5)
j.setfrequency(1,6500000,0)
time.sleep(5)
j.setfrequency(1,0,0)
j.setchannelenable(False,False)
j.disconect()

