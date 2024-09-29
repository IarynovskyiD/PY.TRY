from six import moves
from tensorflow import double
from tensorflow.python.ops.weak_tensor_ops import operator
from tensorflow.python.util.tf_export import kwarg_only

x = 15
price = 9.99
discount = 0.2
result = price * ( 1 - discount)
print(result)

name = "ralf"
name = "rall"
print(name+name)

man = "Bob"
print(f"Hello {man}")
man = "Alex"
print(f"Hello {man}")
greeting = "Hello {}, llll {}"
print(greeting.format(name,man))

list = ["a", "b", "c"]
tauple = ("a", "b", "c", "d")
set = {"a", "b", "e"}
set2 = {"a", "b", "c", "d"}
print(f"{list[0]}, {tauple[1]}")
list.append("dddd")
print(f"{list}")
coc = set2.difference(set)
print(coc)
coc = set2.union(set)
print(coc)
coc = set2.intersection(set)
print(coc)
set = coc
print(set is coc)

day_of_week = "Tuesday"
if day_of_week == "Monday":
    print("have a good day")
elif day_of_week == "Tuesday":
    print("have a baaaaadb day")
else:
    print("have a bad day")
print("have a good day!!!!!")

moves = {"baba", "mama", "papa"}
ass = input("What do you wont ?")
print(ass in moves  )
if ass in ("ba", "j" ):
    print("yes")
elif ass != "o":
    print("no")
else:
    print("yessssss")
for moves in moves:
    print(moves)

numbers = [1,2,3,4,5]
double = [num * 2 for num in numbers]
print(numbers)
print(double)
x = 3
x = x + 5
print(x)

def multiply(*args):
    total = 1
    for num in args:
         total *= num
    return total
print(multiply(1,2,3,4,5))

def apply(*num, operator):
    if operator == "*":
       return multiply(*num)
    if operator == "+":
       return sum(num)
    else: return "numMMM"

print(apply(1,2,3,4,5, operator="*"))


from pyt import ppr
ppr()


import functools

user = {"username": "jose", "password": "12345!"}
def make_secure(funk):
    @functools.wraps(funk)
    def secure_funk(*args, **kwargs):
        if user["password"] == "12345!":
            return funk(*args, **kwargs)
        else:
            return "wrong password"
    return secure_funk

@make_secure
def get_user_page():
    return f"/page/{user['username']}"

print(get_user_page())


a = "hello"
b = a
print(id(a), id(b))
a += "world"
print(id(a), id(b))




from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

name = "americos"
fox = "sox"
man = "super"
kwargs ={
    "name": name,
    "fox": fox,
    "man": man
}

@app.route('/')
def home():
    return render_template("first.html", **kwargs)

@app.route('/login')
def login():
    return render_template("second.html",**kwargs)


