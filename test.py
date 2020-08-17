#!/usr/bin/python3
""" Test delete feature
"""
import os
# from models.engine.file_storage import FileStorage
# from models.state import State
# from models.user import User
# from console import HBNBCommand
# fs = FileStorage()


# # new_dict = {}
# # all_states = fs.all()
# # for value in all_states:
# #      # why in this not use isinstace?
# #      if State == type(all_states[value]):
# #           new_dict[value] = all_states[value]


# # print(new_dict)

# new_state = User()
# new_state.name = "Pen"
# fs.new(new_state)
# fs.save()

all_states = fs.all()
# print(all_states)
# print()
# print()
for value in all_states:
    if "User.0304ffa6-3e3f-4679-b262-83d46d7f8d84" == all_states[value]:
        del(all_states[value])
        fs.save()
        break

# print()
# print()
# print(all_states)

co = HBNBCommand()
co.onecmd("create User")
