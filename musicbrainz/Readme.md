# Musicbrainz
Currently under development,
Steps are:
1. Download the data from the api with `data/extract.py`, get `initial_compact.jsonld`
2. get all ids to reconcile with `jsonld/looping-approach/get_ids.py` and get the csv `ids.csv`
3. Reconcile `ids.csv` with OpenRefine (use history script `open_re_history,json`)
4. Export to `extracted_ids.csv` and run `merge_reconciled.py` to generate the final `compact.jsonld`

These code will preserve the existing structure of the jsonld from Musicbrainz and only replace the ids of certain entities to wikidata IDs when necessary.