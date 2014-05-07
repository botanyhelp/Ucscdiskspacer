"""Program to report total size, in bytes, of UCSC genome browser databases
It is useful to estimate how large the databases are before you download: 

rsync -azvP rsync://hgdownload.cse.ucsc.edu/mysql/danRer5/ /var/mysql/danRer5/

Requires subprocess
Requires rsync binary on PATH

Use it like this for a zebrafish and human assembly:

python ucsc_disk_spacer.py danRer5 hg19
THIS COMMAND:
rsync -avn rsync://hgdownload.cse.ucsc.edu/mysql/danRer5/|grep 'total size'| grep 'speedup' |sed 's/total size is //'| sed 's/  speedup.*//'
...REPORTS THIS MANY BYTES OF SIZE:
18775824111
THIS COMMAND:
rsync -avn rsync://hgdownload.cse.ucsc.edu/mysql/hg19/|grep 'total size'| grep 'speedup' |sed 's/total size is //'| sed 's/  speedup.*//'
...REPORTS THIS MANY BYTES OF SIZE:
386958877717
THESE ASSEMBLIES:
danRer5
hg19
TOTAL THIS AMOUNT:
405734701828
"""
import os
import sys
import subprocess
assembly_list = []
total_size = 0
size_list = []
for arg in sys.argv[1:]:
    assembly_list.append(arg)
    rsync_fragment = "rsync -avn rsync://hgdownload.cse.ucsc.edu/mysql/" + arg + "/|grep 'total size'| grep 'speedup' |sed 's/total size is //'| sed 's/  speedup.*//'"
    print("THIS COMMAND:")
    print(rsync_fragment)
    p = subprocess.Popen(rsync_fragment, shell=True, stdout=subprocess.PIPE)
    print("...REPORTS THIS MANY BYTES OF SIZE:")
    output = p.stdout.readlines()
    for line in output:
        print line.strip()
        size_list.append(line.strip())

total_size = 0
for size_item in size_list:
    total_size += int(size_item)
print("THESE ASSEMBLIES:")
for assembly in assembly_list:
    print(assembly)
print("TOTAL THIS AMOUNT:")
print(total_size)
