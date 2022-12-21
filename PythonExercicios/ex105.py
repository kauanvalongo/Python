def notas(* n, sit=False):
    dic = {}
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['total'] = len(n)
    dic['media'] = sum(n)/len(n)
    if sit:
        if dic['media'] >=7:
            dic['situ'] = 'Situação BOA!'
        elif dic['media'] >= 5:
            dic['situ'] = 'Situação RAZOÁVEL.'
        else:
            dic['situ'] = 'Situação HORRÍVEL!'
    return dic

resp = notas(5.5, 2.3, 6, 3, sit=True)
print(resp)



