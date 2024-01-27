class MonkeyBananaProblem:
    def __init__(self):
        self.state = {
            'monkey': 'on floor',
            'banana': 'hung from ceiling',
            'block': 'near window'
        }
        self.goal_state = {
            'monkey': 'has banana',
            'banana': 'hung from ceiling',
            'block': 'under monkey' 
        }
        self.actions = [
            'walk to window',
            'drag chair to center',
            'climb chair',
            'grab banana'
        ]

    def is_goal_state(self):
        return self.state == self.goal_state

    def execute_action(self, action):
        if action == 'walk to window':
            if self.state['monkey'] == 'on floor':
                self.state['monkey'] = 'near window'
        elif action == 'drag chair to center':
            if self.state['block'] == 'near window':
                self.state['block'] = 'center'
        elif action == 'climb chair':
            if self.state['monkey'] == 'near window' and self.state['block'] == 'center':
                self.state['monkey'] = 'on block'
                self.state['block'] = 'under monkey'
        elif action == 'grab banana':
            if self.state['monkey'] == 'on block':
                self.state['monkey'] = 'has banana'
        else:
            print("Invalid action!")

    def solve(self):
        plan = []
        while not self.is_goal_state():
            possible_actions = []
            for action in self.actions:
                temp_state = self.state.copy()
                self.execute_action(action)
                if temp_state != self.state:  
                    possible_actions.append(action)
                self.state = temp_state
            if len(possible_actions) == 0:
                print("No solution found!")
                break
            chosen_action = possible_actions[0]
            self.execute_action(chosen_action)
            plan.append(chosen_action)
            print(f"Performed action: {chosen_action}")
        print("Plan to get the banana:", plan)


if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    problem.solve()
