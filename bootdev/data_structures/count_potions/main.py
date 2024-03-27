def count_potions(inventory):
    for i in inventory: 
        count = 0
        if inventory[i] == "Healing potion":
            count += 1
    return count
