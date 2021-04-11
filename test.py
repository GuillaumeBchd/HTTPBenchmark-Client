import argparse
import subprocess
import re
import time
from tqdm import tqdm
from datetime import datetime

def url(arg_value):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not regex.match(arg_value):
        raise argparse.ArgumentTypeError
    return arg_value


parser = argparse.ArgumentParser(description="Http benchmarking script that launch the wrk utility.")
parser.add_argument("url", type=url, help="url that we want to test. (exemple: https://google.fr/)")

args = parser.parse_args()

if __name__ == "__main__":

    timer = 30

    start = time.time()
    out = subprocess.Popen(['./wrk', '-t12', '-c400', '-d{}s'.format(timer), args.url],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    
    for i in tqdm(range(timer*100)):
        time.sleep(0.01)

    stdout, stderr = out.communicate()

    now = datetime.now() 
    now = now.strftime("%m-%d-%Y_%H-%M-%S")

    filename = "{}".format(now)

    if stdout:
        print(stdout.decode("utf-8"))
        with open("./out/{}.txt".format(filename), 'w') as f:
            f.write(stdout.decode("utf-8"))
    if stderr:
        print(stderr.decode("utf-8") )
        with open("./out/err_{}.txt".format(filename), 'w') as f:
            f.write(stderr.decode("utf-8"))

