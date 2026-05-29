"""persistent injection into sqlite"""
from ingest import load_faq_data
import os
from pathlib import Path

def build_index_persistent(documents):
    index = TextSearchIndex(
        text_fields=['question', 'section', 'answer'],
        keyword_fields=['course'],
        db_path=Path(__file__).resolve().parent.parent / 'database' / 'faq.db'
    )

    for doc in docs_llm:
        index.add(doc)
        print(f'Added: {doc["question"][:60]}...')
        time.sleep(0.5)
        return index

