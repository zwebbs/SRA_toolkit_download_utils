# File Name
# Created By:
# Created On:
# Purpose: Automate downloads of FASTQ files from NCBI SRA

import argparse
import subprocess


# Function Definitions
#---------------------

def prefetch_fastq(sra_numbers, extra_args=None):
    # loop through the SRA numbers and prefetch them each in 
    # an independent subprocess call
    for sra_id in sra_numbers:
        prefetch_cmd = f"prefetch {sra_id} {extra_args}"
        print (f"Currently Downloading: {sra_id}")
        print(f"The Command Was: {prefetch_cmd}")
        subprocess.call(prefetch_cmd, shell=True)
    return

def extract_fastq_from_srafile(sra_numbers, input_path="~/ncbi/public/sra/",
        output_dir="fastq/", extra_args=None):
    # loop through the SRA numbers and unpack the downloaded FASTQs from their
    # corresponding .sra files. also uses independent subprocess calls
    for sra_id in sra_numbers:
        sra_filepath = f"{input_path}{sra_id}.sra" 
        fasterq_dump_cmd = f"fasterq-dump --outdir {output_dir} {extra_args} {sra_filepath}" 
        print(f"Currently Unpacking: {sra_id}")
        print(f"The Command Was: {fasterq_dump_cmd}")
        subprocess.call(fasterq_dump_cmd, shell=True)


# Main Execution
#----------------

if __name__ == "__main__":
    pass




