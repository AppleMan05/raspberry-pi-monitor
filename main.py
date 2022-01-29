import psutil
import subprocess
from pushbullet import Pushbullet


pb = Pushbullet("")
#print(pb.devices)
dev = pb.get_device('')


temperature = psutil.sensors_temperatures()['cpu_thermal'][0][1]
ram_used = psutil.virtual_memory()[2]
cpu_usage = psutil.cpu_percent(1)


processName = 'smbd'
listOfProcessObjects = []
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name'])
        if processName.lower() in pinfo['name'].lower() :
            listOfProcessObjects.append(pinfo)
    except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
        pass


dev.push_note("Temperature summary", f"Temperature={temperature}\nRAM used={ram_used}%\nCPU usage={cpu_usage}%")
dev.push_note("SMB status", f"Connected clients = {len(listOfProcessObjects) - 2}")
