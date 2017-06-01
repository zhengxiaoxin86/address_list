import argparse
data_path = "./address.txt"
parser = argparse.ArgumentParser(description='CLI address book')
parser.add_argument('action',choices=['add', 'show'], default='add', help='add or display address')
parser.add_argument('-n','--name',help='add your name')
parser.add_argument('-p','--phone',help='add your phone')
args = parser.parse_args()
if args.action == 'add':
    if args.name == None:
        parser.error('name is required')
    if args.phone == None:
        parser.error('phone is required')
    r = open(data_path,'a')
    r.write("Name:%s\t Phone:%s\n"%(args.name,args.phone))
    print args.name,args.phone
else:
   print open(data_path,'r').read()
    
