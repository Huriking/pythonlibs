actions = {
    "Get Ingredients": {
        "needs": [],
        "gives": ["Have Ingredients"]
    },
    "Preheat Oven": {
        "needs": [],
        "gives": ["Oven Ready"]
    },
    "Mix Ingredients": {
        "needs": ["Have Ingredients"],
        "gives": ["Batter Ready"]
    },
    "Pour Batter": {
        "needs": ["Batter Ready"],
        "gives": ["Pan Ready"]
    },
    "Bake Cake": {
        "needs": ["Pan Ready", "Oven Ready"],
        "gives": ["Cake Baked"]
    }
}

done_things = set()
final_goal = "Cake Baked"
all_goals = [final_goal]
plan_steps = []

while final_goal not in done_things:
    current_step = []

    for action, data in actions.items():
        if action in done_things:
            continue
        if all(need in done_things for need in data["needs"]):
            current_step.append(action)

    if not current_step:
        print("Goal State cannot be reached.")
        break

    for action in current_step:
        done_things.add(action)
        for result in actions[action]["gives"]:
            done_things.add(result)
            all_goals.append(result)

    plan_steps.append(current_step)

print("The plan to bake cake: ")
for i, step in enumerate(plan_steps, 1):
    print(f"Step {i}: {', '.join(step)}")
