#!/usr/bin/python3
""" Is where the console will be execute
The main library it will execute the main class"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import sys
from cmd import Cmd
import json


class HBNBCommand(Cmd):
    """contains the entry point of the command interpreter"""
    if sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)' + '\n'
    classes = ('User', 'BaseModel', 'State', 'Place', 'City',
               'Amenity', 'Review')

    def do_quit(self, input):
        """ Is the function it will exit the program """
        return True

    def emptyline(self):
        """This function doesnt do anything"""
        pass

    def do_EOF(self, input):
        """ Is the function it will exit the program """
        print()
        return True

    def help_quit(self, input):
        """ Is for help to thought the console"""
        print("To exit put the commands: quit or CTRL + D")

    def do_count(self, classes):
        """ Is the function to count how many classes are in the json """
        counter = 0
        for key in storage.all().keys():
            # para partir la clave y ver cuantas clases hay
            if classes == key.split('.')[0]:
                counter += 1
        print(counter)

    def default(self, inp):
        """ Is for check the exit status and others commands"""
        # parcea el argumento
        args = inp.split('.')
        # mira si el argumento coincide con las clases
        if args[0] in self.classes:
            # mira si hay algo despues del punto, args ya esta con split
            if len(args) > 1:
                # obtener el nombre de la clase
                class_arg = args[0]
                # quitarle los parentecis () al City.all()
                args = args[1].split('(', 1)
                commands = {'all': self.do_all, 'count': self.do_count,
                            'show': self.do_show, 'destroy': self.do_destroy,
                            'update': self.exc_update}
                # recibe el tipo de comando
                command = args[0]
                if command in commands:
                    # se hace el try por si solo pasan City.all
                    try:
                        # le hago split para recibir la ID y no recibirla "",
                        # mandarle el y con errores
                        arguments = args[1][:-1].split(',', 1)

                        # mira si son estas dos opciones solo para mandar
                        # nombre de la clase
                        if command in ('count', 'all'):
                            commands[command](class_arg)
                        else:
                            # this is for quitar los "" en el id
                            arguments[0] = arguments[0].replace('"', '', 2)
                            # print(arguments)
                            # unir los argumentos porque son una lista
                            arguments = class_arg + " " + ''.join(arguments)
                            # print(arguments)
                            commands[command](arguments)
                    except IndexError:
                        pass

        if inp == 'quit':
            return self.do_quit(inp)

    def exc_update(self, args):
        """ This function excute the command update"""

        # hace un split hasta la id para recibir los argumentos
        args = args.split(' ', 2)
        # quitarle todos los elementos de un dictionario para
        # convertirlo en string
        for char in ["'", "\"", ",", "{", "}", ":"]:
            if char in args[2]:
                args[2] = args[2].replace(char, "")

        # parsear los argumentos
        args[2] = args[2].split()
        instances = []
        # convertirlos en una lista y poderlos mandarlos a ejecutarse por orden
        for word in range(0, len(args[2]), 2):
            args[2][word + 1] = "\"" + args[2][word + 1] + "\""
            instances.append(args[2][word] + ' ' + args[2][word + 1])

        for instance in instances:
            self.do_update(args[0] + ' ' + args[1] + ' ' + instance)
            storage.save()

        # print(args[1].replace("'", "\""))
        # return dictionary

    def do_all(self, kika):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all"""
        if len(kika) == 0:
            print([str(v) for v in storage.all().values()])

        elif kika not in self.classes:
            print('** class doesn\'t exist **')
        else:
            print([str(v) for k, v in storage.all().items() if kika in k])

    def do_create(self, inp):
        """ Creates a new instance of BaseModel, saves it and prints the id """
        if len(inp.split()) == 1:
            if inp in self.classes:
                new_inst = 0
                if inp == 'BaseModel':
                    new_inst = BaseModel()
                elif inp == 'User':
                    new_inst = User()
                elif inp == 'State':
                    new_inst = State()
                elif inp == 'Place':
                    new_inst = Place()
                elif inp == 'City':
                    new_inst = City()
                elif inp == 'Amenity':
                    new_inst = Amenity()
                elif inp == 'Review':
                    new_inst = Review()
                print(new_inst.id)
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')

    def do_show(self, inp):
        """ is the commnad to show the representation of an
        instance based on the class name """
        # si no pasan nada imprime misisng
        if len(inp) != 0:
            # aca mira si es igual a Base Model
            if inp.split()[0] in self.classes:
                if len(inp.split()) >= 2:
                    # This is for make the class.id
                    key = inp.split()[0] + '.' + inp.split()[1]
                    if key in storage.all():
                        a = storage.all()
                        print(a[key])
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
          Deletes an instance based on the class    name and id
        """
        if not line:
            print('** class name missing **')
        else:
            if not line.split()[0] in self.classes:
                print('** class doesn\'t exist **')
            else:
                if len(line.split()) < 2:
                    print('** instance id missing **')
                else:
                    line = line.split()
                    obje_id = line[0] + '.' + line[1]
                    if obje_id not in storage.all():
                        print('** no instance found **')
                    else:
                        del storage.all()[obje_id]
                        storage.save()

    def do_update(self, args):
        """ This will update the json file"""
        args = args.split()

        if len(args) != 0:
            if args[0] in self.classes:
                if len(args) == 1:
                    print('** instance id missing **')
                else:
                    key = args[0] + '.' + args[1]
                    if key in storage.all():
                        if len(args) > 2:
                            if len(args) <= 3:
                                print('** value missing **')
                            else:
                                setattr(
                                    storage.all()[key],
                                    args[2],
                                    args[3][1:-1])
                                storage.all()[key].save()
                        else:
                            print('** attribute name missing **')
                    else:
                        print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
