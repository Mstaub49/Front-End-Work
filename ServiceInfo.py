import psutil
import time
import datetime

while True:
    print(datetime.datetime.now())
    for proc in psutil.process_iter():
        try:
            pr = proc.as_dict()
            #print(f'{pr["name"]}\t{pr["cpu_percent"]}\t{pr["num_threads"]}\t{" ".join(pr["cmdline"][1:]) if pr["cmdline"] else ""}')
            print(f'{pr["name"]}\t{pr["cpu_percent"]}\t{" ".join(pr["cmdline"][1:]) if pr["cmdline"] else ""}')
        except (OSError, psutil.AccessDenied):
            print(pr.name(), 'ACCESS DENIED')
    print('\n*** Ctrl-C to Exit ***\n\n')
    print(datetime.datetime.now())
    time.sleep(30) # Sleep for 10 Mins
