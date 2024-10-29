import psutil
import tkinter as tk

# Función para mostrar la información en una ventana
def mostrar_informacion(info):
    ventana = tk.Tk()
    ventana.title("Información del Sistema")

    etiqueta = tk.Label(ventana, text=info, padx=10, pady=10)
    etiqueta.pack()

    ventana.mainloop()

# Información de la CPU
cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq(percpu=True)

info_cpu = ""
for cpu, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    info_cpu += f"CPU {cpu} - Frecuencia del Núcleo: {freq.current} MHz, Uso de CPU: {percent}%\n"

# Información de la memoria virtual
virtual_memory = psutil.virtual_memory()
info_memoria_virtual = f"\nInformación de la Memoria Virtual:\nTotal: {virtual_memory.total / (1024 ** 3): .2f} GB\n"\
                       f"Usado: {virtual_memory.used / (1024 ** 3): .2f} GB\n"\
                       f"Libre: {virtual_memory.free / (1024 ** 3): .2f} GB"

# Información de la red
net_io = psutil.net_io_counters()
info_red = f"\nInformación de la Red:\nBytes recibidos: {net_io.bytes_recv}\nBytes enviados: {net_io.bytes_sent}"

# Información de la temperatura
try:
    temperatures = psutil.sensors_temperatures()
    info_temperatura = "\nInformación de la Temperatura:\n"
    for name, entries in temperatures.items():
        info_temperatura += f"{name}: {', '.join([f'{entry.current}°C' for entry in entries])}\n"
except AttributeError:
    info_temperatura = "\nInformación de la Temperatura no disponible."

# Información de la batería (para laptops)
try:
    battery = psutil.sensors_battery()
    info_bateria = "\nInformación de la Batería:\n"
    if battery.power_plugged:
        info_bateria += f"Estado: Conectado, Porcentaje de Batería: {battery.percent}%"
    else:
        info_bateria += "Estado: No Conectado"
except AttributeError:
    info_bateria = "\nInformación de la Batería no disponible."

# Información del disco
disk = psutil.disk_usage('/')
info_disco = f"\nInformación del Disco:\nTotal de Espacio en Disco: {disk.total / (1024 ** 3): .2f} GB\n"\
              f"Espacio en Disco Usado: {disk.used / (1024 ** 3): .2f} GB\n"\
              f"Espacio en Disco Libre: {disk.free / (1024 ** 3): .2f} GB"

# Concatenar toda la información
informacion_completa = info_cpu + info_memoria_virtual + info_red + info_temperatura + info_bateria + info_disco

# Mostrar la información en una ventana
mostrar_informacion(informacion_completa)
