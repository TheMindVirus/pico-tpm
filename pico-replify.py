#pico-replify - Desktop utility for converting micropython to readable strings for REPL

InputFile = "pico-tpm.py"
OutputFile = "pico-tpm.repl.py"
NewLine = "\n"

file = open(InputFile, "r")
data = file.read()
file.close()

newData = "data = \"\"" + NewLine
for line in data.splitlines():
    newData += "data += \"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\\n\"" + NewLine

newData += "file = open(\"" + InputFile.replace(" ", "").replace("-", "_") + "\", \"w\")" + NewLine
newData += "file.write(data)" + NewLine
newData += "file.close()" + NewLine

file = open(OutputFile, "w")
file.write(newData)
file.close()

print("Done! Upload using Thonny REPL. Usage: import " + InputFile.replace(" ", "").replace("-", "_").replace(".py", ""))
