# LinkedMusic Data Lake

Pipeline to extract, clean, flatten, merge, and reconcile database data. You can find specifications and instructions for each database in the subdirectories, in `<database>_pipeline.md`.

Currently there is no central orchestration script for each database, as in you will have to run each scripts separately (up to 3-4 scripts per database, instructions in each subdirectory). This will be implemented as more automation is introduced in the data reconciliation step. 