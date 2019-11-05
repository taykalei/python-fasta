import sys


def read_fasta(filename):
    """
    Read a FASTA format sequence from the named file
    """
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            seq = seq + line
    f.close()
    return seq

if len(sys.argv) <2:
	print ("Need to provide filename as argument")
	exit(1)

print(read_fasta(sys.argv[1]))



# In[ ]:




