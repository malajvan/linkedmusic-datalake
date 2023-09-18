import json

doc = json.loads(open('tunes_naive.json',"r").read())

for rec in doc:
    rec['@id'] = f"tunes:{rec.pop('tune_id')}"
    rec['@type'] = "wd:Q2188189" #musical_work
    rec['P1476'] = rec.pop('tunes_name')
    
    rec['database'] = 'thesession:'
    try:
        rec['P4970'] = rec.pop('aliases_alias')
    except KeyError:
        pass
    rec['@context'] = 'https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/the_session/jsonld/context.json'


    rec['P2550'] = rec.pop('recordings')
    for r in rec['P2550']:
        r['@id'] = f"recordings:{r.pop('recordings_id')}"
        r['@type'] = "wd:Q3302947" #
        try:
            r['P175'] = r.pop('recordings_artist')
            r['P1476'] = r.pop('recordings_recording')
            r['P2635'] = r.pop('recordings_track')
            r['P1545'] = r.pop('recordings_track') # ignoring recordings number
        except KeyError:
            pass
        del r['recordings_number']
    try:
        rec['P9533'] = rec.pop('tune_settings')
        for s in rec['P9533']:
            s['@id'] = f"https://thesession.org/tunes/{rec['@id'].split(':')[1]}#setting{s.pop('tunes_setting_id')}"
            s['@type'] = "wd:Q113899068"
            s['P136'] = f"https://thesession.org/tunes/search?type={s.pop('tunes_type')}"
            s['P3440'] = s.pop('tunes_meter')
            s['P826'] = s.pop('tunes_mode')
            s['P577'] = s.pop("tunes_date").replace(' ','T')
            s['P50'] = s.pop('tunes_username')

    except KeyError:
        pass    
pretty_json = json.dumps(doc, indent=4)
with open('compact.jsonld', 'w') as json_file:
    json_file.write(pretty_json)
