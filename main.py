#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from senators_average_age import senators_average_age
from senators_parity import senators_parity

if __name__ == "__main__":
    average = senators_average_age()
    print(
        f"Les scénateurs actifs français ont une moyenne d'âge de {average}\
 ans."
    )
    parity = senators_parity()
    print(f"Le pourcentage de femmes au sénat est de {parity}%")
