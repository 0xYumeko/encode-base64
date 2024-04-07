print('''
   __       ______       __               ____     __ 
  / /  ___ / / / /____ _/ /_____ ________|_  /____/ / 
 / _ \/ -_) / / __/ _ `/  '_/ -_) __/ __//_ </ __/ _ \
/_//_/\__/_/_/\__/\_,_/_/\_\\__/_/  \__/____/_/ /_.__/
                                                      
''')

import base64
file_org = input ("Your File 'py' >> : ")
with open(file_org,'rb') as f :
    data = f.read()
    dumps_base64 = base64.b64encode(data)
    print(dumps_base64)
    end_fil = open("base64-"+ file_org,"w")
    end_fil.write("import base64\n")
    end_fil.write("exec(base64.b64decode("+repr(dumps_base64)+"))")
    end_fil.close()

def most_classes(dictionary):
    max_classes = 0
    most_active_teacher = None
    for teacher, classes in dictionary.items():
        if len(classes) > max_classes:
            max_classes = len(classes)
            most_active_teacher = teacher
    return most_active_teacher

print("Done !")










#helltakerc3rb