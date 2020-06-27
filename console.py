#!/usr/bin/python3

""" Hello world """

from models import storage
from cmd import Cmd
from models.base_model import BaseModel
import models


class HBNBCommand(Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, inp):
        '''exit'''
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def help_quit(self):
        """ Is for help to thought the console"""
        print("To exit put the commands: quit or CTRL + D")

    def default(self, inp):
        """ Is for check the exit status """
        if inp == 'quit':
            return self.do_exit(inp)

    def do_all(self, kika):
        '''
            Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all
        '''

        if len(kika) == 0:
            print([str(v) for v in models.storage.all().values()])

        elif kika != "BaseModel":
            print('** class doesn\'t exist **')
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if kika in k])

    def do_create(self, inp):
        """ Creates a new instance of BaseModel, saves it and prints the id """
        if len(inp.split()) == 1:
            if inp == 'BaseModel':
                new_inst = BaseModel()
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
            if inp.split()[0] == 'BaseModel':
                if len(inp.split()) == 2:
                    if 'BaseModel.' + inp.split()[1] in storage.all():
                        a = storage.all()
                        print(a['BaseModel.' + inp.split()[1]])
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
            if line.split()[0] != 'BaseModel':
                print('** class doesn\'t exist **')
            else:
                if len(line.split()) != 2:
                    print('** instance id missing **')
                else:
                    line = line.split()
                    obje_id = line[0] + '.' + line[1]
                    print(storage.all()[obje_id])
                    if obje_id not in storage.all():
                        print('** no instance found **')
                    else:
                        del storage.all()[obje_id]
                        storage.save()
# destroy BaseModel e005ef85-0a44-4b88-acbd-6076c09b4c51
# create BaseModel

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
