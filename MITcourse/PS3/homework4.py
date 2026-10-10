import random

andi = []
benita = []
evelyn = []
doris = []
chole = []
fatima = []

andi = [benita, evelyn, doris]
benita = [andi, chole, fatima, doris]
evelyn = [andi, chole, fatima, doris]
doris = [evelyn, andi, benita, fatima]
chole = [benita, evelyn]
fatima = [benita, doris, evelyn]

people_all = [andi, benita, evelyn, doris, chole, fatima]
a = []

while True:

    a = random.choice(people_all)


def find_fist(a):
    try:
         
    except