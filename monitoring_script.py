import psutil
import os
import sys
import argparse

import email, smtplib, ssl
import io
import urllib.request

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



print('Do you want enter threshold parameters? (yes/no)')
x = input()
if x == 'yes':
    print('Please enter threshold parameters for load CPU in %:')
    a = int(input())
    print('Please enter threshold parameters for load RAM in %:')
    b = int(input())
    print('Please enter threshold parameters for load DISK in %:')
    c = int(input())

    with open('module_for_script.py', 'w') as file:
        file.write('cpu_percent=' + str(a) + '\n' + 'ram_percent=' + str(b) + '\n' + 'disk_percent=' + str(b))
        file.close()
    import module_for_script
else:
    import module_for_script
    print('Okay, threshold parameters for CPU is',module_for_script.cpu_percent,'%, for RAM is',module_for_script.ram_percent,'%, for DISK is',module_for_script.disk_percent,'%.')
def main():
    count = 0

#    print('Load Average stats:', get_loadaverage())
    print('CPU usage is', get_cpu_usage_pct(),'%.')
    print('RAM usage is', (get_ram_usage_pct()), '%, it is', (get_ram_usage()), 'MB of total',
          (get_ram_total()), 'MB.')
    print('Disk usage is', (get_disk_usage_pct()), '%, free disk space is', (get_disk_free()), 'MB, of',
          (get_disk_total()), 'MB.')

    if get_cpu_usage_pct() > module_for_script.cpu_percent:
        print('WARNING: CPU usage more than',module_for_script.cpu_percent,'%')
        count+=1
    if get_ram_usage_pct() > module_for_script.ram_percent:
        print('WARNING: MEMORY usage more than',module_for_script.ram_percent,'%')
        count+=1
    if get_disk_usage_pct() > module_for_script.disk_percent:
        print('WARNING: DISK usage more than',module_for_script.disk_percent,'%')
        count+=1

    if count > 0:
        print('try to send message')
        mailer()



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


def mailer():



    message = MIMEMultipart("alternative")
    message["Subject"] = "Warning"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """<html>
Hello, DISK usage {link}%, CPU usage {link2}%, RAM usage {link3}%!
</html>
""".format(link=module_for_script.disk_percent, link2=module_for_script.cpu_percent, link3=module_for_script.ram_percent)



    part2 = MIMEText(html, "html")

    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

if __name__ == "__main__":
    main()


