def presenteer(totaal,a={}):
    for key,value in a.items():
        print(f'{key} : {value} euro')
    print('==========================')
    print(f'totaal : {totaal} euro')