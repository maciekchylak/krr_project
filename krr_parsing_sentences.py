import copy
import numpy as np
                #{0 : [[strzelba_naladowana,kurczak_zyje], [strzelba_naladowana,!kurczak_zyje]],
                # 1: [[strzelba_naladowana,kurczak_zyje], [strzelba_naladowana,!kurczak_zyje]]}
states = {0:[[]]} # [[strzelba_naladowana,kurczak_zyje], [strzelba_naladowana,!kurczak_zyje]]
#states_models =  [{0:},{0:}]
# fluents = ["strzelba_naladowana", "kurczak_zyje", "slonce_swieci"]
# fluents = ["drzwi_otwarte", "pieniadze","blokada_aktywna"]
#agents = ["strzelec"]
agents_actions = {}
actions_conditions = {}#klucz: agent,akcja value: [precon, postcon]
                        #agents_actions = {"strzelec":["laduje","strzela"]}
                        #actions_conditions = {(strzelec,strzela,): [[["!strzelba_naladowana"],["ma dodatkowe ammo"]],["stzelba_naladowana"]],
                                            #"strzelec_strzela": [["strzelba_naladowana"],["!kurczak_zyje"]]}
agents_actions_impossible = {}
actions_conditions_impossible = {}
agents_actions_releases = {}
actions_conditions_releases = {}
after_sequences={}#(A1,A2,A3):[[formula, fromula1], [formula,formula2]],(A1,A2,A4):[formula]
after_observable_sequences = {}
statments = {"initial_fluents":[[]], #["kurczak_zyje", "strzelba_naladowana"],["!kurczak_zyje","strzelba_naladowana"],[]
             "always":[[]]}

# sequences = ["initially kurczak_zyje",
#              "initially slonce_swieci",
#               "strzal by strzelec releases !kurczak_zyje if kurczak_zyje",
#               "strzal by strzelec causes !strzelba_naladowana if kurczak_zyje",
#               "impossible strzal by strzelec if !strzelba_naladowana",
#               "przeladowanie by strzelec causes strzelba_naladowana if !strzelba_naladowana",
#             #   "always kurczak_zyje",
#              "!slonce_swieci after strzal, przeladowanie, strzal"
#               ]

# sequences = [ "initially pieniadze",
#               "initially drzwi_otwarte",
#               "initially !blokada_aktywna",
#               "zamknij by domownik causes !drzwi_otwarte if drzwi_otwarte",
#               "zablokuj by domownik causes blokada_aktywna if !blokada_aktywna and !drzwi_otwarte",
#               "wlam by zlodziej releases !pieniadze if !blokada_aktywna",
#               "impossible zablokuj by domownik if drzwi_otwarte",
#               "impossible zamknij by domownik if blokada_aktywna"
#               ]


# sequences = [ "initially pieniadze or !drzwi_otwarte"
#               ]

# sequences = [
#     "initially pieniadze",
#     "initially blokada_aktywna",
#     "initially drzwi_otwarte",
#     "always drzwi_otwarte",
#     "zamknij by domownik causes !drzwi_otwarte if drzwi_otwarte",
#     "zamknij1 by domownik causes !pieniadze if blokada_aktywna",
#     "impossible zamknij1 by domownik if blokada_aktywna"

# ]


#baba 1
# fluents = ["p","q"]
# sequences = [ "initially !p and !q",
#               "fire by agent causes p or q"]
# program = ["agent fire"]
# query = ["possibly p and q after program"] #False


# #seba 1
# fluents = ["drzwi_otwarte", "pieniadze","blokada_aktywna"]
# sequences = [ "initially pieniadze",
#               "initially drzwi_otwarte",
#               "initially !blokada_aktywna",
#               "zamknij by domownik causes !drzwi_otwarte if drzwi_otwarte",
#               "zablokuj by domownik causes blokada_aktywna if !blokada_aktywna and !drzwi_otwarte",
#               "wlam by zlodziej releases !pieniadze if !blokada_aktywna",
#               "impossible zablokuj by domownik if drzwi_otwarte",
#               "impossible zamknij by domownik if blokada_aktywna"
#               ]
# program = ["domownik zamknij", "domownik zablokuj", "zlodziej wlam"]
# query = ["possibly pieniadze after"] #True

# program = ["zlodziej wlam", "domownik zablokuj", "zlodziej wlam"]
# query = ["program realizable always"] #False

# program = ["domownik zamknij", "zlodziej wlam"]
# query = ["active zlodziej in program"] #False

# sequences = [ "initially pieniadze",
#               "initially drzwi_otwarte",
#               "initially !blokada_aktywna",
#               "zamknij by domownik causes !drzwi_otwarte if drzwi_otwarte",
#               "zablokuj by domownik causes blokada_aktywna if !blokada_aktywna and !drzwi_otwarte",
#               "wlam by zlodziej causes !pieniadze if !blokada_aktywna",
#               "impossible zablokuj by domownik if drzwi_otwarte",
#               "impossible zamknij by domownik if blokada_aktywna"
#               ]
# program = ["domownik zamknij", "zlodziej wlam"]
# query = ["active zlodziej in program"] #Ture

# maciek1
# fluents = ["open", "hasCard"]
# sequences = [
#             "initially !open",
#             "insertCard by bill causes open",
#             "impossible insertCard by bill if !hasCard"
# ]
# program = ["bill insertCard"]
# query = ["necessary open after (bill insertCard)"] #False

# program = ["bill insertCard"]
# query = ["realizable always"] #False

# #maciek2
# fluents = ["loaded", "alive"]
# sequences = [
#             "initially alive",
#             "load by bill causes loaded",
#             "shoot by bill causes !loaded",
#             "shoot by bill causes !alive if loaded"
# ]
# # program = ["bill load", "bill shoot"]
# # query = ["program realizable always"] # True

# program = ["bill load", "bill shoot"]
# query = ["necessary !alive after program"] #True

# maciek3
# fluents = ["loaded", "alive", "walking"]
# sequences = [
#             "initially loaded and walking",
#             "always !walking or alive",
#             "load by bill causes loaded",
#             "shoot by bill causes !loaded",
#             "shoot by bill causes !alive if loaded"
# ]
# program = ["bill shoot"]
# query = ["necessary walking after program"] #True

# program = ["bill shoot"]
# query = ["realizable always"] #True


# maciek4
# fluents = ["loaded", "alive"]
# sequences = [
#             "initially !loaded and alive",
#             "load by bill causes loaded",
#             "shoot by bill causes !loaded",
#             "shoot by bill causes !alive if loaded",
#             "spin by bill releases !loaded if loaded"
]
# program = ["bill load", "bill shoot", "bill load", "bill spin"]
# query = ["possibly !loaded after program"] # True
# program = ["bill load", "bill spin"]
# query = ["possibly alive after program"] # True

historical_actions =[]

for seq in sequences:
    if "initially" in seq:#done
        seq = seq[len("initially")+1:]
        if "or" in seq:
            seq1, seq2 = seq.split(" or ")
            copied = copy.deepcopy(statments["initial_fluents"])
            statments["initial_fluents"] = statments["initial_fluents"] + copied
            for i in range(len(statments["initial_fluents"])):
                if i<len(copied):
                    statments["initial_fluents"][i].append(seq1)
                else:
                    statments["initial_fluents"][i].append(seq2)
        elif "and" in seq:
            seq1, seq2 = seq.split(" and ")
            for i in range(len(statments["initial_fluents"])):  
                statments["initial_fluents"][i].append(seq1)
                statments["initial_fluents"][i].append(seq2)
        else:
            for i in range(len(statments["initial_fluents"])):  
                statments["initial_fluents"][i].append(seq)

    elif "observable" in seq:
        seq = seq[len("observable")+1:]
        seq1, seq2 = seq.split(" after ")
        actions_ = tuple(seq2.split(", "))
        if not actions_ in after_observable_sequences.keys():
            after_observable_sequences[actions_] = [[]]
        if "or" in seq1:
            seq11, seq21 = seq1.split(" or ")
            copied = copy.deepcopy(after_observable_sequences[actions_])
            after_observable_sequences[actions_] = after_observable_sequences[actions_] + copied
            for i in range(len(after_observable_sequences[actions_])):
                if i<len(copied):
                    after_observable_sequences[actions_][i].append(seq11)
                else:
                    after_observable_sequences[actions_][i].append(seq21)
        elif "and" in seq1:
            seq11, seq21 = seq1.split(" and ")
            for i in range(len(after_observable_sequences[actions_])):  
                after_observable_sequences[actions_][i].append(seq11)
                after_observable_sequences[actions_][i].append(seq21)
        else:
            for i in range(len(after_observable_sequences[actions_])):  
                after_observable_sequences[actions_][i].append(seq1)    
    elif "after" in seq:
        seq1, seq2 = seq.split(" after ")
        actions_ = tuple(seq2.split(", "))
        if not actions_ in after_sequences.keys():
            after_sequences[actions_] = [[]]
        if "or" in seq1:
            seq11, seq21 = seq1.split(" or ")
            copied = copy.deepcopy(after_sequences[actions_])
            after_sequences[actions_] = after_sequences[actions_] + copied
            for i in range(len(after_sequences[actions_])):
                if i<len(copied):
                    after_sequences[actions_][i].append(seq11)
                else:
                    after_sequences[actions_][i].append(seq21)
        elif "and" in seq1:
            seq11, seq21 = seq1.split(" and ")
            for i in range(len(after_sequences[actions_])):  
                after_sequences[actions_][i].append(seq11)
                after_sequences[actions_][i].append(seq21)
        else:
            for i in range(len(after_sequences[actions_])):  
                after_sequences[actions_][i].append(seq1)    
    elif "causes" in seq:
        seq4 = None
        seq1, seqrest = seq.split(" by ")
        seq2, seqrest = seqrest.split(" causes ")
        if "if" in seqrest:
            seq3,seq4 = seqrest.split(" if ")
        else:
            seq3 = seqrest
        if not (seq2,seq1) in agents_actions.keys():
            agents_actions[seq2] = []
            actions_conditions[(seq2,seq1)] = [[[]],[[]]]
        agents_actions[seq2].append(seq1)
        #actions_conditions[(seq2,seq1)]
        
        #done
        if "or" in seq3:
            seq31, seq32 = seq3.split(" or ")
            copied = copy.deepcopy(actions_conditions[(seq2,seq1)][1])
            actions_conditions[(seq2,seq1)][1] = actions_conditions[(seq2,seq1)][1] + copied
            for i in range(len(actions_conditions[(seq2,seq1)][1])):
                if i<len(copied):
                    actions_conditions[(seq2,seq1)][1][i].append(seq31)
                else:
                    actions_conditions[(seq2,seq1)][1][i].append(seq32)
        elif "and" in seq3:
            seq31, seq32 = seq3.split(" and ")
            for i in range(len(actions_conditions[(seq2,seq1)][1])):  
                actions_conditions[(seq2,seq1)][1][i].append(seq31)
                actions_conditions[(seq2,seq1)][1][i].append(seq32)
        else:
            for i in range(len(actions_conditions[(seq2,seq1)][1])):  
                actions_conditions[(seq2,seq1)][1][i].append(seq3)

        if not seq4==None:
            if "or" in seq4:
                seq41, seq42 = seq4.split(" or ")
                copied = copy.deepcopy(actions_conditions[(seq2,seq1)][0])
                actions_conditions[(seq2,seq1)][0] = actions_conditions[(seq2,seq1)][0] + copied
                for i in range(len(actions_conditions[(seq2,seq1)][0])):
                    if i<len(copied):
                        actions_conditions[(seq2,seq1)][0][i].append(seq41)
                    else:
                        actions_conditions[(seq2,seq1)][0][i].append(seq42)
            elif "and" in seq4:
                seq41, seq42 = seq4.split(" and ")
                for i in range(len(actions_conditions[(seq2,seq1)][0])):  
                    actions_conditions[(seq2,seq1)][0][i].append(seq41)
                    actions_conditions[(seq2,seq1)][0][i].append(seq42)
            else:
                for i in range(len(actions_conditions[(seq2,seq1)][0])):  
                    actions_conditions[(seq2,seq1)][0][i].append(seq4)

    elif "impossible" in seq:
        seq = seq.split("impossible ")[1]
        seq1, seqrest = seq.split(" by ")
        seq2, seq3 = seqrest.split(" if ")
        if not (seq2,seq1) in agents_actions_impossible.keys():
            agents_actions_impossible[seq2] = []
            actions_conditions_impossible[(seq2,seq1)] = [[[]],[[]]]
        agents_actions_impossible[seq2].append(seq1)
        
        #done
        if "or" in seq3:
            seq31, seq32 = seq3.split(" or ")
            copied = copy.deepcopy(actions_conditions_impossible[(seq2,seq1)][0])
            actions_conditions_impossible[(seq2,seq1)][0] = actions_conditions_impossible[(seq2,seq1)][0] + copied
            for i in range(len(actions_conditions_impossible[(seq2,seq1)][0])):
                if i<len(copied):
                    actions_conditions_impossible[(seq2,seq1)][0][i].append(seq31)
                else:
                    actions_conditions_impossible[(seq2,seq1)][0][i].append(seq32)
        elif "and" in seq3:
            seq31, seq32 = seq3.split(" and ")
            for i in range(len(actions_conditions_impossible[(seq2,seq1)][0])):  
                actions_conditions_impossible[(seq2,seq1)][0][i].append(seq31)
                actions_conditions_impossible[(seq2,seq1)][0][i].append(seq32)
        else:
            for i in range(len(actions_conditions_impossible[(seq2,seq1)][0])):  
                actions_conditions_impossible[(seq2,seq1)][0][i].append(seq3)

        
    elif "releases" in seq:
        seq4 = None
        seq1, seqrest = seq.split(" by ")
        seq2, seqrest = seqrest.split(" releases ")
        if "if" in seqrest:
            seq3,seq4 = seqrest.split(" if ")
        else:
            seq3 = seqrest
        if not (seq2,seq1) in agents_actions_releases.keys():
            agents_actions_releases[seq2] = []
            actions_conditions_releases[(seq2,seq1)] = [[[]],[[]]]
        agents_actions_releases[seq2].append(seq1)
        #actions_conditions[(seq2,seq1)]
        
        #done
        for i in range(len(actions_conditions_releases[(seq2,seq1)][1])):  
            actions_conditions_releases[(seq2,seq1)][1][i].append(seq3)

        if not seq4==None:
            if "or" in seq4:
                seq41, seq42 = seq4.split(" or ")
                copied = copy.deepcopy(actions_conditions_releases[(seq2,seq1)][0])
                actions_conditions_releases[(seq2,seq1)][0] = actions_conditions_releases[(seq2,seq1)][0] + copied
                for i in range(len(actions_conditions_releases[(seq2,seq1)][0])):
                    if i<len(copied):
                        actions_conditions_releases[(seq2,seq1)][0][i].append(seq41)
                    else:
                        actions_conditions_releases[(seq2,seq1)][0][i].append(seq42)
            elif "and" in seq4:
                seq41, seq42 = seq4.split(" and ")
                for i in range(len(actions_conditions_releases[(seq2,seq1)][0])):  
                    actions_conditions_releases[(seq2,seq1)][0][i].append(seq41)
                    actions_conditions_releases[(seq2,seq1)][0][i].append(seq42)
            else:
                for i in range(len(actions_conditions_releases[(seq2,seq1)][0])):  
                    actions_conditions_releases[(seq2,seq1)][0][i].append(seq4)
    elif "always" in seq:
        seq = seq[len("always")+1:]
        if "or" in seq:
            seq1, seq2 = seq.split(" or ")
            copied = copy.deepcopy(statments["always"])
            statments["always"] = statments["always"] + copied
            for i in range(len(statments["always"])):
                if i<len(copied):
                    statments["always"][i].append(seq1)
                else:
                    statments["always"][i].append(seq2)
        elif "and" in seq:
            seq1, seq2 = seq.split(" and ")
            for i in range(len(statments["always"])):  
                statments["always"][i].append(seq1)
                statments["always"][i].append(seq2)
        else:
            for i in range(len(statments["always"])):  
                statments["always"][i].append(seq)
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! blad")

print(f"Initial fluents :{statments['initial_fluents']}")
print(f"After sequences :{after_sequences}")
print(f"After observable sequences :{after_observable_sequences}")
print(f"actions_conditions :{actions_conditions}")
print(f"actions_conditions_impossible :{actions_conditions_impossible}")
print(f"actions_conditions_releases :{actions_conditions_releases}")
print(f"always :{statments['always']}")




states[0] = copy.deepcopy(statments["initial_fluents"])
for f in fluents:
    new_statements = []
    for l in statments["initial_fluents"]:
        if "!" + f in l or f in l:
            new_statements.append(l)
            continue
        else:
            l_copy_1 = copy.deepcopy(l)
            l_copy_1.append(f)
            new_statements.append(l_copy_1)
            l_copy_2 = copy.deepcopy(l)
            l_copy_2.append("!" + f)
            new_statements.append(l_copy_2)
    new_statements = [list(x) for x in set(tuple(sorted(x)) for x in new_statements)]        
    states[0] = new_statements

print(f"states0 {states}")

new_statements = []
for states_model in states[0]:
    for posibility2 in statments["always"]:
        boolean = True
        for fluent in posibility2:
            if not fluent in states_model:
                boolean = False
                break
        if boolean:
            break
    if boolean:                   
        new_statements.append(states_model)
states[0] = new_statements        


print(f"states1 {states}")
print(f"statments[initial_fluents] {statments['initial_fluents']}")

        
parsed_program = []
for p in program:
    a,b = p.split(" ")
    parsed_program.append((a,b))


if True:
    if True:
        def value_query_necessary():
            for i,(agent, action) in enumerate(parsed_program):
                states[i+1]=[]
                historical_actions.append(action)  
                for state in states[i]:
                    boolean_always = True 
                    #impossible
                    if (agent, action) in actions_conditions_impossible.keys():
                        for posibility in actions_conditions_impossible[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break                         
                        if  boolean==True:
                            continue                             
                    #causes
                    states_or =[]
                    if (agent, action) in actions_conditions.keys():
                        for posibility in actions_conditions[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    boolean_always = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            boolean_always = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    # states[i+1].append(state_copied)
                                    # state = state_copied
                                    states_or.append(state_copied)
                                    print(f"states_or {states_or}")
                        else:
                            states[i+1].append(state)
                    #release
                    if (agent, action) in actions_conditions_releases.keys():
                        for posibility in actions_conditions_releases[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            for posibility in actions_conditions_releases[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    states[i+1].append(state_copied)
                        else:
                            states[i+1].append(state)
                    if boolean_always:
                        #states[i+1].append(state)
                        for state_or in states_or:
                            states[i+1].append(state_or) 
                                        
                states[i+1] = [list(x) for x in set(tuple(x) for x in states[i+1])]
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for state in states[i+1]:
                            state_copied = copy.deepcopy(state)
                            for formula in formulas:
                                for fluent in formula:
                                    if fluent in state_copied:
                                        continue
                                    elif "!" in postcondtion:
                                        state_copied.remove(fluent[1:])
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                                    else:
                                        state_copied.remove("!"+fluent)
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                        states[i+1] = state_new
            if len(states[len(states)-1]) == 0:
                return False 
            for state in states[len(states)-1]:
                formula = query[0].split("necessary ")[1].split(" after")[0]
                formula2 = None
                if "or" in formula:
                    formula, formula2 = formula.split(" or ")
                    if not formula in state and not formula2 in state:
                        return False
                elif "and" in formula:
                    formula, formula2 = formula.split(" and ")
                    if not formula in state or not formula2 in state:
                        return False
                else:
                    if not formula in state:
                        return False
            return True

                        
                        
                    


        def value_query_possibly():
            states_models = []
            for state in states[0]:
                states_models.append({0:[state]})
            for i,(agent, action) in enumerate(parsed_program):
                for states_model in states_models:
                    states_model[i+1]=[]
                historical_actions.append(action)  
                for states_model in states_models:
                    for state in states_model[i]:
                        boolean_always = True
                        #impossible
                        if (agent, action) in actions_conditions_impossible.keys():
                            for posibility in actions_conditions_impossible[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break                         
                            if  boolean==True:
                                continue                             
                        #causes
                        states_or =[]
                        if (agent, action) in actions_conditions.keys():
                            for posibility in actions_conditions[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            print(f"boolean {boolean}")    
                            if boolean:
                                
                                for posibility in actions_conditions[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    print(f"posibility {posibility}")
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                            print(f"state_copied {state_copied}")
                                        else:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                            print(f"state_copied {state_copied}")
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        boolean_always = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                boolean_always = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        # states[i+1].append(state_copied)
                                        # state = state_copied
                                        states_or.append(state_copied)
                                        print(f"states_or {states_or}")
                                    
                            else:
                                states_model[i+1].append(state)
                        #release
                        if (agent, action) in actions_conditions_releases.keys():
                            for posibility in actions_conditions_releases[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            if boolean:
                                
                                for posibility in actions_conditions_releases[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                        else:
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        states_model[i+1].append(state_copied)
                            else:
                                states_model[i+1].append(state)
                        if boolean_always:                
                            # states_model[i+1].append(state) 
                            for state_or in states_or:
                                states_model[i+1].append(state_or) 

                for states_model in states_models: #remve the same states in model                         
                    states_model[i+1] = [list(x) for x in set(tuple(x) for x in states_model[i+1])]  
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for states_model in states_models:
                            for state in states_model[i+1]:
                                state_copied = copy.deepcopy(state)
                                for formula in formulas:
                                    for fluent in formula:
                                        if fluent in state_copied:
                                            continue
                                        elif "!" in postcondtion:
                                            state_copied.remove(fluent[1:])
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)
                                        else:
                                            state_copied.remove("!"+fluent)
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)                
                            states_model[i+1] = state_new
            print(f"states_models {states_models}")

            for states_model in states_models:
                if len(states_model[len(states_model)-1]) == 0:
                    return False 
                for state in states_model[len(states_model)-1]:
                    formula = query[0].split("possibly ")[1].split(" after")[0]
                    formula2 = None
                    if "or" in formula:
                        formula, formula2 = formula.split(" or ")
                        if formula in state or formula2 in state:
                            break
                    elif "and" in formula:
                        formula, formula2 = formula.split(" and ")
                        if formula in state and formula2 in state:
                            break
                    else:
                        if formula in state:
                            break
                    return False    
            return True

                                
                                
        def activity_query():
            formula_agent = query[0].split("active ")[1].split(" in ")[0]
            for i,(agent, action) in enumerate(parsed_program):
                states[i+1]=[]
                historical_actions.append(action)  
                for state in states[i]:
                    boolean_always = True
                    #impossible
                    if (agent, action) in actions_conditions_impossible.keys():
                        for posibility in actions_conditions_impossible[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break                         
                        if  boolean==True:
                            if agent ==formula_agent:
                                return False
                            continue                             
                    #causes
                    states_or =[]
                    if (agent, action) in actions_conditions.keys():
                        for posibility in actions_conditions[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            for posibility in actions_conditions[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    boolean_always = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            boolean_always = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    # states[i+1].append(state_copied)
                                    if formula_agent == agent:
                                        if state==state_copied:
                                            return False
                                    states_or.append(state_copied)
                                    print(f"states_or {states_or}")

                                else:
                                    if formula_agent == agent:
                                        return False
                        else:
                            if formula_agent == agent:
                                return False
                            states[i+1].append(state)

                    if boolean_always:
                        # states[i+1].append(state) 
                        for state_or in states_or:
                            states[i+1].append(state_or) 
                    #release
                    if (agent, action) in actions_conditions_releases.keys():
                        if formula_agent == agent:
                            return False
                        for posibility in actions_conditions_releases[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions_releases[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    states[i+1].append(state_copied)
                        else:
                            states[i+1].append(state)
                    
                                        
                states[i+1] = [list(x) for x in set(tuple(x) for x in states[i+1])]
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for state in states[i+1]:
                            state_copied = copy.deepcopy(state)
                            for formula in formulas:
                                for fluent in formula:
                                    if fluent in state_copied:
                                        continue
                                    elif "!" in postcondtion:
                                        state_copied.remove(fluent[1:])
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                                    else:
                                        state_copied.remove("!"+fluent)
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                        states[i+1] = state_new
            return True            
                        

        def realizability_query_always():
            for i,(agent, action) in enumerate(parsed_program):
                states[i+1]=[]
                historical_actions.append(action)  
                for state in states[i]:
                    boolean_always  = True
                    #impossible
                    if (agent, action) in actions_conditions_impossible.keys():
                        for posibility in actions_conditions_impossible[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break                         
                        if  boolean==True:
                            return False
                            continue                             
                    #causes
                    states_or =[]
                    if (agent, action) in actions_conditions.keys():
                        for posibility in actions_conditions[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    boolean_always = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            boolean_always = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    # states[i+1].append(state_copied)
                                    # state = state_copied
                                    states_or.append(state_copied)
                                    print(f"states_or {states_or}")
                                else:
                                    return False    
                        else:
                            states[i+1].append(state)
                    #release
                    if (agent, action) in actions_conditions_releases.keys():
                        for posibility in actions_conditions_releases[(agent,action)][0]:
                            boolean = True
                            for fluent in posibility:
                                if not fluent in state:
                                    boolean = False
                                    break
                            if boolean:
                                break
                        if boolean:
                            
                            for posibility in actions_conditions_releases[(agent,action)][1]:
                                state_copied = copy.deepcopy(state)
                                for postcondtion in posibility:
                                    if postcondtion in state_copied:
                                        continue
                                    if "!" in postcondtion:
                                        print(f"postcondtion {postcondtion}")
                                        print(f"state_copied {state_copied}")
                                        state_copied.remove(postcondtion[1:])
                                        state_copied.append(postcondtion)
                                    else:
                                        state_copied.remove("!"+postcondtion)
                                        state_copied.append(postcondtion)
                                #always        
                                for posibility2 in statments["always"]:
                                    boolean = True
                                    for fluent in posibility2:
                                        if not fluent in state_copied:
                                            boolean = False
                                            break
                                    if boolean:
                                        break
                                if boolean:                   
                                    states[i+1].append(state_copied)
                                else:
                                    return False

                        else:
                            states[i+1].append(state)   
                    if boolean_always:             
                        # states[i+1].append(state) 
                        for state_or in states_or:
                            states[i+1].append(state_or) 
                                        
                states[i+1] = [list(x) for x in set(tuple(x) for x in states[i+1])]
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for state in states[i+1]:
                            state_copied = copy.deepcopy(state)
                            for formula in formulas:
                                for fluent in formula:
                                    if fluent in state_copied:
                                        continue
                                    elif "!" in postcondtion:
                                        state_copied.remove(fluent[1:])
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                                    else:
                                        state_copied.remove("!"+fluent)
                                        state_copied.append(fluent)
                                        state_new.append(state_copied)
                        states[i+1] = state_new
            return True



        def realizability_query_ever():
            states_models = []
            for state in states[0]:
                states_models.append({0:[state]})
            for i,(agent, action) in enumerate(parsed_program):
                for states_model in states_models:
                    states_model[i+1]=[]
                historical_actions.append(action)  
                for states_model in states_models:
                    for state in states_model[i]:
                        boolean_always = True 
                        #impossible
                        if (agent, action) in actions_conditions_impossible.keys():
                            for posibility in actions_conditions_impossible[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break                         
                            if  boolean==True:
                                continue                             
                        #causes
                        states_or =[]
                        if (agent, action) in actions_conditions.keys():
                            for posibility in actions_conditions[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            if boolean:
                                
                                for posibility in actions_conditions[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                        else:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        boolean_always = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                boolean_always = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        # states[i+1].append(state_copied)
                                        # state = state_copied
                                        states_or.append(state_copied)
                                        print(f"states_or {states_or}")
                            else:
                                states_model[i+1].append(state)
                        #release
                        if (agent, action) in actions_conditions_releases.keys():
                            for posibility in actions_conditions_releases[(agent,action)][0]:
                                boolean = True
                                for fluent in posibility:
                                    if not fluent in state:
                                        boolean = False
                                        break
                                if boolean:
                                    break
                            if boolean:
                                for posibility in actions_conditions_releases[(agent,action)][1]:
                                    state_copied = copy.deepcopy(state)
                                    for postcondtion in posibility:
                                        if postcondtion in state_copied:
                                            continue
                                        if "!" in postcondtion:
                                            print(f"postcondtion {postcondtion}")
                                            print(f"state_copied {state_copied}")
                                            state_copied.remove(postcondtion[1:])
                                            state_copied.append(postcondtion)
                                        else:
                                            state_copied.remove("!"+postcondtion)
                                            state_copied.append(postcondtion)
                                    #always        
                                    for posibility2 in statments["always"]:
                                        boolean = True
                                        for fluent in posibility2:
                                            if not fluent in state_copied:
                                                boolean = False
                                                break
                                        if boolean:
                                            break
                                    if boolean:                   
                                        states_model[i+1].append(state_copied)
                            else:
                                states_model[i+1].append(state)
                        if boolean_always:
                            # states_model[i+1].append(state) 
                            for state_or in states_or:
                                states_model[i+1].append(state_or) 

                for states_model in states_models: #remve the same states in model                         
                    states_model[i+1] = [list(x) for x in set(tuple(x) for x in states_model[i+1])]  
                for k in after_sequences.keys():
                    n = len(k)
                    last_n_actions = historical_actions[-n:]
                    if tuple(last_n_actions) == k:
                        formulas = after_sequences[k]
                        state_new = []
                        for states_model in states_models:
                            for state in states_model[i+1]:
                                state_copied = copy.deepcopy(state)
                                for formula in formulas:
                                    for fluent in formula:
                                        if fluent in state_copied:
                                            continue
                                        elif "!" in postcondtion:
                                            state_copied.remove(fluent[1:])
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)
                                        else:
                                            state_copied.remove("!"+fluent)
                                            state_copied.append(fluent)
                                            state_new.append(state_copied)                
                            states_model[i+1] = state_new

            for states_model in states_models:
                state_tab = states_model[len(states_model)-1]
                if len(state_tab)==0:
                    return False
            return True                     
                    


if "active" in query[-1]:
    answer = activity_query()
    print(answer)
elif "necessary" in query[-1]:
    answer = value_query_necessary()
    print(answer)
elif "possibly" in query[-1]:
    answer = value_query_possibly()
    print(answer)
elif "always" in query[-1]:
    answer = realizability_query_always()
    print(answer)
elif "ever" in query[-1]:
    answer = realizability_query_ever()
    print(answer)
    
else:
    print("blad")


print(f"states {states}")
print(answer)
