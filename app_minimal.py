# import warnings
# warnings.filterwarnings('ignore')
#
# import os
# import sys
# from django.utils.text import slugify
# import pandas as pd
# from thoipapy.thoipa import parser, get_md5_checksum, run_THOIPA_prediction
# from thoipapy.utils import make_sure_path_exists
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
#         sys.stdout.write("\nprotein name slugified from {} to {}\n".format(input_ser["name"], protein_name))
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