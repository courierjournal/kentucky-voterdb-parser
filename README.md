# kentucky-voterdatabaseparser
Python script to parse the fixed width voter database file provided by KY SBE. The resulting output file is a properly formatted CSV file with column names that can be used for editing or ingestion into a database.

**Usage:** `python convert.py {FILENAME}.txt`. The resulting output file is `output.csv`. The file provided by the SBE is typically +700MB, parsing may take around 30 seconds.
