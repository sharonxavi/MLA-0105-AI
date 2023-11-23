class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position = 'Start'  
        self.has_box = False  
        self.bananas_reached = False  
    def move(self, action):
        if action == 'Climb':
            if self.monkey_position == 'Start' and self.has_box:
                self.monkey_position = 'OnBox'
                print("Monkey climbed on the box.")
            else:
                print("Can't climb. Position or box status is incorrect.")
        elif action == 'Push':
            if self.monkey_position == 'Start' and not self.has_box:
                self.has_box = True
                print("Monkey pushed the box.")
            else:
                print("Can't push the box. Position or box status is incorrect.")
        elif action == 'Reach':
            if self.monkey_position == 'OnBox' and self.has_box:
                self.bananas_reached = True
                print("Monkey reached the bananas!")
            else:
                print("Can't reach the bananas. Position or box status is incorrect.")
        else:
            print("Invalid action.")

    def get_status(self):
        print(f"Monkey position: {self.monkey_position}")
        print(f"Has box: {self.has_box}")
        print(f"Bananas reached: {self.bananas_reached}")

mb_problem = MonkeyBananaProblem()

mb_problem.get_status() 

mb_problem.move('Push')
mb_problem.move('Climb')
mb_problem.move('Reach')

mb_problem.get_status()  
