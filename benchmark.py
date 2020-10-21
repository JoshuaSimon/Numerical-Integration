import subprocess
import numpy as np
import matplotlib.pyplot as plt
from time import time

cmd1 = r"D:\\Dokumente\\VS Code\\Visual Basic\\NumericIntegration\\NumericIntegration\\bin\Debug\\NumericIntegration.exe"
cmd2 = r"D:\\Dokumente\\VS Code\\C#\\NumericIntegration\\NumericIntegration\\bin\Debug\\NumericIntegration.exe"
durations = range(1, 500)

#output1 = subprocess.call([cmd1], stdin=None, stdout=None, stderr=None, shell=False)
#output2 = subprocess.call([cmd2], stdin=None, stdout=None, stderr=None, shell=False)

time_vb = []
time_cs = []

for i in durations:
    time_start_vb = time()
    p = subprocess.Popen(args=[cmd1], stdout=subprocess.PIPE, shell=False)
    (output1, err1) = p.communicate()
    p_status = p.wait()
    time_vb.append(time() - time_start_vb)

    time_start_cs = time()
    p = subprocess.Popen(args=[cmd2], stdout=subprocess.PIPE, shell=False)
    (output2, err2) = p.communicate()
    p_status = p.wait()
    time_cs.append(time() - time_start_cs)


time_vb = np.array(time_vb)
time_cs = np.array(time_cs)

print("Mean runtime of VB: ", time_vb.mean())
print("Mean runtime of CS: ", time_cs.mean())

plt.plot(durations, time_vb, label="VB")
plt.plot(durations, time_cs, label="C#")
plt.ylabel("Time in sec")
plt.xlabel("Iteration")
plt.legend()
plt.show()

