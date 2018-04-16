import sys
import xml
import xml.etree.ElementTree as ET
import StringIO

def main():

    if len(sys.argv) != 2 or not sys.argv[1].endswith('.ivy'):
        print 'usage: {} <file>.ivy'.format(sys.argv[0])

    inpname = sys.argv[1]
    outname = inpname[:-3]+'md'

    try: 
        with open(inpname) as f:
            content = f.readlines()
    except IOError:
        print 'file {} not found'.format(inpname)
        exit(1)

    try:
        outf = open(outname,'w')
    except:
        print 'could not open {} for output'.format(outname)


    with outf:
        for line in content[1:]:
            if line.strip().startswith('#'):
                comment = '#'.join(line.split('#')[1:])
                if comment.startswith(' '):
                    comment = comment[1:]
                outf.write(comment)
            else:
                outf.write('    '+line)