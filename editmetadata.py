import argparse
import pyexiv2

def clearallmetadata(imgname, preserve):
    metadata = pyexiv2.ImageMetadata(imgname)
    metadata.read()
    metadata.clear()
    metadata.write(preserve)
def modifymode(imgname, preserve):
    metadata = pyexiv2.ImageMetadata(imgname)
    metadata.read()
    for key, value in metadata.iteritems():
        print key, value.raw_value
    modkey = raw_input("key to modify (q to quit):")
    while not modkey == 'q':
        print "Editing : "+str(metadata[modkey].raw_value)
        modvalue = raw_input("New value: (q to quit):")
        if modvalue == "q":
            break
        metadata[modkey].raw_value = str(modvalue)
        modkey = raw_input("key to modify (q to quit):")
    metadata.write(preserve)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img", help="image file to manipulate")
    parser.add_argument("--clear","-c",help="clear all meta data",action="store_true")
    parser.add_argument("--preserve","-p",help="preserve iamge mdifiod date ",action="store_true")
    args = parser.parse_args()
    if args.img:
        if args.clear:
            clearallmetadata(args.img, args.preserve)
        else:
            modifymode(args.img,args.preserve)
    else:
        print parser.usage

if __name__=='__main__':
    main()