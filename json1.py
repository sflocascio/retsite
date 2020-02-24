

# Split the uploaded TXT file into 4 different files

with open('ret.txtrpt') as fo:
    op = ''
    start = 0
    cntr = 1
    for x in fo.read().split("\n"):
        if not x.strip():
            if(start == 1):
                with open(str(cntr) + '.txt', 'w') as opf:
                    opf.write(op)
                    opf.close()
                    op = ''
                    cntr += 1
            else:
                start = 1
        else:
            if (op == ''):
                op = x
            else:
                op = op + '\n' + x
    num_files = cntr - 2
    print(num_files)
    fo.close()