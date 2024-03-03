def word_count_memo(document, memos):
    copy_memos = memos.copy()
    if document not in copy_memos:
        copy_memos[document] = word_count(document)
        return word_count(document), copy_memos
    else: 
        return copy_memos[document], copy_memos
    


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
