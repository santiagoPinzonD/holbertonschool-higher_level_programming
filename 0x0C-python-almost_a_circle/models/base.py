#!/usr/bin/python3
"""create a class"""
import json


class Base():
    """create a class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init of class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this is a function that return a
        representation of the string json of list_dictionaries
        return already serialized
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this is a method of class cls,
        this method create a file called regardless
        of the name of class cls.__name  + extensión .json
        first use the method to_dictionary that receive a list_objs
        example self.height this the store in a list that tha receive
        the method to_json_string y make the representation of this list
        and the write in a file
        """
        file = cls.__name__ + ".json"
        with open(file, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list1 = [x.to_dictionary() for x in list_objs]
                f.write(cls.to_json_string(list1))

    @staticmethod
    def from_json_string(json_string):
        """this is a function that return a list
        deserialized
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """this is a function where create a
        object dummy  and this is passed like
        a kwargs k/v and there assign to each atribute
        and return x that is the instance with all
        attributes already set:
        """
        if cls.__name__ == "Rectangle":
            x = cls(4, 7)
            x.update(**dictionary)
            return x
        else:
            x = cls(1)
            x.update(**dictionary)
            return x

    @classmethod
    def load_from_file(cls):
        """ this is a function that create a list_objs
        first try open the file, in loads store the called
        of from_json_string that return a list deserialized
        this the read after I go through and after i create
        a list1 that i starting to assign to each atributte
        and this store in list1 y this return list1
        """
        file = cls.__name__ + ".json"
        try:
            list1 = []
            with open(file, encoding="utf-8") as f:
                loads = Base.from_json_string(f.read())
                for x in loads:
                    list1 += [cls.create(**x)]
                return list1
        except:
                return []
