## Rules
## Drawing own name disallowed
## Drawing partners name disallowed

import random

class DrawingMachine:
    
    ## 2d array [["Person1", "Person2"]]
    ## people ["Person1", "Person2"]
    def __init__(self, people, relationships):
        self.people = people
        self.already_picked = set()
        self.relationshMap = dict()
        for i in range(len(relationships)):
            self.relationshMap[relationships[i][0]] = relationships[i][1]
            self.relationshMap[relationships[i][1]] = relationships[i][0]
        
    def draw_name(self, person):
        while True:
            random_index = random.randint(0, len(self.people) - 1)
            picked = self.people[random_index]
            if picked == person:
                if len(self.already_picked) == len(self.people) - 1 and person not in self.already_picked:
                    return None
                continue
            elif picked in self.already_picked:
                continue
            elif person in self.relationshMap and self.relationshMap[person] == picked:
                if len(self.already_picked) == len(self.people) - 1:
                    return None
                elif len(self.already_picked) == len(self.people) - 2 and person not in self.already_picked:
                    return None
                continue
            break
        self.already_picked.add(picked)
        return picked
        
    def draw_all(self):
        ## answer : [["Person1", "Person2"]]
        answer = []
        restart = False
       
        ## Need to take care of edge case where last person is stuck with an
        ## invalid person. In that case restart
        while True:
            self.already_picked = set()
            answer = []
            restart = False
            for person in self.people:
                drawed_person = self.draw_name(person)
                if drawed_person == None:
                    restart = True
                    break
                answer.append([person, drawed_person])
            if restart: continue
            else: break
        
        return answer
        
game = DrawingMachine(["P", "C", "D", "A", "E", "G", "RR"], [["P", "A"], ["E", "C"], ["RR", "G"]])

assignments = game.draw_all()
print(assignments)