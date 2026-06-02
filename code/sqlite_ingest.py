"""persistent injection into sqlite"""
from ingest import load_faq_data
from sqlitesearch import TextSearchIndex

import os
from pathlib import Path

def build_index_persist_init(documents):
    index = TextSearchIndex(
        text_fields=['question', 'section', 'answer'],
        keyword_fields=['course'],
        db_path=Path(__file__).resolve().parent.parent / 'database' / 'faq.db'
    )

    index.clear()

    index.fit(documents)
    # fit() is used to do full index or initial the index.
    # add() can expand existing index
    index.close()
    return index


