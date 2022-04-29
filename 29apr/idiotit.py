
#Naive approach
#to find index of maximum and
#minimum element in the array.
value_list=[]
#min and max indexes are taken 1st element 
#In some cases list might be a single element
min_ele,max_ele=value_list[0],value_list[0] 
for i in range(1,len(value_list)):
    if value_list[i]<min_ele:
        min_ele=value_list[i]
    if value_list[i]>max_ele:
        max_ele=value_list[i]
print('Minimum Element in the list',value_list,'is',min_ele)
print('Maximum Element in the list',value_list,'is',max_ele)