import os



### Script to run cazy webscraper
### activate conda environment 'webscraper'


the_strain = "Streptomyces clavuligerus DSM 738"
your_email = "andreas.lawaetz@strath.ac.uk"
### build cazy database
### only by strain
# os.system(f'cazy_webscraper --strain "{the_strain}" {your_email} --db_output strep_clav.db')
### or genus
the_genus = 'Streptomyces'
# os.system(f'cazy_webscraper --genera "{the_genus}" {your_email} --db_output streptomyces.db')

# Download the corresponding genbank protein sequence for each protein in the local CAZy database
# os.system(f'cw_get_genbank_seqs streptomyces.db {your_email} --classes GH')


### extract protein sequences
### Execute command from folder with database
### directories to put fasta files cannot be existing already
fasta_directory = '/Users/andreas/strep_cazy/fasta_dir'
fasta_file_dir = '/Users/andreas/strep_cazy/all_fasta_dir/all.FASTA'
blastdb = '/Users/andreas/strep_cazy/blast_db/cazy_blast.db'
### put all sequences in different fasta files
# os.system(f'cw_extract_db_seqs cazydb.db genbank uniprot --fasta_dir {fasta_directory} --force')
### put all sequences in the same fasta file
# os.system(f'cw_extract_db_seqs strep_clav.db genbank --fasta_file {fasta_file_dir}')
### Make blast database
# os.system(f'cw_extract_db_seqs cazydb.db genbank --blastdb {blastdb}')
### Extract sequences belonging to certain class
# output_dir = '/Users/andreas/strep_cazy/GH_dir/GH.FASTA'
# os.system(f'cw_extract_db_seqs strep_clav.db genbank --classes GH --fasta_file {output_dir}')
# output_dir = '/Users/andreas/strep_cazy/GH_CE_dir/GH_CE.FASTA'
# os.system(f'cw_extract_db_seqs strep_clav.db genbank --classes GH,CE --fasta_file {output_dir}')
### extract GH13 families
output_dir = '/Users/andreas/strep_cazy/GH13_dir/GH13.FASTA'
os.system(f'cw_extract_db_seqs strep_clav.db genbank --families GH13 --fasta_file {output_dir}')