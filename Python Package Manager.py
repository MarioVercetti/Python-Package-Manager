import os
import subprocess
import sys
import keyboard


def main():
    print("What do you want to do?")
    print("1.Install Package")
    print("2.Uninstall Package")
    print("3.Check what packages i have installed")
    print("4.run package")
    print("5.reinstall package")
    choice = input()
    if choice == "1":
        print("type what package do you want to install:")
        package = input()
        os.system("cmd /k pip install " + package)
        print("package is installed!")
        print("press enter to go back")
        keyboard.wait("enter")
        main()
    if choice == "2":
        print("type what package do you want to uninstall:")
        package = input()
        os.system("cmd /k pip uninstall " + package)
        print("package is uninstalled!")
        print("press enter to go back")
        keyboard.wait("enter")
        main()
    if choice == "3":
        # I don't know what this does, but it works
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
        print(installed_packages)
        print("=====================================================")
        print("press enter to go back")
        keyboard.wait("enter")
        main()
    if choice == "4":
        print("type name of the package you want to run:")
        package = input()
        os.system("cmd /k " + package)
    if choice == "5":
        print("type what package do you want to uninstall:")
        package = input()
        print("Uninstalling the package..")
        os.system("cmd /k pip uninstall " + package)
        print("Installing the package..")
        os.system("cmd /k pip install " + package)
        print("press enter to go back")
        keyboard.wait("enter")
        main()
        

if __name__ == '__main__':
    main()
