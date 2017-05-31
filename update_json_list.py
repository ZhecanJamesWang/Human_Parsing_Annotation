import os

src='data/images/'
tar='data/annotations/'

flist=os.listdir(src)

src_list=[]
tar_list=[]

for add in flist:
	name, ext=os.path.splitext(add)
	tar_add=tar+name+'.png'
	#print src+add
	#print tar_add
	src_list.append(src+add)
	tar_list.append(tar_add)
	
	
	
import json

result={}
result['labels']=[
    "Background"，
	"Hat"，
	"Hair"，
	"Glove"，
	"Sunglasses"，
	"Upper-clothes"，
	"Dress"，
	"Coat"，
	"Socks"，
	"Pants"，
	"Jumpsuits"，
	"Scarf"，
	"Skirt"，
	"Face"，
	"Left-arm"，
	"Right-arm"，
	"Left-leg"，
	"Right-leg"，
	"Left-shoe"，
	"Right-shoe"
  ]
  
result["imageURLs"]=src_list
result["annotationURLs"]=tar_list

json.dump(result, open('multi_person.json', 'w'), sort_keys=True, indent=4)