from bs4 import BeautifulSoup
import os

for filename in os.listdir("./hu/raw/"):
    print(filename)
    with open("./hu/raw/"+filename,"r") as sourceFile:
        with open("./hu/pretty/"+filename,"x") as destFile:
            soup = BeautifulSoup(sourceFile,'html.parser')
            for data in soup.find_all("p"): 
                
                destFile.write(data.get_text())