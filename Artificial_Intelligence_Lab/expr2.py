print("enter any two subject you like from the following-")
print("maths,programming,biology,physics,AI concepts,chemistry")
sub1=input("1st subject-")
sub2=input("2nd subject-")

if sub1=="maths" and sub2=="physics" or sub2=="math" and sub1=="physics":
   print("mechanical engineering")
elif sub1=="chemistry" and sub2=="biology" or sub2=="chemistry" and sub1=="biology":
    print("biotechnology")
elif sub1=="maths" and sub2=="programming" or sub2=="maths" and sub1=="programming":
    print("computer engineering")    
elif sub1=="AI concepts" and sub2=="programming" or sub2=="AI concepts" and sub1=="programming":
    print("artificial intelligence and machine learing engineering")
elif sub1=="maths" and sub2=="programming" or sub2=="maths" and sub1=="programming":
    print("artificial intelligence and data science")
else:
    print("somthing went wrong!!:(")
        
