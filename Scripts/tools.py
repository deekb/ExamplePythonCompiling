from argparse import ArgumentParser
import hashlib
import os

def AbsolutePath(path : str) -> str:
    return(os.path.expanduser(os.path.join(os.path.abspath(os.path.dirname(os.path.expanduser(__file__))), path)))

print(os.path.dirname(os.path.abspath(__file__)))

def ReHash() -> None:
    with open("../hashes.md5", "w") as hashfile:
        for _file in os.listdir("/home/derek/PycharmProjects/ExamplePythonCompiling/Scripts"):
            if os.path.join(os.path.dirname(os.path.abspath(__file__)), _file).endswith(".py"):
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), _file), "rb") as f:
                    file_hash = hashlib.md5()
                    while chunk := f.read(8192):
                        file_hash.update(chunk)
                hashfile.write(file_hash.hexdigest() + ":" + os.path.join(os.path.dirname(os.path.abspath(__file__)), _file) + "\n")
                print(f"ReHashed {os.path.join(os.path.dirname(os.path.abspath(__file__)), _file)}")
    print("Done")
    return()

parser = ArgumentParser()
parser.add_argument('--ReHash', action='store_true', help='Generate new hashes for libraries')
parser.add_argument('--build', action='store_true', help='Build binary and appimage')
args = parser.parse_args()

if args.ReHash:
    ReHash()
    
        

if args.build:
    os.system(f"ln -s {AbsolutePath('../Generated-Binaries/*')} {AbsolutePath('../Appimage-Root/AppRun')}")
    """
    print("Re-Hashing python files so that they can be verified in build")
    ReHash()
    print("Preparing and building (May take up to 5 mins)")
    os.system(f"bash {AbsolutePath('../BuildBinary.sh')}")
    print("nuitka compilation finished with no errors\ncopying binary to appimage")
    os.system(f"ln -s {AbsolutePath('../Generated-Binaries/*')}  {AbsolutePath('../Appimage-Root/AppRun')}")
    os.system(f"cd {AbsolutePath('../Generated-Appimages')}; {AbsolutePath('../.dependencies/appimagetool.AppImage')} {AbsolutePath('../.Appimage-Root')}")
    print("^^Ignore the above waring unless you are using this in production^^".upper())"""