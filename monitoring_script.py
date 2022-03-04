import psutil
import os
import sys


def main():
    print('Load Average stats:', get_loadaverage())
    print('CPU usage is', get_cpu_usage_pct(),'%.')
    print('RAM usage is', (get_ram_usage_pct()), '%, it is', (get_ram_usage()), 'MB of total',
          (get_ram_total()), 'MB.')
    print('Disk usage is', (get_disk_usage_pct()), '%, free disk space is', (get_disk_free()), 'MB, of',
          (get_disk_total()), 'MB.')
    if get_cpu_usage_pct() > 4:
        print('WARNING: CPU ultilization more than 4%')
    if get_ram_usage_pct() > 70:
        print('WARNING: MEMORY ultilization more than 70%')
    if get_disk_usage_pct() > 10:
        print('WARNING: DISK ultilization more than 10%')



def get_ram_usage():
    return psutil.virtual_memory().total - psutil.virtual_memory().available >> 20


def get_ram_total():
    return psutil.virtual_memory().total >> 20


def get_ram_usage_pct():
    return psutil.virtual_memory().percent


def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.5)


def get_disk_usage_pct():
    return psutil.disk_usage('/').percent


def get_disk_free():
    return psutil.disk_usage('/').free >> 20


def get_disk_total():
    return psutil.disk_usage('/').total >> 20


def get_loadaverage():
    return psutil.getloadavg()

if __name__ == "__main__":
    main()


