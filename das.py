# mydict = {
#     'Suren':9,
#     'Hakob':8,
#     'Hayk':10,
#     'Musho':3
# }
# mydict['Musho'] = 9
# mydict['Ero'] = 1
# mydict['Ero'] = 8
# mydict.pop('Hayk')


# print(mydict)
# print(mydict.keys())
# print(mydict.values())
# print(mydict.get('Hayk'))


# for i in mydict.copy():
#     if i == 'Ero':
#         mydict[i] = -5
#     else:
#         mydict['Ero'] = -10

# print(mydict)

# s = 'a,2,b,5,c,8,a,4,e,11'


# import random
# mydict = {}
# names = ['Liam','Noah','Olivia','Emma','Amelia','Luna','Mateo','Messi','Lucas','Tatev']

# # xndir 1
# for i in names:
#     mydict[i] = random.randint(0,11)
# # xndir 2
# print(sum(mydict.values())/len(mydict))
# print(mydict)
# # xndir 3
# for i in mydict:
#     if mydict[i] >= 5:
#         print(i,mydict[i],'Lav')
#     else:
#         print(i,mydict[i],'Vat')


# mydict = {'Liam':6,
#           'Noah':76,
#           'Olivia':40,
#           'Emma':45,
#           'Amelia':90,
#           'Luna':10
#           }

# name = input('Enter Name: ')
# print(mydict.get(name))

# 


mydict = {
    '.,?!:':1,
    'ABC':2,
    'DEF':3,
    'GHI':4,
    'JKL':5,
    'MNO':6,
    'PQRS':7,
    'TUV':8,
    'WXYZ':9,
    ' ':0
}
text = input('Enter text: ').upper()
tver = ''

for i in text:
    for j in mydict:
        if i in j:
            tver+=(j.index(i)+1)*str(mydict[j])
        break
print(tver)

