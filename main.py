import pandas as pd
import numpy as np


# Data Cleaning Functions

def fill_missing_english(df):
    """Replace missing English marks with column average"""
    df["english"].fillna(df["english"].mean(), inplace=True)
    return df


# Academic Calculation Functions

def calculate_total(df):
    """Add Total column"""
    df["Total"] = df["math"] + df["english"] + df["science"]
    return df

def calculate_average(df):
    """Add Average column"""
    df["Average"] = df["Total"] / 3
    return df


# Grading and Result Functions

def assign_grades(df):
    """Assign Grade based on Average"""
    conditions = [
        df["Average"] >= 80,
        df["Average"] >= 70,
        df["Average"] >= 60,
        df["Average"] >= 50
    ]
    grades = ["A+", "A", "B", "C"]
    df["Grade"] = np.select(conditions, grades, default="F")
    return df

def assign_result(df):
    """Assign Pass/Fail based on Grade"""
    df["Result"] = df["Grade"].apply(
        lambda x: "Pass" if x in ["A+", "A", "B", "C"] else "Fail"
    )
    return df


# Ranking Functions

def assign_rank(df):
    """Rank students based on Total marks"""
    df["Rank"] = df["Total"].rank(ascending=False, method="dense").astype(int)
    df = df.sort_values("Rank")
    return df
