letter='''dear <|name|>,
you are selected !
<|date|>'''
name=input("enter your name: ")
date=input("enter date: ")
print(letter.replace('<|name|>',name).replace('<|date|>',date))
print(letter.replace("selected","selected now"))