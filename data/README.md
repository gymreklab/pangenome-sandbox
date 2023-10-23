# Download data sources

Reference pangenomes/assembly info

```
# Minigraph cactus
wget -P /data/ https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/filtered/hprc-v1.0-mc-grch38-maxdel.10mb.gfa.gz

# Minigraph
wget -P /data/ https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph/hprc-v1.0-minigraph-grch38.gfa.gz

# PGR-tk version
wget -P /data https://giab-data.s3.amazonaws.com/PGR-TK-Files/pgr-tk-HGRP-y1-evaluation-set-v0.tar
tar xvf /data/pgr-tk-HGRP-y1-evaluation-set-v0.tar
```

# Reference genomes

```
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/CHM13/assemblies/analysis_set/chm13v2.0.fa.gz
wget https://hgdownload.cse.ucsc.edu/goldenpath/hg38/bigZips/hg38.fa.gz
```