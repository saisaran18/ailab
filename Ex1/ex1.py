people = [{"name":"Alice" , "age":25 , "city":"New York"},
          {"name":"Bob" , "age":30 , "city":"Los Angeles"},
          {"name":"Charlie" , "age":35 , "city":"Chicago"},
          {"name":"David" , "age":40 , "city":"Houston"},
          {"name":"Eve" , "age":45 , "city":"Phoenix"}
          ]
def bsearch(people,targetn):
    s_people = sorted(people,key=lambda x:x["name"])
    left,right=0,len(s_people)-1
    while left<=right:
        mid=(left+right)//2
        if s_people[mid]["name"]==targetn:
            return s_people[mid]
        elif s_people[mid]["name"]<targetn:
            left=mid+1
        else:
            right=mid-1
    return None
targetn=input("Enter the name that you wanna search:")
result=bsearch(people,targetn)
if result:
    print(f"Found {targetn}:{result}")
else:
    print(f"{targetn} not found in the list")
