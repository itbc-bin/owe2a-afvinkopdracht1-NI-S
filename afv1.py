# Naam:
# Datum:
# Versie:

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's. Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestand="alpaca_test.fa"                             
    headers, seqs = lees_inhoud(bestand)
    
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:",headers[i])
            check_is_dna = Is_Dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")
    
def lees_inhoud(bestands_naam):
    headers = []
    seqs = []
    seq = ""
  try:
      bestand = open(bestands_naam)
      for line in bestand :
           line = line.strip()
           if ">" in line :
               if seq != "" :
                   seqs.append(seq)
                   seq = ""
               headers.append(line)
           else :
               seq += line.strip()
       seqs.append(seq)
       return headers, seqs
  except IOError:
      print("Het is geen FASTA bestand")
  except FileNotFoundError:
      print("Het bestand is niet gevonden")
  except:
      print("Er is een onbekende fout opgetreden")



    
def Is_Dna(seq):
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        Dna = "Het is DNA"
    return Dna


def knipt(alpaca_seq):

    bestand = open("enzymen.txt")
    if alpaca_seq and bestand == NULL:
        print("De functie krijgt niet de verwachte input")

    for line in bestand:
        naam,seq=line.split(" ")
        seq = seq.strip().replace("^","")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")
    


main()
