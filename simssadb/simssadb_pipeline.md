# SimssaDB flattening and json-ld structures

> Summary:  
>   1. Upload SQL dump to local postgreSQL database
>   2. With output run `flattening/SQL_query.py`
>   3. Reconcile with OpenRefine
>   4. With output run `flattening/restructure.py`
>   5. With output run `jsonld/generate_jsonld.py `(which also takes `jsonld/context.jsonld` as the initial context)

## 1. Extracting columns and feature flattening
I was provided with an SQL dump . I then wrote a python script [SQP_query.py](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/flattening/SQL_query.py) to query the data dump and generate the initial flattened csv [file](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/flattening/initial_flattened.csv). I also performed flattening of the extracted features under this file. Note that each row represents a file. We later found out that the desired entity is a musical_work (which can be associated with multiple files), and is reflattened in step 3.

## 2. Reconciliation with OpenRefine
I performed OpenRefine reconciliation. You can see the reconciled file [here](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/reconciled_WikiID.csv)
The following is a list of reconciled columns:
- genre_style
- genre_type
- file_format
- contributor_full_name (composer)
  

## 3. Reconcile column names and generating json-ld
Currently the json-ld is generated as follow:  
In [`restructure.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/flattening/restructure.py):
- filter where contributor is composer
- get the first 1000 entries
- flattened/pivot to have each entry be musical work instead of files
- Create [final_flattened.csv](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/flattening/final_flattened.csv)



In [`generate_jsonld.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/generate_jsonld.py):
- convert short_rec.csv to json documents 
- Loop through each json document and edit each entry, creating the compact jsonld. Each json document is a musical work, and the files are listed as nested json documents in a list. More information can be found in [`generate_jsonld.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/generate_jsonld.py)
  
    **Note:** This is **not optimal**. See in Future Todos entry 2. This approach should create a more uniformed contexts and avoid errors. This should also make the process a lot faster for larger data dumps


- Generate the jsonld file at [`compact.jsonld`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/compact.jsonld)
- The contexts used in the compact.jsonld file is imported from [`context.jsonld`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/context.jsonld)
- Test jsonld and its contexts with PyLD. We use the file [`pyld_test.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/PyLD/pyld_test.py) to use PyLD's expand function to generate [`expanded.json`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/PyLD/expanded.json)


## 4. Future Todos:
1. Cleanup and standardize contexts. Document how contexts must be created for subsequent databases
2. Revert the json-ld process: instead of creating a compact json-ld document and context, try creating an expanded json and use PyLD's compact function to create contexts. This can be done after we agree on the structure of the jsonld file
3. Restructure the pipeline -> we should push flattening of the musical_work_id to the top of the pipeline for more easy to understand and manage code.