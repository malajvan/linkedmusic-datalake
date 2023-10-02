# CantusDB flattening and json-ld structures

> Summarize:    
>   1. Reconcile the flattened csv dump
>   2. With the output run `jsonld/generate_jsonld.py`(which also takes `jsonld/context.jsonld` as an input)

I was provided with a csv file of 50 entries of CantusDB (see [here](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/cantusdb_50_chants%20(1).csv))
Since each lines represent a chant_id already, there was no need to flatten like simssadb. 

## 1. Reconciliation with OpenRefine
I performed OpenRefine reconciliation with 3 columns: **genre, mode_name, and composer** (which defaulted to Anonymous since all values of this column is so)
I then generate the csv with the corresponding wikidata IDs in the reconciled cells (see [here](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/cantus_reconciled.csv))
You can use `openrefine/history.json` to apply reconciliation steps and `openrefine/export_template.json` to export the file.  

## 2. Reconcile column names and generating json-ld
Currently the json-ld is generated as follow:
In [`generate_jsonld.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/jsonld/generate_jsonld.py)
- Load the reconciled csv as a dataframe in pandas and convert them to json documents (each corresponds to an entry/line in the csv)
- Loop through each json document and edit each entry, creating the compact jsonld. More information can be found in [`generate_jsonld.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/jsonld/generate_jsonld.py)
  
    **Note:** This is **not optimal**. See in Future Todos entry 2. This approach should create a more uniformed contexts and avoid errors. This should also make the process a lot faster for larger data dumps
- Generate the jsonld file at [`compact.jsonld`](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/jsonld/compact.jsonld)
- The contexts used in the compact.jsonld file is imported from [`context.jsonld`](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/jsonld/context.jsonld)
- Test jsonld and its contexts with PyLD. We use the file [`test.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/jsonld/test.py) to use PyLD's expand function to generate [`expanded.json`](https://github.com/malajvan/linkedmusic-datalake/blob/main/cantusdb/jsonld/expanded.json)
