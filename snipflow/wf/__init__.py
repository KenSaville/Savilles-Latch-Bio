"""
fetch reference genome using efetch, fastq files  using fastq dump, find snps 
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile, LatchDir


@small_task
def fetch_ref_genome_task(ACC: str) -> LatchFile:
    ''' Get accession number as input and fectch fasta file from ncbi '''

    # A reference to  output.
    ref_file= Path("ref_genome.fa").resolve()
    
    
    # This is from the biostar handbook.  ACC will be input by user on latch.  It is a genbank accession number
    _efetch_cmd = [
        "efetch",
        "-db",
        "nuccore",
        "-format",
        "fasta",
        "-id",
        ACC,
     ]

    # get the string sequence output from efectch
    seq = subprocess.run(_efetch_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')

    # write sequence to a file
    f = open('ref_genome.fa', "w") 
    f.write(seq)
    f.close()

    # return file - will be a=saved to data folder on latch.  is actually displayed as an IGV genome
    # This function worked on console.latch.bio.  But have added the /root/ref_genome.fa.  Need to check to see if this is nessary.
    return LatchFile(str(ref_file), "latch:///ref_genome.fa")

    # still working on this one.  fastq dump returns two files, so will need to return them in a dir.  There is documentation for how to do this in SDK documentation 
    # There's also a github page with info on how to do this.  https://github.com/JLSteenwyk/latch_library
    
@small_task

def fastq_dump(
    SRR : str,  #this should be an SRR referring to an SRA read archive, supplied by user on latch.  For ebola example use "SRR1553500"
    
    ):
    
# SRR = "SRR1553500"  #uncomment to use this SRR    
    _fastq_dump_cmd = [
       "fastq-dump",
       SRR       
     ]

#local_dir = "/root/fastq_files"


    subprocess.run(_fastq_dump_cmd)

    return file_glob("*.fastq", "/root/fastq_outputs")

@workflow
def variant_caller (ACC: str, SRR: str) -> (LatchFile, LatchDir):
    """ Fetch ref genome:  input an accession number, fetch ref genome using efetch.  will use this for snp finding later.
        Input SRR number to Fetch sequencing reads using fastq dump
        coming soon ... align fastq files fto ref genome with bwa, call variants with bcftools
       
    

    markdown header
    ----

    Write some documentation about your workflow in
    markdown here:

    > Regular markdown constructs work as expected.

    
    

    __metadata__:
        display_name: Variant Caller
        author:  
            name: Ken Saville
            email: ksaville@albion.edu
            github:
        repository:
        license:
            id: MIT

    Args:

        ACC:
          Accession number for reference genomeo test ude AF086833
          T
          
          __metadata__:
            display_name: ACC
       
        SRR:
          SRA number for sequencing reads
          to test use SRR1553500
          
          __metadata__:

            display name: SRR
      
    """
    
    return fetch_ref_genome_task(ACC=ACC), fastq_dump(SRR=SRR)
