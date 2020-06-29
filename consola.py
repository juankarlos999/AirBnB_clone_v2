#!/usr/bin/python3
""" Is where the console will be execute
The main library it will execute the main class"""

from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import sys


class HBNBCommand(Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
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
        return True

    def help_quit(self, input):
        """ Is for help to thought the console"""
        print("To exit put the commands: quit or CTRL + D")

    def default(self, inp):
        """ Is for check the exit status """
        if inp == 'quit':
            return self.do_quit(inp)

    def do_all(self, kika):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all"""
        if len(kika) == 0:
            print([str(v) for v in storage.all().values()])

        elif not kika in self.classes:
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
        """is the commnad to show the representation of an
        instance based on the class name"""
        # si no pasan nada imprime misisng
        if len(inp) != 0:
            # aca mira si es igual a Base Model
            if inp.split()[0] in self.classes:
                if len(inp.split()) == 2:
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
                if len(line.split()) != 2:
                    print('** instance id missing **')
                else:
                    line = line.split()
                    obje_id = line[0] + '.' + line[1]
                    if not obje_id in storage.all():
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
                                setattr(storage.all()[key], args[2], args[3][1:-1])
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
    try:
        # this is for avoid the ctrl + C
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        sys.exit(0)
