import os

import pandas as pd
# import geopandas as gpd

from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# response = supabase.rpc("create_well_table").execute()

# gdf = gpd.read_parquet("wells.geoparquet")

# def check(line, srid = 4326):
#     if line is None:
#         return None
    
#     if line.is_empty:
#         return None
    
#     for x, y in line.coords:
#         if pd.isna(x) or pd.isna(y):
#             return None
    
#     if line.geom_type == "Point":
#         return f"SRID={srid};{line.wkt}"

# for index, row in enumerate(gdf.itertuples()):
#     new_row = {
#         "well": str(row.well),
#         "field": str(row.field),
#         "platform": str(row.platform),
#         "mapview": None if row.xy is None else f"SRID={4326};{row.xy.wkt}",
#     }
#     # supabase.table("well").insert(new_row).execute()
#     if row.well == "C29":
#         print(row.well, row.field, row.platform)
#     # print(f"Success in row number: {index}")
# else:
#     print("Done!")


# new_row = {
#     "well": 'C29Y',
#     "field": 'ACG',
#     "platform": 'WA',
#     "mapview": None,
# }

# well_well = supabase.table("well").select("well").execute()
# rate_well = supabase.table("rate").select("well").execute()
# rate_well = supabase.table("unique_rate_wells").select("well").execute()

# print(well_well)

# print(len(well_well.data))
# print(len(rate_well.data))

# print(rate_well)

# well_well = pd.DataFrame(well_well.data)
# rate_well = pd.DataFrame(rate_well.data)

# print(well_well['well'])
# print(rate_well['well'])

# print(rate_well['well'].unique())
# print(well_well['well'].unique())

# conds = rate_well['well'].isin(well_well['well'])
# missing = rate_well['well'].loc[~conds]

# print(rate_well['well'] - well_well['well'])

# for index, row in enumerate(gdf.itertuples()):
#     if row.well == "A12":
#         print(row.well, row.field, row.platform)

# print(missing)

# supabase.table("well").insert(new_row).execute()