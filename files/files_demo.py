fw = open("sample.txt", 'w')
fw.write("Writing to sample filen with sample text\n")
fw.write("Writing some more text in second line")
fw.close()

fr = open("text.txt", "r")
txtt = fr.read()
print txtt

fr.close()
