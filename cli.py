"""Interactive pricing calculator for Vie Limo employees.

Run with:  python3 cli.py
"""

from all_hotels import HOTELS, REGION_NAMES
from pricing_calculator import calculate_price

DAY_TYPES = [
    ("weekday", "Weekday (Sun–Thu)"),
    ("friday", "Friday"),
    ("saturday", "Saturday"),
]

BOOKING_TYPES = [
    ("room", "Room only"),
    ("combo", "Combo (night 1 combo rate + room rate after)"),
]


def vnd(amount):
    """Format a number as VND with comma separators, e.g. 1500000 -> '1,500,000đ'."""
    return f"{int(amount):,}đ"


def choose(prompt, options):
    """Show a numbered menu and return the chosen option.

    ``options`` is a list of ``(value, label)`` tuples. Returns the chosen
    ``value``. Re-prompts until a valid number is entered.
    """
    print(f"\n{prompt}")
    for i, (_, label) in enumerate(options, start=1):
        print(f"  {i}. {label}")

    while True:
        raw = input("Enter number: ").strip()
        if not raw.isdigit():
            print("  ! Please enter one of the numbers shown.")
            continue
        idx = int(raw)
        if 1 <= idx <= len(options):
            return options[idx - 1][0]
        print(f"  ! Please enter a number between 1 and {len(options)}.")


def ask_int(prompt, minimum=0):
    """Prompt for a whole number >= ``minimum``. Re-prompts on invalid input."""
    while True:
        raw = input(f"{prompt}: ").strip()
        if not raw.lstrip("-").isdigit():
            print("  ! Please enter a whole number.")
            continue
        value = int(raw)
        if value < minimum:
            print(f"  ! Please enter a number >= {minimum}.")
            continue
        return value


def ask_yes_no(prompt):
    """Return True for yes, False for no."""
    while True:
        raw = input(f"{prompt} (y/n): ").strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  ! Please answer y or n.")


def select_region():
    options = [(key, REGION_NAMES.get(key, key)) for key in HOTELS]
    return choose("Select a region:", options)


def select_hotel(region):
    options = [
        (key, key.replace("_", " ").title())
        for key in HOTELS[region]
    ]
    return choose("Select a hotel:", options)


def select_room(region, hotel):
    rooms = HOTELS[region][hotel]["rooms"]
    options = []
    for key, data in rooms.items():
        label = data.get("description") or key.replace("_", " ").title()
        options.append((key, label))
    return choose("Select a room type:", options)


def display_result(result):
    """Print a formatted VND breakdown for a calculate_price() result."""
    print("\n" + "=" * 40)
    if result.get("error"):
        print(f"  ⚠  {result['message']}")
        print("=" * 40)
        return

    if result["booking_type"] == "room":
        print("  Booking type:       Room only")
        print(f"  Base price:         {vnd(result['base_price'])}")
        print(f"  Extra adults fee:   {vnd(result['extra_adults_fee'])}")
        print(f"  Child surcharge:    {vnd(result['child_surcharge'])}")
    else:  # combo
        print("  Booking type:       Combo")
        print(f"  Night 1 (combo):    {vnd(result['night_1_combo'])}")
        print(f"  Remaining nights:   {vnd(result['remaining_nights_room'])}")

    print("-" * 40)
    print(f"  TOTAL:              {vnd(result['total'])}")
    print("=" * 40)


def run_one():
    """Walk the employee through a single price calculation."""
    region = select_region()
    hotel = select_hotel(region)
    room_type = select_room(region, hotel)

    print()
    num_adults = ask_int("Number of adults", minimum=1)
    num_children = ask_int("Total number of children", minimum=0)
    children_ages = []
    for i in range(num_children):
        age = ask_int(f"  Age of child {i+1}", minimum=0)
        children_ages.append(age)
    child_free_age = HOTELS[region][hotel].get("child_free_age", 6)
    num_children_free = sum(1 for age in children_ages if age < child_free_age)
    num_children_paid = sum(1 for age in children_ages if age >= child_free_age)
    num_nights = ask_int("Number of nights", minimum=1)
    day_type = choose("Select day type:", DAY_TYPES)
    booking_type = choose("Select booking type:", BOOKING_TYPES)

    result = calculate_price(
        region, hotel, room_type,
        num_adults, num_children_paid, num_nights,
        day_type, booking_type,
    )
    display_result(result)
    print(f"  → {num_children_free} child(ren) free, {num_children_paid} child(ren) charged")


def main():
    print("=" * 40)
    print("   VIE LIMO — Hotel Pricing Calculator")
    print("=" * 40)
    try:
        while True:
            run_one()
            if not ask_yes_no("\nCalculate another price?"):
                break
    except (KeyboardInterrupt, EOFError):
        print()  # tidy newline after ^C / ^D
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
