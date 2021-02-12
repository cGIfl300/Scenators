import csv


def senators_parity():
    """return the % of women senators"""
    with open(
            "data/odsen_general.csv", encoding="utf-8", newline=""
    ) as csvfile:
        reader = csv.DictReader(csvfile, quotechar="%")
        total_senators = 0
        total_women = 0
        for row in reader:
            is_woman = row["Qualite"] != "M."
            if is_woman:
                total_women += 1
            total_senators += 1

    return int(total_women * 100 / total_senators)
