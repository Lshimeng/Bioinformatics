import os
os.chdir("/home/lshimeng/work/ugt/12/tree/blast/")
from Bio import SeqIO
from Bio.Blast import NCBIWWW
import time
SeqNumber = 0
for record in SeqIO.parse("12.seq", "fasta"):
    SeqNumber += 1
    try:
        result_handle = NCBIWWW.qblast("blastp", "pdb", record.seq)
        save_file = open('xml\\'+str(SeqNumber)+'.xml', 'w')
        save_file.write(result_handle.read())
        save_file.close()
        print (SeqNumber,' OK!')
    except:
        print (SeqNumber,' Error! Will try again later!')
        time.sleep(60)
        SeqNumber -=1
print ("Done!")