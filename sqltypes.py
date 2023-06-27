from typing import Any


class varchar:
    pass

class varchar:
    def __init__(self, value: str|int|dict|set|list|function=None) -> None:
        """ Variable characters Type. If a string is provided
        then the length is the length of the string, if an int 
        is provided then the length is the value. If Nothing is
        provided then the length is 256 and the value is None. 
         
        Args:
            value (str | int): any string or integer value
        """
        if isinstance(value, int):
            self.length = value
            self.value = str(None)
        elif isinstance(value, str):
            self.length = len(value)
            self.value = value
        elif isinstance(value, None):
            self.length = 256
            self.value = str(None)
        else:
            self.value = str(value)
            self.length = len(self.value)
        self.__class__ = f"VARCHAR({self.length})"
        self.__index = 0
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("VarChar values must be string")
        if len(value) > self.length:
            raise ValueError(f"{len(value)} is greater than {self.length}")
        self.value = value
    
    def __str__(self):
        return self.value

    def __len__(self):
        return self.length
    
    def __contains__(self, value):
        return value in self.value
    
    def __ne__(self, value: any) -> bool:
        if isinstance(value, str):
            return self.value == value
        elif isinstance(value, varchar):
            return self.value == value.value
        else:
            raise ValueError(f"{value} is not of Type VarChar or string")

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, str):
            return self.value == __value
        elif isinstance(__value, varchar):
            return self.value == __value.value
        else:
            raise ValueError(f"{__value} is not of Type VarChar or string")

    def __add__(self, __value:object) -> varchar:
        if isinstance(__value, str):
            return varchar(self.value + __value)
        elif isinstance(__value, varchar):
            return varchar(self.value+__value.value)
        else:
            raise ValueError(f"{__value} is not of Type VarChar or string")

    
    def __sub__(self, __value:object) -> varchar:
        if isinstance(__value, str):
            return varchar(self.value - __value)
        elif isinstance(__value, varchar):
            return varchar(self.value-__value.value)
        else:
            raise ValueError(f"{__value} is not of Type VarChar or string")

    def __enter__(self):
        return iter(self.value)

    def __getattribute__(self, __name: str) -> Any:
        if __name == "length":
            return self.length
        elif __name == "value":
            return self.value
        elif __name == "name":
            return "VARCHAR"
        elif __name == "type":
            return "varchar"
        elif __name == "query":
            return f"VARCHAR({self.length})"
        else:
            raise KeyError(f"varchar['{__name}'] is not a valid attribute")
    
    @property
    def type(self):
        return self.__getattribute__("query")
    
    @property 
    def query(self):
        return self.type
    
    def __bool__(self):
        return None
    
    def __call__(self, value: str|int):
        if isinstance(value, str):
            self.value = value
            self.length = len(value)
        elif isinstance(value, int):
            self.value = str(None)
            self.length = value
    
    def __gt__(self, __value: int|str|varchar) -> bool|TypeError:
        if isinstance(__value, int):
            return self.length > __value
        elif isinstance(__value, str):
            return self.value > __value
        elif isinstance(__value, varchar):
            return self.length > __value.length
        else:
            raise TypeError("Cannot compare with non-string/non-integer/non-varchar types.")
    
    def __iter__(self):
        self.__index = 0
        return iter(self.value)
    
    def __next__(self):
        self.__index += 1
        if self.__index == self.length:
            raise StopIteration()
        
    def __getitem__(self, key: int) -> str|IndexError:
        try:
            return self.value[key]
        except IndexError:
            raise IndexError("String index out of range")
    
    def __setitem__(self, key: int, value: str) -> str|IndexError:
        try:
            self.value[key] = value
        except IndexError:
            return IndexError("String index out of range")
    
    def __ge__(self, __value: int|str|varchar) -> bool:
        if isinstance(__value, int):
            return self.length >= __value
        elif isinstance(__value, str):
            return self.value >= __value
        elif isinstance(__value, varchar):
            return self.length >= __value.length
        else:
            raise TypeError("Cannot compare with non-string/non-integer/non-varchar types.")
    
    
    def __le__(self, __value):
        if isinstance(__value, int):
            return self.length <= __value
        elif isinstance(__value, str):
            return self.value <= __value
        elif isinstance(__value, varchar):
            return self.length <= __value.length
        else:
            raise TypeError("Cannot compare with non-string/non-integer/non-varchar types.")
    
    def __unpack__(self, *items):
        if len(items) > self.length:
            raise ValueError(f" too many values to unpack (expected: {self.length} )")
        elif len(items) < self.length:
            raise ValueError(f"Not enough  values to unpack (expected:{self.length})")
        return [x for x in self.value]
            
    def upper(self):
        return self.value.upper()
    
    def lower(self):
        return self.value.lower()
    
    def capitalize(self):
        return self.value.capitalize()
    
    def reversed(self):
        return "".join([x for x in self.value][::-1])
    
    def startswith(self, __value: str|varchar):
        return self.value.startswith(__value)
    
    def endswith(self, __value: str|varchar):
        if isinstance(__value, varchar):
            return self.value.startswith(__value.value)
        elif isinstance(__value, str):
            return self.value.endswith(__value)
        elif isinstance(__value, int):
            return self.value.endswith(str(__value))
    
    def __lt__(self, __value: int|str|varchar) -> bool|TypeError:
        if isinstance(__value, int):
            return self.length < __value
        elif isinstance(__value, str):
            return self.value < __value
        elif isinstance(__value, varchar):
            return self.length < __value.length
        else:
            raise TypeError("Cannot compare with non-string/non-integer/non-varchar types.")
    
