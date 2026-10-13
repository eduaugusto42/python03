#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = parse_inventory()
    print(f"Got inventory: {inventory}")
    keys: list[str] = list(inventory.keys())
    print(f"Item list: {keys}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(keys)} items: {total}")
    if total != 0:
        for key in keys:
            print(
                f"Item {key} represents "
                f"{round((inventory[key] / total) * 100, 1)}%"
            )
    most_item: str = ""
    most_qty: int = -1
    least_item: str = ""
    least_qty: float = float("inf")
    for key in keys:
        qty: int = inventory[key]
        if qty > most_qty:
            most_qty = qty
            most_item = key
        if qty < least_qty:
            least_qty = qty
            least_item = key
    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for item in sys.argv[1:]:
        parts: list[str] = item.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{item}'")
            continue
        key: str = parts[0].strip()
        value_str: str = parts[1].strip()
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value_str)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
    return inventory


if __name__ == "__main__":
    main()
