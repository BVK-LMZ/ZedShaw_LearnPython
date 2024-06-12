# ZedShaw Python Exercise #39
# This Exercise is all about... DICTS

States = {
    'MD' : "Maryland",
    'FL' : "Florida"
    }


#items() to iterate through the dict
for short in States.items():
    print(short)

print("----------")

#by having two args we can seperate the key and the value
for short,full in States.items():
    print(f"{short} aka {full}")