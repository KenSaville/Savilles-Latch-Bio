# Savilles Latch Bio
 Repo of Latch Bio workflows

 First workflow is called snipflow.

 The goal of this wf is to

 1.  Download a genome file from genbank as fasta using efectch.  initially this will be used for viral genomes, using ebola as an example.
 2.  download a sequencing project from SRA  of new ebola isolates to find variants, using fasterq-dump
 3. align sequences using bwa  
4. find variants usinf bcf tools
5. result in vcf file that can be loaded to IGV to visualize variants.

above will be registered with latch bio as a workflow.

The basic command line code for this is based on code from the biostar handbook by Istvan Albert

https://www.biostarhandbook.com/
