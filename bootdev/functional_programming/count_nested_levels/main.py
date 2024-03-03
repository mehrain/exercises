def count_nested_levels(nested_documents, target_document_id, level=1):
    levels = level
    for document_id, sub_documents in nested_documents.items():
        if document_id == target_document_id:
            return levels
        else:
            found_level = count_nested_levels(sub_documents, target_document_id, level + 1)
            if found_level != -1:
                return found_level
    return -1






'''
Old version of the function

def count_nested_levels(nested_documents, target_document_id, level=1):
    levels = level
    for document in nested_documents:
        if document != target_document_id:
            levels += 1 
        elif document == target_document_id:
            return levels
        else: 
            return -1
'''