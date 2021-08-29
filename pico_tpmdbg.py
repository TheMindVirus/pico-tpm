#pico-tpm.py - 29/08/2021 @ 01:17
import hashlib

Header = "[TPM]: "
HashFile = "hashfile.txt"
Hashes = []

CommandStore = "store"
CommandFetch = "fetch"

ResponseOK = "OK"
ResponseError = "ERROR"

def main():
    while True:
        try:
            userInput = input(Header)
            command = userInput.split(" ", 1)
            print(command)
            
            file = open(HashFile, "r")
            data = file.read()
            file.close()
            
            Hashes = data.splitlines()
            hash = str(hashlib.sha256(command[1]).digest())
            print(hash)
            
            if (command[0].lower() == CommandStore):
                Hashes.append(hash)
                
                data = "\n".join(x for x in Hashes)
                file = open(HashFile, "w")
                file.write(data)
                file.close()
                
                Hashes = []
                print(Header + ResponseOK)
                
            elif (command[0].lower() == CommandFetch):
                match = False
                
                for line in Hashes:
                    if (line == hash):
                        print(Header + hash)
                        match = True
                        break
                
                if (match == False):
                    raise
                
            else:
                raise
        except Exception as e:
            print(Header + ResponseError)
            raise e

if __name__ == "__main__":
    main()
