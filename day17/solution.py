# target_area = {"x": [20,30], "y": [-10,-5]} # sample
target_area = {"x": [34, 67], "y": [-215, -186]}  # input


class Probe:
    def __init__(self, start_position, start_velocity):
        self.position = start_position
        self.start_velocity = start_velocity  # part 2
        self.velocity = start_velocity
        self.past_target = False
        self.steps = 0
        self.max_y = -(2 ** 31)

    def __repr__(self):
        return f"steps: {self.steps} max y: {self.max_y} position: {self.position} velocity: {self.velocity} past_target: {self.past_target}"

    def decay(self):

        self.position = [
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        ]
        # print(f"position: {self.position} velocity: {self.velocity}")

        if self.velocity[0] > 0:
            self.velocity[0] -= 1
        elif self.velocity[0] < 0:
            self.velocity[0] += 1

        self.velocity[1] -= 1

        self.steps += 1

        if self.position[1] > self.max_y:
            self.max_y = self.position[1]

    def check_hit(self, area):
        if self.position[0] in range(area["x"][0], area["x"][1] + 1) and self.position[
            1
        ] in range(area["y"][0], area["y"][1] + 1):
            return self.position
        else:
            if self.position[0] > area["x"][1] or self.position[1] < area["y"][0]:
                self.past_target = True
            return False


# part 1
max_y = 0
# part 2, add
starting_velocities_hits = []
for i in range(
    -1000, 1001
):  # range(abs(target_area["y"][0]) + 1): you know what just make the range big
    for j in range(0, 1001):  # range(target_area["x"][1] + 1):
        probe = Probe(start_position=[0, 0], start_velocity=[j, i])
        while probe.past_target == False and probe.check_hit(target_area) == False:
            probe.decay()

        if probe.check_hit(target_area):
            if probe.max_y > max_y:
                max_y = probe.max_y
            starting_velocities_hits.append(tuple(probe.start_velocity))

print(max_y)  # part 1
print(len(starting_velocities_hits))  # part 2
