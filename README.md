# <ins>Swiss-Prot Parser</ins>

#### <ins>Description:</ins>
This Swiss-Prot Parser is a tool designed to help in extracting specific data entries from protein sequence files ([Swiss-Prot Download](https://www.uniprot.org/help/downloads)). It was developed to assist in my Bachelor's research tasks, enabling quick and efficient data extraction. This tool offers customizable search functionality and the ability to generate output files, making it an invaluable asset for biological data analysis.<br><br>

#### <ins>Features:</ins>
- Extract specific data entries from `.dat.txt` files in the Swiss-Prot format.
- Customizable search across different entry types (e.g., ID, SQ, OH).
- Ability to output results to a specified file.
- User-friendly command-line interface.<br><br>

#### <ins>Installation:</ins>
1. Ensure ```Python``` is installed on your system.
2. No external packages are required for this tool, as it only uses the built-in ```sys``` module, making it lightweight and easy to run.<br><br>

#### <ins>Usage:</ins>
Run the script from the command line by providing the path to the data file, search parameters, and output file path. Here are some examples:

- ```python swiss-prot-parser.py .\data\swissprot.dat.txt -AC Q197F8 .\data\output.dat.txt```
<br>In this example, all entries in which the lines AC contain ```Q197F8``` are returned. As AC is the Accession Number and is unique, only a single entry is returned.
The input file here is ```swissprot.dat.txt``` in the folder ```data```. The entries found are stored in the ```data``` folder under ```output.dat.txt```<br><br>
- ```python swiss-prot-parser.py .\data\swissprot.dat.txt -SQ MASNTV -OH "Aedes vexans" .\data\output.dat.txt```
<br>In this example, all entries are returned that contain the sequence (SQ) MASNTV and whose organism host (OH) is Aedes vexans.<br><br>

#### <ins>Example entry:</ins>
```
ID   002R_IIV3               Reviewed;         458 AA.
AC   Q197F8;
DT   16-JUN-2009, integrated into UniProtKB/Swiss-Prot.
DT   11-JUL-2006, sequence version 1.
DT   30-NOV-2010, entry version 13.
DE   RecName: Full=Uncharacterized protein 002R;
GN   ORFNames=IIV3-002R;
OS   Invertebrate iridescent virus 3 (IIV-3) (Mosquito iridescent virus).
OC   Viruses; dsDNA viruses, no RNA stage; Iridoviridae; Chloriridovirus.
OX   NCBI_TaxID=345201;
OH   NCBI_TaxID=7163; Aedes vexans (Inland floodwater mosquito) (Culex vexans).
OH   NCBI_TaxID=42431; Culex territans.
OH   NCBI_TaxID=332058; Culiseta annulata.
OH   NCBI_TaxID=310513; Ochlerotatus sollicitans (eastern saltmarsh mosquito).
OH   NCBI_TaxID=329105; Ochlerotatus taeniorhynchus (Black salt marsh mosquito) (Aedes taeniorhynchus).
OH   NCBI_TaxID=7183; Psorophora ferox.
RN   [1]
RP   NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA].
RX   PubMed=16912294; DOI=10.1128/JVI.00464-06;
RA   Delhon G., Tulman E.R., Afonso C.L., Lu Z., Becnel J.J., Moser B.A.,
RA   Kutish G.F., Rock D.L.;
RT   "Genome of invertebrate iridescent virus type 3 (mosquito iridescent
RT   virus).";
RL   J. Virol. 80:8439-8449(2006).
CC   -----------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see http://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution-NoDerivs License
CC   -----------------------------------------------------------------------
DR   EMBL; DQ643392; ABF82032.1; -; Genomic_DNA.
DR   RefSeq; YP_654574.1; NC_008187.1.
DR   GeneID; 4156251; -.
PE   4: Predicted;
KW   Complete proteome; Virus reference strain.
FT   CHAIN         1    458       Uncharacterized protein 002R.
FT                                /FTId=PRO_0000377938.
SQ   SEQUENCE   458 AA;  53921 MW;  E46E5C85D7ACA139 CRC64;
     MASNTVSAQG GSNRPVRDFS NIQDVAQFLL FDPIWNEQPG SIVPWKMNRE QALAERYPEL
     QTSEPSEDYS GPVESLELLP LEIKLDIMQY LSWEQISWCK HPWLWTRWYK DNVVRVSAIT
     FEDFQREYAF PEKIQEIHFT DTRAEEIKAI LETTPNVTRL VIRRIDDMNY NTHGDLGLDD
     LEFLTHLMVE DACGFTDFWA PSLTHLTIKN LDMHPRWFGP VMDGIKSMQS TLKYLYIFET
     YGVNKPFVQW CTDNIETFYC TNSYRYENVP RPIYVWVLFQ EDEWHGYRVE DNKFHRRYMY
     STILHKRDTD WVENNPLKTP AQVEMYKFLL RISQLNRDGT GYESDSDPEN EHFDDESFSS
     GEEDSSDEDD PTWAPDSDDS DWETETEEEP SVAARILEKG KLTITNLMKS LGFKPKPKKI
     QSIDRYFCSL DSNYNSEDED FEYDSDSEDD DSDSEDDC
//
```