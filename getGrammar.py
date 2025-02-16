# Rules of the grammar 
L1 = {
    "S": [["NP", "VP"],["X1","VP"],["book"],["include"],["prefer"],["Verb","NP"],["X2","PP"],["Verb","PP"],["VP","PP"]],
    "NP": [["Det","Nominal"],["I"],["she"],["me"],["TWA"],["Houston"]],
    "Nominal": [["Nominal","Noun"],["Nominal","PP"],["book"],["flight"],["meal"],["money"],["morning"]],
    "VP": [["Verb","NP"],["Verb","PP"],["VP","PP"],["book"],["include"],["prefer"],["X2","PP"]],
    "PP": [["Preposition","NP"]],
    "X1": [["Aux","NP"]],
    "X2": [["Verb","NP"]],
    "Det": [["that"],["this"],["a"],["the"]],
    "Noun": [["book"],["flight"],["meal"],["money"],["morning"]],
    "Verb":[["book"],["include"],["prefer"]],
    "Aux": [["does"]],
    "Preposition": [["from"],["to"],["on"],["near"],["through"]]
}


Dothraki = {
    "S": [["NP", "VP"],["X1","VP"],["VP","PP"], ["NP","NP"], ["NP","JJ"]],
    "X1": [["Aux","NP"]],
    "Aux": [["hash"]],
    "VP": [["VP","NP"],["VP","ADV"],["astoe"],["dothrak"],["zhilak"],["dothrae"],["VP","PP"],["ittesh"],["VP","Pron"],["nesak"]],
    "PP": [["Preposition","NP"]],
    "NP":[["anha"],["yera"],["yer"],["Dothraki"],["NP","ADV"],["mahrazh"],["mori"],["lajakis"],["NP","JJ"], ["lajak"]],
    "Preposition": [["ki"]],
    "ADV":[["chek"],["ADV","ADV"],["asshekh"]],
    "JJ":[["ivezhi"],["JJ,JJ"],["mori"],['gavork']],
    "Pron":[["haz"]]
}

def useGrammar(grammar):
    if grammar == 'L1':
        return L1
    elif grammar == 'Dothraki':
        return Dothraki
    else:
        print("Grammatica non esistente")