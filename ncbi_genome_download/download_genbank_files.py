### This script finds all the taxids from the Actinomycetota taxon
### And then downloads all the Genbank files connected to those taxID's
### ncbi-genome-download can be installed via Github https://github.com/kblin/ncbi-genome-download


import os
import time 

time_start = time.time()

### The gimme_taxa_script is in the ncbi-genome-download folder from Github. Change path accordingly.
gimme_taxa_script = '/Users/andreaslawaetz/Streptomyces/ncbi_genome_download/ncbi-genome-download-master/contrib/gimme_taxa.py'

### Change output_folder to your own device
output_folder = '/Users/andreaslawaetz/Streptomyces/ncbi_genome_download/Actinomycetota/'
os.makedirs(output_folder, exist_ok = True)
output_taxa_file = output_folder + 'Actinomycetota_taxIDs_J.txt'
taxa_name = 'Actinomycetota'

### make txt file with all taxIDs belonging to Actinomycetota
os.system(f'python {gimme_taxa_script} -j -o {output_taxa_file} {taxa_name}')

### download all genbank files with Actinomycetota taxIDs
os.system(f'ncbi-genome-download --taxids {output_taxa_file} -o {output_folder} -P --parallel 8 -r 10 bacteria')

time_end = time.time()

print(f'excecution time: {time_end - time_start} seconds')