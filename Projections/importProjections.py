
import pandas as pd
import numpy as np
import tabula 

def importPDFProjections():
    tabula.convert_into(f"\\Projections\\NFLDK2024_CS_ClayProjections2024.pdf","Projections\\Qb2-projections.csv",output_format="csv",pages="35")
    tabula.convert_into(f"\\Projections\\NFLDK2024_CS_ClayProjections2024.pdf","Projections\\Rb2-projections.csv",output_format="csv",pages="36-38")
    tabula.convert_into(f"\\Projections\\NFLDK2024_CS_ClayProjections2024.pdf","Projections\\Wr2-projections.csv",output_format="csv",pages="39-43")
    tabula.convert_into(f"\\Projections\\NFLDK2024_CS_ClayProjections2024.pdf","Projections\\Te2-projections.csv",output_format="csv",pages="44,45")
    return

def get_Projections():
    qb = pd.read_csv("Projections\\Qb2-projections.csv")
    rb = pd.read_csv("Projections\\Rb2-projections.csv")
    wr = pd.read_csv("Projections\\Wr2-projections.csv")
    te = pd.read_csv("Projections\\Te2-projections.csv")
    d = pd.read_csv("Projections\\D2-projections.csv")
    k = pd.read_csv("Projections\\K2-projections.csv")

    df = pd.concat([qb,rb,wr,te,d,k],ignore_index=True)

    df.to_csv("Projections\\combined2-projections.csv")
    return df

def main():
    df = get_Projections()


if __name__ == '__main__':
    main()