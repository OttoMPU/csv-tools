import time
import pandas as pd 
from pathlib import Path

def main():
    valinta = input('Valitse toiminto: \n 1) Listojen vertailu \n 2) Duplikaattien poisto listalta \n 3) Sulje ohjelma \n')
    if valinta == '1':
        compare()
    elif valinta == '2':
        deleteduplicates()
    elif valinta == '3':
        appendfiles()
    elif valinta == '4':
        print('Ohjelma suljetaan...')
        time.sleep(2)
        exit
            
def compare():
    print('Ohjelma luo listan niistä riveistä, jotka löytyvät ensimmäisestä mutta puuttuvat toisesta listasta. \n'
        'Listojen täytyy olla samassa kansiossa kuin csv-tools.exe \n'
        '!Kirjoita listojen nimet ilman .csv tiedostopäätettä!')
    input1 = input("Ensimmäisen listan nimi: ")
    input2 = input("Toisen listan nimi: ")
    try:
        with open('.\\' + input1 + '.csv', 'r') as t1, open('.\\' + input2 + '.csv', 'r') as t2:
            List1 = t1.readlines()
            List2 = t2.readlines()
        ts = str(time.time())
        with open('lista_' + ts + '.csv', 'w') as outFile:
            for line in List1:
                if line not in List2:
                    outFile.write(line)
    except:
        print('Tapahtui virhe. Tarkista listojen tiedostotyypit ja nimet. \n')
    main()

def deleteduplicates():
    print('Ohjelma poistaa duplikaatit listalta. \n'
        'Listan täytyy olla samassa kansiossa kuin csv-tools.exe \n'
        '!Kirjoita listan nimi ilman .csv tiedostopäätettä! \n')
    listanimi = input('Anna .csv tiedoston nimi: ')
    sarake = input('Anna sarakkeen nimi jolla rivejä verrataan (esim. email): ')
    ts = str(time.time())
    try:
        d = pd.read_csv(listanimi + '.csv', keep_default_na= False)
        d.drop_duplicates(subset= [sarake], inplace= True, keep= 'first')
        d.to_csv('duplicatesremovedlist_' + ts + '.csv', index=False)
    except:
        print('Tapahtui virhe. Tarkista listan tiedostotyyppi ja nimi. \n')
    main()
    

def appendfiles():
    print('Ohjelma yhdistää csv tiedostot yhdeksi listaksi. \n'
      'Ensimmäinen tiedosto tulee olla samassa kansiossa kuin ohjelman .exe \n'
      'Muut tiedostot täytyy laittaa erilliseen kansioon. \n')
    directory = input("Anna kansion nimi jossa yhdistettävät listat sijaitsee: ")
    filename = input("Anna tiedoston nimi, johon listat yhdistetään (luo uuden tiedoston jos nimellä ei löydy csv:tä): ")
    directory = '.\\' + directory + '\\'
    filename = '.\\' + filename + '.csv'
    with open(filename, 'a+') as f:
        f.write('\n')
    files = Path(directory).glob('*')
    for file in files:
        data = pd.read_csv(file)
        df = pd.DataFrame(data)
        df.to_csv(filename, mode='a', index=False, header=False)
    main()

if __name__ == '__main__':
    main()
