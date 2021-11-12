import os
import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datapath", default = "../dataset/face_cartoon/pa_face", type = str)
    parser.add_argument("--prenum", default = "1", type = str)
    args = parser.parse_args()
    return args

def process(args):
    filelist = os.listdir(args.datapath)
    for file in filelist:
        src_name = os.path.join(args.datapath, file)
        filename = os.path.splitext(file)[0]
        filename = filename.zfill(6)
        filename = args.prenum + filename[1:]
        filetype = os.path.splitext(file)[1]
        dst_name = os.path.join(args.datapath, filename + filetype)
        os.rename(src_name, dst_name)
        


if __name__ == '__main__':
    
    args = arg_parser()
    process(args)  