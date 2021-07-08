lst1=[1,2,3,4]
lst2=[5,6,7]
lst_dict = {}


for k,v in zip(lst1,lst2):
    lst_dict[k]=v
print(lst_dict)