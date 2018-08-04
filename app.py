import warnings
warnings.filterwarnings("ignore")
import matplotlib
matplotlib.use('Agg')
import argparse
import os
import sys
import pandas as pd
from django.utils.text import slugify
from thoipapy.thoipa import get_md5_checksum, run_THOIPA_prediction
from thoipapy.utils import make_sure_path_exists
from pathlib import Path
import glob

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

# read the command line arguments
parser = argparse.ArgumentParser()

parser.add_argument("-d",  # "-directory",
                    help=r'Full path to your input directory that contains input csv files. '
                         r'For example "\Path\to\your\file/input" directory containing '
                         r'"input/Q12983.txt" and "input/P13983.txt".')
parser.add_argument("-i",  # "-input_file",
                    help=r'Full path to your input file with name, TMD_seq, and full_seq.'
                         r'E.g. "\Path\to\your\file\Q12983.txt"')
parser.add_argument("-f",  # "-folder",
                    help=r'Path to your output folder.'
                         r'E.g. "D:\data_thoipapy\Predictions"')

if __name__ == "__main__":
    """
    Example input csv file:
    -----------------------

    name,1c17_A
    TMD_seq,AAVMMGLAAIGAAIGIGILG
    full_seq,MENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA
    """
    sys.stdout.write("\nUsage example:\n")
    sys.stdout.write(r"python thoipa.py -i D:\data\Q12983.txt -f D:\data\predictions")
    sys.stdout.write("\n\nOR process every input file in the -d input folder. "
                     "You can specify the output folder. Otherwise, a default 'output' folder will be "
                     "created in the same directory as the input folder. \n")
    sys.stdout.write(r"python thoipa.py -d D:\your\directory\with\input_text_files")
    sys.stdout.write("\n\n")
    sys.stdout.flush()
    # get the command-line arguments
    args = parser.parse_args()

    if "d" in args:
        # process every input file in the args.d input folder
        input_dir = Path(args.d)
        infile_names = glob.glob(os.path.join(input_dir, "*.txt"))
        infile_list = [file for file in infile_names]
        if args.f:
            output_dir = Path(args.f)
        else:
            output_dir = Path(os.path.split(input_dir)[0]).joinpath("output")
            if not output_dir.is_dir():
                os.makedirs(output_dir)
    elif "i" in args:
        # process only a single input file
        infile_list = [Path(args.i)]
    else:
        raise ValueError("Please include either an input directory of files to process (-d directory),"
                         "or an input file (-i D:\data\Q12983.txt), but not both.")

    for input_csv in infile_list:
        # extract name and sequences from input csv
        input_ser = pd.Series.from_csv(input_csv)

        # convert protein_name to file-format-friendly text, without symbols etc, max 20 characters
        protein_name = slugify(input_ser["name"])[0:20]
        if protein_name != input_ser["name"]:
            sys.stdout.write("\nprotein name modified from {} to directory-folder-friendly {}\n".format(input_ser["name"], protein_name))

        input_ser["slugified_name"] = protein_name

        TMD_seq = input_ser["TMD_seq"]
        full_seq = input_ser["full_seq"]

        # predictions_folder = os.path.normpath(args.f)

        # get checksum
        md5 = get_md5_checksum(TMD_seq, full_seq)
        input_ser["md5"] = md5

        # create output directory based on protein name
        # save the original csv
        out_dir = os.path.join(output_dir, protein_name)
        make_sure_path_exists(out_dir)
        input_ser.to_csv(os.path.join(out_dir, "input.csv"))

        run_THOIPA_prediction(protein_name, md5, TMD_seq, full_seq, out_dir)

    sys.stdout.write("copy your files to local directory:\n"
                     "docker container ls --all\n"
                     "docker cp YOUR_THOIPA_CONTAINERID:/app/output/ ./")


#DEPRECATED STUFF RUNNING THOIPA standalone on only a single input file
# # read the command line arguments
# parser = argparse.ArgumentParser()
#
# parser.add_argument("-i",  # "-input_file",
#                     help=r'Full path to your input file with name, TMD_seq, and full_seq.'
#                          r'E.g. "\Path\to\your\file\Q12983.txt"')
# parser.add_argument("-f",  # "-folder",
#                     help=r'Path to your output folder.'
#                          r'E.g. "D:\data_thoipapy\Predictions"')
#
# if __name__ == "__main__":
#     """
#     Example input csv file:
#     -----------------------
#
#     name,1c17_A
#     TMD_seq,AAVMMGLAAIGAAIGIGILG
#     full_seq,MENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA
#     """
#     sys.stdout.write("\nUsage example:\n")
#     sys.stdout.write(r"python thoipa.py -i D:\data\Q12983.txt -f D:\data\predictions")
#     sys.stdout.write("\n\n")
#     sys.stdout.flush()
#     # get the command-line arguments
#     args = parser.parse_args()
#
#     # extract name and sequences from input csv
#     input_csv = args.i
#     input_ser = pd.Series.from_csv(input_csv)
#
#     # convert protein_name to file-format-friendly text, without symbols etc, max 20 characters
#     protein_name = slugify(input_ser["name"])[0:20]
#     if protein_name != input_ser["name"]:
#         sys.stdout.write("\nprotein name modified from {} to directory-folder-friendly {}\n".format(input_ser["name"], protein_name))
#
#     input_ser["slugified_name"] = protein_name
#
#     TMD_seq = input_ser["TMD_seq"]
#     full_seq = input_ser["full_seq"]
#
#     predictions_folder = os.path.normpath(args.f)
#
#     # get checksum
#     md5 = get_md5_checksum(TMD_seq, full_seq)
#     input_ser["md5"] = md5
#
#     # create output directory based on protein name
#     # save the original csv
#     out_dir = os.path.join(predictions_folder, protein_name)
#     make_sure_path_exists(out_dir)
#     input_ser.to_csv(os.path.join(out_dir, "input.csv"))
#
#     run_THOIPA_prediction(protein_name, md5, TMD_seq, full_seq, out_dir)