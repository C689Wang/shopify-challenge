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
                continue
            elif person in self.relationshMap and self.relationshMap[person] == picked:
                continue
            elif picked in self.already_picked:
                continue
            break
        self.already_picked.add(picked)
        return picked
        
    def draw_all(self):
        ## answer : [["Person1", "Person2"]]
        answer = []
       
        for person in self.people:
            drawed_person = self.draw_name(person)
            answer.append([person, drawed_person])
        
        return answer
        
game = DrawingMachine(["P", "C", "A", "D"], [["P", "A"]])

assignments = game.draw_all()
print(assignments)