# varchar
varchar type usable in mysql and sqlite3. take a look


# usage

```python3
from sqltypes import varchar

string_version = "himom"

himom = varchar(string_version)

over9 = varchar(9001)

print(himom + " how are you")  # himom how are you

print(himom-"mom") # hi

type(himom) # VARCHAR(5)

print(himom.upper()) # HIMOM
print(himmom.reversed()) # momih
print(himom.capitalized()) # Himom

for char in himom:
  print(char)   # h\ni\nm\no\nm\n

x = [x for x in himom] # ["h", "i", "m", "o", "m"]

print(himom < over9)   # True

print(himom == over9) # False

print(himom == "himom") # True

```


![Screenshot 2023-06-27 162905](https://github.com/Donny-GUI/mysql-varchar/assets/108424001/2b0b243a-07e8-4590-99a6-20aefbc56d05)
