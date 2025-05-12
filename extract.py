import bz2

with bz2.open("simplewiki.xml.bz2", "rb") as f_in:
    with open("simplewiki.xml", "wb") as f_out:
        f_out.write(f_in.read())

print("Arquivo descompactado com sucesso!")
