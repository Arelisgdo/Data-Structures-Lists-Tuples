def replace_in_list(mi_lista, idx, elemento):
    if idx < 0 or idx >= len(mi_lista):
        return mi_lista
    mi_lista[idx] = elemento
    return mi_lista
