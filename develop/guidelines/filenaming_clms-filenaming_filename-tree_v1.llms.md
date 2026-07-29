# CLMS Product Filenaming - Filename Tree

Copernicus Land Monitoring Service - Technical Library

This document presents the “Filename Tree” for Copernicus Land Monitoring Service (CLMS) products, offering a structured, visual guide to all valid filename variants. It serves as a practical reference for understanding and constructing CLMS product filenames, detailing the hierarchical options for each field. The tree systematically illustrates choices for product codes, temporal coverage, spatial resolution, geographic extent, and product variables, supported by concrete examples. Designed to complement the CLMS Filenaming Design Principles, this guide facilitates accurate data identification and ensures consistency across the CLMS data catalogue.

Author

European Environment Agency (EEA)

Published

July 24, 2026

Keywords

CLMS filenaming conventions, product naming taxonomy, filename structure, temporal coverage formats, spatial resolution types, geographic extent identifiers, product variable codes, data catalogue schema, MGRS tiling system, LAEA 100km grid, functional urban areas, Copernicus Land Monitoring Service

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

# 1 CLMS Product Filenaming - Filename Tree

*A visual navigation of all possible CLMS filename variants. Each level shows the options for that field. All structural variants are shown, but the lists of variables, tiles, dates & values are exemplary - not exhaustive.*

------------------------------------------------------------------------

    CLMS_{CODE}-{VARIABLE}[-{SUBVARIABLE}]_{TEMPORAL}_{RES}_{EXTENT}_{EPSG}_{VERSION}-{REVISION}.ext

## 1.1 By Product Code

    CLMS_
    ├── VLCC-                          Vegetated Land Cover Characteristics (upgraded HRL)
    │   ├── GRA_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── DLT_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   └── CTY_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── HRL-                           High Resolution Layers (legacy, not yet upgraded)
    │   ├── TCD_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── FTY_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── IMD_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── IBU_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── WAW_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── SWF_S{YYYY}_R5m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── TCD_C{YYYY}-{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   └── IMD_C{YYYY}-{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── NVLCC-                         Non-Vegetated Land Cover Characteristics
    │   └── IMCCS_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── SLF-                           Small Landscape Features
    │   └── SFW_S{YYYY}_R5m_E{XXX}N{YYY}_3035_V01-R01.tif
    │
    ├── WSI-                           Water & Snow/Ice
    │   ├── SP-SCD_A{YYYYMMDD}P1Y_R20m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   ├── SWS-WSM_{YYYYMMDD}T{HHMMSS}_R60m_T{ZZ}{GZD}{AA}_S1B_V01-R00.tif
    │   └── WDS-SSC_{YYYYMMDD}T{HHMMSS}_R60m_T{ZZ}{GZD}{AA}_S1B_V01-R00.tif
    │
    ├── EUHYDRO-                       EU Hydro
    │   └── NET_S{YYYY}_R10m_EUROPE_3035_V02-R00.gpkg
    │
    ├── UA-                            Urban Atlas
    │   ├── LCU_S{YYYY}_V025ha_{FUA}_3035_V01-R00.gpkg
    │   └── LCU_C{YYYY}-{YYYY}_V025ha_{FUA}_3035_V01-R00.gpkg
    │
    ├── CLCPLUS-                       CLC+ Raster
    │   └── LCU_S{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── VPP2-                          Vegetation Phenology & Productivity v2
    │   ├── ST-PPI_A{YYYYMMDD}P10D_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   ├── VPP-SOSD-S1_A{YYYYMMDD}P1Y_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   ├── GPP-TOTAL_A{YYYYMMDD}P1Y_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   └── GPP-TOTAL-QFLAG_A{YYYYMMDD}P1Y_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │
    ├── CLC-                           Corine Land Cover
    │   └── LCU_S{YYYY}_V25ha_EUROPE_3035_V01-R00.gpkg
    │
    └── EGMS-                          European Ground Motion Service
        ├── L3-U_T{YYYYMMDD}P{duration}_V100m_E{XXX}N{YYY}_3035_V01-R00.csv
        ├── L3-EW_T{YYYYMMDD}P{duration}_R100m_E{XXX}N{YYY}_3035_V01-R00.tif
        ├── L2a-A_T{YYYYMMDD}P{duration}_V20-5m_{Orbit}-{BurstID}-{SubSwath}_V01-R00.csv
        └── L2b-D_T{YYYYMMDD}P{duration}_V20-5m_{Orbit}-{BurstID}-{SubSwath}_V01-R00.csv

## 1.2 By Temporal Situation

    {TEMPORAL}_
    ├── {YYYYMMDD}T{HHMMSS}_           Sensing instant    (satellite scene)
    │   └── e.g. 20210217T053159_
    │
    ├── A{YYYYMMDD}P{duration}_        Aggregated          (sub-annual composite)
    │   ├── A20240101P10D_             dekadal
    │   ├── A20240101P1M_              monthly
    │   └── A20240101P1Y_              annual NRT
    │
    ├── S{YYYY}_                       Status              (single reference year)
    │   └── S2021_
    │
    ├── C{YYYY}-{YYYY}_                Change              (change between two Status years)
    │   └── C2018-2021_                3-year change
    │
    └── T{YYYYMMDD}P{duration}_        Timeseries          (multi-year aggregate)
        └── T20190101P5Y_              5-year timeseries

## 1.3 By Resolution

    {RES}_
    ├── R{value}[unit]_                     Raster (pixel spacing)
    │   ├── R1m
    │   ├── R5m
    │   ├── R10m
    │   ├── R20m
    │   ├── R60m
    │   ├── R100m
    │   ├── R300m
    │   ├── R1km
    │   └── R20-5m                          irregular grid
    │
    └── V{value}[unit]_                    Vector MMU / point grid
        ├── V025ha                          vector MMU 0.25ha
        ├── V25ha                           vector MMU 25ha
        ├── V100m                           point grid (regular)
        └── V20-5m                          point grid (irregular)

## 1.4 By Spatial Extent

    {EXTENT}_
    ├── T{ZZ}{GZD}{AA}_                MGRS               (S2 raster tile)
    │   └── T33UVS_
    │
    ├── E{XXX}N{YYY}_                  LAEA 100km         (pan-European grid)
    │   └── E27N48_
    │
    ├── {Orbit}-{BurstID}-{SubSwath}_  IW burst           (EGMS InSAR swath)
    │   └── 054-0154-IW1_
    │
    ├── {NNN}{CC}C{L}_                 FUA code           (Functional Urban Area)
    │   └── DK004L3_
    │
    ├── {CC}_                          Country code       (nation-level vector)
    │   ├── DE_
    │   └── IT_
    │
    ├── DU{NNN}_                       Delivery Unit      (large-area tiling)
    │   └── DU001_
    │
    ├── EUROPE_                        Continental        (entire European continent)
    │
    ├── NORTHERNHEMISPHERE_            Hemispherical      (Northern Hemisphere)
    │
    ├── SOUTHERNHEMISPHERE_            Hemispherical      (Southern Hemisphere)
    │
    └── GLOBAL_                        Global             (full Earth coverage)

## 1.5 By Variable (Sub-product)

*The variable is hyphen-appended to the product code at position 2:* `CLMS_{CODE}-{VARIABLE}[-{SUBVARIABLE}]_…`

    {CODE}-{VARIABLE}_
    ├── {PARAM}                        Single token       (VLCC, NVLCC, SLF, HRL)
    │   ├── GRA, DLT, CTY              (VLCC)
    │   ├── IMCCS, SBCC, SFW, CM       (NVLCC, SLF)
    │   ├── TCD, FTY, IMD, IBU, WAW    (HRL - 10m)
    │   └── SWF                         (HRL - 5m)
    │
    ├── {SUB}-{PARAM}                  Two-level          (WSI, VPP2)
    │   ├── SP-SCD
    │   ├── SWS-WSM, WDS-SSC
    │   └── ST-PPI, VPP-SOSD, GPP-TOTAL
    │
    ├── {SUB}-{PARAM}-{SEASON}         With season        (VPP2)
    │   ├── VPP-SOSD-S1
    │   └── GPP-SEASONAL-S1
    │
    ├── {SUB}[-{PARAM}]-QFLAG          Quality flag       (all products)
    │   ├── ST-PPI-QFLAG               (leaf-level)
    │   ├── VPP-SOSD-QFLAG             (product-level)
    │   └── VPP-QFLAG                  (family-level)
    │
    ├── LCU                            Land Cover Land Use status/change   (UA, CLC, CLCPLUS, RZ, …)
    │
    ├── L3-U, L3-EW                    EGMS velocity grid  (EGMS L3)
    │
    ├── L2a-A, L2a-D, L2b-A, L2b-D    EGMS calibrated     (EGMS L2)
    │
    └── NET, DIR, SUB                  EU Hydro            (EUHYDRO)

## 1.6 Full Example Walkthrough

    CLMS_
         ├── WSI-SP-SCD_                  Water & Snow/Ice - Snow Cover Duration
         │   └── A20240101P1Y_            annual composite
         │       └── R20m_                raster 20m
         │           └── T38TKL_          MGRS tile
         │               └── 3035_        EPSG 3035
         │                   └── V01-R00.tif  version 1, revision 0
         │
         └── EGMS-L2a-A_                  European Ground Motion - L2a ascending
             └── T20190101P5Y_            5-year timeseries
                 └── R20-5m_              irregular grid 20x5m
                     └── 054-0154-IW1_    IW burst
                         └── V01-R00.tif  version 1, revision 0

------------------------------------------------------------------------

*Tree version: draft. Each branch represents a valid structural variant of the CLMS filename convention. See CLMS_Filenaming_Design_Principles.md for the full rules.*

Back to top

## Reuse

EUPL (\>= 1.2)
