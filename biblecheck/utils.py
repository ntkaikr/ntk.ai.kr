# utils.py (필요하면 나중에 분리 가능)
def find_testament_and_section(book_name):
    for testament, sections in BIBLE_STRUCTURE.items():
        for section, books in sections.items():
            if book_name in books:
                return testament, section
    return None, None
