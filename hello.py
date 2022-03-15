# def main():
#    print("Hello World")

# main()

# creat SSH keys to link Cloud9 with github

# make the key

## put this into BASH
### ssh-keygen -t rsa

# make a virtual environment

## into BASH

### python3 -m venv ~/.workingInTheCloud

## activate environment
### source ~/.workingInTheCloud/bin/activate
### which python

# add things to the requirements file and makefile

# run the make file which runs the requirements file
## into bash
# make install

# fun some code that gets things going

x = 3
y = 5


def add(x, y):
    return x + y


print(f"this is the sum: {x}, {y}, {add(x,y)}")
