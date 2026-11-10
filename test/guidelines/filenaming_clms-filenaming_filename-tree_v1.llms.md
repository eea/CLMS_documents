# CLMS Product Filenaming - Filename Tree

Copernicus Land Monitoring Service - Technical Library

This document presents the “Filename Tree” for Copernicus Land Monitoring Service (CLMS) products, offering a structured, visual guide to all valid filename variants. It serves as a practical reference for understanding and constructing CLMS product filenames, detailing the hierarchical options for each field. The tree systematically illustrates choices for product codes, including new EU Hydro products, temporal coverage using ISO 8601 period formats, spatial resolution, geographic extent, and product variables, supported by concrete examples. Designed to complement the CLMS Filenaming Design Principles, this guide facilitates accurate data identification and ensures consistency across the CLMS data catalogue.

Author

European Environment Agency (EEA)

Published

November 6, 2026

Keywords

CLMS filenaming conventions, product naming taxonomy, filename structure, temporal coverage formats, spatial resolution types, geographic extent identifiers, product variable codes, data catalogue schema, MGRS tiling system, LAEA 100km grid, functional urban areas, EU Hydro product naming

  
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
    │   ├── GRA_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── DLT_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   └── CTY_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── HRL-                           High Resolution Layers (legacy, not yet upgraded)
    │   ├── TCD_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── FTY_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── IMD_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── IBU_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── WAW_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── SWF_{YYYY}0101P1Y_R5m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   ├── TCD_C{YYYY}-{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │   └── IMD_C{YYYY}-{YYYY}_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── NVLCC-                         Non-Vegetated Land Cover Characteristics
    │   └── IMCCS_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── SLF-                           Small Landscape Features
    │   └── SFW_{YYYY}0101P1Y_R5m_E{XXX}N{YYY}_3035_V01-R01.tif
    │
    ├── WSI-                           Water & Snow/Ice
    │   ├── SP-SCD_{YYYYMMDD}P1Y_R20m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   ├── SWS-WSM_{YYYYMMDD}T{HHMMSS}_R60m_T{ZZ}{GZD}{AA}_S1B_V01-R00.tif
    │   └── WDS-SSC_{YYYYMMDD}T{HHMMSS}_R60m_T{ZZ}{GZD}{AA}_S1B_V01-R00.tif
    │
    ├── EUHYDRO-                       EU Hydro
    │   └── NET_{YYYY}0101P1Y_R10m_EUROPE_3035_V02-R00.gpkg
    │
    ├── UA-                            Urban Atlas
    │   ├── LCU_{YYYY}0101P1Y_V025ha_{FUA}_3035_V01-R00.gpkg
    │   └── LCU_C{YYYY}-{YYYY}_V025ha_{FUA}_3035_V01-R00.gpkg
    │
    ├── CLCPLUS-                       CLC+ Raster
    │   └── LCU_{YYYY}0101P1Y_R10m_E{XXX}N{YYY}_3035_V01-R00.tif
    │
    ├── VPP2-                          Vegetation Phenology & Productivity v2
    │   ├── ST-PPI_{YYYYMMDD}P10D_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   ├── VPP-SOSD-S1_{YYYYMMDD}P1Y_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   ├── GPP-TOTAL_{YYYYMMDD}P1Y_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │   └── GPP-TOTAL-QFLAG_{YYYYMMDD}P1Y_R10m_T{ZZ}{GZD}{AA}_V01-R00.tif
    │
    ├── CLC-                           Corine Land Cover
    │   └── LCU_{YYYY}0101P1Y_V25ha_EUROPE_3035_V01-R00.gpkg
    │
    └── EGMS-                          European Ground Motion Service
        ├── L3-U_{YYYYMMDD}P{duration}_V100m_E{XXX}N{YYY}_3035_V01-R00.csv
        ├── L3-EW_{YYYYMMDD}P{duration}_R100m_E{XXX}N{YYY}_3035_V01-R00.tif
        ├── L2a-A_{YYYYMMDD}P{duration}_V20-5m_{Orbit}-{BurstID}-{SubSwath}_V01-R00.csv
        └── L2b-D_{YYYYMMDD}P{duration}_V20-5m_{Orbit}-{BurstID}-{SubSwath}_V01-R00.csv

## 1.2 By Temporal Situation

    {TEMPORAL}_
    ├── {YYYYMMDD}T{HHMMSS}_           Sensing instant    (single acquisition)
    │   └── e.g. 20210217T053159_
    │
    ├── {YYYYMMDD}P{duration}_        Period             (start date plus ISO 8601 duration)
    │   ├── 20240101P10D_             dekadal composite
    │   ├── 20240101P1M_              monthly composite
    │   ├── 20240101P1Y_              annual period
    │   ├── 20210101P1Y_              status year
    │   └── 20190101P5Y_              multi-year series
    │
    └── C{YYYY}-{YYYY}_                Change             (change between two reference years)
        └── C2018-2021_                3-year change

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
    ├── {Orbit}-{BurstID}-{SubSwath}_  IW burst           (Sentinel-1 swath)
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
    │   └── SWF                        (HRL - 5m)
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
    ├── L3-U, L3-EW                    EGMS velocity components (EGMS Ortho – L3)
    │
    ├── L2a-A, L2a-D, L2b-A, L2b-D     Orbit (EGMS Calibrated – L2)
    │
    └── NET, DIR, SUB                  EU Hydro            (EUHYDRO)

## 1.6 Full Example Walkthrough

    CLMS_
         ├── WSI-SP-SCD_                  Water & Snow/Ice - Snow Cover Duration
         │   └── 20240101P1Y_            annual period
         │       └── R20m_                raster 20m
         │           └── T38TKL_          MGRS tile
         │               └── 3035_        EPSG 3035
         │                   └── V01-R00.tif  version 1, revision 0
         │
         └── EGMS-L2a-A_                  European Ground Motion - L2a ascending
             └── 20190101P5Y_            5-year period
                 └── R20-5m_              irregular grid 20x5m
                     └── 054-0154-IW1_    IW burst
                         └── V01-R00.tif  version 1, revision 0

------------------------------------------------------------------------

*Tree version: draft. Each branch represents a valid structural variant of the CLMS filename convention. See CLMS_Filenaming_Design_Principles.md for the full rules.*

# 2 Change Log

| Date | Version | Summary |
|----|----|----|
| 2026-11-10 | 1.2.0 | • Updated the entire 'Filename Tree' and 'By Temporal Situation' sections to align with the new temporal naming convention. • Revised numerous example filenames, replacing older 'Status', 'Aggregated', and 'Timeseries' prefixes with the new 'Period' format. • Updated document metadata. |
| 2026-10-29 | 1.1.0 | Initial publication of the 'CLMS Product Filenaming - Filename Tree' document, offering a visual and structured navigation of CLMS filename variants by product code, temporal situation, resolution, spatial extent, and variable. |

Back to top

## Reuse

EUPL (\>= 1.2)
