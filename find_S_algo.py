import csv
data=[]
h=[]

def updateHypothesis(x,h):
    if h==[]:
        return x
    
    for i in range(0,len(h)):
        if x[i].upper() != h[i].upper():
            h[i]='?'
    return h
#     print("Hypotheis: ",h)



with open('/kaggle/input/find-s-algorithm-dataset/ws.csv') as csvfile:
    reader = csv.reader(csvfile)
    print("Data:")
    for row in reader:
        data.append(row)
        print(row)
        
if data:
    for x in data:
#         print(x)
        if x[-1].upper()=="YES":
            x.pop()
            h=updateHypothesis(x,h)
#             print(h)
            
print("\n Hypotheis: ",h)
    
# data = open('/kaggle/input/find-s-algorithm-dataset/ws.csv')
# data = csv.reader(data)
# print(data)

Data:
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']
['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes']
['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No']
['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']

 Hypotheis:  ['Sunny', 'Warm', '?', 'Strong', '?', '?']

