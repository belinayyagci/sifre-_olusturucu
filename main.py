file_name = input("Dosya ismi gir:\n")
data = input("Dosyaya ne kaydetmek istersin:\n")

with open(f"{file_name}.txt""w") as doc:
    doc.write(data)