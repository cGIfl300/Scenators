#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import datetime


def age_moyen_scenateurs():
    """return the average age of france's senators."""
    current_year = int(datetime.datetime.now().year)
    with open(
            "data/odsen_general.csv", encoding="utf-8", newline=""
    ) as csvfile:
        reader = csv.DictReader(csvfile, quotechar="%")
        total_years = 0
        total_senators = 0
        for row in reader:
            birth_date = int(row["Date naissance"][0:4])
            age_scenator = current_year - birth_date
            if row["etat"] == "ACTIF":
                total_years += age_scenator
                total_senators += 1
    return int(total_years / total_senators)


if __name__ == "__main__":
    average = age_moyen_scenateurs()
    print(
        f"Les scénateurs actifs français ont une moyenne d'âge de {average}\
ans."
    )
