class Robot():
    def __init__(self, nome, massa, tipologia):
        self.nome = nome
        self.massa = massa
        if(tipologia == "umanoide"):
            self.tipologia = tipologia
        else:
            self.tipologia = "no"
    def stampaNome(self):
        print(f"Nome del robot: {self.nome}")
       
    def pericolositàRobot(self):
        return (self.tipologia == "umanoide" and self.massa > 100)

def main():
    robot = Robot("a", 120, "umanoide")
    robot1 = Robot("b", 90, "umanoide")
    robot.stampaNome()
    robot.pericolositàRobot()
    robot1.stampaNome()
    if(robot1.pericolositàRobot() == True):
        print("è pericoloso")
    else:
        print("non è pericoloso")

if __name__ == "__main__":
    main()