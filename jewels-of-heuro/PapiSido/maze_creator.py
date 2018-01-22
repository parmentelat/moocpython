# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:08:13 2018

@author: franc
"""

from jewels import save_tabrect as save
import numpy as np

def austria101(fname ="austria101"):
    with open(fname + ".txt", "r", encoding='utf-8')as fload:
        l0 = fload.readline()
        dim1 = int(l0)
        print(f"lecture de {fname}.txt => dim1 {dim1}")
        table = []
        for ss in fload:
            print(ss)
            ligne = []
            for i in range(dim1):
                sd = ss[7*i + 1:7*i+8]
                ligne = ligne + [int(sd)]
            table.append(ligne)
            print(ligne)
    print(table)
    save(fname, table)


if __name__ == "__main__":
    austria101("austria101")
