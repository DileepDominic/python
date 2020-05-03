
#Unpacking to multiple variables
a,b = 1,2

print("a", a)
print("b", b)

#Unpacking complex data types
student = ['Dominic',2011, ['Chemistry','Physics','Mathematics'] , (80,85,94) , 123456 ]
name, batch , subjects , marks , rollumber = student

print("name",name)
print("subjects",subjects)

#Throw away variables
student2 = ['Dominic',2011, ['Chemistry','Physics','Mathematics'] , (80,85,94) , 123456 ]
name2, _ , subjects2 , marks2 , _ = student2

print(marks2)




