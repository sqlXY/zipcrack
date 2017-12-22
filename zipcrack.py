import zipfile
import argparse
import Queue
import threading
import os
import time

class crack(threading.Thread):    
    def __init__(self, zipfile, queue, flag):  
        super(crack, self).__init__()
        self._z = zipfile 
        self._q = queue
        self._flag = flag

    def run(self):
        while self._flag[0] != True and not self._q.empty():
            password = self._q.get()
            try:
                self._z.extractall(pwd = str(password))
                print '[+] zip password is %s' % (password)
                self._flag[0] = True
                break
            except Exception as e:
                pass

def listToQueue(plist):
    q = Queue.Queue()
    for i in plist:
        q.put(i.strip('\n'))
    return q

def crackMain(zfile, passfile, threads):
    flag = [False]
    zfile = zipfile.ZipFile(zfile)
    with open(passfile, 'r') as pf:
        passQ = listToQueue(pf.readlines())
        
    for i in range(threads):
        th = crack(zfile, passQ, flag)
        th.setDaemon(True)  
        th.start()

    maxqsize = passQ.qsize()
    while not passQ.empty():
        size = maxqsize - passQ.qsize()
        _ = int(maxqsize/50) if int(maxqsize/50) > 1 else 1
        if size % _ == 0:
            print '[*] processing [%d/%d]' % (size, maxqsize)

    time.sleep(1)
    if flag[0] == False:
        print '[*] Unfortunately, did not crack it.'


def main():
    parser = argparse.ArgumentParser(description = "This program is used to crack the zip file password.")
    parser.add_argument('--zipfile', '-z', required = True, help = "required a zipfile")
    parser.add_argument('--dictionary', '-d', required = True, help = "required a dictionary")
    parser.add_argument('--threads', '-t', required = False, default = 10, help = "input your crack threads(default 10)")

    args = parser.parse_args()

    if not os.path.exists(args.zipfile):
        print '[-] zip file path error.'
        return
    if not os.path.exists(args.dictionary):
        print '[-] dictionary file path error.'
        return
    if not zipfile.is_zipfile(args.zipfile):
        print '[-] file is not a zip file.'
        return
    
    crackMain(args.zipfile, args.dictionary, int(args.threads))


if __name__ == '__main__':
    main()
