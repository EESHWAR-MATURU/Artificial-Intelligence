def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    jug1_current = 0
    jug2_current = 0

    while jug1_current != target_amount and jug2_current != target_amount:
        print(
            f"Jug 1: {jug1_current}/{jug1_capacity} | Jug 2: {jug2_current}/{jug2_capacity}")

        if jug1_current == 0:
            jug1_current = jug1_capacity
        elif jug2_current == jug2_capacity:
            jug2_current = 0
        else:
            transfer_amount = min(jug1_current, jug2_capacity - jug2_current)
            jug1_current -= transfer_amount
            jug2_current += transfer_amount

    print(
        f"Jug 1: {jug1_current}/{jug1_capacity} | Jug 2: {jug2_current}/{jug2_capacity}")
    print("Goal achieved!")


water_jug_problem(4, 3, 2)
