#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analisys ===")
    inventory = parse_inventory()
    print(f"Got inventory: {inventory}")
    keys = list(inventory.keys())
    print(f"Item list: {keys}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(keys)} items: {total}")
    most = keys[0]
    least = keys[0]
    for key in keys:
        print(
                f"Item {key} represents "
                f"{round((inventory[key] / total) * 100, 1)}%"
                )
        if inventory[key] > inventory[most]:
            most = key
        if inventory[key] < inventory[least]:
            least = key
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory['magic_item'] = 1
    print(f"Updated inventory: {inventory}")


def parse_inventory() -> dict[str, int]:
    inventory = {}

    for item in sys.argv[1:]:
        if len(item.split(':')) != 2:
            print(f"Error - invalid parameter '{item}'")
            continue
        key, value = item.split(':')
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
    return inventory


if __name__ == "__main__":
    main()
