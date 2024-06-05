import os
import subprocess

def installExpress():
    os.system("npm install express")

def createReactApp(name):
    if name.strip() == "":
        name = "my app"
    os.system("npx create-react-app " + name)

def clearScreen():
    os.system("cls")

createReactApp("test")