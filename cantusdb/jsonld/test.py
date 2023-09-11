from pyld import jsonld
import json

        
tested = {
        "volpiano": "1---km-ok-kjh-k-nmlkij--lkjh-jkjk---km-ok-kjh-k--nmlkj-lkjh--jkjk---khk-mlk-m-nno-ponmlk-lmk-hjk---k-m-nno-ponmlk--lnk-hjk-lk7---k-m-nno-po-rqpo-pnm-nno-po-onm-o-pmlk-k-llm-ok-nmlkij--lk---khg-k--mlk-m-nno-po-onmlk--lnl--hjk--lk-h-jK--lk---k-m-nno--om-nnonmlkj--l-lln-onlk-ml77---hijk---lnk-hjk-onmlk-hjkkJ--lk---khg-hg-hhk-lk--o-k-llm-nlk-kkJ--lk--hijk---k---km-onm--oq-rq-rqpo-pnm-o-k-llm-nlkl7-hjkkJ--lk---k-llm-okIjh-k--nmlkj--l-lln-onlkij--lk---hjk-lk---m-nno-po-mno---rpop---mno--km-nlk---khk--mlkj-lk--hijk---omo-pro-srqpo-pro--mno7--po---o-k-llm--o-k-llm-nlk--l-hjk---k---mnlk--lhijk--lk---khk--lk-ml-llnmlk-kkJ--lk--k---oml-o-po---o-ooq-rq-srqpo--pro-po-o--k-llm-nlk7--lk---k-llm---ml---nmlk-lk--hijk---k-llm--nmlkj-klm--ok-nm---nlk-lk--hijk---k--lm--nml--m---3---oknnm---opo-rqpo--k-llm-nlk--lijk7--lk---o-k-llm-nlk-lk--opo-rqpo-po-srqpo-pro-mno-opo-rqpo-o-ppq-rpo-pro-mno-ok-mnlk-lnk-lk--hijk---lk--k---4",
        "@context": "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/cantusdb/jsonld/context.jsonld",
        "@id": "chant:588586",
        "@type": "wd:Q23072435",
        "database": "cantusdb:",
        "P86": "wdt:Q4233718",
        "P1922": "Ave Maria o auctrix vitae ",
        "P136": "wd:Q604748",
        "Q731978": "wd:None",
        "Q4484726": "C",
        "source": "src:588309"
    }
with open('./expanded.json','w') as injson:
    injson.write(json.dumps(jsonld.expand(tested), indent=2))