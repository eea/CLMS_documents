# CLC+ Core User Manual
European Environment Agency (EEA)
2026-06-03

- [<span class="toc-section-number">1</span>
  Introduction](#introduction)
  - [<span class="toc-section-number">1.1</span> CLC+ Core in a
    nutshell](#clc-core-in-a-nutshell)
  - [<span class="toc-section-number">1.2</span> Getting
    started?](#getting-started)
  - [<span class="toc-section-number">1.3</span> Webpage
    elements](#webpage-elements)
    - [<span class="toc-section-number">1.3.1</span> Header](#header)
    - [<span class="toc-section-number">1.3.2</span> Content](#content)
  - [<span class="toc-section-number">1.4</span>
    Organisations](#organisations)
  - [<span class="toc-section-number">1.5</span> Users](#users)
    - [<span class="toc-section-number">1.5.1</span> User
      Profile](#user-profile)
    - [<span class="toc-section-number">1.5.2</span> User Profile
      View](#user-profile-view)
  - [<span class="toc-section-number">1.6</span> Data
    Catalogue](#data-catalogue)
  - [<span class="toc-section-number">1.7</span> Auxiliary / Supporting
    functions](#auxiliary--supporting-functions)
    - [<span class="toc-section-number">1.7.1</span> Search and
      Filter](#search-and-filter)
    - [<span class="toc-section-number">1.7.2</span> Pop-ups/Inline
      Notifications](#pop-upsinline-notifications)
    - [<span class="toc-section-number">1.7.3</span> Notifications
      messages](#notifications-messages)
  - [<span class="toc-section-number">1.8</span> Projections (of
    national datasets)](#projections-of-national-datasets)
  - [<span class="toc-section-number">1.9</span> About
    EAGLE](#about-eagle)
- [<span class="toc-section-number">2</span> EAGLE](#eagle2)
  - [<span class="toc-section-number">2.1</span> General overview of the
    EAGLE concept](#general-overview-of-the-eagle-concept)
  - [<span class="toc-section-number">2.2</span> Approach and
    implementation used by the CLC+ CORE
    Consortium](#approach-and-implementation-used-by-the-clc-core-consortium)
    - [<span class="toc-section-number">2.2.1</span> Mapping Approach of
      the Consortium](#mapping-approach-of-the-consortium)
  - [<span class="toc-section-number">2.3</span> EAGLE Ontology
    overview](#eagle-ontology-overview)
  - [<span class="toc-section-number">2.4</span> View details of EAGLE
    Ontology](#view-details-of-eagle-ontology)
  - [<span class="toc-section-number">2.5</span> EAGLE approval stamp
    for Ingestions](#eagle-approval-stamp-for-ingestions)
  - [<span class="toc-section-number">2.6</span> Lessons learned for the
    EAGLE barcoding
    approach](#lessons-learned-for-the-eagle-barcoding-approach)
- [<span class="toc-section-number">3</span> Ingestions](#ingestions)
  - [<span class="toc-section-number">3.1</span> Generic
    workflow](#generic-workflow)
  - [<span class="toc-section-number">3.2</span> Add
    Ingestion](#add-ingestion)
    - [<span class="toc-section-number">3.2.1</span> Raster
      dataset](#raster-dataset)
    - [<span class="toc-section-number">3.2.2</span> Vector
      dataset](#vector-dataset)
  - [<span class="toc-section-number">3.3</span> Remarks on the
    Ingestion process](#remarks-on-the-ingestion-process)
  - [<span class="toc-section-number">3.4</span> Retry or
    Delete](#retry-or-delete)
  - [<span class="toc-section-number">3.5</span> Status of an
    Ingestion](#status-of-an-ingestion)
  - [<span class="toc-section-number">3.6</span> Input
    Classes](#input-classes)
  - [<span class="toc-section-number">3.7</span> Edit
    Ingestion](#edit-ingestion)
  - [<span class="toc-section-number">3.8</span> Publish
    Ingestion](#publish-ingestion)
  - [<span class="toc-section-number">3.9</span> Reuse
    Ingestion](#reuse-ingestion)
- [<span class="toc-section-number">4</span> Extraction](#extraction)
  - [<span class="toc-section-number">4.1</span> Status of an
    Extraction](#status-of-an-extraction)
  - [<span class="toc-section-number">4.2</span> Add
    Extraction](#add-extraction)
  - [<span class="toc-section-number">4.3</span> Edit
    Extraction](#edit-extraction)
  - [<span class="toc-section-number">4.4</span> Add Input Classes to
    Extraction](#add-input-classes-to-extraction)
  - [<span class="toc-section-number">4.5</span> Output
    Classes](#output-classes)
    - [<span class="toc-section-number">4.5.1</span> Some definitions
      for a better understanding (also see
      Glossary)](#some-definitions-for-a-better-understanding-also-see-glossary)
    - [<span class="toc-section-number">4.5.2</span> Create Output
      Classes](#create-output-classes)
    - [<span class="toc-section-number">4.5.3</span> Create Class
      Conditions/Rulesets](#create-class-conditionsrulesets)
  - [<span class="toc-section-number">4.6</span> How is the extraction
    result computed?](#how-is-the-extraction-result-computed)
  - [<span class="toc-section-number">4.7</span> Preview Extraction and
    download result](#preview-extraction-and-download-result)
  - [<span class="toc-section-number">4.8</span> Publish Extraction and
    download result](#publish-extraction-and-download-result)
  - [<span class="toc-section-number">4.9</span> Reuse
    Extraction](#reuse-extraction)
  - [<span class="toc-section-number">4.10</span> Delete
    Extraction](#delete-extraction)
  - [<span class="toc-section-number">4.11</span> Recommendations and
    lessons learned](#recommendations-and-lessons-learned)
- [<span class="toc-section-number">5</span> FAQ (Frequently Asked
  Questions)](#faq-frequently-asked-questions)
- [<span class="toc-section-number">6</span> Admin User only - see
  separate Annex](#admin-user-only---see-separate-annex)
- [<span class="toc-section-number">7</span> Glossary](#glossary)
- [<span class="toc-section-number">8</span> List of
  abbreviations](#list-of-abbreviations)
- [<span class="toc-section-number">9</span> Annex](#annex)

Date: 2023-12-21

Doc. Version: Issue 4.0

Content ID: /

**Document Control Information**

| Document Title | CLC+ Core User Guideline |
|----|----|
| Project Title | CLC+ Core production and provision of complementary consultancy services |
| Document Author | Thomas Mathis (Cloudflight), Tanja Gasber (GeoVille), Amelie Lindmayer (GAF) |
| Project Owner | Tobias Langanke (EEA) |
| Project Manager | Tobias Langanke (EEA) |
| Document Code | / |
| Document Version | Issue 4.0 |
| Distribution |  |
| Date | 2023-12-20 |

**Document Approver(s) and Reviewer(s):**

| Name                | Role     | Action          | Date       |
|---------------------|----------|-----------------|------------|
| Tim Wiltzius (CLF)  | Reviewer | Document review | 2023-12-20 |
| Johannes Vass (CLF) | Reviewer | Document review |            |

**Document history**

| Revision | Date | Created by | Short description of changes |
|----|----|----|----|
| 1.0 | 2022-04-08 | CLC+ Core consortium (CLF, GV, GAF) | Initial document creation |
| 2.0 | 2022-06-10 | CLC+ Core consortium (CLF, GV, GAF) | Restructure of entire document, extension of Extraction chapter and Admin User section |
| 3.0 | 2023-06-06 | CLC+ Core consortium (CLF, GV, GAF) | Adaption of rule 3 in the current version of the CLC+ Core system |
| 4.0 | 2023-12-22 | CLC+ Core consortium (CLF, GV, GAF) | Update of the entire document with all newly implemented features and improvements of the system (within SC8) |

**Applicable Documents (AD)**

| **ID** | **Document Name / Content** |
|----|----|
| AD01 | Tender Specifications – EEA/DIS/R0/20/019 – Copernicus Land Monitoring Service – Production of the CLC+ Core and Provision of Complementary Consultancy Services |
| AD02 | Consortium’s Technical Proposal – in response to Call for tenders EEA/DIS/R0/20/019 – CLC+CORE Technical Proposal - v2.0 |
| AD03 | Specific Contract No 3436/R0-COPERNICUS/EEA.58286 |
| AD04 | Minutes of the KOM (CLC+Core_KOM_Minutes.docx) |
| AD05 | PM1 - Project Management and Governance Plan (CLC+Core_Deliverable_PM1_Project_Management_Plan_V1.0.pdf) |
| AD06 | Implementation of CLC+ based on the EAGLE concept –Additional support for further development of CLC+<br><br>databases (CLC+ and CLC+ instances, namely CLC+ LULUCF instance and CLC+ Legacy instance) - Task 4: From CLC+ Core to CLC+ Legacy - 3436/R0-Copernicus/EEA.57755 |
| AD07 | PM2 - 1st Project Management and Status Report (CLC+Core_Deliverable_PM2_1st-Project-Management-Status-Report_V1.0.pdf) |
| AD08 | CLC+ Core Decision Log_V1.4 (CLC+Core_Decision_log_V1.4.pdf) |
| AD09 | D1 - Software Design (CLC+Core_D1_Software \_Design_V1.0.pdf) |
| AD10 | D3.2.1 - Demonstration and documentation of ingested CLMS datasets, under this Service Contract (CLC+Core_Deliverable_D3.2.1_Demonstration-and-documentation-of-ingested-CLMS-datasets_V01.pdf) |
| AD11 | D3.1 - Documentation of deployment of CLC+ Core products to DIAS – cloud service (CLC+Core_Deliverable_D3.1_Documentation of deployment of CLC+ Core products to DIAS_V1.0.pdf) |
| AD12 | LULUCF_classes_simplified_EAGLE_query_rules_20210325.xlsx (Provided by EAGLE Group) |
| AD13 | Specific contract no 3506_R0-COPERNCA_EEA.59433 |

# Introduction

This User Guideline is designed to provide documentation for the users
of CLC+ Core[^1]. This documentation aims to describe all user
interfaces and functionalities from the user's point of view.
Furthermore, additional useful information, experiences and
recommendations have been added to provide the user with the most
comprehensive guideline possible.

For a better understanding the described functionalities are highlighted
with markers containing numbers (see example on the left side) in the
text and within the screenshots.

Further important notes and remarks are marked with a green outline.

In addition, in section [5](#faq-frequently-asked-questions) frequently
asked questions are collected and a [Glossary](#glossary) (see section
[7](#glossary)) was added at the end of the user guideline explaining
the most common terms relevant to the CLC+ Core system.

## CLC+ Core in a nutshell

With CLC+ Core, the European Environment Agency (EEA) offers you a
consistent multi-use grid-based, web-based Land Cover/Land Use (LC/LU)
hybrid data repository. Following up on the CLC+ Backbone, the CLC+ Core
constitutes the second stage of the CLC+ Product Suite (see [Figure
1‑1](#_Ref151465617)). The CLC+ Core provides a flexible database
approach to incorporate existing and future European Copernicus Land
Monitoring Service (CLMS) products as well as various national land
cover (LC) and land use (LU) datasets, by standardised integration along
the EAGLE language, which further enables the Extraction of various CLC+
Instances. CLC+ Core will thus be able to provide unprecedented
information to strengthen Europe’s leading role in climate change impact
mitigation and the management of environmental monitoring in support of
programmes and policies such as Land Use, Land-Use Change and Forestry
(LULUCF) and the European Green Deal. The goal of the CLC+ suite is to
become the new European standard in land monitoring, within the CLMS.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image3.png"
style="width:6.41944in;height:2.60328in"
data-fig-alt="This diagram illustrates the conceptual architecture and data flow for the CLC+ (Copernicus Land Monitoring Service next-generation land cover/land use) system, organised into three main stages: CLC+ Backbone, CLC+ Core, and CLC+ Instance. 1. **CLC+ Backbone:** This initial stage is depicted as a detailed, parcel-level land cover map, showing a fine-grained classification of different land cover types, including urban areas, water bodies, and vegetation. It represents the foundational high-resolution data. 2. **CLC+ Core:** This central stage processes and integrates data. It is represented by a 3D cube labelled &#39;Spatial domain&#39;, implying a multi-dimensional data structure. The &#39;EAGLE Data Model&#39; is explicitly cited as governing the data within this core. The CLC+ Core integrates four types of input data: * **Pan-European** data (represented by EU stars). * **Memberstate LC/LU Data** (Land Cover/Land Use), illustrated by a map of Europe with the &#39;INSPIRE&#39; (Infrastructure for Spatial Information in the European Community) label. * **Local** data (indicated by a map pin icon). * **Imagery and reference data** (symbolised by a database and document icon). 3. **CLC+ Instance:** This final stage represents the application and realisation of the CLC+ Core data. It includes an example of a &#39;National LULUCF (Land Use, Land Use Change and Forestry) realisation&#39; for Turkey, shown as a colour-coded map indicating different land cover patterns, with a zoomed-in inset. Below this, a dashboard interface presents various functionalities: &#39;Dashboard&#39;, &#39;DD Monitor&#39;, &#39;Archive&#39;, &#39;EF Reviewer&#39;, &#39;CBR Portal&#39;, and &#39;Geo Portal&#39;, with accompanying icons and example data visualisations like pie charts and bar charts." />

This diagram illustrates the conceptual architecture and data flow for
the CLC+ (Copernicus Land Monitoring Service next-generation land
cover/land use) system, organised into three main stages: CLC+ Backbone,
CLC+ Core, and CLC+ Instance.

1.  **CLC+ Backbone:** This initial stage is depicted as a detailed,
    parcel-level land cover map, showing a fine-grained classification
    of different land cover types, including urban areas, water bodies,
    and vegetation. It represents the foundational high-resolution data.
2.  **CLC+ Core:** This central stage processes and integrates data. It
    is represented by a 3D cube labelled “Spatial domain”, implying a
    multi-dimensional data structure. The “EAGLE Data Model” is
    explicitly cited as governing the data within this core. The CLC+
    Core integrates four types of input data:
    - **Pan-European** data (represented by EU stars).
    - **Memberstate LC/LU Data** (Land Cover/Land Use), illustrated by a
      map of Europe with the “INSPIRE” (Infrastructure for Spatial
      Information in the European Community) label.
    - **Local** data (indicated by a map pin icon).
    - **Imagery and reference data** (symbolised by a database and
      document icon).
3.  **CLC+ Instance:** This final stage represents the application and
    realisation of the CLC+ Core data. It includes an example of a
    “National LULUCF (Land Use, Land Use Change and Forestry)
    realisation” for Turkey, shown as a colour-coded map indicating
    different land cover patterns, with a zoomed-in inset. Below this, a
    dashboard interface presents various functionalities: “Dashboard”,
    “DD Monitor”, “Archive”, “EF Reviewer”, “CBR Portal”, and “Geo
    Portal”, with accompanying icons and example data visualisations
    like pie charts and bar charts.

<span id="_Ref151465617" class="anchor"></span>**Figure 1‑1: CLC+
Product suite overview (from left to right) with the CLC+ Core database
solution (middle) hosting integrated CLMS, and potentially ancillary and
national LC/LU data.**

The following chapters provide a brief overview about the CLC+ Core
System and how to perform an Ingestion or Extraction. Chapter 0 gives an
introduction about how to get started and the main functionalities of
the CLC+ Core. Further, you get to information about the Organizations
and User that are part of the System. The EAGLE concept, as a main part
of the System, is described in chapter [0](#_Toc65609501). In this
section you get tips and hints how to perform the EAGLE barcoding. There
are already several datasets in the CLC+ Core System. The process how to
ingest your own data in the System is described in chapter
[3](#ingestions) whereas chapter [4](#extraction) explains the creation
of an Extraction. The Frequently Asked Questions (FAQ) section
([5](#faq-frequently-asked-questions)) provides the user a summary of
questions and their answers regarding the CLC+ Core environment.

**Please note that this guideline is a living document which will be
updated regularly.**

## Getting started?

The CLC+ Core **Login** Page (see [Figure 1‑2](#_Ref151465691)) uses the
EIONET Portal for authentication. If you already have an **EIONET
account**, use your EIONET credentials to gain access:
[clcplus-core.land.copernicus.eu](https://clcplus-core.land.copernicus.eu).
If you are not logged in, the login app routes you automatically to the
login.

If you do not have an EIONET account yet, please contact the [Eionet
Helpdesk](https://www.eionet.europa.eu/about/helpdesk?msclkid=265000d2aa8b11ec89be0ad26fcd73b0)
to create one.

If you already have an account but forgot your password, you can reset
your password here: [Eionet
passwor](https://www.eionet.europa.eu/password-reset)d reset.

The European Environment Information and Observation Network (EIONET) is
a partnership network of the European Environment Agency (EEA) and its
38 member and cooperating countries. EEA and Eionet gather and develop
data, knowledge, and advice policy makers about Europe's environment.
The Eionet helpdesk is a central contact point for support requests
related to Eionet account management and IT troubleshooting on Eionet
web sites, tools and services.

Eionet user accounts are created for those who need access to Eionet
websites, tools and services that require Eionet login. **New user
accounts can only be created by the Eionet Helpdesk and the National
Focal Points.** The Eionet helpdesk is manned throughout the opening
hours of EEA and generally responds to the ticket within 24 hours.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image4.png"
style="width:6.09347in;height:3.98288in"
data-fig-alt="Screenshot of the EIONET Portal login page for CLC+ Core, set against an aerial background image of agricultural fields, roads, and farm buildings. In the top-centre, the CLC+ Core logo is displayed, featuring stylized green buildings and a wheat stalk. The central white login box is titled &#39;EIONET Portal&#39; with the EIONET logo (a stylized globe with gears). Inside the login box, there are two input fields: &#39;Login Name*&#39; with a pre-filled value &#39;clccore&#39;, and &#39;Password*&#39; with a masked pre-filled value &#39;********&#39;. Below these fields is a green &#39;LOGIN&#39; button and a blue &#39;Forgot your password?&#39; link. A blue circular icon with a white question mark is visible in the bottom right corner of the screen." />

Screenshot of the EIONET Portal login page for CLC+ Core, set against an
aerial background image of agricultural fields, roads, and farm
buildings. In the top-centre, the CLC+ Core logo is displayed, featuring
stylized green buildings and a wheat stalk. The central white login box
is titled “EIONET Portal” with the EIONET logo (a stylized globe with
gears). Inside the login box, there are two input fields: “Login Name*”
with a pre-filled value ”clccore”, and ”Password*” with a masked
pre-filled value “\*\*\*\*\*\*\*\*”. Below these fields is a green
“LOGIN” button and a blue “Forgot your password?” link. A blue circular
icon with a white question mark is visible in the bottom right corner of
the screen.

<span id="_Ref151465691" class="anchor"></span>**Figure 1‑2: CLC+ Core
login page**

## Webpage elements

In this section, the general page elements are described to give an
overview of the structure of this website, its navigation and its
content (see [Figure 1‑3](#_Ref151621809)).

### Header

The **Header** section contains the Navigation Menu (see [Figure
1‑3](#_Ref151621809)). The different tabs will be described in the
respective sections of this document:

- Data Catalogue (section [1.6](#data-catalogue)),

- EAGLE Ontology (section [0](#_Toc65609501)),

- About EAGLE (section [1.9](#about-eagle)),

- Organisations (section [1.31.3](#webpage-elements)),

- Users (section [1.5](#users))

- Notifications (see section [1.7.3](#notifications-messages)) and

- User Profile (section [1.5.1](#user-profile)).

### Content

The **Content** represents the section between the Header and the Footer
area and varies depending on which tab is opened (see [Figure
1‑3](#_Ref151621809)). The Data Catalogue (section
[1.6](#data-catalogue)) is the landing page / starting point of CLC+
Core. To navigate through the system, simply click on the relevant
navigation tabs or entries.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image7.png"
style="width:6.925in;height:3.80556in"
data-fig-alt="This image displays a tabular view of the Data Catalogue within the Copernicus Land Monitoring Service (CLMS) CLC+ Core system, showing entries for various ingested High Resolution Layer (HRL) and other land monitoring products. The table lists 9 entries (items 21-30 of 31) with the following columns: | EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | INSPIRE Themes | |---|---|---|---|---|---|---|---|---|---|---|---|---| | | HRL - Dominant Leaf Type (DLT) | [document icon] | 05.09.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Forest Type (FTY) 2018 | [document icon] | 10.03.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | HRL - Grassland (GRA) 2018 | [document icon] | 05.09.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Imperviousness Density (IMD) 2018 | [document icon] | 09.03.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.01.2017 - 31.12.2019 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Tree Cover Density (TCD) 2018 | [document icon] | 09.03.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Water and Wetness (WAT) 2018 | [document icon] | 06.09.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.01.2012 - 31.12.2018 | Copernicus Land Monitoring Service, European Environment Agency | info@eea.europa.eu | USED | Land cover | | | Natura 2000 (N2K) 2018 | [document icon] | 21.06.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2019 | 15.05.2017 - 14.09.2019 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | Riparian Zones (RZ) 2018 | [document icon] | 21.06.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.03.2018 - 31.07.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | Riparian Zones (RZ) 2018 | [document icon] | 21.02.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.03.2018 - 31.07.2018 | European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | Urban Atlas (UA) 2018 | [document icon] | 20.06.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 29.06.2017 - 01.09.2018 | Copernicus Land Monitoring Service, European Environment Agency | Matteo.Mattiuzzi | USED | Land use, Land cover | The table provides an overview of various CLMS High Resolution Layers (HRLs), Natura 2000 (N2K) data, Riparian Zones (RZ), and Urban Atlas (UA) products for the European Environment Agency, mostly from the 2018 reference year, categorised by INSPIRE Themes like &#39;Land cover&#39; and &#39;Land use, Land cover&#39;. Above the table, filtering options include &#39;My organisation/s,&#39; &#39;My data,&#39; &#39;Ingestions&#39; (currently active), and &#39;Extractions,&#39; along with a search bar and buttons for &#39;Add Ingestion&#39; and &#39;Add Extraction.&#39; Pagination at the bottom indicates &#39;21 - 30 of 31&#39; items are displayed, with 10 items per page. Logos for Copernicus, EAGLE, European Commission, and the European Environment Agency are visible at the bottom." />

This image displays a tabular view of the Data Catalogue within the
Copernicus Land Monitoring Service (CLMS) CLC+ Core system, showing
entries for various ingested High Resolution Layer (HRL) and other land
monitoring products. The table lists 9 entries (items 21-30 of 31) with
the following columns: \| EAGLE Approved \| Name \| Type \| Created At
\| Created By \| Country \| Region \| Reference Year \| Time Range \|
Organisation/s \| Contact Person \| Status \| INSPIRE Themes \|
\|—\|—\|—\|—\|—\|—\|—\|—\|—\|—\|—\|—\|—\| \| \| HRL - Dominant Leaf Type
(DLT) \| \[document icon\] \| 05.09.2023 \| CLC+ Core User Administrator
\| European Environment Agency \| - \| 2018 \| 01.03.2018 - 31.10.2018
\| Copernicus Land Monitoring Service, European Environment Agency \|
copernicus@eea.europa.eu \| USED \| Land cover \| \| \| HRL - Forest
Type (FTY) 2018 \| \[document icon\] \| 10.03.2023 \| CLC+ Core User
Administrator \| European Environment Agency \| European Environment
Agency \| 2018 \| 01.03.2018 - 31.10.2018 \| Copernicus Land Monitoring
Service, European Environment Agency \| copernicus@eea.europa.eu \| USED
\| Land use, Land cover \| \| \| HRL - Grassland (GRA) 2018 \|
\[document icon\] \| 05.09.2023 \| CLC+ Core User Administrator \|
European Environment Agency \| - \| 2018 \| 01.03.2018 - 31.10.2018 \|
Copernicus Land Monitoring Service, European Environment Agency \|
copernicus@eea.europa.eu \| USED \| Land cover \| \| \| HRL -
Imperviousness Density (IMD) 2018 \| \[document icon\] \| 09.03.2023 \|
CLC+ Core User Administrator \| European Environment Agency \| European
Environment Agency \| 2018 \| 01.01.2017 - 31.12.2019 \| Copernicus Land
Monitoring Service, European Environment Agency \|
copernicus@eea.europa.eu \| USED \| Land cover \| \| \| HRL - Tree Cover
Density (TCD) 2018 \| \[document icon\] \| 09.03.2023 \| CLC+ Core User
Administrator \| European Environment Agency \| - \| 2018 \|
01.03.2018 - 31.10.2018 \| Copernicus Land Monitoring Service, European
Environment Agency \| copernicus@eea.europa.eu \| USED \| Land cover \|
\| \| HRL - Water and Wetness (WAT) 2018 \| \[document icon\] \|
06.09.2023 \| CLC+ Core User Administrator \| European Environment
Agency \| - \| 2018 \| 01.01.2012 - 31.12.2018 \| Copernicus Land
Monitoring Service, European Environment Agency \| info@eea.europa.eu \|
USED \| Land cover \| \| \| Natura 2000 (N2K) 2018 \| \[document icon\]
\| 21.06.2023 \| CLC+ Core User Administrator \| European Environment
Agency \| European Environment Agency \| 2019 \| 15.05.2017 - 14.09.2019
\| Copernicus Land Monitoring Service, European Environment Agency \|
copernicus@eea.europa.eu \| USED \| Land use, Land cover \| \| \|
Riparian Zones (RZ) 2018 \| \[document icon\] \| 21.06.2023 \| CLC+ Core
User Administrator \| European Environment Agency \| European
Environment Agency \| 2018 \| 01.03.2018 - 31.07.2018 \| Copernicus Land
Monitoring Service, European Environment Agency \|
copernicus@eea.europa.eu \| USED \| Land use, Land cover \| \| \|
Riparian Zones (RZ) 2018 \| \[document icon\] \| 21.02.2023 \| CLC+ Core
User Administrator \| European Environment Agency \| European
Environment Agency \| 2018 \| 01.03.2018 - 31.07.2018 \| European
Environment Agency \| copernicus@eea.europa.eu \| USED \| Land use, Land
cover \| \| \| Urban Atlas (UA) 2018 \| \[document icon\] \| 20.06.2023
\| CLC+ Core User Administrator \| European Environment Agency \|
European Environment Agency \| 2018 \| 29.06.2017 - 01.09.2018 \|
Copernicus Land Monitoring Service, European Environment Agency \|
Matteo.Mattiuzzi \| USED \| Land use, Land cover \| The table provides
an overview of various CLMS High Resolution Layers (HRLs), Natura 2000
(N2K) data, Riparian Zones (RZ), and Urban Atlas (UA) products for the
European Environment Agency, mostly from the 2018 reference year,
categorised by INSPIRE Themes like “Land cover” and “Land use, Land
cover”.

Above the table, filtering options include “My organisation/s,” “My
data,” “Ingestions” (currently active), and “Extractions,” along with a
search bar and buttons for “Add Ingestion” and “Add Extraction.”
Pagination at the bottom indicates “21 - 30 of 31” items are displayed,
with 10 items per page. Logos for Copernicus, EAGLE, European
Commission, and the European Environment Agency are visible at the
bottom.

<span id="_Ref151621809" class="anchor"></span>**Figure 1‑3: Content
example - Data Catalogue**

## Organisations

This navigation menu tab provides an overview of the registered
**Organisations** of the CLC+ Core system.

Organisations are taken over by default from EIONET with your first
login to CLC+ Core. Organisations play an important role when you define
the visibility of your Ingestion or Extraction for publishing it. The
visibility can be limited to users from your organisations only or for
the country of the selected Organisation (see sections
[3.8](#publish-ingestion) and
[4.8](#publish-extraction-and-download-result)).

**Search function**, to search for an organisation within the system
(see [Figure 1‑4](#_Ref151465792)). If you are an Admin User, please
refer to section 6.1 in separate Annex.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image8.png"
style="width:6.925in;height:3.82014in"
data-fig-alt="The table lists registered organisations within the Copernicus Land Monitoring Service (CLMS) CLC+ Core system, displaying 4 entries out of 4 total, with a &#39;Search&#39; function present. The table includes columns for `EIONET ID`, `Name`, `E-Mail`, `URL`, `Country`, and `Status`. | EIONET ID | Name | E-Mail | URL | Country | Status | |---|---|---|---|---|---| | - | CLC | | | | ACTIVE | | at_cloudflight | Cloudflight | office@cloudflight.io | https://www.cloudflight.io | Austria/Österreich | ACTIVE | | eu_eea | European Environment Agency | eea@eea.europa.eu | http://www.eea.europa.eu | European Environment | ACTIVE | | de_gaf | GAF AG | info@gaf.de | https://www.gaf.de/ | Germany/Deutschland | ACTIVE | All four listed organisations, including the European Environment Agency (EEA) and GAF AG, have a `Status` of &#39;ACTIVE&#39;. The table displays &#39;Items per page: 10&#39; and indicates &#39;1 - 4 of 4&#39; items are currently shown. This list is accessed via the &#39;Organisations&#39; tab within the CLC+ Core user interface." />

The table lists registered organisations within the Copernicus Land
Monitoring Service (CLMS) CLC+ Core system, displaying 4 entries out of
4 total, with a “Search” function present. The table includes columns
for `EIONET ID`, `Name`, `E-Mail`, `URL`, `Country`, and `Status`.

| EIONET ID | Name | E-Mail | URL | Country | Status |
|----|----|----|----|----|----|
| \- | CLC |  |  |  | ACTIVE |
| at_cloudflight | Cloudflight | office@cloudflight.io | https://www.cloudflight.io | Austria/Österreich | ACTIVE |
| eu_eea | European Environment Agency | eea@eea.europa.eu | http://www.eea.europa.eu | European Environment | ACTIVE |
| de_gaf | GAF AG | info@gaf.de | https://www.gaf.de/ | Germany/Deutschland | ACTIVE |

All four listed organisations, including the European Environment Agency
(EEA) and GAF AG, have a `Status` of “ACTIVE”. The table displays “Items
per page: 10” and indicates “1 - 4 of 4” items are currently shown. This
list is accessed via the “Organisations” tab within the CLC+ Core user
interface.

<span id="_Ref151465792" class="anchor"></span>**Figure 1‑4: Menu item –
Organisations**

## Users

This navigation menu tab provides an overview of the registered **User**
of the CLC+ Core system.

Users are taken over by default from EIONET with your first login to
CLC+ Core. Depending on your role assigned, you have more or less
rights. To open your Profile click on your name. Now you will be
forwarded to the Profile view (section [1.5.1](#user-profile)).

You have the possibility to search for a **User** (see [Figure
1‑5](#_Ref100263548)). If you are an Admin User, please refer to section
6.2 in separate Annex.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image9.png"
style="width:6.925in;height:3.83264in"
data-fig-alt="This table displays the user accounts registered within the CLC+ Core system, a component of the Copernicus Land Monitoring Service (CLMS). The table contains 7 rows of user data, with pagination showing &#39;1 – 7 of 7&#39; items and &#39;Items per page: 10&#39;. | EIONET Username | Last name | First name | Organisation/s | Email | Roles | Status | |---|---|---|---|---|---|---| | clccore | CLC+ Core | User Admin/Support | CLC, European Environment Agency (EEA) | thomas.mathis@cloudflight.io | EAGLE maintainer / Approver, Admin | ACTIVE | | hochpmat | Hochpochler | Matthias | Cloudflight | - | User Administrator / Support | ACTIVE | | jaffrdav | Jaffry | David | Cloudflight | - | Database Administrator, EAGLE | ACTIVE | | kurzmmar | Kurzmann | Markus | Cloudflight | - | - | ACTIVE | | lindmame | Lindmayer | Amelie | GAF AG | amelie.lindmayer@gaf.de | - | ACTIVE | | mathitho | Mathis | Thomas | Cloudflight | - | - | ACTIVE | | rennetho | Renner | Thomas | GAF AG | thomas.renner@gaf.de | - | ACTIVE | The table provides details for each user including their EIONET (European Environment Information and Observation Network) username, full name, associated organisation, email address (if provided), assigned roles within the system, and their current &#39;Status&#39;. All listed users are &#39;ACTIVE&#39;. Key organisations include Cloudflight, GAF AG, and the European Environment Agency (EEA)." />

This table displays the user accounts registered within the CLC+ Core
system, a component of the Copernicus Land Monitoring Service (CLMS).
The table contains 7 rows of user data, with pagination showing “1 – 7
of 7” items and “Items per page: 10”.

| EIONET Username | Last name | First name | Organisation/s | Email | Roles | Status |
|----|----|----|----|----|----|----|
| clccore | CLC+ Core | User Admin/Support | CLC, European Environment Agency (EEA) | thomas.mathis@cloudflight.io | EAGLE maintainer / Approver, Admin | ACTIVE |
| hochpmat | Hochpochler | Matthias | Cloudflight | \- | User Administrator / Support | ACTIVE |
| jaffrdav | Jaffry | David | Cloudflight | \- | Database Administrator, EAGLE | ACTIVE |
| kurzmmar | Kurzmann | Markus | Cloudflight | \- | \- | ACTIVE |
| lindmame | Lindmayer | Amelie | GAF AG | amelie.lindmayer@gaf.de | \- | ACTIVE |
| mathitho | Mathis | Thomas | Cloudflight | \- | \- | ACTIVE |
| rennetho | Renner | Thomas | GAF AG | thomas.renner@gaf.de | \- | ACTIVE |

The table provides details for each user including their EIONET
(European Environment Information and Observation Network) username,
full name, associated organisation, email address (if provided),
assigned roles within the system, and their current ‘Status’. All listed
users are ‘ACTIVE’. Key organisations include Cloudflight, GAF AG, and
the European Environment Agency (EEA).

<span id="_Ref100263548" class="anchor"></span>**Figure 1‑5: Menu item –
Users**

### User Profile

To open the **User Profile** View you can either click on the User
Profile Icon in the Header, which opens a context menu with the actions
‘My Profile’ and ‘Logout’ ([Figure 1‑6](#_Ref100263532)) or in the Users
tab by clicking on your name. You will then be forwarded to the Profile
view. By clicking on Logout your session will be terminated.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image11.png"
style="width:6.925in;height:1.14444in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core system&#39;s Data Catalogue interface. The top navigation bar displays tabs for &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. On the far right, a notification bell icon is visible next to &#39;CLC+ Core User Admin/Support&#39;, which has an open dropdown menu showing &#39;My Profile&#39;, &#39;Version:&#39;, and &#39;Logout&#39;. The main content area is titled &#39;Data Catalogue&#39;. Below the title, a filter and search bar is present. It includes a &#39;Filter&#39; button with a funnel icon, followed by four selection buttons: &#39;My organisation&#39;s&#39; (checked), &#39;My data&#39;, &#39;Ingestions&#39; (checked), and &#39;Extractions&#39;. A search input field labelled &#39;Search&#39; is next, followed by &#39;ADD INGESTION&#39; and &#39;ADD EXTRACTION&#39; buttons. A table of data is displayed below the search bar, with the following headers: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. The first visible row of data in the table shows: * **EAGLE Approved**: [blank] * **Name**: CLC+Backbone (2018) * **Type**: [document icon] * **Created At**: 05.09.2023 * **Created By**: CLC+ Core User Admin... * **Country**: European Environ... * **Region**: - * **Reference Year**: 2018 * **Time Range**: 01.07.2017 - 30.06.2019 * **Organisation/s**: CLC, European En... * **Contact Person**: copernicus@eea.... * **Status**: USED * **INSPIRE Themes**: Land cover" />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) CLC+ Core system’s Data Catalogue interface. The top navigation
bar displays tabs for “Data Catalogue”, “EAGLE Ontology”, “About EAGLE”,
“Organisations”, and “Users”. On the far right, a notification bell icon
is visible next to “CLC+ Core User Admin/Support”, which has an open
dropdown menu showing “My Profile”, “Version:”, and “Logout”.

The main content area is titled “Data Catalogue”. Below the title, a
filter and search bar is present. It includes a “Filter” button with a
funnel icon, followed by four selection buttons: “My organisation’s”
(checked), “My data”, “Ingestions” (checked), and “Extractions”. A
search input field labelled “Search” is next, followed by “ADD
INGESTION” and “ADD EXTRACTION” buttons.

A table of data is displayed below the search bar, with the following
headers: “EAGLE Approved”, “Name”, “Type”, “Created At”, “Created By”,
“Country”, “Region”, “Reference Year”, “Time Range”, “Organisation/s”,
“Contact Person”, “Status”, and “INSPIRE Themes”. The first visible row
of data in the table shows: \* **EAGLE Approved**: \[blank\] \*
**Name**: CLC+Backbone (2018) \* **Type**: \[document icon\] \*
**Created At**: 05.09.2023 \* **Created By**: CLC+ Core User Admin… \*
**Country**: European Environ… \* **Region**: - \* **Reference Year**:
2018 \* **Time Range**: 01.07.2017 - 30.06.2019 \* **Organisation/s**:
CLC, European En… \* **Contact Person**: copernicus@eea…. \* **Status**:
USED \* **INSPIRE Themes**: Land cover

<span id="_Ref100263532" class="anchor"></span>**Figure 1‑6: User
Profile – Actions**

### User Profile View

When you click on the context menu action ‘My Profile’ of the User
Profile Icon you will find yourself within the User Profile view. Thus,
a profile can only be changed by a person with the role ‘User
Administration / support’. Within your Profile you can see several
information (see [Figure 1‑7](#_Ref151622278)) such as:

**General Information:** In this area the most important information
from your user profile is shown which is username, first and last name,
which organisation you are part of and your status. The EIONET button
guides you to the [Eionet
Portal](https://www.eionet.europa.eu/login?came_from=/directory/user%3Fuid%3Dclccore).

**Roles:** In this area it is displayed what roles are assigned to you.
Roles define what you as a user are allowed to do within the CLC+ Core
system from a functional point of view. You are perfectly able to use
the system if there are no roles assigned to you. If you are an Admin
User, please refer to section 6.2 in separate Annex.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image12.png"
style="width:6.925in;height:3.8125in"
data-fig-alt="A screenshot of the CLC+ Core system user interface displaying the &#39;User Profile&#39; view for &#39;Lindmayer Amelie&#39;. The top navigation bar shows tabs for &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, with the user&#39;s name &#39;Lindmayer Amelie&#39; and a bell icon on the far right. The main content area is titled &#39;Users / User &#39;Lindmayer Amelie&#39;&#39;, with an &#39;ACTIVE&#39; status badge next to the user&#39;s name. The left section, &#39;General Information&#39;, lists: - EIONET Username: lindmame - Last name: Lindmayer - First name: Amelie - Organisation/s: GAF AG (linked) - Email: amelie.lindmayer@gaf.de - Status: active Below this information, there is a button labeled &#39;VISIT EIONET FOR CONTACT DETAILS&#39; with an external link icon. The right section, &#39;Roles&#39;, states: &#39;No other role assigned besides the default user role.&#39; The bottom of the screen features logos for &#39;Copernicus Europe&#39;s eyes on Earth&#39;, &#39;EIONET Action Group EAGLE Land Monitoring in Europe&#39;, &#39;European Commission&#39;, and &#39;European Environment Agency&#39;. A blue circle with a white question mark icon is visible in the bottom right corner." />

A screenshot of the CLC+ Core system user interface displaying the “User
Profile” view for ‘Lindmayer Amelie’. The top navigation bar shows tabs
for “Data Catalogue”, “EAGLE Ontology”, “About EAGLE”, “Organisations”,
and “Users”, with the user’s name “Lindmayer Amelie” and a bell icon on
the far right. The main content area is titled “Users / User ‘Lindmayer
Amelie’”, with an “ACTIVE” status badge next to the user’s name.

The left section, “General Information”, lists: - EIONET Username:
lindmame - Last name: Lindmayer - First name: Amelie - Organisation/s:
GAF AG (linked) - Email: amelie.lindmayer@gaf.de - Status: active Below
this information, there is a button labeled “VISIT EIONET FOR CONTACT
DETAILS” with an external link icon.

The right section, “Roles”, states: “No other role assigned besides the
default user role.”

The bottom of the screen features logos for “Copernicus Europe’s eyes on
Earth”, “EIONET Action Group EAGLE Land Monitoring in Europe”, “European
Commission”, and “European Environment Agency”. A blue circle with a
white question mark icon is visible in the bottom right corner.

<span id="_Ref151622278" class="anchor"></span>**Figure 1‑7: View User
Profile (User without special roles)**

In the table below (Table 1‑1) the roles possible in the CLC+ Core
system are listed:

| Role | Description |
|----|----|
| User Administrator / Support | As an User Administrator / Support you are allowed to manage (Add, Edit, Activate/Inactivate) users and organisations within CLC+ Core. Additionally, you can view and edit any Ingestion and Extraction within the CLC+ Core in order to support users if they are in need of help. |
| EAGLE maintainer / Approver | As an EAGLE maintainer you are allowed to add a new EAGLE ontology version to the CLC+ Core and approve EAGLE compliance of Ingestions. |
| System Administrator | For now, this role is only available within CLC+ Core so that it can be seen who is the system administrator. For later this role could be used for additional views like e.g., scheduling view. |
| Database Administrator | For now, this role is only available within CLC+ Core so that it can be seen who is the database administrator. For later this role could be used for additional views like e.g., performance view. |

<span id="_Ref151985895" class="anchor"></span>Table 1‑1: different user
roles in the CLC+ Core system

Note: Only the admin can assign a role to the user

## Data Catalogue

The **Data Catalogue** is the landing page / starting point of CLC+
Core. In the Data Catalogue, you can search for existing Ingestions and
Extractions within CLC+ Core (see [Figure 1‑8](#_Ref151467230)).

**An Ingestion is the input dataset resampled / aggregated to 100 x 100
m spatial resolution**.

Each Ingestion (section [3](#ingestions)) consists of one or more Land
Cover and or Land Use classes. These classes, so called Input Classes
(section [3.6](#input-classes)) in CLC+ Core will be used for
Extractions (section [4](#extraction)). An Extraction can create
independent data products for future Instances by selecting Input
Classes, adding rules that extract the required information. More
information about Ingestions and Extractions are given in sections
[3](#ingestions) and [4](#extraction).

By hovering your mouse cursor over the content, the table entries turn
grey and three dots appear at the end of the line. By clicking on the 3
dots, you have different options. Ingestion/Extraction can be opened in
detail view, or opened in new tab. Further an Ingestion or Extraction
can be reused (e.g. see section [3.9](#reuse-ingestion)) or if it’s the
users own Ingestion/Extraction and it has been published but not yet
used (see section [3.5](#status-of-an-ingestion) or
[4.1](#status-of-an-extraction)) it can be unpublished again. Further a
used Ingestion could be achieved. With a right click on an Extraction
additional options appear (see lower image of [Figure
1‑8](#_Ref151467230)): the user can download Extraction dataset as
GeoTIFF or the Extraction metadata as JSON file directly (further this
data can also be downloaded in the Extraction detail view page see
section [4.8](#publish-extraction-and-download-result).

In addition to the functionalities mentioned above, the data catalogue
is the starting point for adding new data to the system (**Add
Ingestions**) (see [Figure 1‑8](#_Ref151467230) [Figure
1‑9](#_Ref151467380)),

or to start an Extraction configuration (**Add Extractions**) (see
[Figure 1‑8](#_Ref151467230) [Figure 1‑9](#_Ref151467380)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image16.png"
style="width:6.9252in;height:3.81102in"
data-fig-alt="This image displays the Copernicus Land Monitoring Service (CLMS) CLC+ Core Data Catalogue user interface, accessed by a CLC+ Core User Administrator / Support. The interface presents a tabular list of ingested data products, including Urban Atlas (UA), CORINE Land Cover (CLC), CLC Change, High Resolution Layers (HRL) for Grassland, Forest Type, Impervious Built-up, Impervious Density, Tree Cover Density, and Riparian Zones. The main table has the following columns and data: | EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | INSPIRE Themes | |---|---|---|---|---|---|---|---|---|---|---|---|---| | | Urban Atlas (UA) 2012 | [Document icon] | 21.06.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2012 | 24.03.2011 - 15.09.2013 | CLC, European En... | Matteo.Mattiuzzi... | PUBLISHED | Land use, Land cover | | | Urban Atlas (UA) 2018 | [Document icon] | 20.06.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 29.06.2017 - 01.09.2018 | CLC, European En... | Matteo.Mattiuzzi... | USED | Land use, Land cover | | | Corine Land Cover (CL... | [Document icon] | 14.06.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 01.01.2018 - 31.12.2018 | CLC, European En... | copernicus@eea... | PUBLISHED | Land use, Land cover | | | CLC Change 100m rast... | [Document icon] | 25.05.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2011 | 01.01.2011 - 31.12.2018 | CLC, European En... | [unreadable] | DRAFT | Geographical grid systems, [unreadable] | | | HRL - Grassland 2018 | [Document icon] | 10.03.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 01.03.2018 - 31.10.2018 | CLC, European En... | copernicus@eea... | PUBLISHED | Land cover | | | HRL - Forest Type (FTY... | [Document icon] | 10.03.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 01.03.2018 - 31.10.2018 | CLC, European En... | copernicus@eea... | USED | Land cover | | | HRL - Impervious Built-... | [Document icon] | 09.03.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 01.01.2017 - 31.12.2019 | CLC, European En... | copernicus.land@... | PUBLISHED | Land cover | | | HRL - Impervious Densi... | [Document icon] | 09.03.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 01.01.2017 - 31.12.2019 | CLC, European En... | copernicus@eea... | USED | Land cover | | | HRL - Tree Cover Densi... | [Document icon] | 09.03.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 01.01.2017 - 31.12.2019 | CLC, European En... | copernicus@eea... | USED | Land cover | | | Riparian Zones (RZ) 20... | [Document icon] | 21.02.2023 | CLC+ Core User Admin... | European Environ... | European Environ... | 2018 | 01.03.2018 - 31.07.2018 | European Environ... | copernicus@eea... | USED | Land use, Land cover | The header shows navigation links: &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. The current user is &#39;CLC+ Core User Admin/Support&#39;. Filter options include &#39;Filter&#39;, &#39;My organisation/s&#39; (active), &#39;My data&#39;, &#39;Ingestions&#39; (active), and &#39;Extractions&#39;. A search bar is available. Actions include &#39;Add Ingestion&#39;, &#39;Add Extraction&#39;, and an export/download button. A context menu is visible for the &#39;CLC Change 100m rast...&#39; row, offering &#39;Open&#39;, &#39;Open in new tab&#39;, &#39;Reuse&#39;, and &#39;Unpublish&#39; options. Pagination indicates &#39;Items per page: 10&#39; and shows &#39;21 – 30 of 31&#39; total items. The page footer displays the logos of Copernicus, EIONET Action Group EAGLE, European Commission, and European Environment Agency (EEA). The table primarily shows various CLMS land monitoring products, including Urban Atlas, CORINE Land Cover, and several High Resolution Layers, with details on their creation, reference years, time ranges, and INSPIRE Themes (Infrastructure for Spatial Information in the European Community). Most listed products have a &#39;USED&#39; or &#39;PUBLISHED&#39; status, with one &#39;DRAFT&#39; product." />

This image displays the Copernicus Land Monitoring Service (CLMS) CLC+
Core Data Catalogue user interface, accessed by a CLC+ Core User
Administrator / Support. The interface presents a tabular list of
ingested data products, including Urban Atlas (UA), CORINE Land Cover
(CLC), CLC Change, High Resolution Layers (HRL) for Grassland, Forest
Type, Impervious Built-up, Impervious Density, Tree Cover Density, and
Riparian Zones.

The main table has the following columns and data:

| EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | INSPIRE Themes |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | Urban Atlas (UA) 2012 | \[Document icon\] | 21.06.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2012 | 24.03.2011 - 15.09.2013 | CLC, European En… | Matteo.Mattiuzzi… | PUBLISHED | Land use, Land cover |
|  | Urban Atlas (UA) 2018 | \[Document icon\] | 20.06.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 29.06.2017 - 01.09.2018 | CLC, European En… | Matteo.Mattiuzzi… | USED | Land use, Land cover |
|  | Corine Land Cover (CL… | \[Document icon\] | 14.06.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 01.01.2018 - 31.12.2018 | CLC, European En… | copernicus@eea… | PUBLISHED | Land use, Land cover |
|  | CLC Change 100m rast… | \[Document icon\] | 25.05.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2011 | 01.01.2011 - 31.12.2018 | CLC, European En… | \[unreadable\] | DRAFT | Geographical grid systems, \[unreadable\] |
|  | HRL - Grassland 2018 | \[Document icon\] | 10.03.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 01.03.2018 - 31.10.2018 | CLC, European En… | copernicus@eea… | PUBLISHED | Land cover |
|  | HRL - Forest Type (FTY… | \[Document icon\] | 10.03.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 01.03.2018 - 31.10.2018 | CLC, European En… | copernicus@eea… | USED | Land cover |
|  | HRL - Impervious Built-… | \[Document icon\] | 09.03.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 01.01.2017 - 31.12.2019 | CLC, European En… | copernicus.land@… | PUBLISHED | Land cover |
|  | HRL - Impervious Densi… | \[Document icon\] | 09.03.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 01.01.2017 - 31.12.2019 | CLC, European En… | copernicus@eea… | USED | Land cover |
|  | HRL - Tree Cover Densi… | \[Document icon\] | 09.03.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 01.01.2017 - 31.12.2019 | CLC, European En… | copernicus@eea… | USED | Land cover |
|  | Riparian Zones (RZ) 20… | \[Document icon\] | 21.02.2023 | CLC+ Core User Admin… | European Environ… | European Environ… | 2018 | 01.03.2018 - 31.07.2018 | European Environ… | copernicus@eea… | USED | Land use, Land cover |

The header shows navigation links: “Data Catalogue”, “EAGLE Ontology”,
“About EAGLE”, “Organisations”, and “Users”. The current user is “CLC+
Core User Admin/Support”. Filter options include “Filter”, “My
organisation/s” (active), “My data”, “Ingestions” (active), and
“Extractions”. A search bar is available. Actions include “Add
Ingestion”, “Add Extraction”, and an export/download button. A context
menu is visible for the “CLC Change 100m rast…” row, offering “Open”,
“Open in new tab”, “Reuse”, and “Unpublish” options. Pagination
indicates “Items per page: 10” and shows “21 – 30 of 31” total items.
The page footer displays the logos of Copernicus, EIONET Action Group
EAGLE, European Commission, and European Environment Agency (EEA).

The table primarily shows various CLMS land monitoring products,
including Urban Atlas, CORINE Land Cover, and several High Resolution
Layers, with details on their creation, reference years, time ranges,
and INSPIRE Themes (Infrastructure for Spatial Information in the
European Community). Most listed products have a “USED” or “PUBLISHED”
status, with one “DRAFT” product.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image17.png"
style="width:6.925in;height:2.08696in"
data-fig-alt="This image displays the Copernicus Land Cover (CLC+) Core &#39;Data Catalogue&#39; web interface, highlighting an &#39;Extractions&#39; view for a user with the &#39;CLC+ Core User Admin/Support&#39; role. The top navigation bar includes sections for &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. Below the navigation, the main content area is labelled &#39;Data Catalogue&#39; and features interactive filters for &#39;Filter&#39;, &#39;My organisation/s&#39; (checked), &#39;My data&#39;, &#39;Ingestions&#39;, and &#39;Extractions&#39; (checked). A search bar is present, along with &#39;ADD INGESTION&#39; and &#39;ADD EXTRACTION&#39; buttons. The primary content is a table-like display of a single data entry: | EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | INSPIRE Themes | | :------------- | :---------- | :--------- | :--------- | :-------------------------- | :-------------------- | :----- | :------------- | :------------------------ | :----------------------------------- | :------------- | :---------------- | :---------------------- | | [ ] | LULUCF Test | Extraction | 23.08.2023 | CLC+ Core User Admin/Support | Netherlands/Nederland | - | 2018 | 03.01.2017 - 02.01.2020 | CLC, European Environment Agency | [unreadable] | EXTRACTED PREVIEW | Land use. Land cover. | A dropdown menu is shown, offering the following actions for the selected data entry: &#39;Open&#39;, &#39;Open in new tab&#39;, &#39;Download Dataset (GeoTIFF)&#39;, &#39;Download Metadata (JSON)&#39;, &#39;Reuse&#39;, and &#39;Delete&#39;. The table details an extraction of LULUCF (Land Use, Land Use Change, and Forestry) test data, created on 23.08.2023, with a reference year of 2018 and a time range spanning 03.01.2017 to 02.01.2020. The associated organisation is CLC, European Environment Agency, and its status is &#39;EXTRACTED PREVIEW&#39;, linked to &#39;Land use. Land cover.&#39; INSPIRE Themes, referencing the Infrastructure for Spatial Information in the European Community Directive 2007/2/EC." />

This image displays the Copernicus Land Cover (CLC+) Core “Data
Catalogue” web interface, highlighting an “Extractions” view for a user
with the “CLC+ Core User Admin/Support” role. The top navigation bar
includes sections for “Data Catalogue”, “EAGLE Ontology”, “About EAGLE”,
“Organisations”, and “Users”. Below the navigation, the main content
area is labelled “Data Catalogue” and features interactive filters for
“Filter”, “My organisation/s” (checked), “My data”, “Ingestions”, and
“Extractions” (checked). A search bar is present, along with “ADD
INGESTION” and “ADD EXTRACTION” buttons.

The primary content is a table-like display of a single data entry:

| EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | INSPIRE Themes |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| \[ \] | LULUCF Test | Extraction | 23.08.2023 | CLC+ Core User Admin/Support | Netherlands/Nederland | \- | 2018 | 03.01.2017 - 02.01.2020 | CLC, European Environment Agency | \[unreadable\] | EXTRACTED PREVIEW | Land use. Land cover. |

A dropdown menu is shown, offering the following actions for the
selected data entry: “Open”, “Open in new tab”, “Download Dataset
(GeoTIFF)”, “Download Metadata (JSON)”, “Reuse”, and “Delete”. The table
details an extraction of LULUCF (Land Use, Land Use Change, and
Forestry) test data, created on 23.08.2023, with a reference year of
2018 and a time range spanning 03.01.2017 to 02.01.2020. The associated
organisation is CLC, European Environment Agency, and its status is
“EXTRACTED PREVIEW”, linked to “Land use. Land cover.” INSPIRE Themes,
referencing the Infrastructure for Spatial Information in the European
Community Directive 2007/2/EC.

<span id="_Ref151467230" class="anchor"></span>**Figure 1‑8: Data
Catalogue (Ingestions upper image, lower image Extractions view)**

The Data Catalogue lists all Ingestions and Extractions available in the
CLC+ Core system. It is subdivided in several **columns**: EAGLE
Approval (for further details see section
[2.5](#eagle-approval-stamp-for-ingestions)), Name (of the
Ingestion/Extraction), Type (Ingestion or Extraction), Created at,
Created by (user), Country, Region, Reference Year (od
Ingestion/Extraction), Time range (of the original input data),
Organisation, Contact Person, Status and INSPIRE Themes (see [Figure
1‑9](#_Ref151467380)). All columns can be sorted ascending or descending
by clicking on the column heading (arrow symbol appears). Further
columns can be hidden by deselecting them on the right side (symbol next
to ‘Add Extraction’). The specific column then won’t be displayed in the
overview table anymore, but can easily be shown again by activating it
again.

**Filter and Search** for Ingestions and Extractions (see [Figure
1‑9](#_Ref151467380)) is also possible. In order to find already
existing Ingestions / Extractions within CLC+ Core, an option for
searching and filtering the system is available. For more details see
section [1.7.1](#search-and-filter).

Further there are ’**Quick Filters**” available. The user can quickly
filter by “Ingestion”, “Extraction”, “My Organisation” or “My Data” (see
[Figure 1‑9](#_Ref151467380)). By clicking on e.g. “My Data” symbol the
filter for the table blow gets activated (check mark appears) and only
shows then the Ingestions/Extractions = data the user added. Same
applies for “My Organisation” only data shown ingested or extracted by
the user’s organisation are shown. By activating (clicking on the
symbol) for example “Ingestions” only Ingestions are shown in the table.
Each of these quick filter options can easily be deactivated again by
clicking on it again (check mark will disappear) and no filters will be
applied to the table below anymore.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image18.png"
style="width:6.925in;height:1.64167in"
data-fig-alt="A screenshot of the Data Catalogue page within the Copernicus Land Monitoring Service (CLMS) CLC+ Core system. The top navigation bar displays &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, with &#39;Renner Thomas&#39; logged in. The main section is titled &#39;Data Catalogue&#39; and includes interactive controls: a &#39;Filter&#39; button, &#39;My organisation/s&#39; button, &#39;My data&#39; button, and two prominent selection buttons, &#39;Ingestions&#39; (currently selected) and &#39;Extractions&#39;. A &#39;Search&#39; bar is visible to the right of these buttons. Further to the right are action buttons: &#39;ADD INGESTION&#39; and &#39;ADD EXTRACTION&#39;, along with a column selection icon that, when clicked, reveals a dropdown menu with checkboxes for &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, and &#39;Country&#39;. The central area displays a table listing &#39;Ingestions&#39;, which are input datasets typically resampled or aggregated to 100 x 100 m spatial resolution. The table columns are: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, and &#39;Status&#39;. The table contains four rows of data: * **Row 1:** EAGLE Approved (checked), Name &#39;CLC+Backbone (2018)&#39;, Type [icon, no visible text], Created At &#39;05.09.2023&#39;, Created By &#39;CLC+ Core User Admin.&#39;, Country &#39;European Environ...&#39;, Region &#39;-&#39;, Reference Year &#39;2018&#39;, Time Range &#39;01.07.2017 - 30.06.2019&#39;, Organisation/s &#39;CLC, Europ...&#39;, Contact Person &#39;copernicus@eea....&#39;, Status &#39;USED&#39;. * **Row 2:** EAGLE Approved (checked), Name &#39;Coastal Zones (CZ) 20...&#39;, Type [icon, no visible text], Created At &#39;21.06.2023&#39;, Created By &#39;CLC+ Core User Admin.&#39;, Country &#39;European Environ...&#39;, Region &#39;European Environ...&#39;, Reference Year &#39;2018&#39;, Time Range &#39;01.01.2017 - 31.12.2019&#39;, Organisation/s &#39;CLC, Europ...&#39;, Contact Person &#39;info@eea.europa....&#39;, Status &#39;USED&#39;. * **Row 3:** EAGLE Approved (checked), Name &#39;Corine Land Cover (CL...&#39;, Type [icon, no visible text], Created At &#39;06.09.2023&#39;, Created By &#39;CLC+ Core User Admin.&#39;, Country &#39;European Environ...&#39;, Region &#39;-&#39;, Reference Year &#39;2018&#39;, Time Range &#39;01.01.2017 - 31.12.2018&#39;, Organisation/s &#39;CLC, Europ...&#39;, Contact Person &#39;copernicus@eea....&#39;, Status &#39;USED&#39;. * **Row 4:** EAGLE Approved (checked), Name &#39;Corine Land Cover (CL...&#39;, Type [icon, no visible text], Created At &#39;14.06.2023&#39;, Created By &#39;CLC+ Core User Admin.&#39;, Country &#39;European Environ...&#39;, Region &#39;European Environ...&#39;, Reference Year &#39;2018&#39;, Time Range &#39;01.01.2017 - 31.12.2018&#39;, Organisation/s &#39;CLC, Europ...&#39;, Contact Person &#39;copernicus@eea....&#39;, Status &#39;PUBLISHED&#39;." />

A screenshot of the Data Catalogue page within the Copernicus Land
Monitoring Service (CLMS) CLC+ Core system. The top navigation bar
displays “Data Catalogue”, “EAGLE Ontology”, “About EAGLE”,
“Organisations”, and “Users”, with “Renner Thomas” logged in. The main
section is titled “Data Catalogue” and includes interactive controls: a
“Filter” button, “My organisation/s” button, “My data” button, and two
prominent selection buttons, “Ingestions” (currently selected) and
“Extractions”. A “Search” bar is visible to the right of these buttons.
Further to the right are action buttons: “ADD INGESTION” and “ADD
EXTRACTION”, along with a column selection icon that, when clicked,
reveals a dropdown menu with checkboxes for “EAGLE Approved”, “Name”,
“Type”, “Created At”, “Created By”, and “Country”.

The central area displays a table listing “Ingestions”, which are input
datasets typically resampled or aggregated to 100 x 100 m spatial
resolution. The table columns are: “EAGLE Approved”, “Name”, “Type”,
“Created At”, “Created By”, “Country”, “Region”, “Reference Year”, “Time
Range”, “Organisation/s”, “Contact Person”, and “Status”.

The table contains four rows of data: \* **Row 1:** EAGLE Approved
(checked), Name “CLC+Backbone (2018)”, Type \[icon, no visible text\],
Created At “05.09.2023”, Created By “CLC+ Core User Admin.”, Country
“European Environ…”, Region “-”, Reference Year “2018”, Time Range
“01.07.2017 - 30.06.2019”, Organisation/s “CLC, Europ…”, Contact Person
“copernicus@eea….”, Status “USED”. \* **Row 2:** EAGLE Approved
(checked), Name “Coastal Zones (CZ) 20…”, Type \[icon, no visible
text\], Created At “21.06.2023”, Created By “CLC+ Core User Admin.”,
Country “European Environ…”, Region “European Environ…”, Reference Year
“2018”, Time Range “01.01.2017 - 31.12.2019”, Organisation/s “CLC,
Europ…”, Contact Person “info@eea.europa….”, Status “USED”. \* **Row
3:** EAGLE Approved (checked), Name “Corine Land Cover (CL…”, Type
\[icon, no visible text\], Created At “06.09.2023”, Created By “CLC+
Core User Admin.”, Country “European Environ…”, Region “-”, Reference
Year “2018”, Time Range “01.01.2017 - 31.12.2018”, Organisation/s “CLC,
Europ…”, Contact Person “copernicus@eea….”, Status “USED”. \* **Row 4:**
EAGLE Approved (checked), Name “Corine Land Cover (CL…”, Type \[icon, no
visible text\], Created At “14.06.2023”, Created By “CLC+ Core User
Admin.”, Country “European Environ…”, Region “European Environ…”,
Reference Year “2018”, Time Range “01.01.2017 - 31.12.2018”,
Organisation/s “CLC, Europ…”, Contact Person “copernicus@eea….”, Status
“PUBLISHED”.

<span id="_Ref151467380" class="anchor"></span>**Figure 1‑9: Data
Catalogue – Main functionalities**

## Auxiliary / Supporting functions

**Breadcrumbs** appear on sub-pages to show their parent pages. This
helps you to identify how you got to the page you are currently working
on (see [Figure 1‑10](#_Ref151467456)). In addition, it provides you
more information about the context. Breadcrumbs are not clickable.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image19.png"
style="width:6.925in;height:3.82847in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, displaying the details of an &#39;Ingestion&#39; data product titled &#39;HRL - Impervious Density (IMD) 2018&#39;. The interface is structured with general information on the left, an interactive map visualisation, and details on continuous input classes at the bottom. The dataset is marked as &#39;USED&#39;. The &#39;General Information&#39; section provides: - **Name:** HRL - Impervious Density (IMD) 2018 - **Country:** European Environment Agency (38+UK) - **Region:** European Environment Agency (38+UK) - **Reference Year:** 2018 - **Time Range of Ingested Data:** 01.01.2017 - 31.12.2019 - **INSPIRE Themes:** LC Land cover - **Created By:** CLC+ Core User Admin/Support - **Organisation/s:** CLC, European Environment Agency - **Visibility:** Public - All Organisations - **Contact Person:** copernicus@eea.europa.eu - **Link to Document/s:** https://land.copernicus.eu/pan-european/high-resolution-layers/imperviousness/status-maps. An embedded map visualises the Degree of Imperviousness (IMD) using a dark red overlay on a detailed base map of Denmark and parts of southern Sweden (e.g., Malmö region). Heavily urbanised areas such as Copenhagen appear in dark red, indicating high imperviousness. The map has a scale bar showing &#39;10 km&#39; and &#39;5 mi&#39;. A filter indicates &#39;Country * DK Denmark/Danmark&#39;. Below the map, the &#39;Continuous Input Classes&#39; section displays a service URL for the data tiles and a &#39;DOWNLOAD EAGLE BARCODING&#39; button. A table-like structure shows the following for the data product: - **Class Code:** CONTINUOUS - **Name:** Degree of Imperviousness (IMD) - **EAGLE Elements:** Sealed Artificial Surfaces and Constructions +1 - **100% EAGLE compliant:** [checked] - **Colour:** Dark red swatch - **Show in Map:** [toggle on] The top navigation bar includes &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and &#39;CLC+ Core User Admin/Support&#39;. Action buttons include &#39;REPUBLISH ON GEOSERVER&#39;, &#39;ARCHIVE&#39;, and &#39;APPROVE EAGLE COMPLIANCE&#39; associated with the EIONET Action Group EAGLE logo." />

A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core
user interface, displaying the details of an ‘Ingestion’ data product
titled ‘HRL - Impervious Density (IMD) 2018’. The interface is
structured with general information on the left, an interactive map
visualisation, and details on continuous input classes at the bottom.
The dataset is marked as “USED”.

The “General Information” section provides: - **Name:** HRL - Impervious
Density (IMD) 2018 - **Country:** European Environment Agency (38+UK) -
**Region:** European Environment Agency (38+UK) - **Reference Year:**
2018 - **Time Range of Ingested Data:** 01.01.2017 - 31.12.2019 -
**INSPIRE Themes:** LC Land cover - **Created By:** CLC+ Core User
Admin/Support - **Organisation/s:** CLC, European Environment Agency -
**Visibility:** Public - All Organisations - **Contact Person:**
copernicus@eea.europa.eu - **Link to Document/s:**
https://land.copernicus.eu/pan-european/high-resolution-layers/imperviousness/status-maps.

An embedded map visualises the Degree of Imperviousness (IMD) using a
dark red overlay on a detailed base map of Denmark and parts of southern
Sweden (e.g., Malmö region). Heavily urbanised areas such as Copenhagen
appear in dark red, indicating high imperviousness. The map has a scale
bar showing “10 km” and “5 mi”. A filter indicates “Country \* DK
Denmark/Danmark”.

Below the map, the “Continuous Input Classes” section displays a service
URL for the data tiles and a “DOWNLOAD EAGLE BARCODING” button. A
table-like structure shows the following for the data product: - **Class
Code:** CONTINUOUS - **Name:** Degree of Imperviousness (IMD) - **EAGLE
Elements:** Sealed Artificial Surfaces and Constructions +1 - **100%
EAGLE compliant:** \[checked\] - **Colour:** Dark red swatch - **Show in
Map:** \[toggle on\]

The top navigation bar includes “Data Catalogue”, “EAGLE Ontology”,
“About EAGLE”, “Organisations”, “Users”, and “CLC+ Core User
Admin/Support”. Action buttons include “REPUBLISH ON GEOSERVER”,
“ARCHIVE”, and “APPROVE EAGLE COMPLIANCE” associated with the EIONET
Action Group EAGLE logo.

<span id="_Ref151467456" class="anchor"></span>**Figure 1‑10:
Breadcrumbs**

**Pagination** is only available on the page if applicable to the
content of the page, for example where tables / lists exist. With the
pagination you can navigate through the different pages of a table (see
Figure 1‑11). On pages with a higher number, you can find previously
ingested datasets.

**Help function** by clicking on the “?” icon on the bottom right corner
(see Figure 1‑11) a separate Help window opens in which the use can
report any issues or questions. The support contact form can be found
here: <https://land.copernicus.eu/en/contact-service-helpdesk>.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image21.png"
style="width:6.925in;height:3.82847in"
data-fig-alt="This image displays a tabular view of the Data Catalogue within the Copernicus Land Monitoring Service (CLMS) CLC+ Core system, showing entries for various ingested High Resolution Layer (HRL) and other land monitoring products. The table lists 9 entries (items 21-30 of 31) with the following columns: | EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | INSPIRE Themes | |---|---|---|---|---|---|---|---|---|---|---|---|---| | | HRL - Dominant Leaf Type (DLT) | [document icon] | 05.09.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Forest Type (FTY) 2018 | [document icon] | 10.03.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | HRL - Grassland (GRA) 2018 | [document icon] | 05.09.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Imperviousness Density (IMD) 2018 | [document icon] | 09.03.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.01.2017 - 31.12.2019 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Tree Cover Density (TCD) 2018 | [document icon] | 09.03.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.03.2018 - 31.10.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land cover | | | HRL - Water and Wetness (WAT) 2018 | [document icon] | 06.09.2023 | CLC+ Core User Administrator | European Environment Agency | - | 2018 | 01.01.2012 - 31.12.2018 | Copernicus Land Monitoring Service, European Environment Agency | info@eea.europa.eu | USED | Land cover | | | Natura 2000 (N2K) 2018 | [document icon] | 21.06.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2019 | 15.05.2017 - 14.09.2019 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | Riparian Zones (RZ) 2018 | [document icon] | 21.06.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.03.2018 - 31.07.2018 | Copernicus Land Monitoring Service, European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | Riparian Zones (RZ) 2018 | [document icon] | 21.02.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 01.03.2018 - 31.07.2018 | European Environment Agency | copernicus@eea.europa.eu | USED | Land use, Land cover | | | Urban Atlas (UA) 2018 | [document icon] | 20.06.2023 | CLC+ Core User Administrator | European Environment Agency | European Environment Agency | 2018 | 29.06.2017 - 01.09.2018 | Copernicus Land Monitoring Service, European Environment Agency | Matteo.Mattiuzzi | USED | Land use, Land cover | The table provides an overview of various CLMS High Resolution Layers (HRLs), Natura 2000 (N2K) data, Riparian Zones (RZ), and Urban Atlas (UA) products for the European Environment Agency, mostly from the 2018 reference year, categorised by INSPIRE Themes like &#39;Land cover&#39; and &#39;Land use, Land cover&#39;. Above the table, filtering options include &#39;My organisation/s,&#39; &#39;My data,&#39; &#39;Ingestions&#39; (currently active), and &#39;Extractions,&#39; along with a search bar and buttons for &#39;Add Ingestion&#39; and &#39;Add Extraction.&#39; Pagination at the bottom indicates &#39;21 - 30 of 31&#39; items are displayed, with 10 items per page. Logos for Copernicus, EAGLE, European Commission, and the European Environment Agency are visible at the bottom." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image20.png"
data-fig-alt="This image is a screenshot of a digital &#39;Help&#39; form, likely used for submitting support requests within the CLC+ Core system, as indicated by the surrounding context. The form is titled &#39;Help&#39; at the top and features several input fields: a text box for &#39;Summary&#39;, a dropdown selector for &#39;Priority&#39; which defaults to &#39;Medium&#39;, a larger text area for &#39;What are the details of your request?&#39;, an &#39;Attachment (optional)&#39; section with a &#39;Choose file&#39; link, and a text box for &#39;Your contact e-mail&#39;. At the bottom, a &#39;Send&#39; button is displayed. The footer of the form states &#39;Powered by Jira Service Management&#39;. A vertical scrollbar is visible on the right side of the form, and an &#39;x&#39; icon is in the top right corner for closing the form." />

**Figure 1‑11: Pagination and Help function**

### Search and Filter

In order to search for content within CLC+ Core, an option for
**searching** the system is available (see [Figure
1‑12](#_Ref151467805)). This is the grey field / box allows you to enter
text. After typing your search text into the search field, please press
the enter key to start the search process.

Besides the ‘Quick Filters’ (see section [1.6](#data-catalogue)) there
are some more detailed **filter** options which make the search more
user-friendly. You can filter all Ingestions and Extractions in a panel
by: country (single countries or e.g. EEA38+ UK or EU27 etc.), region,
reference year, time range, status or INSPIRE theme. It is also possible
to clear all filters after applying them. Or by click on the Filter
header to close the filter panel again. If the user navigates in the
same tab the filters remain saved until they are cleared.

By default, all archived data is not shown. By activating ‘Show ARCHIVED
data’ also archived data is considered in the filtering process and
results. Further the user can filter for Ingestions which have the EAGLE
Approval stamp (see section [2.5](#eagle-approval-stamp-for-ingestions))
by activating ‘Show only EAGLE approved Ingestions’.

**Filtered results** will be shown then on the right.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image23.png"
style="width:6.925in;height:3.78302in"
data-fig-alt="A screenshot of the CLC+ (Copernicus Land Cover / Land Use plus) Core application&#39;s Data Catalogue interface, focused on the &#39;Ingestions&#39; view, which includes filter options and pagination controls. The top navigation bar displays &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, with &#39;CLC+ Core User Admin/Support&#39; in the top right. The main section is titled &#39;Data Catalogue&#39;. Below this title, several tabs/buttons are visible: &#39;Filter&#39;, &#39;My organisation/s&#39; (checked), &#39;My data&#39;, &#39;Ingestions&#39; (checked), &#39;Extractions&#39;, and a &#39;Search&#39; bar. To the right are &#39;ADD INGESTION&#39;, &#39;ADD EXTRACTION&#39; buttons, and a trash can icon. A &#39;Filter&#39; panel is open on the left, with a &#39;CLOSE&#39; button. It contains input fields for &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time range&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. It also has two toggle switches: &#39;Show only EAGLE approved ingestions&#39; and &#39;Show ARCHIVED data&#39;. The main area on the right displays a table of data ingestions with the following columns: &#39;EAGLE Approved&#39; (with an upward arrow for sorting), &#39;Name&#39;, &#39;Type&#39; (indicated by a folder icon), &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, and &#39;Organisation&#39;. Visible table entries (10 of 33 items, page 1): 1. **CLC+Backbone (2018)**, Type folder icon, Created At 05.09.2023, Created By CLC+ Core User Admi..., Country European Environ..., Region -, Reference Year 2018, Time Range 01.07.2017 - 30.06.2019, Organisation CLC, Europe (checked as EAGLE Approved). 2. **CLC Change 100m rast...**, Type folder icon, Created At 25.05.2023, Created By CLC+ Core User Admi..., Country European Environ..., Region -, Reference Year 2011, Time Range 01.01.2011 - 31.12.2018, Organisation CLC, Europe. 3. **Coastal Zones (CZ) 20...**, Type folder icon, Created At 21.06.2023, Created By CLC+ Core User Admi..., Country European Environ..., Region -, Reference Year 2012, Time Range 01.01.2010 - 31.12.2014, Organisation CLC, Europe. 4. **Coastal Zones (CZ) 20...**, Type folder icon, Created At 21.06.2023, Created By CLC+ Core User Admi..., Country European Environ..., Region -, Reference Year 2018, Time Range 01.01.2017 - 31.12.2019, Organisation CLC, Europe. 5. **Corine Land Cover (CL...**, Type folder icon, Created At 06.09.2023, Created By CLC+ Core User Admi..., Country European Environ..., Region -, Reference Year 2018, Time Range 01.01.2017 - 31.12.2018, Organisation CLC, Europe. 6. **Corine Land Cover (CL...**, Type folder icon, Created At 14.06.2023, Created By CLC+ Core User Admi..., Country European Environ..., Region -, Reference Year 2018, Time Range 01.01.2017 - 31.12.2018, Organisation CLC, Europe. 7. **Effis 2018**, Type folder icon, Created At 05.09.2023, Created By CLC+ Core User Admi..., Country European Environ..., Region -, Reference Year 2018, Time Range 01.01.2018 - 31.12.2018, Organisation CLC, Europe. 8. **Eurocrop 2018**, Type folder icon, Created At 05.09.2023, Created By CLC+ Core User Admi..., Country European Union (...), Region -, Reference Year 2018, Time Range 01.01.2018 - 31.12.2018, Organisation CLC, Europe. 9. **Eurocrop 2018**, Type folder icon, Created At 17.10.2023, Created By CLC+ Core User Admi..., Country European Union (...), Region -, Reference Year -, Time Range -, Organisation CLC, Europe. 10. **Eurocrop 2018 Nordbur...**, Type folder icon, Created At 18.10.2023, Created By CLC+ Core User Admi..., Country Austria/Österreich, Region Nordburgenland, Reference Year -, Time Range -, Organisation CLC, Europe. Pagination controls at the bottom right show &#39;Items per page: 10&#39; and indicate &#39;1 - 10 of 33&#39; total entries, with navigation arrows for first, previous, next, and last page. A blue circular icon with a white question mark, representing a help function, is in the bottom right corner. Logos at the bottom left include &#39;European Union&#39;, &#39;Copernicus&#39;, &#39;BIONET Action Group EAGLE Land Monitoring in Europe&#39;, &#39;European Commission&#39;, and &#39;European Environment Agency&#39;." />

A screenshot of the CLC+ (Copernicus Land Cover / Land Use plus) Core
application’s Data Catalogue interface, focused on the ‘Ingestions’
view, which includes filter options and pagination controls.

The top navigation bar displays “Data Catalogue”, “EAGLE Ontology”,
“About EAGLE”, “Organisations”, and “Users”, with “CLC+ Core User
Admin/Support” in the top right.

The main section is titled “Data Catalogue”. Below this title, several
tabs/buttons are visible: “Filter”, “My organisation/s” (checked), “My
data”, “Ingestions” (checked), “Extractions”, and a “Search” bar. To the
right are “ADD INGESTION”, “ADD EXTRACTION” buttons, and a trash can
icon.

A “Filter” panel is open on the left, with a “CLOSE” button. It contains
input fields for “Country”, “Region”, “Reference Year”, “Time range”,
“Status”, and “INSPIRE Themes”. It also has two toggle switches: “Show
only EAGLE approved ingestions” and “Show ARCHIVED data”.

The main area on the right displays a table of data ingestions with the
following columns: “EAGLE Approved” (with an upward arrow for sorting),
“Name”, “Type” (indicated by a folder icon), “Created At”, “Created By”,
“Country”, “Region”, “Reference Year”, “Time Range”, and “Organisation”.

Visible table entries (10 of 33 items, page 1): 1. **CLC+Backbone
(2018)**, Type folder icon, Created At 05.09.2023, Created By CLC+ Core
User Admi…, Country European Environ…, Region -, Reference Year 2018,
Time Range 01.07.2017 - 30.06.2019, Organisation CLC, Europe (checked as
EAGLE Approved). 2. **CLC Change 100m rast…**, Type folder icon, Created
At 25.05.2023, Created By CLC+ Core User Admi…, Country European
Environ…, Region -, Reference Year 2011, Time Range 01.01.2011 -
31.12.2018, Organisation CLC, Europe. 3. **Coastal Zones (CZ) 20…**,
Type folder icon, Created At 21.06.2023, Created By CLC+ Core User
Admi…, Country European Environ…, Region -, Reference Year 2012, Time
Range 01.01.2010 - 31.12.2014, Organisation CLC, Europe. 4. **Coastal
Zones (CZ) 20…**, Type folder icon, Created At 21.06.2023, Created By
CLC+ Core User Admi…, Country European Environ…, Region -, Reference
Year 2018, Time Range 01.01.2017 - 31.12.2019, Organisation CLC, Europe.
5. **Corine Land Cover (CL…**, Type folder icon, Created At 06.09.2023,
Created By CLC+ Core User Admi…, Country European Environ…, Region -,
Reference Year 2018, Time Range 01.01.2017 - 31.12.2018, Organisation
CLC, Europe. 6. **Corine Land Cover (CL…**, Type folder icon, Created At
14.06.2023, Created By CLC+ Core User Admi…, Country European Environ…,
Region -, Reference Year 2018, Time Range 01.01.2017 - 31.12.2018,
Organisation CLC, Europe. 7. **Effis 2018**, Type folder icon, Created
At 05.09.2023, Created By CLC+ Core User Admi…, Country European
Environ…, Region -, Reference Year 2018, Time Range 01.01.2018 -
31.12.2018, Organisation CLC, Europe. 8. **Eurocrop 2018**, Type folder
icon, Created At 05.09.2023, Created By CLC+ Core User Admi…, Country
European Union (…), Region -, Reference Year 2018, Time Range
01.01.2018 - 31.12.2018, Organisation CLC, Europe. 9. **Eurocrop 2018**,
Type folder icon, Created At 17.10.2023, Created By CLC+ Core User
Admi…, Country European Union (…), Region -, Reference Year -, Time
Range -, Organisation CLC, Europe. 10. **Eurocrop 2018 Nordbur…**, Type
folder icon, Created At 18.10.2023, Created By CLC+ Core User Admi…,
Country Austria/Österreich, Region Nordburgenland, Reference Year -,
Time Range -, Organisation CLC, Europe.

Pagination controls at the bottom right show “Items per page: 10” and
indicate “1 - 10 of 33” total entries, with navigation arrows for first,
previous, next, and last page. A blue circular icon with a white
question mark, representing a help function, is in the bottom right
corner. Logos at the bottom left include “European Union”, “Copernicus”,
“BIONET Action Group EAGLE Land Monitoring in Europe”, “European
Commission”, and “European Environment Agency”.

<span id="_Ref151467805" class="anchor"></span>**Figure 1‑12: Search and
Filter function in the Data Catalogue**

The search function can be found in several tabs in the CLC+ Core
system. In the Data Catalogue you can search for Ingestions and
Extractions (section [3](#ingestions) and [4](#extraction)). Here you
are able to search for Information of each column (Name, Type, Created
at, etc.). The function allows to search Input Classes to be used for an
Extraction (section [4.4](#add-input-classes-to-extraction)) as well as
for Users or Organisations of the CLC+ Core system (section
[1.3](#webpage-elements)).

### Pop-ups/Inline Notifications

**Inline Notifications** are shown immediately after you have triggered
an action for a process that runs in the background e.g. start a
‘Preview’ or ‘Ingestion’. <u>Failed notifications</u> are shown in red
([Figure 1‑13](#_Ref98847093)). They will disappear automatically after
a while. These notifications provide support and information on how to
solve the issue.

In the example in [Figure 1‑13](#_Ref98847093), the EAGLE barcoding is
missing and the Country / Region field has not been filled out –
therefore these fields are highlighted in red, and you get the hint with
the notification to fill out all required fields. If not all required
fields are filled the action/process cannot start.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image24.png"
style="width:6.92939in;height:6.15834in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, displaying the &#39;Data Catalogue / Ingestion &#39;N2K 2018&#39;&#39; screen in DRAFT status. A red banner at the top reads: &#39;Please fill out all the required fields and save your changes! DISMISS&#39;. The interface has a top navigation bar with links: &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. On the right, &#39;User Admin/Support CLC+ Core&#39; is displayed. Action buttons &#39;START INGESTION&#39; and &#39;PUBLISH&#39; are visible at the top right. The left panel, titled &#39;General Information&#39; with an &#39;EDIT&#39; button, details the ingested data: * **Name:** N2K 2018 * **Country:** European Environment Agency (38+UK) * **Region:** - * **Reference Year:** 2018 * **Time Range of Ingested Data:** 15.05.2017 - 14.09.2019 (includes a &#39;?&#39; help icon) * **INSPIRE Themes:** LC Land cover (linked) * **Created By:** User Admin/Support CLC+ Core (linked) * **Organisation/s:** European Environment Agency (linked) * **Contact Person:** copernicus@eea.europa.eu * **Link to Document/s:** (includes a &#39;?&#39; help icon) Below this, a &#39;Description Abstract&#39; states: &#39;Land Cover/Land Use (LC/LU) status map as part of the Copernicus Land Monitoring Service (CLMS) Local Component, tailored to the needs of biodiversity monitoring in selected Natura 2000 (N2K) sites (4790 sites of natural and semi-natural grassland formations listed in Annex I of the Habitats Directive) including a 2 km buffer zone surrounding the sites and covering an area of 631.820 km² across Europe. LC/LU is extracted from VHR satellite data and other available data. The reference year for the classification is 2018. For further information on the CLMS Local Component please refer to https://land.copernicus.eu/local.&#39; The &#39;Lineage&#39; section below the abstract further specifies: &#39;Generation of a Land Cover/Land Use (LC/LU) dataset by visual image interpretation and delineation based on Very High Resolution (VHR) satellite data from 2018 ±1 year. Additional in-situ and ancillary datasets relevant for the production were also integrated into the workflow to support the LC/LU analysis. The classification provides 55 distinct thematic classes. The class definitions follow a pre-defined nomenclature based on the Mapping and Assessment of Ecosystems and their Services.&#39; The right panel features an interactive map of Central Europe, displaying countries like France, Germany, Switzerland, Austria, Czech Republic, Slovakia, Hungary, Romania, and Moldova, with cities such as London, Paris, Köln, Wien, Milano, and București labelled. It includes zoom controls (+/-), a full extent button, and a layers button. Input fields for &#39;Country*&#39; and &#39;Region*&#39; are present, along with a &#39;PREVIEW&#39; button. A message overlaid on the map reads: &#39;Your map is outdated! Please press &#39;PREVIEW&#39; to generate the map according to your new input&#39;. A scale bar shows &#39;200 km&#39; and &#39;100 mi&#39;. The map&#39;s copyright is &#39;Leaflet | EEA Copernicus programme, German Aerospace Center (DLR) CC-BY 3.0&#39;. Below the map is an &#39;Input Classes&#39; table with columns: &#39;Class Code&#39;, &#39;Name*&#39;, &#39;EAGLE Elements*&#39;, &#39;100% EAGLE compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39;. Six rows are partially visible, with &#39;Class Code&#39; and &#39;Name*&#39; values of 1110, 1120, 1210, 1220, 1230," />

A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core
user interface, displaying the “Data Catalogue / Ingestion ‘N2K 2018’”
screen in DRAFT status. A red banner at the top reads: “Please fill out
all the required fields and save your changes! DISMISS”.

The interface has a top navigation bar with links: “Data Catalogue”,
“EAGLE Ontology”, “About EAGLE”, “Organisations”, and “Users”. On the
right, “User Admin/Support CLC+ Core” is displayed. Action buttons
“START INGESTION” and “PUBLISH” are visible at the top right.

The left panel, titled “General Information” with an “EDIT” button,
details the ingested data: \* **Name:** N2K 2018 \* **Country:**
European Environment Agency (38+UK) \* **Region:** - \* **Reference
Year:** 2018 \* **Time Range of Ingested Data:** 15.05.2017 - 14.09.2019
(includes a ‘?’ help icon) \* **INSPIRE Themes:** LC Land cover (linked)
\* **Created By:** User Admin/Support CLC+ Core (linked) \*
**Organisation/s:** European Environment Agency (linked) \* **Contact
Person:** copernicus@eea.europa.eu \* **Link to Document/s:** (includes
a ‘?’ help icon)

Below this, a “Description Abstract” states: “Land Cover/Land Use
(LC/LU) status map as part of the Copernicus Land Monitoring Service
(CLMS) Local Component, tailored to the needs of biodiversity monitoring
in selected Natura 2000 (N2K) sites (4790 sites of natural and
semi-natural grassland formations listed in Annex I of the Habitats
Directive) including a 2 km buffer zone surrounding the sites and
covering an area of 631.820 km² across Europe. LC/LU is extracted from
VHR satellite data and other available data. The reference year for the
classification is 2018. For further information on the CLMS Local
Component please refer to https://land.copernicus.eu/local.” The
“Lineage” section below the abstract further specifies: “Generation of a
Land Cover/Land Use (LC/LU) dataset by visual image interpretation and
delineation based on Very High Resolution (VHR) satellite data from 2018
±1 year. Additional in-situ and ancillary datasets relevant for the
production were also integrated into the workflow to support the LC/LU
analysis. The classification provides 55 distinct thematic classes. The
class definitions follow a pre-defined nomenclature based on the Mapping
and Assessment of Ecosystems and their Services.”

The right panel features an interactive map of Central Europe,
displaying countries like France, Germany, Switzerland, Austria, Czech
Republic, Slovakia, Hungary, Romania, and Moldova, with cities such as
London, Paris, Köln, Wien, Milano, and București labelled. It includes
zoom controls (+/-), a full extent button, and a layers button. Input
fields for “Country*” and ”Region*” are present, along with a “PREVIEW”
button. A message overlaid on the map reads: “Your map is outdated!
Please press”PREVIEW” to generate the map according to your new input”.
A scale bar shows “200 km” and “100 mi”. The map’s copyright is “Leaflet
\| EEA Copernicus programme, German Aerospace Center (DLR) CC-BY 3.0”.

Below the map is an “Input Classes” table with columns: “Class Code”,
“Name*”, ”EAGLE Elements*”, “100% EAGLE compliant”, “Colour”, and “Show
in Map”. Six rows are partially visible, with “Class Code” and “Name\*”
values of 1110, 1120, 1210, 1220, 1230,

<span id="_Ref98847093" class="anchor"></span>**Figure 1‑13: Add
Ingestion – Notification of a failed preview due to missing EAGLE
barcoding and the Country/region field has not been filled out –
therefore these fields are highlighted in red, and you get the hint with
the notification to fill out all required fields.**

**Pop-up notifications** are messages shown on your desktop to grab your
attention. The following figures show some examples for pop-up
notifications (see [Figure 1‑14](#_Ref98938457), [Figure
1‑15](#_Ref98938435) and [Figure 1‑16](#_Ref98938437)). Pop-up
notifications are also shown in case there is an invalid entry in the
uploaded EAGLE barcoding file (see [Figure 1-17](#_Ref152831048)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image25.jpeg"
style="width:6.925in;height:2.79415in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, displaying the &#39;Data Catalogue&#39; section. The top navigation bar includes &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, with &#39;CLC+ Core User Admin/Support&#39; also visible. The main panel, titled &#39;Data Catalogue&#39;, shows a filtering and search bar with options to filter by &#39;My organisation/s&#39;, &#39;My data&#39;, &#39;Ingestions&#39;, and &#39;Extractions&#39;. A search field is present. Action buttons &#39;ADD INGESTION&#39; and &#39;ADD EXTRACTION&#39; are also visible. A list of data items is displayed with the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, and &#39;Status&#39;. Examples of listed data include: * &#39;HRL - Water and Wetne...&#39;, created 06.09.2023 by &#39;CLC+ Core User Admi...&#39; for &#39;European Environ...&#39; in &#39;2018&#39; with a time range of &#39;01.01.2012 - 31.12.2018&#39;, status &#39;USED&#39;. * &#39;N2K 2018&#39; (Natura 2000), created 21.06.2023, status &#39;USED&#39;. * &#39;Riparian Zones (RZ) 20...&#39; (Riparian Zones), created 21.06.2023, status &#39;USED&#39;. * &#39;Urban Atlas (UA) 2018&#39;, created 20.06.2023, status &#39;USED&#39;. * &#39;Urban_Atlas_IBK_2018&#39;, created 21.11.2023, for &#39;Austria/Osterei...&#39;, with status &#39;UPLOAD_ERROR!&#39;. A pop-up window titled &#39;Uploading error for ingestion: Urban_Atlas_IBK_2018&#39; is centrally displayed. The error message states: &#39;The upload failed because the url directed to a file which is not supported for ingestion. It needs to contain a file of the type: tif, TIF, TIFF, zip, h5, gpkg.&#39; It further advises: &#39;If the url opens a download page, please enter the download link you find there as the source for the upload.&#39; It provides an error ID: &#39;84a7a295-53b7-42b1-87ba-b70d167c11f1&#39; and suggests using &#39;RETRY&#39; or &#39;RETRY MERGE&#39; actions, or &#39;DELETE&#39; the ingestion if changes are not possible. Buttons &#39;CLOSE&#39;, &#39;DELETE&#39;, &#39;RETRY&#39;, and &#39;RETRY MERGE&#39; are available. The bottom of the main panel shows pagination controls: &#39;Items per page: 10&#39; and &#39;11 - 20 of 32&#39;. On the right side, a &#39;Notifications&#39; panel lists recent activities, with a &#39;MARK ALL AS READ&#39; option. Notifications include &#39;Urban_Atlas_IBK_2018 uploading error&#39; (indicated by a red exclamation mark, &#39;Just now&#39;, &#39;8 minutes ago&#39;) and &#39;Urban_Atlas_IBK_2018 processing finished&#39; (indicated by a green checkmark, &#39;4 minutes ago&#39;, &#39;20 minutes ago&#39;). Also listed are multiple &#39;LULUCF firstCov extracted&#39;, &#39;LULUCF sumCov extracted&#39;, and &#39;LULUCF maxCov extracted&#39; notifications (all with green checkmarks, &#39;26 days ago&#39; or &#39;27 days ago&#39;)." />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) CLC+ Core user interface, displaying the “Data Catalogue”
section. The top navigation bar includes “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”, with “CLC+ Core
User Admin/Support” also visible.

The main panel, titled “Data Catalogue”, shows a filtering and search
bar with options to filter by “My organisation/s”, “My data”,
“Ingestions”, and “Extractions”. A search field is present. Action
buttons “ADD INGESTION” and “ADD EXTRACTION” are also visible.

A list of data items is displayed with the following columns: “EAGLE
Approved”, “Name”, “Type”, “Created At”, “Created By”, “Country”,
“Region”, “Reference Year”, “Time Range”, “Organisation/s”, “Contact
Person”, and “Status”. Examples of listed data include: \* “HRL - Water
and Wetne…”, created 06.09.2023 by “CLC+ Core User Admi…” for “European
Environ…” in “2018” with a time range of “01.01.2012 - 31.12.2018”,
status “USED”. \* “N2K 2018” (Natura 2000), created 21.06.2023, status
“USED”. \* “Riparian Zones (RZ) 20…” (Riparian Zones), created
21.06.2023, status “USED”. \* “Urban Atlas (UA) 2018”, created
20.06.2023, status “USED”. \* “Urban_Atlas_IBK_2018”, created
21.11.2023, for “Austria/Osterei…”, with status “UPLOAD_ERROR!”.

A pop-up window titled “Uploading error for ingestion:
Urban_Atlas_IBK_2018” is centrally displayed. The error message states:
“The upload failed because the url directed to a file which is not
supported for ingestion. It needs to contain a file of the type: tif,
TIF, TIFF, zip, h5, gpkg.” It further advises: “If the url opens a
download page, please enter the download link you find there as the
source for the upload.” It provides an error ID:
“84a7a295-53b7-42b1-87ba-b70d167c11f1” and suggests using “RETRY” or
“RETRY MERGE” actions, or “DELETE” the ingestion if changes are not
possible. Buttons “CLOSE”, “DELETE”, “RETRY”, and “RETRY MERGE” are
available.

The bottom of the main panel shows pagination controls: “Items per page:
10” and “11 - 20 of 32”.

On the right side, a “Notifications” panel lists recent activities, with
a “MARK ALL AS READ” option. Notifications include “Urban_Atlas_IBK_2018
uploading error” (indicated by a red exclamation mark, “Just now”, “8
minutes ago”) and “Urban_Atlas_IBK_2018 processing finished” (indicated
by a green checkmark, “4 minutes ago”, “20 minutes ago”). Also listed
are multiple “LULUCF firstCov extracted”, “LULUCF sumCov extracted”, and
“LULUCF maxCov extracted” notifications (all with green checkmarks, “26
days ago” or “27 days ago”).

<span id="_Ref98938457" class="anchor"></span>**Figure 1‑14: Pop-up
Notification about deleting Ingestion. If an Ingestion upload was not
successful, you can either delete the Ingestion or retry with different
datasets or input parameters.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image26.png"
style="width:6.925in;height:3.00347in"
data-fig-alt="This image is a screenshot of the CLC+ Core (Copernicus Land Monitoring Service) Data Catalogue user interface, displaying a list of data &#39;Ingestions&#39; and a modal dialog for confirming deletion. The header navigation includes &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and &#39;CLC+ Core User Admin/Support&#39;. The main &#39;Data Catalogue&#39; view features a filter and search bar: * &#39;Filter&#39; button * Two checkboxes: &#39;My organisation/s&#39; (checked) and &#39;My data&#39; (unchecked). * Two toggle buttons: &#39;Ingestions&#39; (checked) and &#39;Extractions&#39; (unchecked). * A search bar with &#39;Search&#39; as placeholder text. * Action buttons: &#39;Add Ingestion&#39;, &#39;Add Extraction&#39;, a trash can icon, and a dropdown arrow. Below this, a table lists various data ingestions with the following columns: * **EAGLE Approved**: (mostly blank) * **Name**: Examples include &#39;UA_IBK_2018&#39;, &#39;Test 2023_10_19&#39;, &#39;Eurocrop 2018 Nordbur...&#39;, &#39;LULUCF Eagle Test&#39;, &#39;HRL - Water and Wetness...&#39;, &#39;Corine Land Cover (CLC+...&#39;, &#39;HRL - Grassland 2018&#39;. * **Type**: Document icon for all visible entries. * **Created At**: Dates ranging from &#39;21.11.2023&#39; to &#39;05.09.2023&#39;. * **Created By**: Consistently &#39;CLC+ Core User Admi...&#39;. * **Country**: Examples include &#39;Austria/Österreich&#39;, &#39;European Environ...&#39;. * **Region**: Examples include &#39;Innsbruck&#39;, &#39;Linz-Wels&#39;. * **Reference Year**: &#39;2018&#39; or &#39;-&#39;. * **Time Range**: &#39;01.01.2018 - 31.12.2018&#39;, &#39;01.01.2017 - 31.12.2018&#39;, &#39;01.03.2018 - 31.10.2018&#39;, or &#39;-&#39;. * **Organisation/s**: &#39;CLC, European En...&#39; for all visible entries. * **Contact Person**: &#39;info@eea.europa...&#39; or &#39;copernicus@eea...&#39;. * **Status**: Values include &#39;INGESTED&#39;, &#39;INGESTED_PREVIEW&#39;, &#39;DRAFT&#39;, and &#39;USED&#39;. * **INSPIRE Themes**: &#39;Land use, Land cover&#39; or &#39;-&#39;. At the bottom of the table, pagination controls indicate &#39;Items per page: 10&#39; and &#39;1 - 10 of 32&#39; total items. A modal dialog box is overlaid on the table, titled &#39;Delete Ingestion &#39;UA_IBK_2018&#39;&#39;. The dialog text reads: &#39;Are you sure you want to delete Ingestion &#39;UA_IBK_2018&#39;? Deleting this Ingestion will also delete all uploaded files and configurations.&#39; It presents two buttons: &#39;CANCEL&#39; and &#39;DELETE&#39; (highlighted in green)." />

This image is a screenshot of the CLC+ Core (Copernicus Land Monitoring
Service) Data Catalogue user interface, displaying a list of data
‘Ingestions’ and a modal dialog for confirming deletion.

The header navigation includes “Data Catalogue”, “EAGLE Ontology”,
“About EAGLE”, “Organisations”, “Users”, and “CLC+ Core User
Admin/Support”.

The main “Data Catalogue” view features a filter and search bar: \*
“Filter” button \* Two checkboxes: “My organisation/s” (checked) and “My
data” (unchecked). \* Two toggle buttons: “Ingestions” (checked) and
“Extractions” (unchecked). \* A search bar with “Search” as placeholder
text. \* Action buttons: “Add Ingestion”, “Add Extraction”, a trash can
icon, and a dropdown arrow.

Below this, a table lists various data ingestions with the following
columns: \* **EAGLE Approved**: (mostly blank) \* **Name**: Examples
include “UA_IBK_2018”, “Test 2023_10_19”, “Eurocrop 2018 Nordbur…”,
“LULUCF Eagle Test”, “HRL - Water and Wetness…”, “Corine Land Cover
(CLC+…”, “HRL - Grassland 2018”. \* **Type**: Document icon for all
visible entries. \* **Created At**: Dates ranging from “21.11.2023” to
“05.09.2023”. \* **Created By**: Consistently “CLC+ Core User Admi…”. \*
**Country**: Examples include “Austria/Österreich”, “European Environ…”.
\* **Region**: Examples include “Innsbruck”, “Linz-Wels”. \* **Reference
Year**: “2018” or “-”. \* **Time Range**: “01.01.2018 - 31.12.2018”,
“01.01.2017 - 31.12.2018”, “01.03.2018 - 31.10.2018”, or “-”. \*
**Organisation/s**: “CLC, European En…” for all visible entries. \*
**Contact Person**: “info@eea.europa…” or “copernicus@eea…”. \*
**Status**: Values include “INGESTED”, “INGESTED_PREVIEW”, “DRAFT”, and
“USED”. \* **INSPIRE Themes**: “Land use, Land cover” or “-”.

At the bottom of the table, pagination controls indicate “Items per
page: 10” and “1 - 10 of 32” total items.

A modal dialog box is overlaid on the table, titled “Delete Ingestion
‘UA_IBK_2018’”. The dialog text reads: “Are you sure you want to delete
Ingestion ‘UA_IBK_2018’? Deleting this Ingestion will also delete all
uploaded files and configurations.” It presents two buttons: “CANCEL”
and “DELETE” (highlighted in green).

<span id="_Ref98938435" class="anchor"></span>**Figure 1‑15: Pop-up
Notification about deleting Ingestion**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image27.png"
style="width:6.925in;height:3.35417in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core system user interface, showing an &#39;Upload Documents&#39; confirmation pop-up window. The pop-up displays the title &#39;Upload Documents&#39; and asks: &#39;Are you sure that you want to upload the documents?&#39;. A warning states: &#39;Please be aware, that in the case of metadata, legend or barcoding file the already entered input will be overwritten!&#39;. The user can choose between &#39;CANCEL&#39; and &#39;UPLOAD DOCUMENTS&#39; buttons. Behind the pop-up, parts of the data input/review interface are visible: - Initial metadata fields: &#39;Initial Spatial Resolution: 10 m&#39;, &#39;Initial Coordinate Reference System: EPSG:3035&#39;, &#39;Initial Type of Data: Vector&#39;, &#39;Excluded Class Code: -&#39;. - An &#39;Additional Documents&#39; section, containing an &#39;Upload Document/s&#39; button and descriptive text: &#39;All documents that help to understand the content, including legend files which will be used to automatically create input classes and metadata files which will be used to automatically prefill the data description.&#39; - A listed document with a trashcan icon: &#39;Riparian_Zones_2018_EAGLE_Barcoding_Template_3.1.2_23.12.2021_v1.xlsx&#39;. - Partially visible rows of a table listing land cover classes, including: - Code 1320: &#39;Land without current use&#39; (Open Sealed Surfaces, +9) - Code 1400: &#39;Green urban, sport and leisure facilities&#39; (Sealed Artificial Surfaces, +9) - Code 2110: &#39;Arable irrigated and non-irrigated land&#39; (Bare Soils, +6) - Code 2120: &#39;Greenhouses&#39; (Specific Buildings, +6) - Code 2210: &#39;Vineyards, fruit trees and berry plantations&#39; (Bare Soils, +10) - Code 2330: &#39;Land principally occupied by agriculture, with significant areas of natural vegetation&#39; (Boulders, Stones, +10) - Code 2340: &#39;Agro-forestry&#39; (Bare Soils, +5) - Code 3110: &#39;Natural &amp; semi-natural broadleaved forest&#39; (Trees, +8) - Code 3120: &#39;Highly artificial broadleaved plantations&#39; (Bare Soils, +9) - Code 3210: &#39;Natural &amp; semi-natural coniferous forest&#39; (Trees, +6) Each class row also includes two green checkmark icons and a small coloured square representing the class colour." />

A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core
system user interface, showing an “Upload Documents” confirmation pop-up
window. The pop-up displays the title “Upload Documents” and asks: “Are
you sure that you want to upload the documents?”. A warning states:
“Please be aware, that in the case of metadata, legend or barcoding file
the already entered input will be overwritten!”. The user can choose
between “CANCEL” and “UPLOAD DOCUMENTS” buttons.

Behind the pop-up, parts of the data input/review interface are
visible: - Initial metadata fields: “Initial Spatial Resolution: 10 m”,
“Initial Coordinate Reference System: EPSG:3035”, “Initial Type of Data:
Vector”, “Excluded Class Code: -”. - An “Additional Documents” section,
containing an “Upload Document/s” button and descriptive text: “All
documents that help to understand the content, including legend files
which will be used to automatically create input classes and metadata
files which will be used to automatically prefill the data
description.” - A listed document with a trashcan icon:
“Riparian_Zones_2018_EAGLE_Barcoding_Template_3.1.2_23.12.2021_v1.xlsx”. -
Partially visible rows of a table listing land cover classes,
including: - Code 1320: “Land without current use” (Open Sealed
Surfaces, +9) - Code 1400: “Green urban, sport and leisure facilities”
(Sealed Artificial Surfaces, +9) - Code 2110: “Arable irrigated and
non-irrigated land” (Bare Soils, +6) - Code 2120: “Greenhouses”
(Specific Buildings, +6) - Code 2210: “Vineyards, fruit trees and berry
plantations” (Bare Soils, +10) - Code 2330: “Land principally occupied
by agriculture, with significant areas of natural vegetation” (Boulders,
Stones, +10) - Code 2340: “Agro-forestry” (Bare Soils, +5) - Code 3110:
“Natural & semi-natural broadleaved forest” (Trees, +8) - Code 3120:
“Highly artificial broadleaved plantations” (Bare Soils, +9) - Code
3210: “Natural & semi-natural coniferous forest” (Trees, +6) Each class
row also includes two green checkmark icons and a small coloured square
representing the class colour.

<span id="_Ref98938437" class="anchor"></span>**Figure 1‑16: Pop-up
Notification about uploading documents**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image28.png"
style="width:6.3in;height:3.74792in"
data-fig-alt="Screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core system user interface, displaying an &#39;Error!&#39; pop-up notification over a list of land cover classification entries. The error message states: &#39;There was an error parsing the uploaded EAGLE Barcoding File. Could not parse the Input Classes in the following Excel columns: G, M, O, AC, AM, AQ&#39;. A green button labelled &#39;CLOSE&#39; is present at the bottom right of the pop-up. Partially visible in the background is a table or list of land cover definitions, with columns for a numerical code, &#39;Name *&#39;, and a corresponding land cover type. Visible entries include: * [unreadable code] / Land without current use / Open Sealed Surfaces * 14100 / Name * Green urban areas / Buildings * 14200 / Name * Sports and leisure facilities / Sealed Artificial Surfaces and Construction sites * 21000 / Name * Arable land (annual crops) / Standing Water * [partially obscured] / Commercial Crop Production * [partially obscured] / Forestry * [partially obscured] / Land Areas Not In Other Economic Use * [partially obscured] / Bare Rock * 33000 / Name * Open spaces with little or no vegetation * 40000 / Name * Wetlands / Liquid Water Bodies * 50000 / Name * Water / Open Sealed Surfaces The &#39;Name *&#39; field indicates it is a required input." />

Screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core
system user interface, displaying an “Error!” pop-up notification over a
list of land cover classification entries. The error message states:
“There was an error parsing the uploaded EAGLE Barcoding File. Could not
parse the Input Classes in the following Excel columns: G, M, O, AC, AM,
AQ”. A green button labelled “CLOSE” is present at the bottom right of
the pop-up.

Partially visible in the background is a table or list of land cover
definitions, with columns for a numerical code, “Name *“, and a
corresponding land cover type. Visible entries include:* \[unreadable
code\] / Land without current use / Open Sealed Surfaces \* 14100 / Name
\* Green urban areas / Buildings \* 14200 / Name \* Sports and leisure
facilities / Sealed Artificial Surfaces and Construction sites \* 21000
/ Name \* Arable land (annual crops) / Standing Water \* \[partially
obscured\] / Commercial Crop Production \* \[partially obscured\] /
Forestry \* \[partially obscured\] / Land Areas Not In Other Economic
Use \* \[partially obscured\] / Bare Rock \* 33000 / Name \* Open spaces
with little or no vegetation \* 40000 / Name \* Wetlands / Liquid Water
Bodies \* 50000 / Name \* Water / Open Sealed Surfaces

The “Name \*” field indicates it is a required input.

<span id="_Ref152831048" class="anchor"></span>**Figure 1-17: Pop-up
Notification about errors in the uploaded EAGLE barcoding file and the
hint in which columns in the Excel file there are some potential
errors.**

### Notifications messages

The user gets notified whenever there is a change of status happening
with the user’s Ingestion or Extraction. Whenever a Ingestion or
Extraction gets published, assuming it was published with public
visibility (see section [3.8](#publish-ingestion) and
[4.8](#publish-extraction-and-download-result)) all users get a
notification about the new publication.

The following events/status changes trigger a **notification message**
(examples see [Figure 1‑19](#_Ref151471608)):

- Ingestion Uploading Error

- Ingestion Processing Error

- Ingestion Processing Cancelled

- Ingestion Processing Finished

- Ingestion Ingesting Error

- Ingestion Ingesting Cancelled

- Ingestion Ingested

- Ingestion Published

- Extraction Extracting Error

- Extraction Extracting Cancelled

- Extraction Extracted

- Extraction Published

- Barcoding approved by EAGLE.

- Barcoding approval revoked

- New EAGLE ontology version published

**Notifications** are shown in the header (see clock icon on the upper
right corner next to the User profile/user name). Whenever there is a
new notification available and unread a blue dot appears next to the
clock icon (see Figure 1‑18).

By clicking on the **notification’s icon**, a more detailed view of the
notifications opens which includes all notifications (see Figure 1‑18).
By clicking on the notification or by clicking “Mark all as read” (all)
notifications get read and the blue dot disappears.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image30.png"
data-fig-alt="This image is a screenshot of the &#39;Data Catalogue&#39; user interface within a web application, likely for the Copernicus Land Monitoring Service (CLMS). The top header includes navigation links for &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, along with user support information (&#39;CLC+ Core User Admin / Support&#39;) and notification icons. The main section of the interface is titled &#39;Data Catalogue&#39; and features a filter bar with options: a &#39;Filter&#39; button and checkboxes labeled &#39;My organisation/s&#39;, &#39;My data&#39;, &#39;Ingestions&#39;, and &#39;Extractions&#39;. A search bar is present, alongside two prominent green buttons: &#39;ADD INGESTION&#39; and &#39;ADD EXTRACTION&#39;. Below the filter bar, a table-like display lists various data products with the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. All visible entries under &#39;EAGLE Approved&#39; show a checkmark. The &#39;Type&#39; column displays a document icon for all entries. &#39;Created By&#39; is consistently &#39;CLC+ Core User Admin&#39;, and &#39;Status&#39; is &#39;USED&#39;. The table displays the following data products (first 10 of 33 total items): * **CLC+ Backbone (2018)**: Created 05.09.2023, Country European Environment, Region -, Reference Year 2018, Time Range 01.07.2017 - 30.06.2019, Organisation/s CLC European Environment, Contact Person copernicus@eea.eu, Status USED, INSPIRE Themes Land-cover. * **Coastal Zones (CZ) 2018**: Created 21.06.2023, Country European Environment, Region European Environment, Reference Year 2018, Time Range 01.01.2017 - 31.12.2018, Organisation/s" />

This image is a screenshot of the “Data Catalogue” user interface within
a web application, likely for the Copernicus Land Monitoring Service
(CLMS). The top header includes navigation links for “Data Catalogue”,
“EAGLE Ontology”, “About EAGLE”, “Organisations”, and “Users”, along
with user support information (“CLC+ Core User Admin / Support”) and
notification icons.

The main section of the interface is titled “Data Catalogue” and
features a filter bar with options: a “Filter” button and checkboxes
labeled “My organisation/s”, “My data”, “Ingestions”, and “Extractions”.
A search bar is present, alongside two prominent green buttons: “ADD
INGESTION” and “ADD EXTRACTION”.

Below the filter bar, a table-like display lists various data products
with the following columns: “EAGLE Approved”, “Name”, “Type”, “Created
At”, “Created By”, “Country”, “Region”, “Reference Year”, “Time Range”,
“Organisation/s”, “Contact Person”, “Status”, and “INSPIRE Themes”. All
visible entries under “EAGLE Approved” show a checkmark. The “Type”
column displays a document icon for all entries. “Created By” is
consistently “CLC+ Core User Admin”, and “Status” is “USED”.

The table displays the following data products (first 10 of 33 total
items): \* **CLC+ Backbone (2018)**: Created 05.09.2023, Country
European Environment, Region -, Reference Year 2018, Time Range
01.07.2017 - 30.06.2019, Organisation/s CLC European Environment,
Contact Person copernicus@eea.eu, Status USED, INSPIRE Themes
Land-cover. \* **Coastal Zones (CZ) 2018**: Created 21.06.2023, Country
European Environment, Region European Environment, Reference Year 2018,
Time Range 01.01.2017 - 31.12.2018, Organisation/s

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image29.png"
style="width:6.9252in;height:1.33071in"
data-fig-alt="This image displays a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core User Interface, specifically the &#39;Data Catalogue&#39; view and a &#39;Notifications&#39; sidebar. The top navigation bar features links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. On the right, a notifications bell icon with a blue dot indicates unread notifications, alongside the &#39;CLC+ Core User Admin/Support&#39; user profile. The &#39;Data Catalogue&#39; section includes filtering options: &#39;Filter&#39;, &#39;My organisation/s&#39; (checked), &#39;My data&#39; (checked), &#39;Ingestions&#39; (checked), and &#39;Extractions&#39; (unchecked). A search bar is present, along with action buttons &#39;ADD INGESTION&#39;, &#39;ADD EXTRACTION&#39;, and icons for delete and download actions. The main content area is a table presenting data entries with the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, and &#39;Status&#39;. | EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | |:---------------|:------------------------------|:--------------|:-----------|:----------------------------|:----------------------------|:---------------------------|:---------------|:--------------------------|:--------------------------------|:---------------------------|:--------| | ✓ | CLC+Backbone (2018) | [Document icon] | 05.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | - | 2018 | 01.07.2017 - 30.06.2019 | CLC, European Environment Agency | copernicus@eea.europa.eu | USED ✓ | | ✓ | Coastal Zones (CZ) 20... | [Document icon] | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | European Environment Agency | 2018 | 01.01.2017 - 31.12.2" />

This image displays a screenshot of the Copernicus Land Monitoring
Service (CLMS) CLC+ Core User Interface, specifically the “Data
Catalogue” view and a “Notifications” sidebar.

The top navigation bar features links to “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”. On the right, a
notifications bell icon with a blue dot indicates unread notifications,
alongside the “CLC+ Core User Admin/Support” user profile.

The “Data Catalogue” section includes filtering options: “Filter”, “My
organisation/s” (checked), “My data” (checked), “Ingestions” (checked),
and “Extractions” (unchecked). A search bar is present, along with
action buttons “ADD INGESTION”, “ADD EXTRACTION”, and icons for delete
and download actions.

The main content area is a table presenting data entries with the
following columns: “EAGLE Approved”, “Name”, “Type”, “Created At”,
“Created By”, “Country”, “Region”, “Reference Year”, “Time Range”,
“Organisation/s”, “Contact Person”, and “Status”.

| EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| ✓ | CLC+Backbone (2018) | \[Document icon\] | 05.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | \- | 2018 | 01.07.2017 - 30.06.2019 | CLC, European Environment Agency | copernicus@eea.europa.eu | USED ✓ |
| ✓ | Coastal Zones (CZ) 20… | \[Document icon\] | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | European Environment Agency | 2018 | 01.01.2017 - 31.12.2 |  |  |  |

<span id="_Toc154044680" class="anchor"></span>**Figure 1‑18:
Notifications at the header (blue dot if new/unread notifications is
available), by clicking on the clock the notifications open up on the
right.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image34.png"
style="width:3.0392in;height:1.3969in"
data-fig-alt="The image displays two notification examples within a user interface for the Copernicus Land Monitoring Service (CLMS), specifically related to Corine Land Cover (CLC) 2018. The first notification, marked with a grey circular arrow icon containing a checkmark, states &#39;Corine Land Cover (CLC) 2018 published.&#39; and indicates it occurred &#39;5 days ago • You&#39;. The second notification, marked with a green checkmark icon, states &#39;Corine Land Cover (CLC) 2018 processing finished.&#39; and indicates it occurred &#39;6 days ago • You&#39;. Both &#39;Corine Land Cover (CLC) 2018&#39; texts are blue and underlined, suggesting they are clickable links for more details. These notifications represent status changes within a CLMS data management process." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image35.png"
style="width:2.76655in;height:1.42413in"
data-fig-alt="Screenshot of two user interface notifications, likely from a CLMS (Copernicus Land Monitoring Service) application. Each notification displays a red circular icon with a white exclamation mark, indicating a warning or error status. The first notification states: &#39;Corine Land Cover (CLC) 2018 processing error.&#39; The timestamp below it is &#39;9 days ago • You&#39;. The second notification states: &#39;Corine Land Cover (CLC) 2018 processing cancelled.&#39; The timestamp below it is also &#39;9 days ago • You&#39;. Both &#39;Corine Land Cover (CLC) 2018&#39; phrases are presented as blue hyperlinks. These examples illustrate system notifications for status changes related to CLC data processing." />

<span id="_Ref151471608" class="anchor"></span>**Figure 1‑19: Examples
for notification of status changes.**

Further if the users email address is added in the user profile an email
with the notification will be send automatically if the notification is
not read within 15 min (see below [Figure 1‑20](#_Ref151472379)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image36.png"
style="width:5.38844in;height:3.13785in"
data-fig-alt="This image is a screenshot of a notification from the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover+) Core System. The notification is displayed as if it were an email or an in-application alert. The sender is identified as &#39;CLC+ Core System &lt;clcplus-noreply@eea.europa.eu&gt;&#39;. The subject line states &#39;[CLC+ Core] &#39;HRL Grassland 2018 - Luxembourg&#39; published&#39;. The main body of the notification is titled &#39;Ingestion &#39;HRL Grassland 2018 - Luxembourg&#39; published&#39; and contains the message &#39;Hi Amelie, the ingestion &#39;HRL Grassland 2018 - Luxembourg&#39; was published by you.&#39; Below the message, a button labelled &#39;OPEN INGESTION&#39; is displayed. The footer of the notification also shows &#39;CLC+ Core&#39;. This notification indicates a status change related to the publication of the High Resolution Layer (HRL) Grassland product for Luxembourg from 2018." />

This image is a screenshot of a notification from the Copernicus Land
Monitoring Service (CLMS) CLC+ (CORINE Land Cover+) Core System. The
notification is displayed as if it were an email or an in-application
alert. The sender is identified as “CLC+ Core System
<clcplus-noreply@eea.europa.eu>”. The subject line states “\[CLC+ Core\]
‘HRL Grassland 2018 - Luxembourg’ published”. The main body of the
notification is titled “Ingestion ‘HRL Grassland 2018 - Luxembourg’
published” and contains the message “Hi Amelie, the ingestion ‘HRL
Grassland 2018 - Luxembourg’ was published by you.” Below the message, a
button labelled “OPEN INGESTION” is displayed. The footer of the
notification also shows “CLC+ Core”. This notification indicates a
status change related to the publication of the High Resolution Layer
(HRL) Grassland product for Luxembourg from 2018.

<span id="_Ref151472379" class="anchor"></span>**Figure 1‑20:
Notification email in case of an unread notification**

## Projections (of national datasets)

In general, datasets in national projections can be ingested into the
CLC+ Core. Since there is such a large number of different
**projections**, we ask for your understanding that the system cannot
take all projections into account. We have therefore limited ourselves
to the projections that are supported as national projections in the
CLMS products and by GDAL (see Annex Table 0‑4).

## About [EAGLE](https://land.copernicus.eu/eagle)

Within the Navigation Menu you can find the entry “**About EAGLE**”
which brings you directly to the [homepage of the EAGLE
group](https://land.copernicus.eu/en/eagle?tab=main) (see [Figure
1‑21](#_Ref151986403)) when clicking on it. On this page you can find
additional information about EAGLE, documentations and tools and the
context and background of the Pan-European Implementation of CLC+ based
on the EAGLE concept.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image37.png"
style="width:6.925in;height:3.82361in"
data-fig-alt="This is a screenshot of a Copernicus Land Monitoring Service (CLMS) webpage providing information about &#39;EAGLE&#39;. The page features a standard website layout with a green header bar containing navigation links for &#39;Technical assistance&#39;, &#39;News and Events&#39;, &#39;Work opportunities&#39;, and &#39;Register/Login&#39;, along with a search bar. The main header includes the &#39;Copernicus Europe&#39;s eyes on Earth&#39; logo and the &#39;Land Monitoring Service&#39; logo, accompanied by primary navigation links: &#39;CLMS portfolio&#39;, &#39;Dataset catalogue&#39;, &#39;Data viewer&#39;, &#39;Use cases&#39;, and &#39;About us&#39;. A breadcrumb navigation shows &#39;Home &gt; EAGLE&#39;. The main content area is titled &#39;EAGLE&#39; and features a left-hand navigation menu with the &#39;Main&#39; section highlighted, followed by &#39;The concept:&#39;, &#39;Introduction and context&#39;, &#39;Technical implementation&#39;, &#39;Bar-Coding&#39;, &#39;Use cases of EAGLE concept&#39;, &#39;Relation with ISO standards&#39;, and &#39;Document archive&#39;. The main text block provides details about EAGLE: * &#39;EAGLE - Action Group on land monitoring in Europe of the European environment information and observation network (Eionet).&#39; * &#39;Since 2008, the EAGLE Group has been developing a solution and proof of concept to support the semantic and technical framework of a European harmonised information capacity for land monitoring.&#39; * &#39;The EAGLE Group is a self-initiated and open group of land monitoring experts from different European Environment Agency (EEA) member countries, mostly – but not only – in their roles as Eionet members. Thus, the EAGLE Group brings together knowledge and experiences from existing land cover (LC) and land use (LU) classification approaches and initiatives in a bottom-up approach.&#39; * &#39;Meanwhile, EAGLE is acknowledged by the Copernicus Land Monitoring Service (CLMS) as an instrumental and crucial component to support a general shift of focus from classification to characterisation, and EAGLE compliance is enforced in all newer CLMS products.&#39; * &#39;The EAGLE concept is explicitly mentioned in the Copernicus Work Programmes as an essential pillar to support the challenging new use cases of the 2nd generation CORINE Land Cover (CLC), also known as CLC+. The EAGLE concept is now operationally implemented as a central component of the CLC+ implementation, to guarantee a standardized integration approach of different LC/LU products.&#39; A footer bar at the bottom also displays the &#39;Copernicus Europe&#39;s eyes on Earth&#39; logo." />

This is a screenshot of a Copernicus Land Monitoring Service (CLMS)
webpage providing information about “EAGLE”. The page features a
standard website layout with a green header bar containing navigation
links for “Technical assistance”, “News and Events”, “Work
opportunities”, and “Register/Login”, along with a search bar. The main
header includes the “Copernicus Europe’s eyes on Earth” logo and the
“Land Monitoring Service” logo, accompanied by primary navigation links:
“CLMS portfolio”, “Dataset catalogue”, “Data viewer”, “Use cases”, and
“About us”.

A breadcrumb navigation shows “Home \> EAGLE”. The main content area is
titled “EAGLE” and features a left-hand navigation menu with the “Main”
section highlighted, followed by “The concept:”, “Introduction and
context”, “Technical implementation”, “Bar-Coding”, “Use cases of EAGLE
concept”, “Relation with ISO standards”, and “Document archive”.

The main text block provides details about EAGLE: \* “EAGLE - Action
Group on land monitoring in Europe of the European environment
information and observation network (Eionet).” \* “Since 2008, the EAGLE
Group has been developing a solution and proof of concept to support the
semantic and technical framework of a European harmonised information
capacity for land monitoring.” \* “The EAGLE Group is a self-initiated
and open group of land monitoring experts from different European
Environment Agency (EEA) member countries, mostly – but not only – in
their roles as Eionet members. Thus, the EAGLE Group brings together
knowledge and experiences from existing land cover (LC) and land use
(LU) classification approaches and initiatives in a bottom-up approach.”
\* “Meanwhile, EAGLE is acknowledged by the Copernicus Land Monitoring
Service (CLMS) as an instrumental and crucial component to support a
general shift of focus from classification to characterisation, and
EAGLE compliance is enforced in all newer CLMS products.” \* “The EAGLE
concept is explicitly mentioned in the Copernicus Work Programmes as an
essential pillar to support the challenging new use cases of the 2nd
generation CORINE Land Cover (CLC), also known as CLC+. The EAGLE
concept is now operationally implemented as a central component of the
CLC+ implementation, to guarantee a standardized integration approach of
different LC/LU products.”

A footer bar at the bottom also displays the “Copernicus Europe’s eyes
on Earth” logo.

<span id="_Ref151986403" class="anchor"></span>**Figure 1‑21: Homepage
of the EAGLE group on land.copernicus.eu**

<span id="_Toc65609501" class="anchor"></span>

# [EAGLE](https://land.copernicus.eu/eagle)[^2]

Since 2008, the **EAGLE** Group has been developing a solution and proof
of concept to support the semantic and technical framework of a European
harmonised information capacity for land monitoring. The EAGLE Group is
a self-initiated and open group of land monitoring experts from
different European Environment Agency (EEA) member countries, mostly –
but not only – in their roles as EIONET members. Thus, the EAGLE Group
brings together knowledge and experiences from existing land cover (LC)
and land use (LU) classification approaches and initiatives in a
bottom-up approach.

Meanwhile, EAGLE barcoding is acknowledged by the Copernicus Land
Monitoring Service (CLMS) as an instrumental and crucial component to
support a general shift of focus from classification to
characterisation, and EAGLE compliance is enforced in all newer CLMS
products.

In the “**EAGLE Ontology**” tab you can inspect the current and older
EAGLE ontologies. You can download the EAGLE barcoding file template you
will need for the EAGLE barcoding (section 2.3). Additionally, expert
users have the possibility to add new EAGLE ontologies (section 6.3 in
separate Annex). The most current version of the EAGLE matrix is
v3.2[^3] which is also implemented already in the current version of the
CLC+ Core system. In the current EAGLE matrix version some elements have
been deleted and the barcoding values were reduced to X-5 instead of
before X,0-6.

In this section, you will be further given a general overview of the
EAGLE concept and the approach and implementation the CLC+ consortium
used for the EAGLE barcoding for the CLMS products ingested in the CLC+
Core system. To prove the concept also two national datasets for the
Netherlands and Spain were EAGLE barcoded and uploaded to the system.

## General overview of the EAGLE concept

The EAGLE concept[^4] is explicitly mentioned in the Copernicus Work
Programmes as an essential pillar to support the challenging new use
cases of the 2nd generation CORINE Land Cover (CLC), also known as CLC+.
The EAGLE concept is now operationally implemented as a central
component of the CLC+ implementation, to guarantee a standardized
integration approach of different LC/LU products.

The EAGLE concept has been established to ease the collection of data of
different classification systems and nomenclatures, with the aim to make
them comparable. The concept is based on a set of attributes that allow
the description of landscape objects. The EAGLE matrix itself is
presented in the form of an Excel cross table and is subdivided into
three main blocks. The matrix elements represent atomic landscape
descriptors of:

1.  LAND COVER Components – LCC,

2.  LAND USE Attributes – LUA,

3.  LAND CHARACTERISTICS – LCH

In the CLMS products, such as the HRLs, each class in the nomenclature
is coded by a specific number and definition. Compliance with the EAGLE
data model is ensured by switching to an object-based approach,
providing an INSPIRE-compatible distinction between LCC, LUA and
complementary object characteristics (CH). The connection and compliance
of the hierarchical CLC-driven and CODE level-based nomenclature to the
EAGLE data model is established via the EAGLE barcoding file. The EAGLE
barcoding values (see Annex Table 0-1) provide a semantic translation of
class definitions into the EAGLE matrix elements[^5].

[Figure 2‑1](#_Ref98942013) shows HRL IMD as example: Barcode of value 5
means that the input class directly relates to the EAGLE element
(*LCC_1_1_1* *Sealed Artificial Surfaces and Constructions*) and
therefore the spatial coverage of the class can be considered the
spatial coverage of the EAGLE element. A pure exclusive solitary element
and nothing else besides the 5-coded element is contained. Additionally,
a factor defines the coverage of the EAGLE element for the Input Class.
Value range is from 0.0 to 1.0. Together with the percentage coverage of
the Input Class for each cell it defines the coverage of the EAGLE
element for each cell. For example, if an Input Class has got a
percentage coverage of 80% for the specific cell and a factor of 0.5 is
applied to the specific EAGLE element, the coverage of the EAGLE element
for this cell is 40%.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image38.png"
style="width:3.99637in;height:2.97936in"
data-fig-alt="This table presents a hierarchical classification of Land Cover Components (LCC) as part of an EAGLE (European Ground Motion Service) barcoding template. The table includes metadata information at the top: &#39;Class Code*&#39; (with instruction &#39;If continuous dataset, enter &#39;0&#39; as Class Code&#39;), &#39;Name*&#39;, &#39;Degree of Imperviousness (IMD)&#39; (showing a value of &#39;0&#39; for the top-level LCC entry), &#39;100% EAGLE Compliant*&#39; (with possible values &#39;Yes&#39; / &#39;No&#39;, showing &#39;Yes&#39; for the top-level LCC entry), and &#39;Colour Code&#39; (with possible values &#39;only hex colour codes e.g. #87CEFA&#39;). The main body of the table contains the following columns: | URI | Land Cover Component | Barcode | Factor | [unreadable column] | |---|---|" />

This table presents a hierarchical classification of Land Cover
Components (LCC) as part of an EAGLE (European Ground Motion Service)
barcoding template. The table includes metadata information at the top:
“Class Code*” (with instruction ”If continuous dataset, enter ‘0’ as
Class Code”), ”Name*”, “Degree of Imperviousness (IMD)” (showing a value
of “0” for the top-level LCC entry), “100% EAGLE Compliant\*” (with
possible values “Yes” / “No”, showing “Yes” for the top-level LCC
entry), and “Colour Code” (with possible values “only hex colour codes
e.g. #87CEFA”).

The main body of the table contains the following columns: \| URI \|
Land Cover Component \| Barcode \| Factor \| \[unreadable column\] \|
\|—\|—\|

<span id="_Ref98942013" class="anchor"></span>**Figure 2‑1: The EAGLE
matrix for HRL Imperviousness degree (excerpt).**

## Approach and implementation used by the CLC+ CORE Consortium

It should be mentioned that the EAGLE barcoding was performed to the
best of the CLC+ Core consortiums’ knowledge and belief using a
‘simplified’ approach. The aim of this approach was not to describe the
Ingestion in the best and most extensive way, it is more to have the
best basis for the planed Extraction.

Therefore, we established several rules (section
[2.2.1](#mapping-approach-of-the-consortium)), which we followed
performing the EAGLE barcoding and might help other users creating their
own barcoding. With this approach the available CLMS datasets have been
ingested (see in Annex Table 0‑2). They are detectable as they were
created exclusively by the „User Admin /Support CLC+ Core” User.

### Mapping Approach of the Consortium

1.  **Stick to the guidelines / nomenclature**

- Go through the guidelines document, check the definition chapter, and
  identify land cover, land use and characteristics aspects. Also keep
  in mind the list of included categories.

2.  **Reduce complexity**

- Limit the complexity and simplify the barcoding (example see [Figure
  2‑2](#_Ref151986473)). Focus on the most useful codes and highest
  possible hierarchy levels, considering the future Extractions.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image39.png"
style="width:6.26806in;height:2.55556in"
data-fig-alt="This table displays a hierarchical classification of Land Cover Components (LCC) and their corresponding EAGLE data model barcoding values. | URI | Code | Label | Level | Barcode (Reduced complexity) | Factor (Reduced complexity) | Barcode (More explicit barcoding) | Factor (More explicit barcoding) | | :----------------------------------- | :------------- | :---------------------------------------- | :---- | :--------------------------- | :-------------------------- | :-------------------------------- | :------------------------------- | | `https://dd.ee/LCC` | `LCC` | Land Cover Components |" />

This table displays a hierarchical classification of Land Cover
Components (LCC) and their corresponding EAGLE data model barcoding
values.

| URI | Code | Label | Level | Barcode (Reduced complexity) | Factor (Reduced complexity) | Barcode (More explicit barcoding) | Factor (More explicit barcoding) |
|:---|:---|:---|:---|:---|:---|:---|:---|
| `https://dd.ee/LCC` | `LCC` | Land Cover Components |  |  |  |  |  |

<span id="_Ref151986473" class="anchor"></span>**Figure 2‑2: Comparison
simplified or more explicit barcoding**

3.  **Try to not interpret**

- Open sea is 100% marine water and therefore mapped with value of 5. It
  likely includes fishing but has not been mentioned in the guidelines
  thus, this LCC was not mapped ([Figure 2‑3](#_Ref100052219)).

- On the other hand, sometimes the Land Use is absolutely clear from the
  nomenclature. The Netherlands BBG dataset describes on class: "Inland
  water for mineral extraction”, which can be mapped as displayed in
  [Figure 2‑4](#_Ref100052208).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image40.png"
style="width:6.26806in;height:5.13194in"
data-fig-alt="This table presents an excerpt of an EAGLE (EIONET Action Group on Land monitoring in Europe) matrix, used for defining Land Cover / Land Use (LULC) classification. The matrix includes the following metadata properties: * **Class Code (If continuous dataset, enter &#39;0&#39; as Class Code)**: Value not specified for the overall table. * **EM**: 84100 * **EN**: Open sea * **100% EAGLE Compliant (Possible Values: &#39;Yes&#39; / &#39;No&#39;)**: Yes * **Colour Code (Possible values: only hex colour codes e.g. #87CEFA)**: #e6f5f3 The main classification data is structured as follows: | URI | Code | Label | Level | Barcode | Factor | |:---|:---|:---|:---:|:---:|:---:| | https://dd.e (truncated) | LCC-2_1_2 | Reeds, Bamboos, Canes | 4 | | | | https://dd.e (truncated) | LCC-2_2_2 | Non-Graminoids (Forbs, Ferns) | 3 | | | | https://dd.e (truncated) | LCC-2_3 | Succulents, Cacti | 2 | | | | https://dd.e (truncated) | LCC-2_4 | Lichens, Mosses, Algae | 2 | | | | https://dd.e (truncated) | LCC-2_4_1 | Lichens | 3 | | | | https://dd.e (truncated) | LCC-2_4_2 | Mosses | 3 | | | | https://dd.e (truncated) | LCC-2_4_3 | Algae | 3 | | | | https://dd.e (truncated) | LCC-2_4_3_1 | Macro Algae | 4 | | | | https://dd.e (truncated) | LCC-2_4_3_2 | Micro Algae (Plankton) | 4 | | | | https://dd.e (truncated) | LCC-3 | Water | 1 | 5 | | | https://dd.e (truncated) | LCC-3_1 | Liquid Water Bodies | 2 | | | | https://dd.e (truncated) | LCC-3_1_1 | Inland Water Bodies | 3 | | | | https://dd.e (truncated) | LCC-3_1_1_1 | Water Course | 4 | | | | https://dd.e (truncated) | LCC-3_1_1_2 | Standing Water | 4 | | | | https://dd.e (truncated) | LCC-3_1_2 | Marine Waters | 3 | | | | https://dd.e (truncated) | LCC-3_2 | Solid Waters | 2 | | | | https://dd.e (truncated) | LCC-3_2_1 | Snow | 3 | | | | https://dd.e (truncated) | LCC-3_2_2 | Ice, Glaciers | 3 | | | | https://dd.e (truncated) | LUA | Land Use Attributes | 0 | | | | https://dd.e (truncated) | LUA-1 | Primary Production Sector | 1 | | | | https://dd.e (truncated) | LUA-1_1 | Agriculture | 2 | | | | https://dd.e (truncated) | LUA-1_1_1 | Commercial Crop Production | 3 | | | | https://dd.e (truncated) | LUA-1_1_2 | Farming Infrastructure | 3 | | | | https://dd.e (truncated) | LUA-1_1_2_1 | Animal Husbandry | 4 | | | | https://dd.e (truncated) | LUA-1_1_2_2 | Farming Storage | 4 | | | | https://dd.e (truncated) | LUA-1_1_2_3 | Other Farming Infrastructure | 4 | | | | https://dd.e (truncated) | LUA-1_1_3 | Production for Own Consumption | 3 | | | | https://dd.e (truncated) | LUA-1_2 | Forestry | 2 | | | | https://dd.e (truncated) | LUA-1_3 | Mining and Quarrying | 2 | | | | https://dd.e (truncated) | LUA-1_4 | Aquaculture and Fishing | 2 | | | | https://dd.e (truncated) | LUA-1_4_1 | Aquaculture | 3 | | | | https://dd.e (truncated) | LUA-1_" />

This table presents an excerpt of an EAGLE (EIONET Action Group on Land
monitoring in Europe) matrix, used for defining Land Cover / Land Use
(LULC) classification. The matrix includes the following metadata
properties: \* **Class Code (If continuous dataset, enter “0” as Class
Code)**: Value not specified for the overall table. \* **EM**: 84100 \*
**EN**: Open sea \* **100% EAGLE Compliant (Possible Values: “Yes” /
“No”)**: Yes \* **Colour Code (Possible values: only hex colour codes
e.g. #87CEFA)**: \#e6f5f3

The main classification data is structured as follows:

| URI | Code | Label | Level | Barcode | Factor |
|:---|:---|:---|:--:|:--:|:--:|
| https://dd.e (truncated) | LCC-2_1_2 | Reeds, Bamboos, Canes | 4 |  |  |
| https://dd.e (truncated) | LCC-2_2_2 | Non-Graminoids (Forbs, Ferns) | 3 |  |  |
| https://dd.e (truncated) | LCC-2_3 | Succulents, Cacti | 2 |  |  |
| https://dd.e (truncated) | LCC-2_4 | Lichens, Mosses, Algae | 2 |  |  |
| https://dd.e (truncated) | LCC-2_4_1 | Lichens | 3 |  |  |
| https://dd.e (truncated) | LCC-2_4_2 | Mosses | 3 |  |  |
| https://dd.e (truncated) | LCC-2_4_3 | Algae | 3 |  |  |
| https://dd.e (truncated) | LCC-2_4_3_1 | Macro Algae | 4 |  |  |
| https://dd.e (truncated) | LCC-2_4_3_2 | Micro Algae (Plankton) | 4 |  |  |
| https://dd.e (truncated) | LCC-3 | Water | 1 | 5 |  |
| https://dd.e (truncated) | LCC-3_1 | Liquid Water Bodies | 2 |  |  |
| https://dd.e (truncated) | LCC-3_1_1 | Inland Water Bodies | 3 |  |  |
| https://dd.e (truncated) | LCC-3_1_1_1 | Water Course | 4 |  |  |
| https://dd.e (truncated) | LCC-3_1_1_2 | Standing Water | 4 |  |  |
| https://dd.e (truncated) | LCC-3_1_2 | Marine Waters | 3 |  |  |
| https://dd.e (truncated) | LCC-3_2 | Solid Waters | 2 |  |  |
| https://dd.e (truncated) | LCC-3_2_1 | Snow | 3 |  |  |
| https://dd.e (truncated) | LCC-3_2_2 | Ice, Glaciers | 3 |  |  |
| https://dd.e (truncated) | LUA | Land Use Attributes | 0 |  |  |
| https://dd.e (truncated) | LUA-1 | Primary Production Sector | 1 |  |  |
| https://dd.e (truncated) | LUA-1_1 | Agriculture | 2 |  |  |
| https://dd.e (truncated) | LUA-1_1_1 | Commercial Crop Production | 3 |  |  |
| https://dd.e (truncated) | LUA-1_1_2 | Farming Infrastructure | 3 |  |  |
| https://dd.e (truncated) | LUA-1_1_2_1 | Animal Husbandry | 4 |  |  |
| https://dd.e (truncated) | LUA-1_1_2_2 | Farming Storage | 4 |  |  |
| https://dd.e (truncated) | LUA-1_1_2_3 | Other Farming Infrastructure | 4 |  |  |
| https://dd.e (truncated) | LUA-1_1_3 | Production for Own Consumption | 3 |  |  |
| https://dd.e (truncated) | LUA-1_2 | Forestry | 2 |  |  |
| https://dd.e (truncated) | LUA-1_3 | Mining and Quarrying | 2 |  |  |
| https://dd.e (truncated) | LUA-1_4 | Aquaculture and Fishing | 2 |  |  |
| https://dd.e (truncated) | LUA-1_4_1 | Aquaculture | 3 |  |  |
| https://dd.e (truncated) | LUA-1\_ |  |  |  |  |

<span id="_Ref100052219" class="anchor"></span>**Figure 2‑3: Coastal
Zones - "Open Sea" land cover components, land use attributes**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image41.png"
style="width:6.26806in;height:4.07292in"
data-fig-alt="This table presents a hierarchical classification system for Land Cover (LCC) and Land Use Attributes (LUA) as used in the Copernicus Land Monitoring Service (CLMS) EAGLE barcoding approach. The table defines specific categories with their Uniform Resource Identifier (URI) prefix, Code, Label, and hierarchical Level. It also contains global metadata settings and specific Barcode values for some entries. Global metadata includes: * Class Code (If continuous dataset, enter &#39;0&#39; as Class Code): 76 * Name: Inland water for mineral extraction * 100% EAGLE Compliant (Possible Values: &#39;Yes&#39; / &#39;No&#39;): Yes * Colour Code (Possible values: only hex colour codes e.g. #87CEFA): #FFFFFF The main body of the table, visible from row 48 to 75, is as follows: | URI | Code | Label | Level | Barcode | Factor | |---|---|---|---|---|---| | https://dd. | LCC-2_4_3 | Algae | 3 | | | | https://dd. | LCC-2_4_3_1 | Macro Algae | 4 | | | | https://dd. | LCC-2_4_3_2 | Micro Algae (Plankton) | 4 | | | | https://dd. | LCC-3 | Water | 1 | | | | https://dd. | LCC-3_1 | Liquid Water Bodies | 2 | 3 | | | https://dd. | LCC-3_1_1 | Inland Water Bodies | 3 | | |" />

This table presents a hierarchical classification system for Land Cover
(LCC) and Land Use Attributes (LUA) as used in the Copernicus Land
Monitoring Service (CLMS) EAGLE barcoding approach. The table defines
specific categories with their Uniform Resource Identifier (URI) prefix,
Code, Label, and hierarchical Level. It also contains global metadata
settings and specific Barcode values for some entries.

Global metadata includes: \* Class Code (If continuous dataset, enter
“0” as Class Code): 76 \* Name: Inland water for mineral extraction \*
100% EAGLE Compliant (Possible Values: “Yes” / “No”): Yes \* Colour Code
(Possible values: only hex colour codes e.g. #87CEFA): \#FFFFFF

The main body of the table, visible from row 48 to 75, is as follows:

| URI         | Code        | Label                  | Level | Barcode | Factor |
|-------------|-------------|------------------------|-------|---------|--------|
| https://dd. | LCC-2_4_3   | Algae                  | 3     |         |        |
| https://dd. | LCC-2_4_3_1 | Macro Algae            | 4     |         |        |
| https://dd. | LCC-2_4_3_2 | Micro Algae (Plankton) | 4     |         |        |
| https://dd. | LCC-3       | Water                  | 1     |         |        |
| https://dd. | LCC-3_1     | Liquid Water Bodies    | 2     | 3       |        |
| https://dd. | LCC-3_1_1   | Inland Water Bodies    | 3     |         |        |

<span id="_Ref100052208" class="anchor"></span>**Figure 2‑4: NL BBG -
"Inland water for mineral extraction"**

4.  **Interpretation might be necessary for differentiation**

- Even if we stated under d. that interpretation should be avoided,
  sometimes the barcoding will need a little “interpretation” to
  differentiate classes or their use.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image42.png"
style="width:6.26806in;height:4.33125in"
data-fig-alt="This table presents a hierarchical classification of Land Use Attributes (LUA), their corresponding codes, descriptive labels, and hierarchical levels, along with associated &#39;barcode&#39; values for two specific land cover Class Codes: 3110 (Natural &amp; semi-natural broadleaved forest) and 3120 (Highly artificial broadleaved plantations). The headers are structured as follows: | URI | Code | Label | Level | Class Code 3110 (Natural &amp; semi-natural broadleaved forest) - Barcode | Class Code 3110 (Natural &amp; semi-natural broadleaved forest) - Factor | Class Code 3120 (Highly artificial broadleaved plantations) - Barcode | Class Code 3120 (Highly artificial broadleaved plantations) - Factor | |---|---|---|---|---|---|---|---| | https://dd.e. | LUA | Land Use Attributes | 0 | | | | | | https://dd.e. | LUA-1 | Primary Production Sector | 1 | | | | | | https://dd.e. | LUA-1_1 | Agriculture | 2 | | | | | | https://dd.e. | LUA-1_1_1 | Commercial Crop Production | 3 | | | | | | https://dd.e. | LUA-1_1_2 | Farming Infrastructure | 3 | | | | |" />

This table presents a hierarchical classification of Land Use Attributes
(LUA), their corresponding codes, descriptive labels, and hierarchical
levels, along with associated “barcode” values for two specific land
cover Class Codes: 3110 (Natural & semi-natural broadleaved forest) and
3120 (Highly artificial broadleaved plantations).

The headers are structured as follows:

| URI | Code | Label | Level | Class Code 3110 (Natural & semi-natural broadleaved forest) - Barcode | Class Code 3110 (Natural & semi-natural broadleaved forest) - Factor | Class Code 3120 (Highly artificial broadleaved plantations) - Barcode | Class Code 3120 (Highly artificial broadleaved plantations) - Factor |
|----|----|----|----|----|----|----|----|
| https://dd.e. | LUA | Land Use Attributes | 0 |  |  |  |  |
| https://dd.e. | LUA-1 | Primary Production Sector | 1 |  |  |  |  |
| https://dd.e. | LUA-1_1 | Agriculture | 2 |  |  |  |  |
| https://dd.e. | LUA-1_1_1 | Commercial Crop Production | 3 |  |  |  |  |
| https://dd.e. | LUA-1_1_2 | Farming Infrastructure | 3 |  |  |  |  |

<span id="_Toc137576632" class="anchor"></span>**Figure 2‑5: Natura
2000 - "(Semi-)Natural Forest" vs "Plantations" land use attribute
mapping**

5.  **Consider Land Cover and Land Use separately**

- Not always both land cover and land use will be useful for
  Extractions. Sometimes we have a very heterogeneous land cover setting
  but clear land use, and vice-versa. Some classes will not offer much
  insight due to a (potential) combination of abiotic, biotic and water
  land cover components. For such classes, the land use section might be
  more useful.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image43.png"
style="width:6.26806in;height:6.98819in"
data-fig-alt="This table presents a hierarchical classification of Land Cover Components (LCC) used in the Copernicus Land Monitoring Service (CLMS) CLC+ system. The table includes 54 rows of entries, organised into three main categories: Abiotic / Non-Vegetated Surfaces and Objects (LCC-1), Biotic / Vegetation (LCC-2), and Water (LCC-3). Each entry has a Uniform Resource Identifier (URI), a hierarchical Code, a descriptive Land Cover Component name, and a numeric Level indicating its position in the hierarchy. Some entries also have a &#39;Barcode&#39; value. The metadata for the classification system is provided in cells C4:AJ5: * &#39;Class Code* (If continuous dataset, enter &#39;0&#39; as Class Code)&#39; * &#39;Name*&#39; * &#39;100% EAGLE Compliant* (Possible Values: &#39;Yes&#39; / &#39;No&#39;)&#39;: &#39;Yes&#39; * &#39;Colour Code (Possible values: only hex colour codes e.g. #87CEFA)&#39;: &#39;#000000&#39; * Cell AI4: &#39;41&#39; * Cell AJ4: &#39;Sports area&#39; | URI | Code | Land Cover Components | Level | Barcode | Factor | |---|---|---|---|---|---| | https://dd. | LCC | Land Cover Components | 0 | | | | https://dd. | LCC-1 | Abiotic / Non-Vegetated Surfaces and Objects | 1 | | | | https://dd. | LCC-1_1 | Artificial Surfaces and Constructions | 2 | | | | https://dd. | LCC-1_1_1 | Sealed Artificial Surfaces and Constructions | 3 | 1 | | | https://dd. | LCC-1_1_1_1 | Buildings | 4 | | | | https://dd. | LCC-1_1_1_1_1 | Conventional Buildings | 5 | | | | https://dd. | LCC-1_1_1_1_2 | Specific Buildings | 5 | | | | https://dd. | LCC-1_1_1_2 | Specific Structures and Facilities | 4 | | | | https://dd. | LCC-1_1_1_3 | Open Sealed Surfaces | 4 | | | | https://dd. | LCC-1_1_2 | Non-Sealed Artificial Surfaces | 3 | | | | https://dd. | LCC-1_1_2_1 | Open Non-Sealed Artificial Surfaces | 4 | 1 | | | https://dd. | LCC-1_1_2_2 | Waste Materials | 4 | | | | https://dd. | LCC-1_2 | Natural Material Surfaces | 2 | | | | https://dd. | LCC-1_2_1 | Consolidated Surfaces | 3 | | | | https://dd. | LCC-1_2_1_1 | Bare Rock | 4 | | | | https://dd. | LCC-1_2_1_2 | Hard Pan | 4 | | | | https://dd. | LCC-1_2_2 | Unconsolidated Surfaces | 3 | | | | https://dd. | LCC-1_2_2_1 | Mineral Fragments | 4 | | | | https://dd. | LCC-1_2_2_1_1 | Boulders, Stones | 5 | | | | https://dd. | LCC-1_2_2_1_2 | Pebbles, Gravel, Tuff | 5 | | | | https://dd. | LCC-1_2_2_1_3 | Sand, Grit | 5 | 1 | | | https://dd. | LCC-1_2_2_1_4 | Clay, Silt | 5 | | | | https://dd. | LCC-1_2_2_1_5 | Mixed Unsorted Material | 5 | | | | https://dd. | LCC-1_2_2_2 | Bare Soils | 4 | 1 | | | https://dd. | LCC-1_2_2_3 | Natural Deposits | 4 | | | | https://dd. | LCC-1_2_2_3_1 | Inorganic Deposits | 5 | | | | https://dd. | LCC-1_2_2_3_2 | Organic Deposits (Peat) | 5 | | | | https://dd. | LCC-2 | Biotic / Vegetation | 1 | 3 | | | https://dd. | LCC-2_1 | Woody Vegetation | 2 | | | | https://dd. | LCC-2_1_1 | Trees | 3 | | | | https://dd. | LCC-2_1_2 | Bushes, Shrubs | 3 | | | | https://dd. | LCC-2_1_2_1 | Regular Bushes | 4 | | | | https://dd. | LCC-2_1_2_2 | Dwarf Shrubs | 4 | | | | https://dd. | LCC-2_2 | Herbaceous Vegetation (Grass-Like, Forbs, Ferns) | 2 | | | | https://dd. | LCC-2_2_1 | Graminoids (Grass-Like) | 3 | | | | https://dd. | LCC-2_2_1_1 | Grasses, Sedges, Rushes, Cereals | 4 | | | | https://dd. | LCC-2_2_1_2 | Reeds, Bamboos, Canes | 4 | | | | https://dd. | LCC-2_2_2 | Non-Graminoids (Forbs, Ferns) | 3 | | | | https://dd. | LCC-2_3 | Succulents, Cacti | 2 | | | | https://dd. | LCC-2_4 | Lichens, Mosses, Algae | 2 | | | | https://dd. | LCC-2_4_1 | Lichens | 3 | | | | https://dd. | LCC-2_4_2 | Mosses | 3 | | | | https://dd. | LCC-2_4_3 | Algae | 3 | | | | https://dd. | LCC-2_4_3_1 | Macro Algae | 4 | | | | https://dd. | LCC-2_4_3_2 | Micro Algae (Plankton) | 4 | | | | https://dd. | LCC-3 | Water | 1 | | | | https://dd. | LCC-3_1 | Liquid Water Bodies | 2 | | | | https://dd. | LCC-3_1_1 | Inland Water Bodies | 3 | 1 | | | https://dd. | LCC-3_1_1_1 | Water Course | 4 | | | | https://dd. | LCC-3_1_1_2 | Standing Water | 4 | | | | https://dd. | LCC-3_1_2 | Marine Waters | 3 | | | | https://dd. | LCC-3_2 | Solid Waters | 2 | | | | https://dd. | LCC-3_2_1 | Snow | 3 | | | | https://dd. | LCC-3_2_2 | Ice, Glaciers | 3 | 1 | | This table details the hierarchical breakdown of land cover classes, providing specific codes and descriptions for various natural and artificial surfaces, vegetation types, and water bodies. The &#39;Barcode&#39; column appears to assign specific numeric identifiers to certain aggregated or distinct land cover elements within the classification." />

This table presents a hierarchical classification of Land Cover
Components (LCC) used in the Copernicus Land Monitoring Service (CLMS)
CLC+ system. The table includes 54 rows of entries, organised into three
main categories: Abiotic / Non-Vegetated Surfaces and Objects (LCC-1),
Biotic / Vegetation (LCC-2), and Water (LCC-3). Each entry has a Uniform
Resource Identifier (URI), a hierarchical Code, a descriptive Land Cover
Component name, and a numeric Level indicating its position in the
hierarchy. Some entries also have a “Barcode” value.

The metadata for the classification system is provided in cells C4:AJ5:
\* “Class Code\* (If continuous dataset, enter”0” as Class Code)” \*
“Name*”* ”100% EAGLE Compliant\* (Possible Values: “Yes” / “No”)“:”Yes”
\* “Colour Code (Possible values: only hex colour codes e.g. #87CEFA)”:
“\#000000” \* Cell AI4: “41” \* Cell AJ4: “Sports area”

| URI | Code | Land Cover Components | Level | Barcode | Factor |
|----|----|----|----|----|----|
| https://dd. | LCC | Land Cover Components | 0 |  |  |
| https://dd. | LCC-1 | Abiotic / Non-Vegetated Surfaces and Objects | 1 |  |  |
| https://dd. | LCC-1_1 | Artificial Surfaces and Constructions | 2 |  |  |
| https://dd. | LCC-1_1_1 | Sealed Artificial Surfaces and Constructions | 3 | 1 |  |
| https://dd. | LCC-1_1_1_1 | Buildings | 4 |  |  |
| https://dd. | LCC-1_1_1_1_1 | Conventional Buildings | 5 |  |  |
| https://dd. | LCC-1_1_1_1_2 | Specific Buildings | 5 |  |  |
| https://dd. | LCC-1_1_1_2 | Specific Structures and Facilities | 4 |  |  |
| https://dd. | LCC-1_1_1_3 | Open Sealed Surfaces | 4 |  |  |
| https://dd. | LCC-1_1_2 | Non-Sealed Artificial Surfaces | 3 |  |  |
| https://dd. | LCC-1_1_2_1 | Open Non-Sealed Artificial Surfaces | 4 | 1 |  |
| https://dd. | LCC-1_1_2_2 | Waste Materials | 4 |  |  |
| https://dd. | LCC-1_2 | Natural Material Surfaces | 2 |  |  |
| https://dd. | LCC-1_2_1 | Consolidated Surfaces | 3 |  |  |
| https://dd. | LCC-1_2_1_1 | Bare Rock | 4 |  |  |
| https://dd. | LCC-1_2_1_2 | Hard Pan | 4 |  |  |
| https://dd. | LCC-1_2_2 | Unconsolidated Surfaces | 3 |  |  |
| https://dd. | LCC-1_2_2_1 | Mineral Fragments | 4 |  |  |
| https://dd. | LCC-1_2_2_1_1 | Boulders, Stones | 5 |  |  |
| https://dd. | LCC-1_2_2_1_2 | Pebbles, Gravel, Tuff | 5 |  |  |
| https://dd. | LCC-1_2_2_1_3 | Sand, Grit | 5 | 1 |  |
| https://dd. | LCC-1_2_2_1_4 | Clay, Silt | 5 |  |  |
| https://dd. | LCC-1_2_2_1_5 | Mixed Unsorted Material | 5 |  |  |
| https://dd. | LCC-1_2_2_2 | Bare Soils | 4 | 1 |  |
| https://dd. | LCC-1_2_2_3 | Natural Deposits | 4 |  |  |
| https://dd. | LCC-1_2_2_3_1 | Inorganic Deposits | 5 |  |  |
| https://dd. | LCC-1_2_2_3_2 | Organic Deposits (Peat) | 5 |  |  |
| https://dd. | LCC-2 | Biotic / Vegetation | 1 | 3 |  |
| https://dd. | LCC-2_1 | Woody Vegetation | 2 |  |  |
| https://dd. | LCC-2_1_1 | Trees | 3 |  |  |
| https://dd. | LCC-2_1_2 | Bushes, Shrubs | 3 |  |  |
| https://dd. | LCC-2_1_2_1 | Regular Bushes | 4 |  |  |
| https://dd. | LCC-2_1_2_2 | Dwarf Shrubs | 4 |  |  |
| https://dd. | LCC-2_2 | Herbaceous Vegetation (Grass-Like, Forbs, Ferns) | 2 |  |  |
| https://dd. | LCC-2_2_1 | Graminoids (Grass-Like) | 3 |  |  |
| https://dd. | LCC-2_2_1_1 | Grasses, Sedges, Rushes, Cereals | 4 |  |  |
| https://dd. | LCC-2_2_1_2 | Reeds, Bamboos, Canes | 4 |  |  |
| https://dd. | LCC-2_2_2 | Non-Graminoids (Forbs, Ferns) | 3 |  |  |
| https://dd. | LCC-2_3 | Succulents, Cacti | 2 |  |  |
| https://dd. | LCC-2_4 | Lichens, Mosses, Algae | 2 |  |  |
| https://dd. | LCC-2_4_1 | Lichens | 3 |  |  |
| https://dd. | LCC-2_4_2 | Mosses | 3 |  |  |
| https://dd. | LCC-2_4_3 | Algae | 3 |  |  |
| https://dd. | LCC-2_4_3_1 | Macro Algae | 4 |  |  |
| https://dd. | LCC-2_4_3_2 | Micro Algae (Plankton) | 4 |  |  |
| https://dd. | LCC-3 | Water | 1 |  |  |
| https://dd. | LCC-3_1 | Liquid Water Bodies | 2 |  |  |
| https://dd. | LCC-3_1_1 | Inland Water Bodies | 3 | 1 |  |
| https://dd. | LCC-3_1_1_1 | Water Course | 4 |  |  |
| https://dd. | LCC-3_1_1_2 | Standing Water | 4 |  |  |
| https://dd. | LCC-3_1_2 | Marine Waters | 3 |  |  |
| https://dd. | LCC-3_2 | Solid Waters | 2 |  |  |
| https://dd. | LCC-3_2_1 | Snow | 3 |  |  |
| https://dd. | LCC-3_2_2 | Ice, Glaciers | 3 | 1 |  |

This table details the hierarchical breakdown of land cover classes,
providing specific codes and descriptions for various natural and
artificial surfaces, vegetation types, and water bodies. The “Barcode”
column appears to assign specific numeric identifiers to certain
aggregated or distinct land cover elements within the classification.

<span id="_Toc137576633" class="anchor"></span>**Figure 2‑6: NL BBG -
"Sports Area" which includes land cover component ice rinks**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image44.png"
style="width:6.26806in;height:3.71389in"
data-fig-alt="This table presents a hierarchical classification of Land Use Attributes (LUA) with corresponding codes, labels, and levels, alongside mapping information such as &#39;Class Code&#39; and &#39;Name&#39;. The overall classification is identified as &#39;Sports area&#39; with a Class Code of 41, designated as &#39;100% EAGLE Compliant&#39; (Yes) and having a Colour Code of #000000. The table content is as follows: | URI | Code | Label | Level | Barcode | Factor | | :----------- | :------------- | :------------------------------------------ | :---- | :------ | :----- | | https://dd. | LUA-3_3_4_2 | Monastery | 4 | | | | https://dd. | LUA-3_3_4_3 | Cemetery | 4 | | | | https://dd. | LUA-3_3_5 | Other Community Services | 3 | | | | https://dd. | LUA-3_4 | Cultural, Entertainment and Recreational Services | 2 | | | | https://dd. | LUA-3_4_1 | Cultural Services | 3 | | | | https://dd. | LUA-3_4_1_1 | Indoor Cultural Service | 4 | | | | https://dd. | LUA-3_4_1_2 | Outdoor Cultural Service | 4 | | | | https://dd. | LUA-3_4_2 | Entertainment | 3 | | | | https://dd. | LUA-3_4_3 | Sports Infrastructure | 3 | 5 | | | https://dd. | LUA-3_4_3_1 | Golf Course | 4 | | | | https://dd. | LUA-3_4_3_2 | Ski Piste | 4 | | | | https://dd. | LUA-3_4_3_3 | Outdoor Racecourse | 4 | | | | https://dd. | LUA-3_4_3_4 | Sport Hall | 4 | | | | https://dd. | LUA-3_4_3_5 | Stadium | 4 | | | | https://dd. | LUA-3_4_3_6 | Swimming Pool | 4 | | | | https://dd. | LUA-3_4_3_7 | Sports Ground | 4 | | | | https://dd. | LUA-3_4_3_8 | Indoor Sport-/Fitness Facility | 4 | | | | https://dd. | LUA-3_4_3_9 | Yacht harbour, Sport Boat Marina | 4 | | | | https://dd. | LUA-3_4_4 | Open Air Recreational Areas | 3 | | | | https://dd. | LUA-3_4_4_1 | Urban Greenery and City Parks | 4 | | | | https://dd. | LUA-3_4_4_2 | (Semi-)Natural Areas Used for Recreation | 4 | | | | https://dd. | LUA-3_4_5 | Other Recreational Services | 3 | | | | https://dd. | LUA-3_4_5_1 | Allotment Garden | 4 | | | | https://dd. | LUA-3_4_5_2 | Amateur Fishing | 4 | | | | https://dd. | LUA-3_5 | Other Services | 2 | | | | https://dd. | LUA-4 | Transport Networks, Logistics, Utilities | 1 | | | The table details Land Use Attributes (LUA) from Level 1 to 4, covering categories such as &#39;Other Community Services&#39;, &#39;Cultural, Entertainment and Recreational Services&#39;, and &#39;Transport Networks, Logistics, Utilities&#39;. Notably, &#39;Sports Infrastructure&#39; (LUA-3_4_3) is assigned a &#39;Barcode&#39; value of &#39;5&#39;, with its sub-categories including specific facilities like &#39;Golf Course&#39;, &#39;Ski Piste&#39;, &#39;Stadium&#39;, and &#39;Swimming Pool&#39;, all at Level 4. The `URI` entries are partially visible as &#39;https://dd.&#39;." />

This table presents a hierarchical classification of Land Use Attributes
(LUA) with corresponding codes, labels, and levels, alongside mapping
information such as “Class Code” and “Name”. The overall classification
is identified as “Sports area” with a Class Code of 41, designated as
“100% EAGLE Compliant” (Yes) and having a Colour Code of \#000000.

The table content is as follows:

| URI | Code | Label | Level | Barcode | Factor |
|:---|:---|:---|:---|:---|:---|
| https://dd. | LUA-3_3_4_2 | Monastery | 4 |  |  |
| https://dd. | LUA-3_3_4_3 | Cemetery | 4 |  |  |
| https://dd. | LUA-3_3_5 | Other Community Services | 3 |  |  |
| https://dd. | LUA-3_4 | Cultural, Entertainment and Recreational Services | 2 |  |  |
| https://dd. | LUA-3_4_1 | Cultural Services | 3 |  |  |
| https://dd. | LUA-3_4_1_1 | Indoor Cultural Service | 4 |  |  |
| https://dd. | LUA-3_4_1_2 | Outdoor Cultural Service | 4 |  |  |
| https://dd. | LUA-3_4_2 | Entertainment | 3 |  |  |
| https://dd. | LUA-3_4_3 | Sports Infrastructure | 3 | 5 |  |
| https://dd. | LUA-3_4_3_1 | Golf Course | 4 |  |  |
| https://dd. | LUA-3_4_3_2 | Ski Piste | 4 |  |  |
| https://dd. | LUA-3_4_3_3 | Outdoor Racecourse | 4 |  |  |
| https://dd. | LUA-3_4_3_4 | Sport Hall | 4 |  |  |
| https://dd. | LUA-3_4_3_5 | Stadium | 4 |  |  |
| https://dd. | LUA-3_4_3_6 | Swimming Pool | 4 |  |  |
| https://dd. | LUA-3_4_3_7 | Sports Ground | 4 |  |  |
| https://dd. | LUA-3_4_3_8 | Indoor Sport-/Fitness Facility | 4 |  |  |
| https://dd. | LUA-3_4_3_9 | Yacht harbour, Sport Boat Marina | 4 |  |  |
| https://dd. | LUA-3_4_4 | Open Air Recreational Areas | 3 |  |  |
| https://dd. | LUA-3_4_4_1 | Urban Greenery and City Parks | 4 |  |  |
| https://dd. | LUA-3_4_4_2 | (Semi-)Natural Areas Used for Recreation | 4 |  |  |
| https://dd. | LUA-3_4_5 | Other Recreational Services | 3 |  |  |
| https://dd. | LUA-3_4_5_1 | Allotment Garden | 4 |  |  |
| https://dd. | LUA-3_4_5_2 | Amateur Fishing | 4 |  |  |
| https://dd. | LUA-3_5 | Other Services | 2 |  |  |
| https://dd. | LUA-4 | Transport Networks, Logistics, Utilities | 1 |  |  |

The table details Land Use Attributes (LUA) from Level 1 to 4, covering
categories such as “Other Community Services”, “Cultural, Entertainment
and Recreational Services”, and “Transport Networks, Logistics,
Utilities”. Notably, “Sports Infrastructure” (LUA-3_4_3) is assigned a
“Barcode” value of ‘5’, with its sub-categories including specific
facilities like “Golf Course”, “Ski Piste”, “Stadium”, and “Swimming
Pool”, all at Level 4. The `URI` entries are partially visible as
“https://dd.”.

<span id="_Toc137576634" class="anchor"></span>**Figure 2‑7: NL BBG -
"Sports Area" has a clear land use barcoding**

For a better understanding of the data and to describe the parent
classes content wise in more detail, the Level 1 classes are
differentiated into subtypes of these LULUCF parent classes. The Level 2
and 3 classes are no official classes, and each country may define the
classes in the way that best suits the country’s specific
characteristics. This concrete subdivision is based on the examples
mentioned in the official class definitions or auxiliary subdivision
done by the EAGLE group and adapted by the CLC+ Core consortium \[AD11\]
(Table 0‑3 see Annex). It is recommended to involve specific experts to
support the subclass definitions to best meet the reporting
requirements.

Further, the consortium recommends assigning the EAGLE elements to the
respective (sub)classes. In a first round, select all the required EAGLE
elements that should describe the subclass as best as possible. In Table
0‑3 (see Annex), an example is shown of the category “Grassland” with
its subclasses and the identified EGLE elements relevant for Extraction.
The procedure has to be done for all the remaining categories as well.
In a second round check the availability of the EAGLE element in the
input classes together with the barcoding value. This second round is
very important to ensure that the rule will have an output. If the rule
is not true, the outcome will be empty. I.e. forest class “clear cuts”
can be described best with the following EAGLE elements: LCC
“bushes/shrubs and herbaceous vegetation”, LUA “forestry” and LCH “clear
cut” besides other elements. In this case the LCH attribute is not
barcoded in any of the CLC input classes although it would be very well
describing this subclass. Due to this fact it cannot be used in the rule
or if used, the output would be empty.

## [EAGLE Ontology](https://land.copernicus.eu/eagle/work-results-documentation-and-tools) overview

After you have clicked on “**EAGLE Ontology**”, you will see the EAGLE
Ontology overview (see [Figure 2‑9](#_Ref151986517)), which shows you a
list of the EAGLE Ontology (EAGLE barcoding file) versions within CLC+
Core. You can see detailed information about the version, creation date
(created on), creator (created by) and description of the respective
EAGLE version.

Users with the role “EAGLE maintenance” have the possibility to add a
new version to the system. This is described in more detail at section
63. In separate Annex for Admin Users. Once a new EAGLE ontology version
is published all users get a notification (see section
[1.7.3](#notifications-messages)).

Users are also able to **download the EAGLE barcoding template using
this button. Additionally, the EAGLE templates and other tools can be
accessed
[here](https://land.copernicus.eu/en/eagle?tab=document_archive)**. You
can use this template to map/translate your dataset and upload your data
together with the EAGLE barcoding. This is the recommended way
performing the EAGLE barcoding – alternatively, the data can be mapped
while editing the Ingestion.

**Note: In general, you need to barcode all classes. There is a
possibility to re-structure / aggregate your classes to a less detailed
level** **in an external GIS <u>BEFORE</u> uploading them to the system.
This is recommended if your national dataset is very detailed which does
not provide more value to the Extraction but to reduce the amount of
input classes and the effort of the EAGLE barcoding.** In [Figure
2‑8](#_Ref99878072) below, the original 337 classes (GEWASCODE) from the
Dutch LPIS dataset were reduced /aggregated to 16 classes (LGN). To do
this:

- Add a new column (enter name and select datatype integer)

- Select all polygons with value i.e. 372 (select by attributes)

- Open the filed calculator and add value 1 for all selected entries

- Repeat until all values have a new class code assigned

- **Now, that you have everything reclassified, you can start the EAGLE
  barcoding**

> <img
> src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image45.png"
> style="width:3.62068in;height:3.24961in"
> data-fig-alt="The table lists 25 distinct crop types with their corresponding `GEWASCODE` (Crop Code), `GEWASOMSCHRIJVING` (Crop Description), and `LGN` (Local Group Number). The `LGN` column groups these crops into five categories: | GEWASCODE | GEWASOMSCHRIJVING | LGN | |---|---|---| | 372 | Rand, grenzend aan bouwland, hoofdzakelijk be[unreadable] | 1 | | 3807 | Rietzwenkgras, anders dan voor industriegras | 1 | | 3805 | Rietzwenkgras, industriegras | 1 | | 3523 | Veldbeemdgras | 1 | | 3513 | Westerwolds raaigras | 1 | | 317 | Maïs, corncob mix | 2 | | 2032 | Maïs, energie- | 2 | | 316 | Maïs, korrel- | 2 | | 259 | Maïs, snij- | 2 | | 814 | Maïs, suiker- | 2 | | 2025 | Aardappelen, bestrijdingsmaatregel AM | 3 | | 2014 | Aardappelen, consumptie | 3 | | 2015 | Aardappelen, poot NAK | 3 | | 2016 | Aardappelen, poot TBM | 3 | | 2017 | Aardappelen, zetmeel | 3 | | 1949 | Aardperen | 4 | | 256 | Bieten, suiker- | 4 | | 257 | Bieten, voeder- | 4 | | 235 | Gerst, winter- | 5 | | 236 | Gerst, zomer- | 5 | | 2652 | Granen, overig | 5 | | 238 | Haver | 5 | | 670 | Japanse haver | 5 | | 237 | Rogge (geen snijrogge) | 5 | The `LGN` categorisation includes: - Group 1: Field margins and various types of fescue, bluegrass, and ryegrass. - Group 2: Different types of maize (corncob mix, energy, grain, silage, sweet). - Group 3: Potatoes for specific uses (pest control &#39;AM&#39;, consumption, certified seed &#39;NAK&#39;, seed &#39;TBM&#39;, starch). - Group 4: Unspecified potatoes (&#39;Aardperen&#39;) and both sugar and fodder beets. - Group 5: Cereals, including winter barley, summer barley, other cereals, oats, Japanese oats, and rye (excluding silage rye). This table provides a detailed local land use/land cover classification, consistent with the Copernicus Land Monitoring Service (CLMS) CLC+ Core User Manual&#39;s recommendation for Member States to define specific subtypes of LULUCF parent classes." />
> <img
> src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image46.png"
> style="width:2.41612in;height:3.22149in"
> data-fig-alt="This table presents a classification scheme mapping numerical Land Cover Generic Numbers (LGN) to specific land cover and land use categories, likely used within the Copernicus Land Monitoring Service (CLMS) CLC+ Core or EAGLE frameworks for land cover/land use mapping. | LGN | Category Description | |---|---| | 0 | &#39;Shrubs, paths, ...&#39; | | 1 | Pasture | | 2 | Maize | | 3 | Potatoes | | 4 | Sugar beet | | 5 | Cereals | | 6 | Other crops | | 9 | Orchards | | 10 | Flower bulbs | | 11 | Deciduous Trees | | 16 | Fresh Water | | 42 | Reeds | | 45 | Natural Grassland | | 61 | Tree nurseries | | 62 | Fruit cultivation | | 77 | &#39;other landscape element&#39; | The table provides a set of identifiers and their corresponding land cover/land use definitions, ranging from agricultural types like Pasture, Maize, and Cereals, to natural features such as Deciduous Trees, Fresh Water, and Natural Grassland." />

<span id="_Ref99878072" class="anchor"></span>**Figure 2‑8: The original
337 classes (GEWASCODE) from the Dutch LPIS dataset were reduced
/aggregated to 16 classes (LGN).**

You are also able to have a look at the details of each EAGLE Ontology
version by clicking on “open” within the context menu of each EAGLE
Ontology version from the table. The detail page is described in section
[2.4](#view-details-of-eagle-ontology).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image51.png"
style="width:6.925in;height:1.74514in"
data-fig-alt="This image displays a user interface for managing versions of the EAGLE Ontology, a classification system for land cover and land use. The central part of the interface presents a table with columns for &#39;Version&#39;, &#39;Created At&#39;, &#39;Created By&#39;, and &#39;Description&#39;. The table contains one visible entry: | Version | Created At | Created By | Description | | :------ | :--------- | :-------------------------- | :---------- | | 3.1.2 | 25.05.2022 | CLC+ Core User Admin/Support | [unreadable] | An &#39;Open&#39; button is associated with the listed version 3.1.2, allowing access to its details. Above the table, two action buttons are visible: &#39;DOWNLOAD EAGLE BARCODING TEMPLATE&#39; and &#39;ADD NEW VERSION&#39;. The navigation bar at the top includes links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. This interface allows users to manage and access different iterations of the EAGLE Ontology, which is fundamental for land cover/land use (LCLU) classification within the Copernicus Land Monitoring Service (CLMS) and CLC+ (next-generation CORINE Land Cover) initiatives, particularly regarding the use of EAGLE elements and barcoding templates." />

This image displays a user interface for managing versions of the EAGLE
Ontology, a classification system for land cover and land use. The
central part of the interface presents a table with columns for
“Version”, “Created At”, “Created By”, and “Description”.

The table contains one visible entry: \| Version \| Created At \|
Created By \| Description \| \| :—— \| :——— \| :————————– \| :———- \| \|
3.1.2 \| 25.05.2022 \| CLC+ Core User Admin/Support \| \[unreadable\] \|

An “Open” button is associated with the listed version 3.1.2, allowing
access to its details. Above the table, two action buttons are visible:
“DOWNLOAD EAGLE BARCODING TEMPLATE” and “ADD NEW VERSION”. The
navigation bar at the top includes links to “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”. This interface
allows users to manage and access different iterations of the EAGLE
Ontology, which is fundamental for land cover/land use (LCLU)
classification within the Copernicus Land Monitoring Service (CLMS) and
CLC+ (next-generation CORINE Land Cover) initiatives, particularly
regarding the use of EAGLE elements and barcoding templates.

<span id="_Ref151986517" class="anchor"></span>**Figure 2‑9: EAGLE
Ontology overview**

## View details of EAGLE Ontology

After clicking on “Open” for the specific EAGLE Ontology version (see
section 7.1) you will find yourself within the EAGLE Ontology detail
view (see [Figure 2‑10](#_Ref151986549)).

Within the detail view you can find the details and structure of the
specific EAGLE Ontology version and its elements. By
collapsing/expanding the sections you can dig deeper into the structure
of the ontology.

Via the search field you can easily find specific EAGLE elements.

Additionally, you can open the details of each EAGLE element by a
right-click and select “show details” or alternatively, by using the
action “show details” within the context menu of the EAGLE element.

After you clicked on “show details” a dialog will pop up to show you all
relevant information for the specific EAGLE element (see [Figure
2‑11](#_Ref151986570)). You can see in which version (Version), when
(created at) and by whom (created by) it was created, since (since
version) and until (to version) which version it was active in the
ontology, when (changed at) and by whom it has been changed (changed by)
and a description.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image53.png"
style="width:6.925in;height:3.81806in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) web interface for the EAGLE Ontology, displaying Version 3.1.2. The interface presents a hierarchical classification system for environmental data, specifically for Land Cover Components (LCC) and Land Use Attributes (LUA). The &#39;Land Cover Components (LCC)&#39; section is partially expanded and structured as follows: - &#39;Abiotic / Non-Vegetated Surfaces and Objects (LCC-1)&#39; - &#39;Artificial Surfaces and Constructions (LCC-1_1)&#39; - &#39;Sealed Artificial Surfaces and Constructions (LCC-1_1_1)&#39; - &#39;Buildings (LCC-1_1_1_1)&#39; - &#39;Conventional Buildings (LCC-1_1_1_1_1)&#39; - &#39;Specific Buildings (LCC-1_1_1_1_2)&#39; - &#39;Specific Structures and Facilities (LCC-1_1_1_1_2)&#39;. A &#39;Show Details&#39; button is visible to the right of this entry. - &#39;Open Sealed Surfaces (LCC-1_1_1_3)&#39; - &#39;Non-Sealed Artificial Surfaces (LCC-1_1_2)&#39; - &#39;Natural Material Surfaces (LCC-1_2)&#39; - &#39;Biotic / Vegetation (LCC-2)&#39; (collapsed) - &#39;Water (LCC-3)&#39; (collapsed) The &#39;Land Use Attributes (LUA)&#39; section is collapsed, showing its top-level entries: - &#39;Primary Production Sector (LUA-1)&#39; - &#39;Secondary Production Sector (LUA-2)&#39; - &#39;Tertiary Services Sector (LUA-3)&#39; A search bar with placeholder text &#39;Search&#39; is located at the top of the classification list. The top navigation bar of the interface features &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and &#39;CLC+ Core User Admin/Support&#39;. A blue question mark icon, representing a help button, is visible in the bottom right corner." />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) web interface for the EAGLE Ontology, displaying Version 3.1.2.
The interface presents a hierarchical classification system for
environmental data, specifically for Land Cover Components (LCC) and
Land Use Attributes (LUA).

The “Land Cover Components (LCC)” section is partially expanded and
structured as follows: - “Abiotic / Non-Vegetated Surfaces and Objects
(LCC-1)” - “Artificial Surfaces and Constructions (LCC-1_1)” - “Sealed
Artificial Surfaces and Constructions (LCC-1_1_1)” - “Buildings
(LCC-1_1_1_1)” - “Conventional Buildings (LCC-1_1_1_1_1)” - “Specific
Buildings (LCC-1_1_1_1_2)” - “Specific Structures and Facilities
(LCC-1_1_1_1_2)”. A “Show Details” button is visible to the right of
this entry. - “Open Sealed Surfaces (LCC-1_1_1_3)” - “Non-Sealed
Artificial Surfaces (LCC-1_1_2)” - “Natural Material Surfaces
(LCC-1_2)” - “Biotic / Vegetation (LCC-2)” (collapsed) - “Water (LCC-3)”
(collapsed)

The “Land Use Attributes (LUA)” section is collapsed, showing its
top-level entries: - “Primary Production Sector (LUA-1)” - “Secondary
Production Sector (LUA-2)” - “Tertiary Services Sector (LUA-3)”

A search bar with placeholder text “Search” is located at the top of the
classification list. The top navigation bar of the interface features
“Data Catalogue”, “EAGLE Ontology”, “About EAGLE”, “Organisations”,
“Users”, and “CLC+ Core User Admin/Support”. A blue question mark icon,
representing a help button, is visible in the bottom right corner.

<span id="_Ref151986549" class="anchor"></span>**Figure 2‑10: View
details of EAGLE Ontology**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image54.png"
style="width:6.925in;height:3.81736in"
data-fig-alt="A screenshot of the EAGLE Ontology web interface (Version 3.1.2) displaying a pop-up window with detailed information for the &#39;Specific Buildings (LCC-1_1_1_1_2)&#39; element. The interface&#39;s top bar shows navigation links: &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, with &#39;CLC+ Core User Admin/Support&#39; noted. The left panel presents a hierarchical view of the EAGLE Ontology elements, currently expanded to show: * Land Cover Components (LCC) * Abiotic / Non-Vegetated Surfaces and Objects (LCC-1) * Artificial Surfaces and Constructions (LCC-1_1) * Sealed Artificial Surfaces and Constructions (LCC-1_1_1) * Buildings (LCC-1_1_1_1) * Conventional Buildings (LCC-1_1_1_1) * Specific Buildings (LCC-1_1_1_1_2) * Specific Structures and Facilities (LCC-1_1_1_2) * Open Sealed Surfaces (LCC-1_1_1_3) * Non-Sealed Artificial Surfaces (LCC-1_1_2) * Natural Material Surfaces (LCC-1_2) * Biotic / Vegetation (LCC-2) * Water (LCC-3) * Land Use Attributes (LUA) * Primary Production Sector (LUA-1) * Secondary Production Sector (LUA-2) * Tertiary Services Sector (LUA-3) The central pop-up window, titled &#39;Details: Specific Buildings (LCC-1_1_1_1_2)&#39;, provides comprehensive metadata: * A direct URL: `https://dd.eionet.europa.eu/vocabulary/landcover/eagle/LCC-specific-buildings` * Created at: 25.05.2022 * Created by: CLC+ Core User Admin/Support * Since Version: 3.1.2 * To Version: 3.1.2 * Changed at: 25.05.2022 * Changed by: CLC+ Core User Admin/Support * is Header: false * is Parameter: false * Data Element: - * Unit: - * Definition: &#39;The specific (significant) buildings are the buildings of significant size or height with specific physical aspect that make them usable as landmarks and required by use cases such as mapping or travel safety (INSPIRE TWG BU data specifications). Includes: e.g. stadiums, churches, towers, greenhouses (Permanent or temporal installation for crop plantation purposes, mainly with light material like either glass or plastic folia).&#39; A &#39;CLOSE&#39; button is present at the bottom right of the pop-up." />

A screenshot of the EAGLE Ontology web interface (Version 3.1.2)
displaying a pop-up window with detailed information for the “Specific
Buildings (LCC-1_1_1_1_2)” element. The interface’s top bar shows
navigation links: “Data Catalogue”, “EAGLE Ontology”, “About EAGLE”,
“Organisations”, and “Users”, with “CLC+ Core User Admin/Support” noted.

The left panel presents a hierarchical view of the EAGLE Ontology
elements, currently expanded to show: \* Land Cover Components (LCC) \*
Abiotic / Non-Vegetated Surfaces and Objects (LCC-1) \* Artificial
Surfaces and Constructions (LCC-1_1) \* Sealed Artificial Surfaces and
Constructions (LCC-1_1_1) \* Buildings (LCC-1_1_1_1) \* Conventional
Buildings (LCC-1_1_1_1) \* Specific Buildings (LCC-1_1_1_1_2) \*
Specific Structures and Facilities (LCC-1_1_1_2) \* Open Sealed Surfaces
(LCC-1_1_1_3) \* Non-Sealed Artificial Surfaces (LCC-1_1_2) \* Natural
Material Surfaces (LCC-1_2) \* Biotic / Vegetation (LCC-2) \* Water
(LCC-3) \* Land Use Attributes (LUA) \* Primary Production Sector
(LUA-1) \* Secondary Production Sector (LUA-2) \* Tertiary Services
Sector (LUA-3)

The central pop-up window, titled “Details: Specific Buildings
(LCC-1_1_1_1_2)”, provides comprehensive metadata: \* A direct URL:
`https://dd.eionet.europa.eu/vocabulary/landcover/eagle/LCC-specific-buildings`
\* Created at: 25.05.2022 \* Created by: CLC+ Core User Admin/Support \*
Since Version: 3.1.2 \* To Version: 3.1.2 \* Changed at: 25.05.2022 \*
Changed by: CLC+ Core User Admin/Support \* is Header: false \* is
Parameter: false \* Data Element: - \* Unit: - \* Definition: “The
specific (significant) buildings are the buildings of significant size
or height with specific physical aspect that make them usable as
landmarks and required by use cases such as mapping or travel safety
(INSPIRE TWG BU data specifications). Includes: e.g. stadiums, churches,
towers, greenhouses (Permanent or temporal installation for crop
plantation purposes, mainly with light material like either glass or
plastic folia).” A “CLOSE” button is present at the bottom right of the
pop-up.

<span id="_Ref151986570" class="anchor"></span>**Figure 2‑11: View
details of EAGLE element**

In addition, the EAGLE mapping barcoding file of a published Ingestion
can be downloaded on the detail view page of the Ingestion. Either at
the bottom left of the page under “Additional Documents” by clicking on
the file or by using the “Download EAGLE Barcoding” button below the map
view (see [Figure 2-12](#_Ref152831592)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image55.png"
style="width:6.925in;height:3.81875in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) data catalogue interface, detailing the ingestion status and metadata for a &#39;CLC+Backbone (2018)&#39; dataset. The interface is divided into a left sidebar with general information and a main right panel displaying a geographic map of Europe and a table of input classes. The left sidebar, titled &#39;General Information&#39;, provides the following details: - Name: CLC+Backbone (2018) - Country: European Environment Agency (38+UK) - Region: - - Reference Year: 2018 - Time Range of Ingested Data: 01.07.2017 - 30.06.2019 - INSPIRE Themes: LC Land cover (referencing Directive 2007/2/EC, Infrastructure for Spatial Information in the European Community) - Created By: CLC+ Core User Admin/Support - Organisation/s: CLC (CORINE Land Cover), European Environment Agency (EEA) - Visibility: Public - All Organisations - Contact Person: copernicus@eea.europa.eu At the top of the main panel, actions like &#39;REPUBLISH ON GEOSERVER&#39; and &#39;ARCHIVE&#39; are available. Below the &#39;Ingestion &#39;CLC+Backbone (2018)&#39; USED&#39; title, an &#39;APPROVE EAGLE COMPLIANCE&#39; button is displayed next to the &#39;EIONET Action Group EAGLE Land Monitoring in Europe&#39; logo. The main right panel features a map of Europe with country borders and major city labels (e.g., London, Paris, Berlin, Rome, Warsaw, Kyiv, Moscow, Oslo). The map background is a natural-colour satellite mosaic. A scale bar indicates 300 km and 300 mi. Attribution is &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. Search fields for &#39;Country&#39; and &#39;Region&#39; are positioned above the map. Below the map, an &#39;Input Classes&#39; section lists dataset categories. A &#39;DOWNLOAD EAGLE BARCODING&#39; button is present. The table displays &#39;Class Code&#39;, &#39;Name&#39;, &#39;EAGLE Elements&#39;, &#39;100% EAGLE compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39; columns. Two visible rows are: - Class Code 1: Name &#39;Sealed (buildings and flat sealed ...&#39;, EAGLE Elements &#39;Sealed Artificial Surfaces and Con... +4&#39;. It is 100% EAGLE compliant (checked), assigned a red colour, and not shown in the map (toggle off). - Class Code 2: Name &#39;Woody - needle leaved trees&#39;, EAGLE Elements &#39;Trees +1&#39;. It is 100% EAGLE compliant (checked), assigned a green colour, and not shown in the map (toggle off)." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image56.png"
style="width:6.925in;height:1.07361in"
data-fig-alt="This image is a screenshot of a user interface displaying an &#39;Additional Documents&#39; section. Under the &#39;Uploaded Document/s&#39; heading, two clickable links are visible: &#39;CLMS_CLCplus_RASTER_2018_010m_03005_V1_0.xml&#39; and &#39;EAGLEBarcodingTemplate-CLCBackbone2018-7066330542AA7E9E1C6E...&#39; (the end of the second filename is truncated). Below these document links, several organisational logos are present from left to right: the European Union flag with &#39;Copernicus Europe&#39;s eyes on Earth&#39; text, the &#39;EIONET Action Group EAGLE Land Monitoring in Europe&#39; logo, the European Commission logo, and the &#39;European Environment Agency&#39; (EEA) logo. A blue circular icon with a white question mark, likely a help or feedback button, is visible on the far right, partially obscured by a scrollbar. The filenames contain references to &#39;CLCplus&#39;, &#39;RASTER&#39;, &#39;2018&#39;, and &#39;EAGLE&#39;." />

<span id="_Ref152831592" class="anchor"></span>**Figure 2-12: Options
for downloading the EAGLE barcoding file of a published Ingestion.**

## EAGLE approval stamp for Ingestions

The EAGLE barcoding of an Ingestion can be approved for being EAGLE
compliant by any user with the additional role of being an “EAGLE
Maintainer/Approver”. This approval process can only be initiated by
users with this role and is for now only planned for the CLMS products.
If you are an Admin User, please refer to section 6.4 in separate Annex.

The Ingestions gets then a quality stamp/icon in the Data Catalogue
(first column ‘EAGLE approved’). By hovering over it with the mouse an
explanation appears in the grey box: “The EAGLE mapping was reviewed and
approved by the EAGLE Group”. Further when opening the Ingestion itself
the approval appears next to the status (see [Figure
2‑13](#_Ref151645180)). Moreover, when selecting Input classes for an
Extraction (see section [4.4](#add-input-classes-to-extraction)) there
is also the possibility in the ‘add input class’ view to filter by ‘show
only EAGLE approved Input classes’. The EAGLE approval for an Ingestion
can also be revoked again by the EAGLE Maintainer. Each approval change
is saved and displayed in the history of an Ingestion.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image57.png"
style="width:6.925in;height:1.46736in"
data-fig-alt="This image shows a screenshot of the Copernicus Land Monitoring Service (CLMS) Data Catalogue user interface, presenting a table of data ingestion records. The top navigation bar includes options for &#39;Data Catalogue&#39; (currently selected), &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, with the user &#39;Renner Thomas&#39; identified. Below the main title &#39;Data Catalogue&#39;, functional buttons are displayed: &#39;Filter&#39;, &#39;My organisation/s&#39;, &#39;My data&#39;, &#39;Ingestions&#39; (highlighted as currently active), and &#39;Extractions&#39;. A search field labelled &#39;Search&#39; is present, alongside &#39;ADD INGESTION&#39; and &#39;ADD EXTRACTION&#39; buttons. The main content area is a table structured with the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. The table contains three data records: 1. **Row 1:** The dataset &#39;UA_IBK_2018&#39; (Urban Atlas Innsbruck 2018) is listed. It is &#39;EAGLE Approved&#39;, indicated by a checkmark icon with a tooltip stating &#39;The EAGLE mapping was reviewed and approved by the EAGLE Group&#39;. It was created on 21.11.2023 by &#39;CLC+ Core User Admin.&#39;, covers &#39;Austria/Österreich&#39; in the &#39;Innsbruck&#39; region, with a &#39;Reference Year&#39; of 2018 and a &#39;Time Range&#39; of 01.01.2018 - 31.12.2018. The &#39;Organisation/s&#39; is &#39;CLC, European En...&#39; (likely European Environment Agency), the &#39;Contact Person&#39; is &#39;copernicus@eea.europa.eu&#39;, its &#39;Status&#39; is &#39;PUBLISHED&#39;, and the &#39;INSPIRE Themes&#39; are &#39;Land use, Land cover&#39;. 2. **Row 2:** The dataset &#39;CLC+ Backbone (2018)&#39; is listed. It is not &#39;EAGLE Approved&#39;. It was created on 05.09.2023 by &#39;CLC+ Core User Admin.&#39;, covers &#39;European Environ...&#39; (likely European Environment Agency) with no specific region, with a &#39;Reference Year&#39; of 2018 and a &#39;Time Range&#39; of 01.07.2017 - 30.06.2019. The &#39;Organisation/s&#39; is &#39;CLC, European En...&#39;, the &#39;Contact Person&#39; is &#39;copernicus@eea.europa.eu&#39;, its &#39;Status&#39; is &#39;USED&#39;, and the &#39;INSPIRE Themes&#39; are &#39;Land cover&#39;. 3. **Row 3:** The dataset &#39;Coastal Zones (CZ) 2018&#39; is listed. It is not &#39;EAGLE Approved&#39;. It was created on 21.06.2023 by &#39;CLC+ Core User Admin.&#39;, covers &#39;European Environ...&#39; for both &#39;Country&#39; and &#39;Region&#39;, with a &#39;Reference Year&#39; of 2018 and a &#39;Time Range&#39; of 01.01.2017 - 31.12.2019. The &#39;Organisation/s&#39;" />

This image shows a screenshot of the Copernicus Land Monitoring Service
(CLMS) Data Catalogue user interface, presenting a table of data
ingestion records.

The top navigation bar includes options for “Data Catalogue” (currently
selected), “EAGLE Ontology”, “About EAGLE”, “Organisations”, and
“Users”, with the user “Renner Thomas” identified. Below the main title
“Data Catalogue”, functional buttons are displayed: “Filter”, “My
organisation/s”, “My data”, “Ingestions” (highlighted as currently
active), and “Extractions”. A search field labelled “Search” is present,
alongside “ADD INGESTION” and “ADD EXTRACTION” buttons.

The main content area is a table structured with the following columns:
“EAGLE Approved”, “Name”, “Type”, “Created At”, “Created By”, “Country”,
“Region”, “Reference Year”, “Time Range”, “Organisation/s”, “Contact
Person”, “Status”, and “INSPIRE Themes”.

The table contains three data records: 1. **Row 1:** The dataset
“UA_IBK_2018” (Urban Atlas Innsbruck 2018) is listed. It is “EAGLE
Approved”, indicated by a checkmark icon with a tooltip stating “The
EAGLE mapping was reviewed and approved by the EAGLE Group”. It was
created on 21.11.2023 by “CLC+ Core User Admin.”, covers
“Austria/Österreich” in the “Innsbruck” region, with a “Reference Year”
of 2018 and a “Time Range” of 01.01.2018 - 31.12.2018. The
“Organisation/s” is “CLC, European En…” (likely European Environment
Agency), the “Contact Person” is “copernicus@eea.europa.eu”, its
“Status” is “PUBLISHED”, and the “INSPIRE Themes” are “Land use, Land
cover”. 2. **Row 2:** The dataset “CLC+ Backbone (2018)” is listed. It
is not “EAGLE Approved”. It was created on 05.09.2023 by “CLC+ Core User
Admin.”, covers “European Environ…” (likely European Environment Agency)
with no specific region, with a “Reference Year” of 2018 and a “Time
Range” of 01.07.2017 - 30.06.2019. The “Organisation/s” is “CLC,
European En…”, the “Contact Person” is “copernicus@eea.europa.eu”, its
“Status” is “USED”, and the “INSPIRE Themes” are “Land cover”. 3. **Row
3:** The dataset “Coastal Zones (CZ) 2018” is listed. It is not “EAGLE
Approved”. It was created on 21.06.2023 by “CLC+ Core User Admin.”,
covers “European Environ…” for both “Country” and “Region”, with a
“Reference Year” of 2018 and a “Time Range” of 01.01.2017 - 31.12.2019.
The “Organisation/s”

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image58.png"
style="width:6.925in;height:3.22222in"
data-fig-alt="This image is a screenshot of a web interface displaying the &#39;detail view&#39; for an &#39;Ingestion &#39;UA_IBK_2018&#39;&#39; within a data catalogue, likely part of the Copernicus Land Monitoring Service (CLMS) or European Environment Agency (EEA) platform. The page shows general metadata, a geographic map preview, and a table of input classes. The top navigation bar includes &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and indicates the user &#39;Lindmayer Amelie&#39;. The breadcrumb path is &#39;Data Catalogue / Ingestion &#39;UA_IBK_2018&#39;&#39;. The ingestion status is &#39;PUBLISHED&#39; and &#39;Approved by EAGLE&#39;. The left panel, &#39;General Information&#39;, provides: * Name: &#39;UA_IBK_2018&#39; * Country: &#39;Austria/Österreich&#39; * Region: &#39;Innsbruck&#39; * Reference Year: &#39;2018&#39; * Time Range of Ingested Data: &#39;01.01.2018 – 31.12.2018&#39; * INSPIRE Themes: &#39;LU Land use&#39; and &#39;LC Land cover&#39; (referencing Directive 2007/2/EC, the INSPIRE Directive) * Created By: &#39;CLC+ Core User Admin/Support&#39; * Organisation/s: &#39;CLC&#39; (CORINE Land Cover), &#39;European Environment Agency&#39; (EEA) * Visibility: &#39;Public - All Organisations&#39; The central part of the page features an interactive map centered on Innsbruck, Austria. The map shows satellite imagery of mountainous terrain with cities and towns labelled, including Innsbruck, Telfs, Wattens, Schwaz, Imst, Landeck, Sölden, Sterzing, Ehrwald, Garmisch-Partenkirchen, Mittenwald, Oberstdorf, Reutte, and Bad Hindelang. A light green overlay highlights the geographic extent of the data ingestion around the Innsbruck region. The map includes a scale bar showing &#39;10 km&#39; and &#39;5 mi&#39;, and attribution to &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. A search bar above the map filters by &#39;Country * AT Austria/Österreich&#39; and &#39;Region * AT332 Innsbruck&#39;. Below the map, the &#39;Input Classes&#39; section lists data layers. A download button for &#39;EAGLE BARCODING&#39; is prominent. The visible table row shows: * Class Code: &#39;11100&#39; * Name: &#39;11100&#39; * EAGLE Elements: &#39;Sealed Artificial Surfaces and Constructions +10&#39; * 100% EAGLE compliant: checkbox (checked) * Colour: A dark red swatch * Show in Map: toggle switch (off) The light green area visible on the map corresponds to an additional, partially visible, input class with its &#39;Show in Map&#39; toggle enabled." />

This image is a screenshot of a web interface displaying the “detail
view” for an “Ingestion ‘UA_IBK_2018’” within a data catalogue, likely
part of the Copernicus Land Monitoring Service (CLMS) or European
Environment Agency (EEA) platform. The page shows general metadata, a
geographic map preview, and a table of input classes.

The top navigation bar includes “Data Catalogue”, “EAGLE Ontology”,
“About EAGLE”, “Organisations”, “Users”, and indicates the user
“Lindmayer Amelie”. The breadcrumb path is “Data Catalogue / Ingestion
‘UA_IBK_2018’”. The ingestion status is “PUBLISHED” and “Approved by
EAGLE”.

The left panel, “General Information”, provides: \* Name: “UA_IBK_2018”
\* Country: “Austria/Österreich” \* Region: “Innsbruck” \* Reference
Year: “2018” \* Time Range of Ingested Data: “01.01.2018 – 31.12.2018”
\* INSPIRE Themes: “LU Land use” and “LC Land cover” (referencing
Directive 2007/2/EC, the INSPIRE Directive) \* Created By: “CLC+ Core
User Admin/Support” \* Organisation/s: “CLC” (CORINE Land Cover),
“European Environment Agency” (EEA) \* Visibility: “Public - All
Organisations”

The central part of the page features an interactive map centered on
Innsbruck, Austria. The map shows satellite imagery of mountainous
terrain with cities and towns labelled, including Innsbruck, Telfs,
Wattens, Schwaz, Imst, Landeck, Sölden, Sterzing, Ehrwald,
Garmisch-Partenkirchen, Mittenwald, Oberstdorf, Reutte, and Bad
Hindelang. A light green overlay highlights the geographic extent of the
data ingestion around the Innsbruck region. The map includes a scale bar
showing “10 km” and “5 mi”, and attribution to “Leaflet \| © Core003
Mosaic, © OpenStreetMap contributors”. A search bar above the map
filters by “Country \* AT Austria/Österreich” and “Region \* AT332
Innsbruck”.

Below the map, the “Input Classes” section lists data layers. A download
button for “EAGLE BARCODING” is prominent. The visible table row shows:
\* Class Code: “11100” \* Name: “11100” \* EAGLE Elements: “Sealed
Artificial Surfaces and Constructions +10” \* 100% EAGLE compliant:
checkbox (checked) \* Colour: A dark red swatch \* Show in Map: toggle
switch (off) The light green area visible on the map corresponds to an
additional, partially visible, input class with its “Show in Map” toggle
enabled.

<span id="_Ref151645180" class="anchor"></span>**Figure 2‑13: EAGLE
Approval stamp in the Data Catalogue (upper image) and Ingestion view
(lower image).**

## Lessons learned for the EAGLE barcoding approach

In the meanwhile, the consortium gained valuable experience about the
EAGLE barcoding approach in regard to ingesting and extracting datasets
into and from the CLC+ Core System. As the EAGLE barcoding approach is
not trivial, the following lessons learned can be summarized by the
consortium:

- The EAGLE model must be studied in depth along with the
  dataset/nomenclature to be barcoded, which must be divided into its
  fractions. Due to the number of EAGLE elements and possibilities for
  the barcode value, the process of barcoding must be done thoughtfully.
  After an initial version is produced, it may need to be revised and
  discussed several times until it leads to a 'final' version.

- Understanding the nomenclatures are crucial. If the nomenclatures do
  not contain detailed descriptions of the respective classes, barcoding
  is all the more difficult. Often the class definitions leave much room
  for interpretation or even contradict each other. The point is to
  clearly express what characterises the individual class and not to try
  to describe everything that exists or that one could think of as well
  as possible.

- In most hierarchical nomenclatures, level 1 classes are already
  described, which are then further stratified and specified by the next
  level, which can make barcoding difficult.

- Expert knowledge of the datasets is therefore extremely valuable for
  meaningful barcoding. Nevertheless, the determination of the barcode
  value will be subjective depending on the responsible performing the
  barcoding.

- Since Extractions are highly dependent on both the selected input
  classes and the barcoding, a comprehensive knowledge of them is
  essential.

- In general, the more heterogeneous the classes are, the more difficult
  and elaborative the barcoding will become.

- In the best case, you already have a concept in mind of what you want
  to extract, but this is not obligatory. In the case, the barcoding has
  to be reworked and adapted if no optimal results can be achieved.

- The required LCC, LUA and LCH attributes are primarily determined by
  the requirements of the instance classes.

- Changes in the EAGLE barcoding template are covered with the CLC+
  System. The system is always updated to the latest version of the
  template. Older versions are stored in the system and Ingestions and
  Extractions based on the older versions remain valid. Only if the
  EAGLE barcoding is performed on an older version, it will not be
  possible to upload this older template but rather needs to be
  updated/transferred to the latest version.

# Ingestions

As mentioned in the introduction, users are able to add already existing
datasets to the CLC+ Core, such as products of the Copernicus CLMS
portfolio as well as national datasets by performing an **Ingestion**.
Ingestion means to upload datasets to the system and make it available
and usable for all users, a selected user group or only for the
organization of the ingesting user. [Figure 3‑1](#_Ref100264360)
provides a simplified overview of the Ingestion process.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image59.png"
style="width:5.90972in;height:5.97254in"
data-fig-alt="This diagram illustrates the data ingestion and lifecycle workflow within the CLC+ Core System, divided into three main phases: Upload data, Edit Ingestion, and Non-editable Ingestion. 1. **Upload data (orange area):** * The process starts by &#39;Add[ing] Ingestion&#39; which involves uploading a raster or vector dataset. * This is followed by parallel or sequential steps: &#39;Add Parameters and dataset&#39; and &#39;Add metadata, EAGLE barcoding, ...&#39;. * A decision point &#39;Upload successful?&#39; determines the next step. * IF &#39;No&#39;, THEN an &#39;Error Message&#39; is displayed. After the error, the user faces a &#39;Retry or Delete?&#39; decision. IF &#39;Retry&#39;, the process returns to &#39;Add Ingestion&#39;. IF &#39;Delete&#39;, the process leads to the &#39;Deleted&#39; state. * IF &#39;Yes&#39;, THEN the data proceeds to the &#39;Edit Ingestion&#39; phase, entering &#39;Status Draft (dataset ingested)&#39;. 2. **Edit Ingestion (purple area):** * From &#39;Status Draft (dataset ingested)&#39;, the user can &#39;Edit metadata&#39;, &#39;Add EAGLE barcoding file (if not done at upload)&#39;, and &#39;Add country and region for preview and click start preview&#39;. * Clicking &#39;Start Ingestion&#39; changes the status to &#39;Status Ingested_Preview&#39;. * The next status is &#39;Status Ingested&#39;. * Clicking &#39;Publish&#39; transitions the status to &#39;Status Published (Input for Extractions)&#39;, which is highlighted in red. * From &#39;Status Published (Input for Extractions)&#39;, the user can &#39;Perform Extraction using Input Classes from this Ingestion&#39;. * An action &#39;Click Unpublish&#39; can revert &#39;Status Published (Input for Extractions)&#39; back to &#39;Status Draft (dataset ingested)&#39;. * Both &#39;Status Ingested&#39; and &#39;Status Published (Input for Extractions)&#39; can lead to the &#39;Deleted&#39; state via a &#39;Delete&#39; action. 3. **Non-editable Ingestion (green area):** * From &#39;Status Published (Input for Extractions)&#39;, the status can transition to &#39;Status Used&#39;. This transition occurs &#39;Only if Extraction, where input classes are used, changes from status Extracted to a lower status&#39;. * From &#39;Status Used&#39;, clicking &#39;Archive&#39; changes the status to &#39;Status Archived&#39;. * There is a bi-directional arrow between &#39;Status Used&#39; and &#39;Status Archived&#39;, suggesting the possibility to move between these two states." />

This diagram illustrates the data ingestion and lifecycle workflow
within the CLC+ Core System, divided into three main phases: Upload
data, Edit Ingestion, and Non-editable Ingestion.

1.  **Upload data (orange area):**
    - The process starts by “Add\[ing\] Ingestion” which involves
      uploading a raster or vector dataset.
    - This is followed by parallel or sequential steps: “Add Parameters
      and dataset” and “Add metadata, EAGLE barcoding, …”.
    - A decision point “Upload successful?” determines the next step.
      - IF “No”, THEN an “Error Message” is displayed. After the error,
        the user faces a “Retry or Delete?” decision. IF “Retry”, the
        process returns to “Add Ingestion”. IF “Delete”, the process
        leads to the “Deleted” state.
      - IF “Yes”, THEN the data proceeds to the “Edit Ingestion” phase,
        entering “Status Draft (dataset ingested)”.
2.  **Edit Ingestion (purple area):**
    - From “Status Draft (dataset ingested)”, the user can “Edit
      metadata”, “Add EAGLE barcoding file (if not done at upload)”, and
      “Add country and region for preview and click start preview”.
    - Clicking “Start Ingestion” changes the status to “Status
      Ingested_Preview”.
    - The next status is “Status Ingested”.
    - Clicking “Publish” transitions the status to “Status Published
      (Input for Extractions)”, which is highlighted in red.
    - From “Status Published (Input for Extractions)”, the user can
      “Perform Extraction using Input Classes from this Ingestion”.
    - An action “Click Unpublish” can revert “Status Published (Input
      for Extractions)” back to “Status Draft (dataset ingested)”.
    - Both “Status Ingested” and “Status Published (Input for
      Extractions)” can lead to the “Deleted” state via a “Delete”
      action.
3.  **Non-editable Ingestion (green area):**
    - From “Status Published (Input for Extractions)”, the status can
      transition to “Status Used”. This transition occurs “Only if
      Extraction, where input classes are used, changes from status
      Extracted to a lower status”.
    - From “Status Used”, clicking “Archive” changes the status to
      “Status Archived”.
    - There is a bi-directional arrow between “Status Used” and “Status
      Archived”, suggesting the possibility to move between these two
      states.

<span id="_Ref100264360" class="anchor"></span>**Figure 3‑1: Simplified
Ingestion workflow**

Dataset to be uploaded can be common **raster and vector file formats**:

- Shapefile (shp as zip)

- Geopackage (gpkg)

- File geodatabases (gdb)

- Hierarchical Data Format (HDF5)

- GeoTiff (tif/tiff)

Several additional documents can accompany the dataset, such as a
metadata file, a legend / style file (section [3.2.1](#raster-dataset)
and [3.2.2](#vector-dataset)) and the EAGLE barcoding files (section
2.3). By adding them at Ingestion creation, the information is extracted
automatically, otherwise the user need to add this information manually
at a later stage. An Ingestion has been successfully processed, once it
is in the status draft.

An Ingestion comprises the following steps, which are described in more
detail in this section below:

1)  Upload the data (either by attaching a local dataset directly within
    the "Upload Dataset" field or by providing a dataset download URL)
    and configure its settings (section [3.2](#add-ingestion))

2)  Map the Input Classes to the respective EAGLE[^6] barcoding using
    the EAGLE barcoding template (section 2.3). Alternatively, the
    mapping can be performed in the system itself (section
    [3.7](#edit-ingestion))

3)  Edit, preview, start Ingestion and publish the Ingestion

**Please consider that the Ingestion will be resampled**[^7] **and
aggregated to 100 x 100 m. This reduced spatial resolution needs to be
taken into account while setting up the Extraction rules (section
[4.5.1](#some-definitions-for-a-better-understanding-also-see-glossary)).**

## Generic workflow

The key steps required in the development of an Ingestion and Extraction
are (see [Figure 3‑2](#_Ref151987137)):

1.  Knowledge of Reporting or Extraction requirements

2.  Development of an Extraction concept

3.  Identification and selection of relevant and required datasets

4.  Performing an EAGLE barcoding suitable for the Extractions

5.  Ingest dataset into the CLC+ Core System

6.  (Optional) Adaption of EAGLE barcoding and re-ingestion

7.  Publish Ingestion

8.  Selection of Input Classes

9.  Definition of Output Classes including Extraction rulesets

10. Perform an Extraction

11. Publish Extraction

<table style="width:26%;">
<colgroup>
<col style="width: 26%" />
</colgroup>
<tbody>
<tr>
<td><blockquote>
<p><strong>Ingestion</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Ref151987137" class="anchor"></span>**Figure 3‑2: Generic
workflow for the creation of an Ingestion and Extraction.**

## Add Ingestion

### Raster dataset

Clicking the ‘**Add Ingestion**’ button (section [1.6](#data-catalogue)
[Figure 1‑9](#_Ref151467380)) opens the ‘Add Ingestion’ dialog (see
[Figure 3‑3](#_Ref151987176)) where you can define the data format of
your dataset (step 1).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image61.png"
style="width:6.925in;height:3.85278in"
data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core System Data Catalogue web interface, displaying a list of land monitoring datasets and an overlaying &#39;Add Ingestion&#39; dialog box. The main Data Catalogue table shows the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. Visible dataset entries include: - `CLC+Backbone (2018)`: Created At 05.09.2023, Created By CLC+ Core User Admin, Organisation/s European Environment Agency (EEA), Copernicus, Reference Year 2018, Time Range 01.07.2017 - 30.06.2019, Status USED, INSPIRE Themes Land cover. - `Coastal Zones (CZ) 2018`: Created At 21.06.2023, Created By CLC+ Core User Admin, Organisation/s European Environment Agency (EEA), Copernicus, Reference Year 2018, Time Range 01.01.2017 - 31.12.2019, Status USED, INSPIRE Themes Land use, Land cover. - `Corine Land Cover (CLC)`: Created At 06.09.2023, Status PUBLISHED, INSPIRE Themes Land cover. - `HRL - Grassland 2018`: Created At 10.03.2023, Status PUBLISHED, INSPIRE Themes Land cover. Other listed datasets include Corine Land Cover (CLC), Effis 2018, Eurocrop 2018, HRL - Dominant Leaf Type, HRL - Forest Type (FTY), and another HRL - Grassland 2018 entry. The pagination control shows &#39;Items per page: 10&#39; and &#39;1 - 10 of 32&#39; entries. The overlaid &#39;Add Ingestion&#39; dialog represents Step 1, titled &#39;Input Type Selection&#39;. The option &#39;Upload Dataset - Raster&#39; is currently selected. The alternative option is &#39;Upload Dataset - Vector&#39;. The dialog also indicates a subsequent Step 2 as &#39;&#39;Dataset Selection Upload Dataset - Raster&#39;&#39;. The user can click &#39;CANCEL&#39; or &#39;NEXT&#39; to proceed. The page header contains navigation links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and indicates the logged-in user as &#39;Renner Thomas&#39;. Logos at the bottom of the page include Copernicus, EIONET Action Group EAGLE, the European Union flag, European Commission, and the European Environment Agency (EEA) logo." />

This is a screenshot of the Copernicus Land Monitoring Service (CLMS)
CLC+ Core System Data Catalogue web interface, displaying a list of land
monitoring datasets and an overlaying “Add Ingestion” dialog box.

The main Data Catalogue table shows the following columns: “EAGLE
Approved”, “Name”, “Type”, “Created At”, “Created By”, “Country”,
“Region”, “Reference Year”, “Time Range”, “Organisation/s”, “Contact
Person”, “Status”, and “INSPIRE Themes”. Visible dataset entries
include: - `CLC+Backbone (2018)`: Created At 05.09.2023, Created By CLC+
Core User Admin, Organisation/s European Environment Agency (EEA),
Copernicus, Reference Year 2018, Time Range 01.07.2017 - 30.06.2019,
Status USED, INSPIRE Themes Land cover. - `Coastal Zones (CZ) 2018`:
Created At 21.06.2023, Created By CLC+ Core User Admin, Organisation/s
European Environment Agency (EEA), Copernicus, Reference Year 2018, Time
Range 01.01.2017 - 31.12.2019, Status USED, INSPIRE Themes Land use,
Land cover. - `Corine Land Cover (CLC)`: Created At 06.09.2023, Status
PUBLISHED, INSPIRE Themes Land cover. - `HRL - Grassland 2018`: Created
At 10.03.2023, Status PUBLISHED, INSPIRE Themes Land cover. Other listed
datasets include Corine Land Cover (CLC), Effis 2018, Eurocrop 2018,
HRL - Dominant Leaf Type, HRL - Forest Type (FTY), and another HRL -
Grassland 2018 entry. The pagination control shows “Items per page: 10”
and “1 - 10 of 32” entries.

The overlaid “Add Ingestion” dialog represents Step 1, titled “Input
Type Selection”. The option “Upload Dataset - Raster” is currently
selected. The alternative option is “Upload Dataset - Vector”. The
dialog also indicates a subsequent Step 2 as “‘Dataset Selection Upload
Dataset - Raster’”. The user can click “CANCEL” or “NEXT” to proceed.
The page header contains navigation links to “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, “Users”, and indicates the
logged-in user as “Renner Thomas”. Logos at the bottom of the page
include Copernicus, EIONET Action Group EAGLE, the European Union flag,
European Commission, and the European Environment Agency (EEA) logo.

<span id="_Ref151987176" class="anchor"></span>**Figure 3‑3: Add
Ingestion - Step 1 (Data format) - here raster file**

In a second step, further information, such as name and country / region
that describe the data can be entered (step 2 see [Figure
3‑4](#_Ref151987203)). All **mandatory fields** are marked with a \*. In
this example, we will upload the HRL Imperviousness (IMD) for Albania.
Since we want to ingest the whole country, we do not specify a region.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image62.png"
style="width:4.93674in;height:3.16937in"
data-fig-alt="A screenshot of the &#39;Add Ingestion&#39; user interface dialog, illustrating the second step of a two-step process for uploading a raster dataset. The progress indicator shows Step 1 as &#39;Input Type Selection&#39; (greyed out) and Step 2 as active, labelled &#39;&#39;Dataset Selection Upload Dataset - Raster&#39;&#39;. The dialog contains three input fields: &#39;Name *&#39; which is pre-filled with &#39;IMD_2018_Albania&#39;, &#39;Country *&#39; pre-filled with &#39;AL Albania/Shqipëria&#39;, and &#39;Region&#39; which is an empty, greyed-out field. Below these fields, two tabs are visible: &#39;File Upload&#39; which is selected and underlined in green, and &#39;URL Upload&#39;. A vertical scrollbar is visible on the right side of the dialog." />

A screenshot of the “Add Ingestion” user interface dialog, illustrating
the second step of a two-step process for uploading a raster dataset.
The progress indicator shows Step 1 as “Input Type Selection” (greyed
out) and Step 2 as active, labelled “‘Dataset Selection Upload Dataset -
Raster’”. The dialog contains three input fields: “Name *” which is
pre-filled with ”IMD_2018_Albania”, ”Country* ” pre-filled with “AL
Albania/Shqipëria”, and “Region” which is an empty, greyed-out field.
Below these fields, two tabs are visible: “File Upload” which is
selected and underlined in green, and “URL Upload”. A vertical scrollbar
is visible on the right side of the dialog.

<span id="_Ref151987203" class="anchor"></span>**Figure 3‑4: Add
Ingestion - Step 2 (Parameter)**

The data can be uploaded directly from a computer (file upload or per
\`drag and drop\`) or by entering an URL where the data shall be
collected from (step 3 see [Figure 3‑5](#_Ref151987252)). Please also
refer to section 3.3 Remarks on the Ingestion process. The supported
file formats for raster files are:

- Hierarchical Data Format (HDF5)

- GeoTiff (tif/tiff)

In this example below, we chose the file upload from a local computer.
By doing this, an attachment is added to the dialog. **In case the file
size is larger than 5 GB, a warning appears recommending using an URL
upload as the file upload might take a long time.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image64.png"
style="width:4.33858in;height:4.51969in"
data-fig-alt="This screenshot displays the &#39;Add Ingestion&#39; user interface dialog, specifically for &#39;Step 2: &#39;Dataset Selection Upload Dataset - Raster&#39;&#39;, following &#39;Step 1: Input Type Selection&#39;. The active method is &#39;File Upload&#39;, with &#39;URL Upload&#39; as an alternative. Users can upload data by dragging and dropping files into a designated area or by clicking the &#39;UPLOAD DATASET/S&#39; button. The accepted file formats are .tif, .TIF, .tiff, .Tiff, .zip, .h5, and .gpkg. Ten individual raster files are listed as already selected for upload, each named with the pattern &#39;IMD_2018_010m_E[XX]N[YY]_03035_v020.tif&#39;, indicating 2018 High Resolution Layer (HRL) Imperviousness Density (IMD) data at 10 m resolution. Below the file list, two unselected radio button options are presented: &#39;Discrete values&#39; and &#39;Continuous values&#39;." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image63.png"
style="width:3.51887in;height:2.16462in"
data-fig-alt="A screenshot of a file selection dialog within a software interface, titled &#39;IMD_2018_010m_al_03035_v020 &gt; DATA&#39;. This dialog facilitates the ingestion of raster datasets. The main panel lists multiple TIFF files, all following a naming convention prefixed &#39;IMD_2018_010m_&#39;, indicating High Resolution Layer (HRL) Imperviousness Density (IMD) data from the year 2018 with a 10-meter resolution. Examples of visible filenames include &#39;IMD_2018_010m_E50N21_03035_v020.tif&#39;, &#39;IMD_2018_010m_E52N19_03035_v020.tif&#39;, and &#39;IMD_2018_010m_E51N20_03035_v020.tif&#39;. The &#39;Dateiname&#39; (Filename) input field displays &#39;IMD_2018_010m_E52N21_03035_v020.tif&#39; as the selected file, and the file type filter is set to &#39;Benutzerdefinierte Dateien (*.tif)&#39; (User-defined Files (*.tif)). The interface includes navigation buttons, a &#39;Neuer Ordner&#39; (New Folder) button, a &#39;DATA durchsuchen&#39; (Search DATA) bar, and action buttons &#39;Öffnen&#39; (Open) and &#39;Abbrechen&#39; (Cancel). This screenshot demonstrates the process of selecting HRL Imperviousness (IMD) data, such as for Albania, for ingestion into the CLC+ Core system." />

<span id="_Ref151987252" class="anchor"></span>**Figure 3‑5: Add
Ingestion - Step 3 (Data upload via local computer)**

In another example below (see [Figure 3‑7](#_Ref151987383)), we chose
the URL upload from the [CLMS
portal](https://land.copernicus.eu/en/dataset-catalog). Select the
required files on the download page (put them in the shopping cart) (see
[Figure 3‑8](#_Ref151987407)). After sending the order, you will
retrieve a download link via the CLMS portal (depending on the
processing time) and per email. Note that these download links expire
after a while.

**Note: please use a direct download URL (a link that automatically
starts the download immediately). Consider that the system can only
process links which do not require a user login.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image65.png"
style="width:5.29167in;height:5.9375in"
data-fig-alt="This screenshot displays the &#39;Add Ingestion&#39; dialog, specifically focusing on the third step of the data ingestion process within the Copernicus Land Monitoring Service (CLMS) interface, after &#39;Input Type Selection&#39; (Step 1, greyed out) and &#39;Dataset Selection Upload Dataset - Raster&#39; (Step 2, highlighted green). The current view focuses on data upload via URL. The &#39;URL Upload&#39; tab is selected, as opposed to &#39;File Upload.&#39; A URL is entered in the &#39;Enter URL *&#39; field: `https://copernicus-fme.eea.europa.eu/clmsdatadownload/results/18447.zip`. A green checkmark indicates the URL is valid. The &#39;Continuous values&#39; radio button is selected, indicating the nature of the raster data, with &#39;Discrete values&#39; as the alternative option. Below this, an &#39;Excluded Value&#39; input field is present, accompanied by a description: &#39;Exclude all values which do not represent thematic values in the input dataset. Pixels with one of the given values will be counted as NoData in the ingestion. If a TIF dataset specifies a NoData value in its metadata the corresponding value is excluded automatically.&#39; A &#39;Layer Name&#39; input field is also visible, with placeholder text &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; The interface also provides an area for &#39;Drag and Drop&#39; or clicking an &#39;UPLOAD DOCUMENT/S&#39; button for supporting documents like legend files or metadata, which can prefill the data description. Blue numbered circles indicate the &#39;3&#39; for the URL upload and value type selection, signifying this is step 3 of the process." />

This screenshot displays the “Add Ingestion” dialog, specifically
focusing on the third step of the data ingestion process within the
Copernicus Land Monitoring Service (CLMS) interface, after “Input Type
Selection” (Step 1, greyed out) and “Dataset Selection Upload Dataset -
Raster” (Step 2, highlighted green). The current view focuses on data
upload via URL. The “URL Upload” tab is selected, as opposed to “File
Upload.” A URL is entered in the “Enter URL \*” field:
`https://copernicus-fme.eea.europa.eu/clmsdatadownload/results/18447.zip`.
A green checkmark indicates the URL is valid. The “Continuous values”
radio button is selected, indicating the nature of the raster data, with
“Discrete values” as the alternative option.

Below this, an “Excluded Value” input field is present, accompanied by a
description: “Exclude all values which do not represent thematic values
in the input dataset. Pixels with one of the given values will be
counted as NoData in the ingestion. If a TIF dataset specifies a NoData
value in its metadata the corresponding value is excluded
automatically.” A “Layer Name” input field is also visible, with
placeholder text “Enter Layer Name from Dataset which shall be used to
generate Input Classes.” The interface also provides an area for “Drag
and Drop” or clicking an “UPLOAD DOCUMENT/S” button for supporting
documents like legend files or metadata, which can prefill the data
description. Blue numbered circles indicate the “3” for the URL upload
and value type selection, signifying this is step 3 of the process.

<span id="_Ref151987332" class="anchor"></span>**Figure 3‑6: Add
Ingestion - Step 3 (Data upload via URL)**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image66.png"
style="width:5.92681in;height:4.80172in"
data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) website, displaying the download page for the &#39;Imperviousness Density 2018 (raster 10 m and 100 m), Europe, 3-yearly&#39; dataset. The top header includes the &#39;Copernicus Europe&#39;s eyes on Earth&#39; and &#39;Land Monitoring Service&#39; logos. Navigation elements at the top right show &#39;Technical assistance&#39;, &#39;News and Events&#39;, &#39;Work opportunities&#39;, a shopping cart icon with &#39;0&#39; items, and a &#39;Search Site&#39; bar. Main site navigation tabs are &#39;CLMS portfolio&#39;, &#39;Dataset catalogue&#39;, &#39;Data viewer&#39;, &#39;Use cases&#39;, and &#39;About us&#39;. A breadcrumb trail indicates the current page location: &#39;Home &gt; CLMS portfolio &gt; High Resolution Layer Imperviousness &gt; Imperviousness Density 2018 (raster 10 m and 100 m), Europe, 3-yearly&#39;. The main content area features a left-hand navigation pane with &#39;General Info&#39; and &#39;Download&#39; (currently selected). The right-hand pane is structured into several sections for data access: 1. **Download by area**: With the instruction &#39;Use this option if you would like to download the dataset for area(s) of interest.&#39; and a button &#39;Go to download by area&#39;. 2. An image preview box featuring a map of an urban area with reddish-brown impervious surfaces, and a button &#39;View in the data viewer&#39; below it. 3. **Download full dataset**: Provides information that the full dataset can be downloaded as pre-packaged data collections or using the CLMS download API, with a &#39;Click here&#39; link for more details on the API. 4. **Download pre-packaged data collections**: States that &#39;Pre-packaged Imperviousness Density 2018 datasets can be downloaded as 10 m raster files in 100 x 100 km tiles for each EEA38 country and the United Kingdom, as well as a full mosaic for EEA38 countries and the United Kingdom. The 100 m aggregated raster file is provided as a full mosaic for EEA38 countries and the United Kingdom.&#39; This section includes a search bar labelled &#39;Search in the pre-packaged data collection&#39; and indicates &#39;1 selected file(s) - Clear selection X Select all&#39;. A table lists available datasets for download. The columns are &#39;File&#39;, &#39;Area of interest&#39;, &#39;Version&#39;, &#39;Resolution&#39;, &#39;Type&#39;, and &#39;Format&#39;. The visible table rows include: * A checked checkbox for &#39;IMD_2018_010m_al_03035_v020&#39;, corresponding to &#39;Albania&#39;, version &#39;v020&#39;, &#39;10 m&#39; resolution, &#39;Raster&#39; type, and &#39;Geotiff&#39; format. * An unchecked checkbox for &#39;IMD_2018_010m_at_03035_v020&#39;, corresponding to &#39;Austria&#39;, version &#39;v020&#39;, &#39;10 m&#39; resolution, &#39;Raster&#39; type, and &#39;Geotiff&#39; format. * An unchecked checkbox for &#39;IMD_2018_010m_ba_03035_v020&#39;, corresponding to &#39;Bosnia and Herzegovina&#39;, version &#39;v020&#39;, &#39;10 m&#39; resolution, &#39;Raster&#39; type, and &#39;Geotiff&#39; format. * An unchecked checkbox for &#39;IMD_2018_010m_be_03035_v020&#39;, corresponding to &#39;Belgium&#39;, version &#39;v020&#39;, &#39;10 m&#39; resolution, &#39;Raster&#39; type, and &#39;Geotiff&#39; format. This screenshot illustrates the user interface for browsing and selecting High Resolution Layer Imperviousness Density (HRL IMD) data for download, available as pre-packaged datasets for individual countries or regions." />

This is a screenshot of the Copernicus Land Monitoring Service (CLMS)
website, displaying the download page for the “Imperviousness Density
2018 (raster 10 m and 100 m), Europe, 3-yearly” dataset.

The top header includes the “Copernicus Europe’s eyes on Earth” and
“Land Monitoring Service” logos. Navigation elements at the top right
show “Technical assistance”, “News and Events”, “Work opportunities”, a
shopping cart icon with “0” items, and a “Search Site” bar. Main site
navigation tabs are “CLMS portfolio”, “Dataset catalogue”, “Data
viewer”, “Use cases”, and “About us”.

A breadcrumb trail indicates the current page location: “Home \> CLMS
portfolio \> High Resolution Layer Imperviousness \> Imperviousness
Density 2018 (raster 10 m and 100 m), Europe, 3-yearly”.

The main content area features a left-hand navigation pane with “General
Info” and “Download” (currently selected). The right-hand pane is
structured into several sections for data access:

1.  **Download by area**: With the instruction “Use this option if you
    would like to download the dataset for area(s) of interest.” and a
    button “Go to download by area”.
2.  An image preview box featuring a map of an urban area with
    reddish-brown impervious surfaces, and a button “View in the data
    viewer” below it.
3.  **Download full dataset**: Provides information that the full
    dataset can be downloaded as pre-packaged data collections or using
    the CLMS download API, with a “Click here” link for more details on
    the API.
4.  **Download pre-packaged data collections**: States that
    “Pre-packaged Imperviousness Density 2018 datasets can be downloaded
    as 10 m raster files in 100 x 100 km tiles for each EEA38 country
    and the United Kingdom, as well as a full mosaic for EEA38 countries
    and the United Kingdom. The 100 m aggregated raster file is provided
    as a full mosaic for EEA38 countries and the United Kingdom.” This
    section includes a search bar labelled “Search in the pre-packaged
    data collection” and indicates “1 selected file(s) - Clear selection
    X Select all”.

A table lists available datasets for download. The columns are “File”,
“Area of interest”, “Version”, “Resolution”, “Type”, and “Format”. The
visible table rows include: \* A checked checkbox for
“IMD_2018_010m_al_03035_v020”, corresponding to “Albania”, version
“v020”, “10 m” resolution, “Raster” type, and “Geotiff” format. \* An
unchecked checkbox for “IMD_2018_010m_at_03035_v020”, corresponding to
“Austria”, version “v020”, “10 m” resolution, “Raster” type, and
“Geotiff” format. \* An unchecked checkbox for
“IMD_2018_010m_ba_03035_v020”, corresponding to “Bosnia and
Herzegovina”, version “v020”, “10 m” resolution, “Raster” type, and
“Geotiff” format. \* An unchecked checkbox for
“IMD_2018_010m_be_03035_v020”, corresponding to “Belgium”, version
“v020”, “10 m” resolution, “Raster” type, and “Geotiff” format.

This screenshot illustrates the user interface for browsing and
selecting High Resolution Layer Imperviousness Density (HRL IMD) data
for download, available as pre-packaged datasets for individual
countries or regions.

<span id="_Ref151987383" class="anchor"></span>**Figure 3‑7: Add
Ingestion -Step 3 (Get download link via CLMS portal)**

> <img
> src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image67.JPG"
> style="width:4.81132in;height:3.58147in"
> data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) website&#39;s &#39;Downloads&#39; page, displaying the status of data download tasks. The page header includes the Copernicus and Land Monitoring Service logos, along with navigation links such as &#39;Technical assistance&#39;, &#39;News and Events&#39;, &#39;Work opportunities&#39;, &#39;CLMS portfolio&#39;, &#39;Dataset catalogue&#39;, &#39;Data viewer&#39;, &#39;Use cases&#39;, and &#39;About us&#39;. A message at the top warns of &#39;a high load in our download process&#39; and extended queue times due to the &#39;successful launch of the new CLMS website&#39;. The main content area is divided into sections for download task statuses: &#39;Queued&#39;, &#39;In progress&#39;, &#39;Completed&#39;, &#39;Rejected&#39;, and &#39;Cancelled&#39;. All sections except &#39;Completed&#39; show the message &#39;There are no tasks&#39;. The &#39;Completed&#39; section displays a single completed task within a yellow-bordered box. This task is identified as &#39;Task ID: 159773967&#39;, with a &#39;Start date: 24.10.2023 11.30&#39; and &#39;End date: 25.10.2023 18.14&#39;. The downloaded product is specified as &#39;Imperviousness Density (IMD) 2018 (raster 10 m and 100 m), Europe, 3-yearly - Pre-packaged&#39;. A &#39;Download file (15.5 MB)&#39; link is provided, and the download &#39;Expires in 3 days&#39;." /><img
> src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image68.JPG"
> style="width:4.79245in;height:2.92536in"
> data-fig-alt="A screenshot of an email notification received on &#39;Mi 25.10.2023 20:14&#39; from &#39;Copernicus Land Monitoring Service &lt;copernicus@eea.europa.eu&gt;&#39; with the subject &#39;Your download is ready!&#39;. The email states: &#39;Hello, Requested data **159773967** can be downloaded. Please use the following URL to begin the download https://copernicus-fme.eea.europa.eu/clmsdatadownload/results/18447.zip&#39;. The &#39;Datasets&#39; section specifies: &#39;Imperviousness Density 2018 (raster 10 m and 100 m), Europe, 3-yearly - Pre-packaged&#39;. The email is an auto-generated message delivered because the user associated with the email address requested a download, and is signed &#39;Best regards, Copernicus Land Monitoring Service&#39;." />

<span id="_Ref151987407" class="anchor"></span>**Figure 3‑8: Add
Ingestion - Step 3 (Get download link via the portal and via email)**

After selecting the dataset, you need to define if the dataset has
discrete or continuous values[^8] (see [Figure 3‑5](#_Ref151987252) and
[Figure 3‑6](#_Ref151987332)). For example, the HRL WAW and all local
components consists of discrete objects, which have known and definable
boundaries. A lake is a discrete object within the surrounding
landscape. The HRL TCD and IMD however, represent continuous values, as
their values range from 0-100 %, indicating the degree of their
respective characteristic.

In step 4, you have the possibility to **exclude a class code** from
being processed (see [Figure 3‑9](#_Ref151987363)). It excludes all
class codes which stand for an unknown classification (i.e. NoData
values). If a TIF dataset specifies a NoData value in its metadata the
corresponding class is excluded automatically. This is recommended if
you don’t want to have specific values in the statistics/being processed
and for all unclassified/unknown values (i.e. NoData) (step 4). All
pixels in the ingested dataset with an excluded class code will then
appear as NoData pixel in the final Ingestion. If you do not enter a
excluded class code value and the NoData value does not appear in the
TIF metadata, then all classes are “0” in the ingestion, where the
original data always displayed the no-data class.

For **Continuous values** (datasets with continues values/ranges like
e.g. tree cover density values between 0 and 100%) all **values** which
do not represent thematic values in the input dataset will be
**excluded**. Pixels with one of the given values will be counted as
NoData in the ingestion. If a TIF dataset specifies a NoData value in
its metadata the corresponding value is excluded automatically.

For **Discrete values** (datasets with concret, mulitple claseses like
e.g. HRL Forest class 0,1,2) all **class codes** which do not represent
thematic values in the input dataset will be **excluded**. For example,
unclassifiable (254) and outside area (255) pixels should be excluded.
Pixels of the given classes will be counted as NoData in the ingestion.
If a TIF dataset specifies a NoData value in its metadata the
corresponding class is excluded automatically.

In the example, we want to exclude 255 and 254 from being ingested.
Please press enter after entering the value. Alternatively, for discrete
datasets, you are able to hide the values when editing the data (section
[3.7](#edit-ingestion) [Figure 3‑35](#_Ref100162670)) by disabling
single classes with the “eye” symbol before ingesting and publishing an
Ingestion.

Additionally, you can **enter a layer name** which shall be used to
generate input classes if there are <u>more than one layers per</u>
dataset (if several layers are stored in a .gdb for example). If nothing
is defined, the first layer will be selected. In this case, this field
can be omitted.

**Please make sure to avoid special characters, otherwise an error will
occur.** Please also refer to section 3.3 to learn about the
**limitations of data uploads**.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image69.png"
style="width:4.1475in;height:2.17773in"
data-fig-alt="This image is a screenshot of a user interface for the &#39;Add Ingestion&#39; process, displaying &#39;Step 2: &#39;Dataset Selection Upload Dataset - Raster&#39;&#39;. &#39;Step 1: Input Type Selection&#39; is shown as a preceding, completed step. The interface provides two upload methods: &#39;File Upload&#39; and &#39;URL Upload&#39;. The &#39;URL Upload&#39; tab is active, and a direct download URL, &#39;https://copernicus-fme.eea.europa.eu/clmsdatadownload/results/18447.zip&#39;, has been entered into the &#39;Enter URL *&#39; field, indicated by a green checkmark as valid. Below this, the user is prompted to define the dataset&#39;s value type, with &#39;Continuous values&#39; selected over &#39;Discrete values&#39; via radio buttons." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image70.png"
style="width:3.93022in;height:2.69246in"
data-fig-alt="This image is a screenshot of a user interface for data ingestion within the Copernicus Land Monitoring Service (CLMS), focusing on excluded values and file upload mechanisms. The interface displays a section for &#39;Excluded Value&#39; where numeric values &#39;254&#39; and &#39;255&#39; are listed as pre-configured excluded values. Accompanying text explains: &#39;Exclude all values which do not represent thematic values in the input dataset. Pixels with one of the given values will be counted as NoData in the ingestion. If a TIF dataset specifies a NoData value in its metadata the corresponding value is excluded automatically.&#39; Below this is a field labelled &#39;Class Code&#39; for input. A subsequent field for &#39;Layer Name&#39; provides the instruction: &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; The lower portion of the interface features a large dashed-border area for file input, with the text &#39;Drag and Drop OR&#39; and a green button labelled &#39;UPLOAD DOCUMENT/S&#39; with an upward arrow icon." />

<span id="_Ref151987363" class="anchor"></span>**Figure 3‑9: Add
Ingestion - Step 4 (exclude values and enter layer name)**

The fifth step is optional and provides you with the possibility to
upload **additional, supporting files** that help to understand the
content (see [Figure 3‑10](#_Ref151987450)), such as:

- Metadata files,

- Legend files (QGIS layer style file (.qml) or SLD (Styled Layer
  Descriptor) file (.sld); ArcGIS Layer Files (.lyr) are not supported),

- EAGLE Barcoding files.

Files can be uploaded via the explorer or per “drag and drop”. These
additional files will be used to prefill the data descriptions and
define the EAGLE barcodes as well as the style for the Ingestion Classes
(step 5). The upload of these documents can also be performed at a later
stage (section [3.7](#edit-ingestion)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image73.JPG"
style="width:3.25472in;height:3.52805in"
data-fig-alt="This image is a screenshot of the &#39;Add Ingestion&#39; user interface, depicting &#39;Step 2: &#39;Dataset Selection Upload Dataset - Raster&#39;&#39; of a data ingestion process. &#39;Continuous values&#39; is selected as the input type. The interface allows users to specify &#39;Excluded Value&#39; Class Codes, with &#39;254&#39; and &#39;255&#39; currently entered. A description explains that these values, representing non-thematic data, will be counted as NoData in the ingestion. A text field is available for entering a &#39;Layer Name&#39;. Users can upload supporting documents by &#39;Drag and Drop&#39; or using an &#39;UPLOAD DOCUMENT/S&#39; button. Two files are listed as uploaded: &#39;Barcoding3.1.2_Impervious_Degree_v0.3.xlsx&#39; and &#39;IMD_2018_010m_eu_03035_v020.xml&#39;. A checkbox for &#39;Delete raw data&#39; is displayed and is unchecked." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image72.png"
style="width:3.79453in;height:1.74684in"
data-fig-alt="This image is a screenshot of a file selection dialog within a Windows environment, showing files related to &#39;EAGLE Mapping (BarCoding)&#39;. The navigation path at the top indicates `D3.2.1 - Demonstration and docume... &gt; EAGLE Mapping (BarCoding)`. The file list displays four columns: `Name`, `Änderungsdatum` (Modification Date), `Typ` (Type), and `Größe` (Size). The visible files, all identified as `Microsoft Ex...` (likely Excel files), are: * `Barcoding3.1.2_Forest_TreeCoverDensity_v0.3`, modified on 19.01.2022 at 13:43, 518 KB. This file likely relates to Tree Cover Density (TCD). * `Barcoding3.1.2_Grassland_v0.3`, modified on 19.01.2022 at 13:42, 520 KB. This file relates to Grassland (GRA). * `Barcoding3.1.2_Impervious_BuiltUp_v0.3`, modified on 19.01.2022 at 13:42, 525 KB. This file relates to Imperviousness Density (IMD), specifically built-up areas. * `Barcoding3.1.2_Impervious_Degree_v0.3`, modified on 19.01.2022 at 13:41, 518 KB. This file, relating to Imperviousness Density (IMD) degree, is highlighted, indicating selection. * `Barcoding3.1.2_WaterAndWetness_v0.3`, modified on 19.01.2022 at 13:41, 518 KB. This file relates to Water and Wetness (WAW). * `brp2018_frq_TableToExcel_GH`, modified on 24.03.2022 at 17:47, 33 KB. The &#39;Dateiname&#39; (Filename) input field at the bottom displays `Barcoding3.1.2_Impervious_Degree_v0.3`, corresponding to the selected file. Available buttons are `Alle Dateien` (All Files), `Öffnen` (Open), and `Abbrechen` (Cancel). This interface is used for selecting data for ingestion, particularly for High Resolution Layer (HRL) products, which can have either discrete or continuous values." />

<span id="_Ref151987450" class="anchor"></span>**Figure 3‑10: Add
Ingestion - Step 5 (upload additional datasets (i.e. EAGLE barcoding
file))**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image73.JPG"
style="width:3.60377in;height:3.90642in"
data-fig-alt="This image is a screenshot of the &#39;Add Ingestion&#39; user interface, depicting &#39;Step 2: &#39;Dataset Selection Upload Dataset - Raster&#39;&#39; of a data ingestion process. &#39;Continuous values&#39; is selected as the input type. The interface allows users to specify &#39;Excluded Value&#39; Class Codes, with &#39;254&#39; and &#39;255&#39; currently entered. A description explains that these values, representing non-thematic data, will be counted as NoData in the ingestion. A text field is available for entering a &#39;Layer Name&#39;. Users can upload supporting documents by &#39;Drag and Drop&#39; or using an &#39;UPLOAD DOCUMENT/S&#39; button. Two files are listed as uploaded: &#39;Barcoding3.1.2_Impervious_Degree_v0.3.xlsx&#39; and &#39;IMD_2018_010m_eu_03035_v020.xml&#39;. A checkbox for &#39;Delete raw data&#39; is displayed and is unchecked." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image74.png"
style="width:2.99131in;height:1.53765in"
data-fig-alt="This is a screenshot of a Windows file explorer window displaying a metadata file for Copernicus Land Monitoring Service (CLMS) Imperviousness Density (IMD) data. The breadcrumb navigation path at the top shows the file&#39;s location as `Imperviousness_Layers &gt; 2018 &gt; IMD_2018_010m &gt; metadata`. A search for `&#39;metadata&#39;` is active in the top right. The main file list shows one entry: `IMD_2018_010m_eu_03035_V2_0`. Its last modified date is `10.07.2020 14:27`, the file type is `XML-Datei` (XML File), and the size is `43 KB`. At the bottom, a filename field is pre-populated with `IMD_2018_010m_eu_03035_V2_0`, next to buttons labelled `Alle Dateien` (All Files) and `Öffnen` (Open)." />

<span id="_Toc137576649" class="anchor"></span>**Figure 3‑11: Add
Ingestion - Step 5 (upload additional datasets (i.e. Metadata file))**

The last option allows you to specify whether the **raw data**
(original/initial uploaded dataset) can be retained in the system after
processing (see [Figure 3‑12](#_Ref151987498)). The “Delete raw data”
tick box is not ticked by default. If the “delete raw data” is ticked
the initial dataset will be automatically deleted after the creation of
the Ingestion from the CLC+ Core storage. The raw data will only usable
for users of the same organization and the admin user - and only if the
Ingestion processing fails and the failed Ingestion needs to be
processed (retry) again. Otherwise retrying a failed Ingestion
processing step will not be possible and a completely new Ingestion
would need to be initiated. After an Ingestion was successful the raw
dataset is not needed anymore. Note that no user can access the raw data
in the CLC+ Cores data storage.

As soon as the processing step is finished, the raw data cannot be
downloaded or reused anymore by anyone. Finally, if you have defined all
upload parameters, the dataset can be added by pressing the ‘ADD’ button
(see [Figure 3‑12](#_Ref151987498)). While the upload is performed,
please do not leave the page (see [Figure 3‑13](#_Ref151987519)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image76.png"
style="width:4.08063in;height:4.18293in"
data-fig-alt="A screenshot of a user interface for an &#39;Add Ingestion&#39; process, specifically at Step 2, labeled &#39;Dataset Selection Upload Dataset - Raster&#39;. The interface presents options to configure data ingestion for raster datasets. Key elements and controls visible include: 1. **Class Code exclusion**: A section titled &#39;Class Code&#39; with instructional text: &#39;Exclude all values which do not represent thematic values in the input dataset. Pixels with one of the given values will be counted as NoData in the ingestion. If a TIF dataset specifies a NoData value in its metadata the corresponding value is excluded automatically.&#39; It shows two input fields with numerical values &#39;234&#39; and &#39;235&#39; that can be excluded. 2. **Layer Name input**: A text field labeled &#39;Layer Name&#39; with instructional text: &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; 3. **Document upload**: A &#39;Drag and Drop&#39; area or an &#39;UPLOAD DOCUMENT/S&#39; button for additional files. The instructional text explains: &#39;All documents that help to understand the content, including legend files which will be used to automatically create Input Classes and metadata files which will be used to automatically prefill the data description. (No file type restrictions)&#39;. Two files are listed as already uploaded: &#39;Barcoding3.1.2_Impervious_Degree_v0.3.xlsx&#39; and &#39;IMD_2018_010m_eu_03035_v020.xml&#39;. 4. **Delete raw data option**: A checkbox labeled &#39;Delete raw data&#39;. 5. **Navigation buttons**: &#39;CANCEL&#39;, &#39;BACK&#39;, and &#39;ADD&#39; buttons are at the bottom of the interface." />

A screenshot of a user interface for an “Add Ingestion” process,
specifically at Step 2, labeled ‘Dataset Selection Upload Dataset -
Raster’. The interface presents options to configure data ingestion for
raster datasets.

Key elements and controls visible include: 1. **Class Code exclusion**:
A section titled “Class Code” with instructional text: “Exclude all
values which do not represent thematic values in the input dataset.
Pixels with one of the given values will be counted as NoData in the
ingestion. If a TIF dataset specifies a NoData value in its metadata the
corresponding value is excluded automatically.” It shows two input
fields with numerical values “234” and “235” that can be excluded. 2.
**Layer Name input**: A text field labeled “Layer Name” with
instructional text: “Enter Layer Name from Dataset which shall be used
to generate Input Classes.” 3. **Document upload**: A “Drag and Drop”
area or an “UPLOAD DOCUMENT/S” button for additional files. The
instructional text explains: “All documents that help to understand the
content, including legend files which will be used to automatically
create Input Classes and metadata files which will be used to
automatically prefill the data description. (No file type
restrictions)”. Two files are listed as already uploaded:
“Barcoding3.1.2_Impervious_Degree_v0.3.xlsx” and
“IMD_2018_010m_eu_03035_v020.xml”. 4. **Delete raw data option**: A
checkbox labeled “Delete raw data”. 5. **Navigation buttons**: “CANCEL”,
“BACK”, and “ADD” buttons are at the bottom of the interface.

<span id="_Ref151987519" class="anchor"></span>**Figure 3‑12: Add
Ingestion - Step 6 (start the upload)**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image77.png"
style="width:3.57301in;height:2.58481in"
data-fig-alt="A screenshot of a web-based user interface for data ingestion within the Copernicus Land Monitoring Service (CLMS). The main background displays a table with five columns: &#39;Country&#39;, &#39;Region&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, and &#39;Contact Person&#39;. Multiple rows are visible, detailing existing or pending data contributions. Specific table entries are: - Row 1: Country: Hungary/Magyaro..., Region: -, Time Range: 01.07.2017 - 30.06.2019, Organisation/s: European Environ..., Contact Person: copernicus@eea... - Row 2: Country: Luxembourg, Region: -, Time Range: 01.07.2017 - 30.06.2019, Organisation/s: European Environ..., Contact Person: copernicus@eea... - Row 3: Country: European Environ..., Region: -, Time Range: 01.01.2017 - 31.12.2018, Organisation/s: European Environ..., Contact Person: copernicus@eea... - A partially obscured row shows Time Range: 01.03.2018 - 31.10.2018, Organisation/s: European Environ... - Another partially obscured row shows Time Range: 01.01.2017 - 31.12.2019, Organisation/s: European Environ... - A further partially obscured row shows Time Range: 01.01.2017 - 31.12.2019, Organisation/s: European Environ... - The last visible partially obscured row shows Time Range: 15.05.2017 - 14.09.2019, Organisation/s: European Environ... A modal dialog titled &#39;Upload Additional Documents ...&#39; is overlaid on the center of the screen, indicating a file upload process. It displays the current progress as &#39;0.2MB of 1.1MB&#39; and contains the warning: &#39;Please do not leave this page until the upload is finished! Otherwise, the upload will be aborted.&#39; A partial green circular progress indicator is visible above the dialog." />

A screenshot of a web-based user interface for data ingestion within the
Copernicus Land Monitoring Service (CLMS). The main background displays
a table with five columns: “Country”, “Region”, “Time Range”,
“Organisation/s”, and “Contact Person”. Multiple rows are visible,
detailing existing or pending data contributions.

Specific table entries are: - Row 1: Country: Hungary/Magyaro…, Region:
-, Time Range: 01.07.2017 - 30.06.2019, Organisation/s: European
Environ…, Contact Person: copernicus@eea… - Row 2: Country: Luxembourg,
Region: -, Time Range: 01.07.2017 - 30.06.2019, Organisation/s: European
Environ…, Contact Person: copernicus@eea… - Row 3: Country: European
Environ…, Region: -, Time Range: 01.01.2017 - 31.12.2018,
Organisation/s: European Environ…, Contact Person: copernicus@eea… - A
partially obscured row shows Time Range: 01.03.2018 - 31.10.2018,
Organisation/s: European Environ… - Another partially obscured row shows
Time Range: 01.01.2017 - 31.12.2019, Organisation/s: European Environ… -
A further partially obscured row shows Time Range: 01.01.2017 -
31.12.2019, Organisation/s: European Environ… - The last visible
partially obscured row shows Time Range: 15.05.2017 - 14.09.2019,
Organisation/s: European Environ…

A modal dialog titled “Upload Additional Documents …” is overlaid on the
center of the screen, indicating a file upload process. It displays the
current progress as “0.2MB of 1.1MB” and contains the warning: “Please
do not leave this page until the upload is finished! Otherwise, the
upload will be aborted.” A partial green circular progress indicator is
visible above the dialog.

<span id="_Ref151987498" class="anchor"></span>**Figure 3‑13: Add
Ingestion - Step 6 (stay on page)**

### Vector dataset

Clicking the ‘**Add Ingestion**’ button (see section
[1.6](#data-catalogue) [Figure 1‑9](#_Ref151467380)) opens the ‘Add
Ingestion’ dialog (see [Figure 3‑14](#_Ref151987694)) where you can
define the data format of your dataset (step 1).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image78.png"
style="width:6.925in;height:3.81806in"
data-fig-alt="This screenshot displays the EAGLE (Eionet Action Group on Land monitoring in Europe) Data Catalogue web interface, showing a pop-up dialog for &#39;Add Ingestion&#39; with &#39;Input Type Selection&#39; as the first step. The interface is labelled &#39;Data Catalogue&#39; at the top left and includes navigation tabs for &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. The logged-in user is &#39;Renner Thomas&#39;. The main table shows a list of datasets with columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. Visible dataset entries include: * &#39;CLC+Backbone (2018)&#39;, created &#39;05.09.2023&#39;, with &#39;Reference Year&#39; &#39;2018&#39;, &#39;Time Range&#39; &#39;01.07.2017 - 30.06.2019&#39;, &#39;Status&#39; &#39;USED&#39;, and &#39;INSPIRE Themes&#39; &#39;Land cover&#39;. * &#39;Coastal Zones (CZ) 20...&#39;, created &#39;21.06.2023&#39;, &#39;Reference Year&#39; &#39;2018&#39;, &#39;Time Range&#39; &#39;01.01.2017 - 31.12.2019&#39;, &#39;Status&#39; &#39;USED&#39;, and &#39;INSPIRE Themes&#39; &#39;Land use, Land cover&#39;. * &#39;Corine Land Cover (CL...&#39;, created &#39;06.09.2023&#39;, &#39;Status&#39; &#39;PUBLISHED&#39;, &#39;INSPIRE Themes&#39; &#39;Land use, Land cover&#39;. * &#39;Corine Land Cover (CL...&#39;, created &#39;14.06.2023&#39;, &#39;Status&#39; &#39;USED&#39;, &#39;INSPIRE Themes&#39; &#39;Land use, Land cover&#39;. * &#39;Effis 2018&#39;, created &#39;05.09.2023&#39;, &#39;Status&#39; &#39;USED&#39;, &#39;INSPIRE Themes&#39; &#39;Land cover&#39;. * &#39;Eurocrop 2018&#39;, created &#39;05.09.2023&#39;, &#39;Status&#39; &#39;USED&#39;, &#39;INSPIRE Themes&#39; &#39;Land use, Land cover&#39;. * &#39;HRL - Dominant Leaf T...&#39;, created &#39;05.09.2023&#39;, &#39;Status&#39; &#39;USED&#39;, &#39;INSPIRE Themes&#39; &#39;Land use, Land cover&#39;. * &#39;HRL - Forest Type (FTY...&#39;, created &#39;10.03.2023&#39;, &#39;Status&#39; &#39;USED&#39;, &#39;INSPIRE Themes&#39; &#39;Land use, Land cover&#39;. * &#39;HRL - Grassland 2018&#39;, created &#39;10.03.2023&#39;, &#39;Status&#39; &#39;PUBLISHED&#39;, &#39;INSPIRE Themes&#39; &#39;Land use, Land cover&#39;. * &#39;HRL - Grassland 2018&#39;, created &#39;05.09.2023&#39;, &#39;Reference Year&#39; &#39;2018&#39;, &#39;Time Range&#39; &#39;01.03.2018 - 31.10.2018&#39;, &#39;Status&#39; &#39;USED&#39;, and &#39;INSPIRE Themes&#39; &#39;Land cover&#39;. The table pagination shows &#39;Items per page: 10&#39; and &#39;1 - 10 of 32&#39;. A modal &#39;Add Ingestion&#39; dialog is superimposed, indicating &#39;1 Input Type Selection&#39; is the current step, with &#39;2 &#39;Dataset Selection Upload Dataset - Vector&#39;&#39; as the next step. Users can choose to &#39;Upload Dataset - Raster&#39; or &#39;Upload Dataset - Vector&#39;, with the &#39;Upload Dataset - Vector&#39; option currently selected. Action buttons are &#39;CANCEL&#39; and &#39;NEXT&#39;. At the bottom left, logos for &#39;Copernicus&#39;, &#39;EAGLE EIONET Action Group&#39;, &#39;European Commission&#39;, and &#39;European Environment Agency&#39; are visible." />

This screenshot displays the EAGLE (Eionet Action Group on Land
monitoring in Europe) Data Catalogue web interface, showing a pop-up
dialog for “Add Ingestion” with “Input Type Selection” as the first
step. The interface is labelled “Data Catalogue” at the top left and
includes navigation tabs for “EAGLE Ontology”, “About EAGLE”,
“Organisations”, and “Users”. The logged-in user is “Renner Thomas”.

The main table shows a list of datasets with columns: “EAGLE Approved”,
“Name”, “Type”, “Created At”, “Created By”, “Country”, “Region”,
“Reference Year”, “Time Range”, “Organisation/s”, “Contact Person”,
“Status”, and “INSPIRE Themes”. Visible dataset entries include: \*
“CLC+Backbone (2018)”, created “05.09.2023”, with “Reference Year”
“2018”, “Time Range” “01.07.2017 - 30.06.2019”, “Status” “USED”, and
“INSPIRE Themes” “Land cover”. \* “Coastal Zones (CZ) 20…”, created
“21.06.2023”, “Reference Year” “2018”, “Time Range” “01.01.2017 -
31.12.2019”, “Status” “USED”, and “INSPIRE Themes” “Land use, Land
cover”. \* “Corine Land Cover (CL…”, created “06.09.2023”, “Status”
“PUBLISHED”, “INSPIRE Themes” “Land use, Land cover”. \* “Corine Land
Cover (CL…”, created “14.06.2023”, “Status” “USED”, “INSPIRE Themes”
“Land use, Land cover”. \* “Effis 2018”, created “05.09.2023”, “Status”
“USED”, “INSPIRE Themes” “Land cover”. \* “Eurocrop 2018”, created
“05.09.2023”, “Status” “USED”, “INSPIRE Themes” “Land use, Land cover”.
\* “HRL - Dominant Leaf T…”, created “05.09.2023”, “Status” “USED”,
“INSPIRE Themes” “Land use, Land cover”. \* “HRL - Forest Type (FTY…”,
created “10.03.2023”, “Status” “USED”, “INSPIRE Themes” “Land use, Land
cover”. \* “HRL - Grassland 2018”, created “10.03.2023”, “Status”
“PUBLISHED”, “INSPIRE Themes” “Land use, Land cover”. \* “HRL -
Grassland 2018”, created “05.09.2023”, “Reference Year” “2018”, “Time
Range” “01.03.2018 - 31.10.2018”, “Status” “USED”, and “INSPIRE Themes”
“Land cover”. The table pagination shows “Items per page: 10” and “1 -
10 of 32”.

A modal “Add Ingestion” dialog is superimposed, indicating “1 Input Type
Selection” is the current step, with “2 ‘Dataset Selection Upload
Dataset - Vector’” as the next step. Users can choose to “Upload
Dataset - Raster” or “Upload Dataset - Vector”, with the “Upload
Dataset - Vector” option currently selected. Action buttons are “CANCEL”
and “NEXT”.

At the bottom left, logos for “Copernicus”, “EAGLE EIONET Action Group”,
“European Commission”, and “European Environment Agency” are visible.

<span id="_Ref151987694" class="anchor"></span>**Figure 3‑14: Add
Ingestion - Step 1 (Data format) - here vector file**

In a second step, further information, such as name and country / region
that describes the data can be entered (step 2 see [Figure
3‑15](#_Ref151987707)). All **mandatory fields** are marked with a \*.
In this example, we will upload the Urban Atlas 2018 for Innsbruck. As
we want to ingest the area of Innsbruck only in this example, we do
specify Tyrol as region.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image79.png"
style="width:4.01349in;height:3.14495in"
data-fig-alt="This is a screenshot of a user interface for the &#39;Add Ingestion&#39; process, specifically showing &#39;Step 2 Dataset Selection &#39;Upload Dataset - Vector&#39;&#39;, which is highlighted in green. &#39;Step 1 Input Type Selection&#39; is greyed out. The form displays three pre-filled input fields: &#39;Name *&#39; with &#39;UA_2018_Innsbruck&#39;, &#39;Country *&#39; with &#39;AT Austria/Österreich&#39;, and &#39;Region&#39; with &#39;AT33 Tirol&#39;. Below these fields, two options for data upload are presented: &#39;File Upload&#39; is selected and visually indicated as active, while &#39;URL Upload&#39; is an alternative. Under the &#39;File Upload&#39; section, an &#39;Upload Dataset *&#39; area with an upload icon prompts the user with &#39;Please pick files from your Computer&#39;. A vertical scrollbar on the right side indicates that more form content is available." />

This is a screenshot of a user interface for the “Add Ingestion”
process, specifically showing “Step 2 Dataset Selection ‘Upload
Dataset - Vector’”, which is highlighted in green. “Step 1 Input Type
Selection” is greyed out. The form displays three pre-filled input
fields: “Name *” with ”UA_2018_Innsbruck”, ”Country* ” with “AT
Austria/Österreich”, and “Region” with “AT33 Tirol”. Below these fields,
two options for data upload are presented: “File Upload” is selected and
visually indicated as active, while “URL Upload” is an alternative.
Under the “File Upload” section, an “Upload Dataset \*” area with an
upload icon prompts the user with “Please pick files from your
Computer”. A vertical scrollbar on the right side indicates that more
form content is available.

<span id="_Ref151987707" class="anchor"></span>**Figure 3‑15: Add
Ingestion - Step 2 (Parameter)**

The data can be uploaded directly from your computer (file upload or per
\`drag and drop\`) or by entering an URL where the data shall be
collected from (step 3 see [Figure 3‑16](#_Ref151987739)). Please also
refer to section 3.3 Remarks on the Ingestion process. The supported
file formats for vector files:

- shapefile - When uploading a shapefile (shp), its elements need to be
  zipped

- geopackage (gpkg)

- file geodatabases (gdb)

- Hierarchical Data Format (HDF5)

In this example below (see [Figure 3‑16](#_Ref151987739)), we chose the
file upload from a local computer. If successfully defined, an
attachment is added to the dialog. **If the file size is larger than 5
GB, a warning appears recommending using an URL upload as the file
upload might take a long time.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image80.png"
style="width:4.72655in;height:3.35007in"
data-fig-alt="This screenshot displays the &#39;Add Ingestion&#39; user interface, specifically showing &#39;Step 2: Dataset Selection &#39;Upload Dataset - Vector&#39;&#39;. The first step, &#39;1 Input Type Selection&#39;, is shown as completed. The interface offers two tabs for data input: &#39;File Upload&#39; and &#39;URL Upload&#39;, with &#39;File Upload&#39; currently active. Under the &#39;File Upload&#39; section, a mandatory field &#39;Upload Dataset *&#39; with the instruction &#39;Please pick files from your Computer&#39; is present. The file &#39;AT005L3_INNSBRUCK_UA2018_v012.gpkg&#39; has been uploaded. Below this, a mandatory &#39;Attribute Name *&#39; field is populated with &#39;CODE_2018&#39;. An explanation states: &#39;Enter Attribute Name from Dataset (which column from the attribute table shall be taken) which shall be used as Input Parameter for the Class Code.&#39; Two radio button options are available: &#39;Discrete values&#39;, which is selected, and &#39;Continuous values&#39;. A field labelled &#39;Excluded Class Code&#39; is partially visible at the bottom of the interface. This interface is part of the Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation CORINE Land Cover) system for ingesting Urban Atlas 2018 data." />

This screenshot displays the “Add Ingestion” user interface,
specifically showing “Step 2: Dataset Selection ‘Upload Dataset -
Vector’”. The first step, “1 Input Type Selection”, is shown as
completed. The interface offers two tabs for data input: “File Upload”
and “URL Upload”, with “File Upload” currently active.

Under the “File Upload” section, a mandatory field “Upload Dataset *”
with the instruction ”Please pick files from your Computer” is present.
The file ”AT005L3_INNSBRUCK_UA2018_v012.gpkg” has been uploaded. Below
this, a mandatory ”Attribute Name* ” field is populated with
“CODE_2018”. An explanation states: “Enter Attribute Name from Dataset
(which column from the attribute table shall be taken) which shall be
used as Input Parameter for the Class Code.” Two radio button options
are available: “Discrete values”, which is selected, and “Continuous
values”. A field labelled “Excluded Class Code” is partially visible at
the bottom of the interface. This interface is part of the Copernicus
Land Monitoring Service (CLMS) CLC+ (next-generation CORINE Land Cover)
system for ingesting Urban Atlas 2018 data.

<span id="_Ref151987739" class="anchor"></span>**Figure 3‑16: Add
Ingestion - Step 3 (Data upload via local computer)**

In this example below (see [Figure 3‑17](#_Ref151987899)), we chose the
URL upload from the [CLMS portal](https://land.copernicus.eu/). Select
the required files on the download page (put them in the shopping cart)
(see [Figure 3‑18](#_Ref151987915)). After sending the order, you will
retrieve a download link via this page (depending on the processing
time) and per email. Copy the link and enter the URL in the dialog.

**Note: please use a direct download URL (link that automatically starts
the download immediately). Consider that the system can only process
links which do not require a user login.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image81.png"
style="width:5.41251in;height:3.10983in"
data-fig-alt="This image shows a screenshot of the &#39;Add Ingestion&#39; user interface, which is part of a Copernicus Land Monitoring Service (CLMS) tool. The interface outlines a two-step process. Step 1, &#39;Input Type Selection,&#39; is greyed out. Step 2, &#39;&#39;Dataset Selection Upload Dataset - Vector&#39;,&#39; is highlighted in green, indicating it is the active step. Within Step 2, there are two tabs: &#39;File Upload&#39; and &#39;URL Upload.&#39; The &#39;URL Upload&#39; tab is currently selected. The &#39;URL Upload&#39; section contains three input fields, with asterisks indicating mandatory fields: 1. &#39;Enter URL *&#39;: This field is populated with `https://copernicus-fme.eea.europa.eu/clmsdatadownload/results/19239.zip`. A green checkmark confirms the URL has been successfully validated, alongside an &#39;x&#39; icon. A placeholder text &#39;Please enter a source URL&#39; is also visible. 2. &#39;Attribute Name *&#39;: This field is populated with `CODE_2018`. Below it, a descriptive text reads: &#39;Enter Attribute Name from Dataset (column from the attribute table) which shall be used as Input Parameter for the Class Code. Values of the selected attribute column must only contain upper- and lower-case letters, numbers, underscores or hyphens.&#39; 3. &#39;Excluded Class Code&#39;: This field is empty. A vertical scrollbar is visible on the right side of the interface. This screenshot corresponds to &#39;Figure 3-15: Add Ingestion - Step 2 (Parameter)&#39; from the documentation." />

This image shows a screenshot of the “Add Ingestion” user interface,
which is part of a Copernicus Land Monitoring Service (CLMS) tool. The
interface outlines a two-step process. Step 1, “Input Type Selection,”
is greyed out. Step 2, “‘Dataset Selection Upload Dataset - Vector’,” is
highlighted in green, indicating it is the active step. Within Step 2,
there are two tabs: “File Upload” and “URL Upload.” The “URL Upload” tab
is currently selected.

The “URL Upload” section contains three input fields, with asterisks
indicating mandatory fields: 1. “Enter URL *”: This field is populated
with
`https://copernicus-fme.eea.europa.eu/clmsdatadownload/results/19239.zip`.
A green checkmark confirms the URL has been successfully validated,
alongside an ‘x’ icon. A placeholder text ”Please enter a source URL” is
also visible. 2. ”Attribute Name* ”: This field is populated with
`CODE_2018`. Below it, a descriptive text reads: “Enter Attribute Name
from Dataset (column from the attribute table) which shall be used as
Input Parameter for the Class Code. Values of the selected attribute
column must only contain upper- and lower-case letters, numbers,
underscores or hyphens.” 3. “Excluded Class Code”: This field is empty.

A vertical scrollbar is visible on the right side of the interface. This
screenshot corresponds to “Figure 3-15: Add Ingestion - Step 2
(Parameter)” from the documentation.

<span id="_Ref151987899" class="anchor"></span>**Figure 3‑17: Add
Ingestion - Step 3 (Data upload via URL)**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image82.jpeg"
style="width:5.67993in;height:3.31818in"
data-fig-alt="A screenshot of an email from the Copernicus Land Monitoring Service (CLMS) confirming that a data download is ready. The email is dated &#39;Sa 28.10.2023 06:38&#39; and sent from &#39;Copernicus Land Monitoring Service &lt;copernicus@eea.europa.eu&gt;&#39; with the subject &#39;Your download is ready!&#39;. The email body states: &#39;Requested data **8337912519** can be downloaded. Please use the following URL to begin the download: https://copernicus-fme.eea.europa.eu/clmsdatadownload/results/19239.zip&#39;. The datasets listed include: &#39;Urban Atlas Land Cover/Land Use 2018 (vector), Europe, 6-yearly - Pre-packaged&#39;. The email notes it is auto-generated because the user requested a download, and concludes with &#39;Best regards, Copernicus Land Monitoring Service&#39;." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image83.jpeg"
style="width:4.80394in;height:4.34091in"
data-fig-alt="This image is a screenshot displaying two main user interface elements: a file save dialog and a task completion notification. The top portion shows a Windows file save dialog titled &#39;Bitte geben Sie den Dateinamen an, unter dem die Datei gespeichert werden soll...&#39; (Please enter the file name under which the file should be saved...). The current location is &#39;Dieser PC &gt; Downloads&#39;. Quick access shortcuts are visible, including &#39;Downloads&#39; and several folders like &#39;30574_EU_EEA_CLC+Core&#39; and &#39;30715_EEA_CLC+_Instances&#39;. The file list shows recent `.zip` files such as &#39;18447.zip&#39; (26.10.2023 13:41) and &#39;17122.zip&#39; (23.10.2023 07:41). The &#39;Dateiname:&#39; (File name:) field is pre-filled with &#39;19239.zip&#39;, and &#39;Dateityp:&#39; (File type:) is &#39;WinRAR-ZIP-Archiv (*.zip)&#39;. The bottom portion displays a &#39;Completed&#39; task box. It shows &#39;Task ID: 8337912519&#39;, with a &#39;Start date: 26.10.2023 07.11&#39; and &#39;End date: 28.10.2023 04.37&#39;. The task description reads: &#39;Urban Atlas Land Cover/Land Use 2018 (vector), Europe, 6-yearly - Pre-packaged&#39;. A &#39;Download file (44.9 MB) | Expires in 1 days&#39; link is also visible, indicating that the completed task involves a downloadable data product." />

<span id="_Ref151987915" class="anchor"></span>**Figure 3‑18: Add
Ingestion - Step 3 (Get download link via the portal and via email)**

For the vector file, the Attribute Name from the dataset (column from
the attribute table) which shall be used as Input Parameter for the
Class Code needs to be entered (see [Figure 3‑16](#_Ref151987739) and
[Figure 3‑17](#_Ref151987899)), for the raster dataset this is not
required as raster dataset usually consists of one band only. Please
select an integer field (the code and not its description). In general,
strings also work as long as they do not have any special characters.
Allowed: digits, upper-lower case, hyphen, underscore. In this case (see
[Figure 3‑19](#_Ref151987951)), we chose ‘code_2018’.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image84.png"
style="width:5.61979in;height:3.06462in"
data-fig-alt="The table displays attribute data for geospatial features from the dataset &#39;AT005L3_INNSBRUCK_UA2018_v012&#39;. The header indicates &#39;Features Total: 12068, Filtered: 12068, Selected: 0&#39;. | fid | country | fua_name | fua_code | code_2018 | class_2018 | prod_date | |---|---|---|---|---|---|---| | 1 | AT | Innsbruck | AT005L3 | 11210 | Discontinuous urban fabric | 2020-08 | | 2 | AT | Innsbruck | AT005L3 | 14200 | Sports and leisure facilities | 2020-08 | | 3 | AT | Innsbruck | AT005L3 | 11210 | Discontinuous urban fabric | 2020-08 | | 4 | AT | Innsbruck | AT005L3 | 11210 | Discontinuous urban fabric | 2020-08 | | 5 | AT | Innsbruck | AT005L3 | 13400 | Land without current use | 2020-08 | | 6 | AT | Innsbruck | AT005L3 | 11220 | Discontinuous medium density urban fabric | 2020-08 | | 7 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 | | 8 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 | | 9 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 | | 10 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 | | 11 | AT | Innsbruck | AT005L3 | 11240 | Discontinuous very low density urban fabric | 2020-08 | The table provides a sample of 11 records from the Urban Atlas 2018 dataset for Innsbruck, Austria, showing feature IDs, country code (AT for Austria), Functional Urban Area (FUA) name and code, the specific 2018 land use/land cover code and its descriptive class, and the production date of the data (2020-08). The most frequent land cover classes in this sample are &#39;Discontinuous urban fabric&#39; and &#39;Industrial, commercial and transport units&#39;." />

The table displays attribute data for geospatial features from the
dataset “AT005L3_INNSBRUCK_UA2018_v012”. The header indicates “Features
Total: 12068, Filtered: 12068, Selected: 0”.

| fid | country | fua_name | fua_code | code_2018 | class_2018 | prod_date |
|----|----|----|----|----|----|----|
| 1 | AT | Innsbruck | AT005L3 | 11210 | Discontinuous urban fabric | 2020-08 |
| 2 | AT | Innsbruck | AT005L3 | 14200 | Sports and leisure facilities | 2020-08 |
| 3 | AT | Innsbruck | AT005L3 | 11210 | Discontinuous urban fabric | 2020-08 |
| 4 | AT | Innsbruck | AT005L3 | 11210 | Discontinuous urban fabric | 2020-08 |
| 5 | AT | Innsbruck | AT005L3 | 13400 | Land without current use | 2020-08 |
| 6 | AT | Innsbruck | AT005L3 | 11220 | Discontinuous medium density urban fabric | 2020-08 |
| 7 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 |
| 8 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 |
| 9 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 |
| 10 | AT | Innsbruck | AT005L3 | 12100 | Industrial, commercial and transport units | 2020-08 |
| 11 | AT | Innsbruck | AT005L3 | 11240 | Discontinuous very low density urban fabric | 2020-08 |

The table provides a sample of 11 records from the Urban Atlas 2018
dataset for Innsbruck, Austria, showing feature IDs, country code (AT
for Austria), Functional Urban Area (FUA) name and code, the specific
2018 land use/land cover code and its descriptive class, and the
production date of the data (2020-08). The most frequent land cover
classes in this sample are “Discontinuous urban fabric” and “Industrial,
commercial and transport units”.

<span id="_Ref151987951" class="anchor"></span>**Figure 3‑19: Add
Ingestion - Step 3 (Enter Attribute Name from the dataset (column from
the attribute table) which shall be used as Input Parameter for the
Class Code needs to be entered). Here: code_2018**

After selecting the dataset, you need to define if the dataset has
discrete or continuous values[^9]. F**or vector data currently only
discrete values are specified**. In this case, the Urban Atlas consists
of discrete values indicating the degree of its according
characteristic.

In step 4, you have the possibility to **exclude a class code** from
being processed (see [Figure 3‑20](#_Ref151988050)). It excludes all
class codes which stand for an unknown classification (i.e. NoData
values). If a TIF dataset specifies a NoData value in its metadata the
corresponding class is excluded automatically. This is recommended if
you don’t want to have specific values in the statistics/being processed
and for all unclassified/unknown values (i.e. NoData) (step 4). All
pixels in the ingested dataset with an excluded class code will then
appear as NoData pixel in the final Ingestion. If you do not enter a
excluded class code value and the NoData value does not appear in the
TIF metadata, then all classes are “0” in the ingestion, where the
original data always displayed the no-data class.

Please press enter after entering the value. Alternatively, for discrete
datasets, you are able to hide the values when editing the data (section
[3.7](#edit-ingestion) [Figure 3‑35](#_Ref100162670)) by disabling
single classes with the “eye” symbol before ingesting and publishing an
Ingestion.

Additionally, you can **enter a layer name** (see [Figure
3‑20](#_Ref151988050)) which shall be used to generate input classes if
there are <u>more than one layers per</u> dataset (if several layers are
stored in a .gdb for example). If nothing is defined, the first layer
will be selected. In this case, we have three layers and we need the
first one. We write ‘AT005L3_INNSBRUCK_UA2018’ but the first layer would
be selected by default anyways.

**Please make sure to avoid special characters, otherwise an error will
occur.** Please also refer to section 3.3 to learn about the
**limitations of data uploads**.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image86.JPG"
style="width:3.48696in;height:3.63788in"
data-fig-alt="A screenshot of a user interface for the &#39;Add Ingestion&#39; process, specifically depicting &#39;Step 2 &#39;Dataset Selection Upload Dataset - Vector&#39;&#39;. The previous step, &#39;1 Input Type Selection&#39;, is greyed out. The interface presents instructions for &#39;Parameter for the Class Code&#39;, stating that &#39;Values of the selected attribute column must only contain upper- and lower-case letters, numbers, underscores or hyphens.&#39; An &#39;Excluded Value&#39; field is shown, with an explanation that these values, representing non-thematic data, will be counted as &#39;NoData&#39; during ingestion, and that NoData values specified in a TIF dataset&#39;s metadata are automatically excluded. A &#39;Layer Name&#39; field contains the pre-filled value &#39;AT005L3_INNSBRUCK_UA2018&#39; and an instruction to &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; A large dashed-line area indicates a &#39;Drag and Drop&#39; option for files, or users can click an &#39;UPLOAD DOCUMENT/S&#39; button with an arrow-up icon. Below the upload area, a note explains that &#39;All documents that help to understand the content, including legend files which will be used to automatically create Input Classes and metadata files which will be used to automatically prefill the data description. (No file type restrictions)&#39; are to be uploaded. A checkbox labelled &#39;Delete raw data&#39; is present, accompanied by a question mark icon for help. At the bottom of the interface, three action buttons are displayed: &#39;CANCEL&#39;, &#39;BACK&#39;, and &#39;ADD&#39;." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image85.png"
style="width:3.51389in;height:1.10364in"
data-fig-alt="This is a screenshot of a &#39;Select Vector Layers to Add...&#39; dialog box, showing a list of vector layers available for selection. The dialog displays a table with four columns: &#39;Layer ID&#39;, &#39;Layer name&#39;, &#39;Number of features&#39;, and &#39;Geometry type&#39;. The &#39;Description&#39; column is present but empty for all listed layers. Three specific vector layers related to the Copernicus Land Monitoring Service (CLMS) Urban Atlas 2018 (UA2018) data for Innsbruck (AT005L3) are listed: * Layer ID 0: &#39;AT005L3_INNSBRUCK_UA2018&#39; with 12068 features, geometry type &#39;MultiPolygon&#39;. This layer is currently highlighted. * Layer ID 1: &#39;AT005L3_INNSBRUCK_UA2018_Boundary&#39; with 1 feature, geometry type &#39;MultiPolygon&#39;. * Layer ID 2: &#39;AT005L3_INNSBRUCK_UA2018_UrbanCore&#39; with 1 feature, geometry type &#39;MultiPolygon&#39;. At the bottom of the dialog, there are interactive elements including &#39;OK&#39;, &#39;Select All&#39;, and &#39;Cancel&#39; buttons, as well as a checkbox labeled &#39;Add layers to a group&#39;. The dialog title is preceded by a green &#39;Q&#39; icon, indicative of a Geographic Information System (GIS) application. This interface is part of a data ingestion process for uploading spatial data." />

<span id="_Ref151988050" class="anchor"></span>**Figure 3‑20: Add
Ingestion - Step 4 (exclude values and enter layer name)**

The fifth step provides the possibility to upload **additional,
supporting files** that help to understand the content, such as the
metadata files (see [Figure 3‑22](#_Ref151988218)), legend files (see
[Figure 3‑21](#_Ref151988076)) QGIS layer style file (.qml) or SLD
(Styled Layer Descriptor) file (.sld); ArcGIS Layer Files (.lyr) are not
supported), EAGLE Barcoding files (see [Figure 3‑23](#_Ref151988308)).
These additional files will be used prefill the data descriptions and
define the EAGLE barcodes and the style to the Ingestion Classes (step
5). The upload of these documents can also be performed at a later stage
(section [3.7](#edit-ingestion)) and is possible via the explorer or per
“drag and drop”.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image88.JPG"
style="width:3.9913in;height:4.16922in"
data-fig-alt="This screenshot illustrates the &#39;Add Ingestion&#39; process, specifically &#39;Step 2: &#39;Dataset Selection Upload Dataset - Vector&#39;&#39;. &#39;Step 1: Input Type Selection&#39; is greyed out, indicating it&#39;s a previous step. The interface presents a section for &#39;Excluded value&#39; with text explaining that &#39;values which do not represent thematic values in the input dataset&#39; will be counted as NoData, and if a TIF dataset specifies a NoData value in its metadata, it is automatically excluded. A &#39;Layer Name&#39; input field is present, pre-filled with &#39;AT005L3_INNSBRUCK_UA2018&#39;, instructing the user to &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; Below this is a &#39;Drag and Drop&#39; area or an &#39;UPLOAD DOCUMENT/S&#39; button for file uploads. Supplemental text states: &#39;All documents that help to understand the content, including legend files which will be used to automatically create Input Classes and metadata files which will be used to automatically prefill the data description. (No file type restrictions)&#39;. Three linked documents are visible: &#39;Urban_Atlas_2018_EAGLE_Barcoding_Template_3.1.2_23.12.2021_v3.xlsx&#39;, &#39;AT005L3_INNSBRUCK_UA2018_v013.xml&#39;, and &#39;Urban_Atlas_2018_Legend.sld&#39;. A checkbox option to &#39;Delete raw data&#39; is provided. At the bottom, there are &#39;CANCEL&#39;, &#39;BACK&#39;, and &#39;ADD&#39; action buttons." />

This screenshot illustrates the “Add Ingestion” process, specifically
“Step 2: ‘Dataset Selection Upload Dataset - Vector’”. “Step 1: Input
Type Selection” is greyed out, indicating it’s a previous step. The
interface presents a section for “Excluded value” with text explaining
that “values which do not represent thematic values in the input
dataset” will be counted as NoData, and if a TIF dataset specifies a
NoData value in its metadata, it is automatically excluded. A “Layer
Name” input field is present, pre-filled with
“AT005L3_INNSBRUCK_UA2018”, instructing the user to “Enter Layer Name
from Dataset which shall be used to generate Input Classes.” Below this
is a “Drag and Drop” area or an “UPLOAD DOCUMENT/S” button for file
uploads. Supplemental text states: “All documents that help to
understand the content, including legend files which will be used to
automatically create Input Classes and metadata files which will be used
to automatically prefill the data description. (No file type
restrictions)”. Three linked documents are visible:
“Urban_Atlas_2018_EAGLE_Barcoding_Template_3.1.2_23.12.2021_v3.xlsx”,
“AT005L3_INNSBRUCK_UA2018_v013.xml”, and “Urban_Atlas_2018_Legend.sld”.
A checkbox option to “Delete raw data” is provided. At the bottom, there
are “CANCEL”, “BACK”, and “ADD” action buttons.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image87.png"
style="width:3.77729in;height:1.67917in"
data-fig-alt="Screenshot of a file selection dialog from a data ingestion process, showing the user navigating to and selecting a legend file for an Urban Atlas (UA) 2018 dataset. The file path displayed is &#39;UrbanAtlas2018 &gt; AT005L3_INNSBRUCK_UA2018_v012 &gt; Legend&#39;. The dialog presents a list of files with column headers &#39;Name&#39;, &#39;Änderungsdatum&#39; (Modification date), and &#39;Typ&#39; (Type). Three files with the name &#39;Urban_Atlas_2018_Legend&#39; are listed: 1. Type: &#39;ArcGIS Layer&#39;, Modification date: &#39;23.06.2020 14:27&#39; 2. Type: &#39;QGIS Layer Settings&#39;, Modification date: &#39;24.03.2020 16:57&#39; 3. Type: &#39;SLD-Datei&#39; (Styled Layer Descriptor file), Modification date: &#39;24.03.2020 16:58&#39;. This file is highlighted, indicating it is selected. The &#39;Dateiname&#39; (Filename) input field at the bottom shows &#39;Urban_Atlas_2018_Legend.sld&#39;. The buttons &#39;Alle Dateien&#39; (All Files) and &#39;Öffnen&#39; (Open) are visible. This step is part of the &#39;Add Ingestion - Step 3&#39; process, likely for configuring how data attributes are mapped to class codes for styling, as indicated by the selection of a Styled Layer Descriptor (SLD) file." />

Screenshot of a file selection dialog from a data ingestion process,
showing the user navigating to and selecting a legend file for an Urban
Atlas (UA) 2018 dataset. The file path displayed is “UrbanAtlas2018 \>
AT005L3_INNSBRUCK_UA2018_v012 \> Legend”. The dialog presents a list of
files with column headers “Name”, “Änderungsdatum” (Modification date),
and “Typ” (Type). Three files with the name “Urban_Atlas_2018_Legend”
are listed: 1. Type: “ArcGIS Layer”, Modification date: “23.06.2020
14:27” 2. Type: “QGIS Layer Settings”, Modification date: “24.03.2020
16:57” 3. Type: “SLD-Datei” (Styled Layer Descriptor file), Modification
date: “24.03.2020 16:58”. This file is highlighted, indicating it is
selected. The “Dateiname” (Filename) input field at the bottom shows
“Urban_Atlas_2018_Legend.sld”. The buttons “Alle Dateien” (All Files)
and “Öffnen” (Open) are visible. This step is part of the “Add
Ingestion - Step 3” process, likely for configuring how data attributes
are mapped to class codes for styling, as indicated by the selection of
a Styled Layer Descriptor (SLD) file.

<span id="_Ref151988076" class="anchor"></span>**Figure 3‑21: Add
Ingestion - Step 5 (upload additional datasets (i.e. legend / style
file))**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image88.JPG"
style="width:3.96522in;height:4.14197in"
data-fig-alt="This screenshot illustrates the &#39;Add Ingestion&#39; process, specifically &#39;Step 2: &#39;Dataset Selection Upload Dataset - Vector&#39;&#39;. &#39;Step 1: Input Type Selection&#39; is greyed out, indicating it&#39;s a previous step. The interface presents a section for &#39;Excluded value&#39; with text explaining that &#39;values which do not represent thematic values in the input dataset&#39; will be counted as NoData, and if a TIF dataset specifies a NoData value in its metadata, it is automatically excluded. A &#39;Layer Name&#39; input field is present, pre-filled with &#39;AT005L3_INNSBRUCK_UA2018&#39;, instructing the user to &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; Below this is a &#39;Drag and Drop&#39; area or an &#39;UPLOAD DOCUMENT/S&#39; button for file uploads. Supplemental text states: &#39;All documents that help to understand the content, including legend files which will be used to automatically create Input Classes and metadata files which will be used to automatically prefill the data description. (No file type restrictions)&#39;. Three linked documents are visible: &#39;Urban_Atlas_2018_EAGLE_Barcoding_Template_3.1.2_23.12.2021_v3.xlsx&#39;, &#39;AT005L3_INNSBRUCK_UA2018_v013.xml&#39;, and &#39;Urban_Atlas_2018_Legend.sld&#39;. A checkbox option to &#39;Delete raw data&#39; is provided. At the bottom, there are &#39;CANCEL&#39;, &#39;BACK&#39;, and &#39;ADD&#39; action buttons." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image89.png"
style="width:3.2583in;height:1.45208in"
data-fig-alt="Screenshot of a file selection dialog showing the selection of a metadata file. The navigation path indicates the user is in &#39;UrbanAtlas2018 &gt; AT005L3_INNSBRUCK_UA2018_v012 &gt; Metadata&#39;. A file named &#39;AT005L3_INNSBRUCK_UA2018_v012&#39; is highlighted, showing an &#39;Änderungsdatum&#39; (Modification Date) of &#39;15.01.2021 14:48&#39; and a &#39;Typ&#39; (Type) of &#39;XML-Datei&#39; (XML-File). The &#39;Dateiname:&#39; (Filename:) input field at the bottom displays &#39;AT005L3_INNSBRUCK_UA2018_v012&#39;. Buttons for &#39;Alle Dateien&#39; (All Files) and &#39;Öffnen&#39; (Open) are visible. This screenshot appears in the context of an &#39;Add Ingestion - Step 3&#39; process, relating to selecting an attribute name for a class code, as per the surrounding documentation." />

<span id="_Ref151988218" class="anchor"></span>**Figure 3‑22: Add
Ingestion - Step 5 (upload additional datasets (i.e. Metadata file))**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image88.JPG"
style="width:4.31132in;height:4.5035in"
data-fig-alt="This screenshot illustrates the &#39;Add Ingestion&#39; process, specifically &#39;Step 2: &#39;Dataset Selection Upload Dataset - Vector&#39;&#39;. &#39;Step 1: Input Type Selection&#39; is greyed out, indicating it&#39;s a previous step. The interface presents a section for &#39;Excluded value&#39; with text explaining that &#39;values which do not represent thematic values in the input dataset&#39; will be counted as NoData, and if a TIF dataset specifies a NoData value in its metadata, it is automatically excluded. A &#39;Layer Name&#39; input field is present, pre-filled with &#39;AT005L3_INNSBRUCK_UA2018&#39;, instructing the user to &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; Below this is a &#39;Drag and Drop&#39; area or an &#39;UPLOAD DOCUMENT/S&#39; button for file uploads. Supplemental text states: &#39;All documents that help to understand the content, including legend files which will be used to automatically create Input Classes and metadata files which will be used to automatically prefill the data description. (No file type restrictions)&#39;. Three linked documents are visible: &#39;Urban_Atlas_2018_EAGLE_Barcoding_Template_3.1.2_23.12.2021_v3.xlsx&#39;, &#39;AT005L3_INNSBRUCK_UA2018_v013.xml&#39;, and &#39;Urban_Atlas_2018_Legend.sld&#39;. A checkbox option to &#39;Delete raw data&#39; is provided. At the bottom, there are &#39;CANCEL&#39;, &#39;BACK&#39;, and &#39;ADD&#39; action buttons." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image90.png"
style="width:3.21214in;height:1.4in"
data-fig-alt="A screenshot of a file selection dialog within a software application, showing files related to EAGLE Mapping (BarCoding) templates. The breadcrumb path shows &#39;D3.2.1 - Demonstration and docume...&#39; and &#39;EAGLE Mapping (BarCoding)&#39;. The dialog displays a file list with &#39;Name&#39;, &#39;Änderungsdatum&#39; (Modification Date), and &#39;Typ&#39; (Type) columns. The listed files are: * &#39;Riparian_Zones_2018_EAGLE Barcoding Template_3...&#39; (Microsoft Excel file, modified 21.03.2022 15:15). * &#39;SIOSE_LC_EAGLE Barcoding Template_3.1.2_23.12.2...&#39; (Microsoft Excel file, modified 21.03.2022 16:54). * &#39;SIOSE_LU_EAGLE Barcoding Template_3.1.2_23.12.2...&#39; (Microsoft Excel file, modified 21.03.2022 16:54). * &#39;Urban_Atlas_2018_EAGLE Barcoding Template_3.1...&#39; (Microsoft Excel file, modified 10.03.2022 15:57). The file &#39;Urban_Atlas_2018_EAGLE Barcoding Template_3.1...&#39; is highlighted, and its full name, &#39;Urban_Atlas_2018_EAGLE Barcoding Template_3.1.2_23.12.2021_v1&#39;, is shown in the &#39;Dateiname&#39; (Filename) input field. The dialog also contains an &#39;Alle Dateien&#39; (All Files) filter and an &#39;Öffnen&#39; (Open) button. This interface is used for selecting dataset input parameters for class codes during data ingestion." />

<span id="_Ref151988308" class="anchor"></span>**Figure 3‑23: Add
Ingestion - Step 5 (upload additional datasets (i.e. EAGLE barcoding
file))**

The last option allows you to specify whether the **raw data** (original
uploaded dataset) can be retained in the system after processing (see
[Figure 3‑24](#_Ref151988324)). The “Delete raw data” tick box is not
ticked by default. If the “delete raw data” is ticked the initial
dataset will be deleted after the creation of the Ingestion from the
CLC+ Core storage. The raw data will only usable for users of the same
organization and the admin user - and only if the Ingestion processing
fails and the failed Ingestion needs to be processed (retry) again.
Otherwise retrying a failed Ingestion processing step will not be
possible and a completely new Ingestion would need to be initiated.
After an Ingestion was successful the raw dataset is not needed anymore.
Note that no user can access the raw data in the CLC+ Cores data
storage.

As soon as the processing step is finished, the raw data cannot be
downloaded or reused anymore by anyone. Finally, if you have everything
defined, the dataset can be added by pressing the ‘ADD’ button (see
[Figure 3‑24](#_Ref151988324)). While the upload is performed, please do
not leave the page.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image91.png"
style="width:4.20427in;height:3.21475in"
data-fig-alt="This screenshot displays the &#39;Add Ingestion&#39; user interface, specifically Step 4, titled &#39;Dataset Selection &#39;Upload Dataset - Vector&#39;&#39;. The workflow steps &#39;1 Input Type Selection&#39; (greyed out) and &#39;2 Dataset Selection &#39;Upload Dataset - Vector&#39;&#39; (highlighted green) are visible at the top. The main section shows a &#39;Layer Name&#39; input field pre-filled with &#39;AT005L3_INNSBRUCK_UA2018&#39;. A descriptive hint states: &#39;Enter Layer Name from Dataset which shall be used to generate Input Classes.&#39; Below this, an &#39;Upload Document/s&#39; button is present. Further text explains: &#39;All documents that help to understand the content, including legend files which will be used to automatically create Input Classes and metadata files which will be used to automatically prefill the data description.&#39; Three uploaded files are listed: &#39;Urban_Atlas_2018_Legend.sld&#39;, &#39;AT005L3_INNSBRUCK_UA2018_v012.xml&#39;, and &#39;Urban_Atlas_2018_EAGLE Barcoding Template_3.1.2_23.12.2021_v1.xlsx&#39;. A checkbox option to &#39;Delete raw data&#39; is also visible. Navigation buttons &#39;CANCEL&#39;, &#39;BACK&#39;, and &#39;ADD&#39; are positioned at the bottom." />

This screenshot displays the “Add Ingestion” user interface,
specifically Step 4, titled “Dataset Selection ‘Upload Dataset -
Vector’”. The workflow steps “1 Input Type Selection” (greyed out) and
“2 Dataset Selection ‘Upload Dataset - Vector’” (highlighted green) are
visible at the top. The main section shows a “Layer Name” input field
pre-filled with “AT005L3_INNSBRUCK_UA2018”. A descriptive hint states:
“Enter Layer Name from Dataset which shall be used to generate Input
Classes.” Below this, an “Upload Document/s” button is present. Further
text explains: “All documents that help to understand the content,
including legend files which will be used to automatically create Input
Classes and metadata files which will be used to automatically prefill
the data description.” Three uploaded files are listed:
“Urban_Atlas_2018_Legend.sld”, “AT005L3_INNSBRUCK_UA2018_v012.xml”, and
“Urban_Atlas_2018_EAGLE Barcoding Template_3.1.2_23.12.2021_v1.xlsx”. A
checkbox option to “Delete raw data” is also visible. Navigation buttons
“CANCEL”, “BACK”, and “ADD” are positioned at the bottom.

<span id="_Ref151988324" class="anchor"></span>**Figure 3‑24: Add
Ingestion - Step 6 (start the upload)**

## Remarks on the Ingestion process

Usually, a dataset consists of one file / layer. There is no problem in
uploading a single dataset to the system. However, currently there is no
option to upload more than one file from a common folder, a gdb or
gpkg). In such a case, either you indicate the desired file in the
dialogue under ‘layer name’ or the first file in the folder will be
selected automatically for the Ingestion.

In case your data is split into several sub-tiles, such as Urban Atlas
or Riparian Zones, you have 3 possibilities to upload your data in the
system:

- Use the direct download URL from the CLMS portal – **recommended**

- Extract the required layer from GDB / GPKG and merge data into one
  dataset in a GIS software **outside the system** (might not be
  possible due to the size)

- Ingest single datasets (i.e. start the Ingestion process for each
  single file)

For datasets (i.e. gdb, gpkg) that consist of more than one layer (per
file), you need to specify the layer name which shall be used to
generate input classes in the field ‘layer name’. If no specific file is
defined, the first layer will be selected. In the example below we have
three layers in the dataset we want to ingest. For selecting the first
one, we can define ‘AT005L3_INNSBRUCK_UA2018’ under ‘layer name’ or we
skip it as the first layer would be selected by default anyways.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image85.png"
style="width:3.51389in;height:1.10347in"
data-fig-alt="This is a screenshot of a &#39;Select Vector Layers to Add...&#39; dialog box, showing a list of vector layers available for selection. The dialog displays a table with four columns: &#39;Layer ID&#39;, &#39;Layer name&#39;, &#39;Number of features&#39;, and &#39;Geometry type&#39;. The &#39;Description&#39; column is present but empty for all listed layers. Three specific vector layers related to the Copernicus Land Monitoring Service (CLMS) Urban Atlas 2018 (UA2018) data for Innsbruck (AT005L3) are listed: * Layer ID 0: &#39;AT005L3_INNSBRUCK_UA2018&#39; with 12068 features, geometry type &#39;MultiPolygon&#39;. This layer is currently highlighted. * Layer ID 1: &#39;AT005L3_INNSBRUCK_UA2018_Boundary&#39; with 1 feature, geometry type &#39;MultiPolygon&#39;. * Layer ID 2: &#39;AT005L3_INNSBRUCK_UA2018_UrbanCore&#39; with 1 feature, geometry type &#39;MultiPolygon&#39;. At the bottom of the dialog, there are interactive elements including &#39;OK&#39;, &#39;Select All&#39;, and &#39;Cancel&#39; buttons, as well as a checkbox labeled &#39;Add layers to a group&#39;. The dialog title is preceded by a green &#39;Q&#39; icon, indicative of a Geographic Information System (GIS) application. This interface is part of a data ingestion process for uploading spatial data." />

This is a screenshot of a “Select Vector Layers to Add…” dialog box,
showing a list of vector layers available for selection. The dialog
displays a table with four columns: “Layer ID”, “Layer name”, “Number of
features”, and “Geometry type”. The “Description” column is present but
empty for all listed layers.

Three specific vector layers related to the Copernicus Land Monitoring
Service (CLMS) Urban Atlas 2018 (UA2018) data for Innsbruck (AT005L3)
are listed: \* Layer ID 0: “AT005L3_INNSBRUCK_UA2018” with 12068
features, geometry type “MultiPolygon”. This layer is currently
highlighted. \* Layer ID 1: “AT005L3_INNSBRUCK_UA2018_Boundary” with 1
feature, geometry type “MultiPolygon”. \* Layer ID 2:
“AT005L3_INNSBRUCK_UA2018_UrbanCore” with 1 feature, geometry type
“MultiPolygon”.

At the bottom of the dialog, there are interactive elements including
“OK”, “Select All”, and “Cancel” buttons, as well as a checkbox labeled
“Add layers to a group”. The dialog title is preceded by a green “Q”
icon, indicative of a Geographic Information System (GIS) application.
This interface is part of a data ingestion process for uploading spatial
data.

If your required layer is not on the first position of your
folder/gdb/gpkg and in addition the layers of different regions are
named differently (SAR_13_T_USOS vs. SAR_15_T_USOS), you have 2
possibilities to upload your data in the system:

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image92.png"
style="width:2.92515in;height:1.56818in"
data-fig-alt="This table displays a list of available vector layers for selection in a user interface titled &#39;Select Vector Layers to Add...&#39;. The table has five columns: &#39;Layer ID&#39;, &#39;Layer name&#39;, &#39;Number of features&#39;, &#39;Geometry type&#39;, and &#39;Description&#39;. | Layer ID | Layer name | Number of features | Geometry type | Description | | :------- | :------------------ | :----------------- | :------------ | :---------- | | 2 | LISTADO_ATRIBUTOS | 20 | None | | | 3 | LISTADO_COBERTURAS | 62 | None | | | 1 | LISTADO_USOS | 87 | None | | | 0 | SAR_13_TABLA_PLANA | 9445 | None | | | 5 | SAR_13_T_COMBINADA | 981049 | MultiPolygon | | | 6 | SAR_13_T_POLIGONOS | 1963199 | MultiPolygon | | | 7 | SAR_13_T_USOS | 844040 | MultiPolygon | | | 4 | SAR_13_T_VALORES | 2455265 | None | | The &#39;Geometry type&#39; column indicates whether a layer consists of MultiPolygon features or &#39;None&#39; (implying tabular or non-spatial data). Layers with &#39;SAR_13&#39; in their name, such as &#39;SAR_13_T_POLIGONOS&#39;, &#39;SAR_13_T_COMBINADA&#39;, and &#39;SAR_13_T_USOS&#39;, are MultiPolygon geometry types and contain a large number of features, with &#39;SAR_13_T_POLIGONOS&#39; having the most at 1,963,199 features. Layers like &#39;LISTADO_ATRIBUTOS&#39; (List of Attributes), &#39;LISTADO_COBERTURAS&#39; (List of Coverages), and &#39;LISTADO_USOS&#39; (List of Uses) have fewer features and a geometry type of &#39;None&#39;." />
<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image93.png"
style="width:2.80162in;height:1.54016in"
data-fig-alt="A screenshot of a user interface dialog box titled &#39;Select Vector Layers to Add...&#39;. The dialog displays a table with five columns: &#39;Layer ID&#39;, &#39;Layer name&#39;, &#39;Number of features&#39;, &#39;Geometry type&#39;, and &#39;Description&#39;. Six vector layers are listed: - Layer ID 2: LISTADO_ATRIBUTOS, Number of features: 21, Geometry type: None. - Layer ID 0: LISTADO_COBERTURAS, Number of features: 65, Geometry type: None. - Layer ID 1: LISTADO_USOS, Number of features: 86, Geometry type: None. - Layer ID 5: SAR_15_T_COMBINADA, Number of features: 979728, Geometry type: MultiPolygon. - Layer ID 3: SAR_15_T_POLIGONOS, Number of features: 2417938, Geometry type: MultiPolygon. - Layer ID 4: SAR_15_T_USOS, Number of features: 1816094, Geometry type: MultiPolygon. All &#39;Description&#39; fields are empty. The bottom of the dialog contains buttons: &#39;OK&#39;, &#39;Select All&#39;, and &#39;Cancel&#39;. There is also an unchecked checkbox labeled &#39;Add layers to a group&#39; positioned between &#39;Select All&#39; and &#39;Cancel&#39; buttons. The &#39;LISTADO&#39; layers likely represent attribute or classification tables, while the &#39;SAR_15_T&#39; layers represent spatial vector data derived from Synthetic Aperture Radar (SAR) imagery, possibly at 15m resolution, related to land cover and land use." />

- Extract the required layer from GDB / GPKG and merge data into one
  dataset in a GIS software **outside the system** (might be not
  possible due to the size)

- Ingest single datasets (means several single files in the system)

## Retry or Delete

If for some reason the upload was not successful, you have the option of
uploading the data set again (retry). For your convenience, all fields
remain filled in and the data (if the checkbox 'delete raw data' has not
been ticked) is retained. There is also the option to change data or
fields, e.g. if you have found an error.

If you have tried to upload the dataset by mistake, you can delete the
entry.

Both options can be initiated by right clicking on the Ingestion for
which the upload failed (see [Figure 3‑25](#_Ref151988719)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image95.png"
style="width:6.925in;height:3.24514in"
data-fig-alt="A table from the EAGLE Data Catalogue displaying a list of Copernicus Land Monitoring Service (CLMS) datasets with associated metadata. The table shows 10 entries out of 32 total, spanning from item 11 to 20. The table columns are: | EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | |---|---|---|---|---|---|---|---|---|---|---|---| | | HRL - Grassland 2018 | Dataset | 10.03.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.03.2018 - 31.10.2018 | CLC, European Environment Agency | copernicus@eea.europa.eu | PUBLISHED | | | HRL - Impervious Built-up 2018 | Dataset | 09.03.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2017 - 31.12.2019 | CLC, European Environment Agency | copernicus.land@eea.europa.eu | PUBLISHED | | | N2K 2012 | Dataset | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2012 | 07.04.2010 - 06.08.2015 | CLC, European Environment Agency | copernicus@eea.europa.eu | PUBLISHED | | | Riparian Zones (RZ) 2012 | Dataset | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2012 | 14.07.2011 - 25.09.2014 | CLC, European Environment Agency | mpalacios@indra.es | PUBLISHED | | | Urban Atlas (UA) 2012 | Dataset | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2012 | 24.03.2011 - 15.09.2013 | CLC, European Environment Agency | Matteo.Mattiuzzi@eea.europa.eu | PUBLISHED | | | UrbanAtlas_IBK_2018 | Dataset | 21.11.2023 | CLC+ Core User Admin/Support | Austria/Österreich | Innsbruck | - | - | CLC, European Environment Agency | [unreadable] | UPLOAD FAILED | | | CLC+ Backbone (2018) | Dataset | 05.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.07.2017 - 30.06.2019 | CLC, European Environment Agency | copernicus@eea.europa.eu | USED | | | Coastal Zones (CZ) 2018 | Dataset | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2017 - 31.12.2019 | CLC, European Environment Agency | info@eea.europa.eu | USED | | | Corine Land Cover (CLC) 2018 | Dataset | 06.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2017 - 31.12.2018 | CLC, European Environment Agency | [unreadable] | USED | | | Effis 2018 | Dataset | 05.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2018 - 31.12.2018 | CLC, European Environment Agency | [unreadable] | USED | The table entries primarily consist of Copernicus Land Monitoring Service (CLMS) products such as High Resolution Layers (HRL) for Grassland and Impervious Built-up, Natura 2000 (N2K) data, Riparian Zones (RZ), Urban Atlas (UA), CLC+ Backbone, Coastal Zones (CZ), and CORINE Land Cover (CLC). Most datasets are associated with the European Environment Agency (EEA) and have a &#39;PUBLISHED&#39; or &#39;USED&#39; status. One entry, &#39;UrbanAtlas_IBK_2018&#39; for Austria/Innsbruck, shows an &#39;UPLOAD FAILED&#39; status with options to &#39;Retry&#39; or &#39;Delete&#39; in a dropdown menu." />

A table from the EAGLE Data Catalogue displaying a list of Copernicus
Land Monitoring Service (CLMS) datasets with associated metadata. The
table shows 10 entries out of 32 total, spanning from item 11 to 20.

The table columns are: \| EAGLE Approved \| Name \| Type \| Created At
\| Created By \| Country \| Region \| Reference Year \| Time Range \|
Organisation/s \| Contact Person \| Status \|
\|—\|—\|—\|—\|—\|—\|—\|—\|—\|—\|—\|—\| \| \| HRL - Grassland 2018 \|
Dataset \| 10.03.2023 \| CLC+ Core User Admin/Support \| European
Environment Agency \| \| 2018 \| 01.03.2018 - 31.10.2018 \| CLC,
European Environment Agency \| copernicus@eea.europa.eu \| PUBLISHED \|
\| \| HRL - Impervious Built-up 2018 \| Dataset \| 09.03.2023 \| CLC+
Core User Admin/Support \| European Environment Agency \| \| 2018 \|
01.01.2017 - 31.12.2019 \| CLC, European Environment Agency \|
copernicus.land@eea.europa.eu \| PUBLISHED \| \| \| N2K 2012 \| Dataset
\| 21.06.2023 \| CLC+ Core User Admin/Support \| European Environment
Agency \| \| 2012 \| 07.04.2010 - 06.08.2015 \| CLC, European
Environment Agency \| copernicus@eea.europa.eu \| PUBLISHED \| \| \|
Riparian Zones (RZ) 2012 \| Dataset \| 21.06.2023 \| CLC+ Core User
Admin/Support \| European Environment Agency \| \| 2012 \| 14.07.2011 -
25.09.2014 \| CLC, European Environment Agency \| mpalacios@indra.es \|
PUBLISHED \| \| \| Urban Atlas (UA) 2012 \| Dataset \| 21.06.2023 \|
CLC+ Core User Admin/Support \| European Environment Agency \| \| 2012
\| 24.03.2011 - 15.09.2013 \| CLC, European Environment Agency \|
Matteo.Mattiuzzi@eea.europa.eu \| PUBLISHED \| \| \| UrbanAtlas_IBK_2018
\| Dataset \| 21.11.2023 \| CLC+ Core User Admin/Support \|
Austria/Österreich \| Innsbruck \| - \| - \| CLC, European Environment
Agency \| \[unreadable\] \| UPLOAD FAILED \| \| \| CLC+ Backbone (2018)
\| Dataset \| 05.09.2023 \| CLC+ Core User Admin/Support \| European
Environment Agency \| \| 2018 \| 01.07.2017 - 30.06.2019 \| CLC,
European Environment Agency \| copernicus@eea.europa.eu \| USED \| \| \|
Coastal Zones (CZ) 2018 \| Dataset \| 21.06.2023 \| CLC+ Core User
Admin/Support \| European Environment Agency \| \| 2018 \| 01.01.2017 -
31.12.2019 \| CLC, European Environment Agency \| info@eea.europa.eu \|
USED \| \| \| Corine Land Cover (CLC) 2018 \| Dataset \| 06.09.2023 \|
CLC+ Core User Admin/Support \| European Environment Agency \| \| 2018
\| 01.01.2017 - 31.12.2018 \| CLC, European Environment Agency \|
\[unreadable\] \| USED \| \| \| Effis 2018 \| Dataset \| 05.09.2023 \|
CLC+ Core User Admin/Support \| European Environment Agency \| \| 2018
\| 01.01.2018 - 31.12.2018 \| CLC, European Environment Agency \|
\[unreadable\] \| USED \|

The table entries primarily consist of Copernicus Land Monitoring
Service (CLMS) products such as High Resolution Layers (HRL) for
Grassland and Impervious Built-up, Natura 2000 (N2K) data, Riparian
Zones (RZ), Urban Atlas (UA), CLC+ Backbone, Coastal Zones (CZ), and
CORINE Land Cover (CLC). Most datasets are associated with the European
Environment Agency (EEA) and have a “PUBLISHED” or “USED” status. One
entry, “UrbanAtlas_IBK_2018” for Austria/Innsbruck, shows an “UPLOAD
FAILED” status with options to “Retry” or “Delete” in a dropdown menu.

<span id="_Ref151988719" class="anchor"></span>**Figure 3‑25: Add
Ingestion – Retry or delete dataset**

Further there is also the possibility to ‘cancel’ and Ingestion while
its uploading or processing (right click on the processing Ingestion see
[Figure 3‑26](#_Ref151988796)), it will then run into an ‘Uploading
Error’ or ‘Processing Error’ (see section
[3.5](#status-of-an-ingestion)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image96.png"
style="width:6.925in;height:3.25139in"
data-fig-alt="This image displays a screenshot of the CLC+ Core User Admin/Support Data Catalogue interface, listing various Copernicus Land Monitoring Service (CLMS) datasets. The interface includes filtering options (&#39;Filter&#39;, &#39;My organisation/s&#39;, &#39;My data&#39;, &#39;Ingestions&#39;, &#39;Extractions&#39;) and buttons for &#39;Add Ingestion&#39; and &#39;Add Extraction&#39;. The table shows 10 entries (out of 32, displaying items 11-20 per page) with the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39; (represented by a file icon for all entries), &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and an unreadable sortable column header (values &#39;L&#39; or &#39;-&#39;). The table content is: | EAGLE Approved | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | ↑ | |:---------------|:--------------------------------------|:--------------|:------------|:-----------------------------|:------------------------------|:----------|:---------------|:------------------------|:------------------------------------|:-------------------------|:------------|:-| | ✓ | HRL - Grassland 2018 | [file icon] | 10.03.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.03.2018 - 31.10.2018 | CLC, European Environment Agency | copernicus@eea.europa... | PUBLISHED | L | | ✓ | HRL - Impervious Built-... | [file icon] | 09.03.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2017 - 31.12.2019 | CLC, European Environment Agency | copernicus.land@... | PUBLISHED | L | | ✓ | N2K 2012 | [file icon] | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2012 | 07.04.2010 - 06.08.2015 | CLC, European Environment Agency | copernicus@eea.europa... | PUBLISHED | L | | ✓ | Riparian Zones (RZ) 20... | [file icon] | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2012 | 14.07.2011 - 25.09.2014 | CLC, European Environment Agency | mpalacios@indra... | PUBLISHED | L | | ✓ | Urban Atlas (UA) 2012 | [file icon] | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2012 | 24.03.2011 - 15.09.2013 | CLC, European Environment Agency | Matteo.Mattiuzzi... | PUBLISHED | L | | | Urban_Atlas-IBK_2018 | [file icon] | 21.11.2023 | CLC+ Core User Admin/Support | Austria/Österreich | Innsbruck | - | - | CLC, European Environment Agency | | PROCESSING | - | | ✓ | CLC+Backbone (2018) | [file icon] | 05.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.07.2017 - 30.06.2019 | CLC, European Environment Agency | | USED | L | | ✓ | Coastal Zones (CZ) 20... | [file icon] | 21.06.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2017 - 31.12.2019 | CLC, European Environment Agency | info@eea.europa... | USED | L | | ✓ | Corine Land Cover (CL... | [file icon] | 06.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2017 - 31.12.2018 | CLC, European Environment Agency | copernicus@eea.europa... | USED | L | | ✓ | Effis 2018 | [file icon] | 05.09.2023 | CLC+ Core User Admin/Support | European Environment Agency | | 2018 | 01.01.2018 - 31.12.2018 | CLC, European Environment Agency | copernicus@eea... | USED | L | The table showcases various land monitoring products from the Copernicus Land Monitoring Service (CLMS), including High Resolution Layers (HRL) for Grassland and Impervious Built-up (likely Imperviousness Density), Natura 2000 (N2K) data, Urban Atlas (UA) products, Riparian Zones (RZ), Coastal Zones (CZ), CLC+ Backbone, Corine Land Cover (CLC), and European Forest Fire Information System (Effis) data. Most listed datasets have a &#39;PUBLISHED&#39; or &#39;USED&#39; status, with one entry &#39;Urban_Atlas-IBK_2018&#39; from Austria/Innsbruck currently in &#39;PROCESSING&#39;. An overlaying &#39;Cancel&#39; button indicates a pending action for a row that is partially obscured." /><span id="_Ref151988796"
class="anchor"></span>

**Figure 3‑26:Cancel Ingestion while uploading or processing**

## Status of an Ingestion

The **status** indicates the current process of the Ingestion or
Extraction in the system. The status is displayed in the Data Catalogue
for each Ingestion and Extraction in the column ‘Status’ (see [Figure
3‑27](#_Ref151989171)). Table 3‑1 provides a detailed description of
possible status messages. Sections [3.7 Edit Ingestion](#edit-ingestion)
and [4.3 Edit Extraction](#edit-extraction) go into more detail on how
Ingestion- and Extraction-states are changed. For any change of the
status of the users own Ingestion the user gets a notification (see
section [1.7.3](#notifications-messages)) as well as an email
notification. Further all users get notified in whenever a new Ingestion
is published (assuming the Ingestion was published publicly).

In the example below, you can see the different states of Ingestions in
the Data Catalogue view (see [Figure 3‑27](#_Ref151989171)). Several are
Used, one Published, one Draft, one Processing and four Ingestions are
in status Ingested_Preview.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image97.png"
style="width:6.925in;height:2.98542in"
data-fig-alt="A screenshot of the CLC+ (Copernicus Land Cover) Core User Admin support interface, displaying the &#39;Data Catalogue&#39; page. The top navigation bar shows links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and &#39;CLC+ Core User Admin/Support&#39;. The main section features &#39;Data Catalogue&#39; with filter buttons: &#39;Filter&#39;, &#39;My organisation/s&#39; (checked), &#39;My data&#39; (checked), &#39;Ingestions&#39; (checked), and &#39;Extractions&#39; (selected). To the right, there is a search bar and action buttons: &#39;ADD INGESTION&#39;, &#39;ADD EXTRACTION&#39;, and a dropdown menu with a trashcan icon. Below this, a table lists various datasets with the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. Visible rows include: * &#39;Urban Atlas (UA) 2018&#39;, created &#39;20.06.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;European Environ...&#39; with &#39;Reference Year 2018&#39;, &#39;Time Range 29.06.2017 - 01.09.2018&#39;, by &#39;CLC, European En...&#39;, Contact &#39;Matteo.Mattiuzzi...&#39;, &#39;Status USED&#39;, and &#39;INSPIRE Themes Land use, Land cover&#39;. * &#39;Urban Atlas (UA) 2018&#39;, created &#39;20.02.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;European Environ...&#39; with &#39;Reference Year 2018&#39;, &#39;Time Range 01.01.2017 - 31.12.2019&#39;, by &#39;copernicus@eea...&#39;, &#39;Status USED&#39;, and &#39;INSPIRE Themes Land use, Land cover&#39;. * &#39;Urban Atlas (UA) 2012&#39;, created &#39;21.06.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;European Environ...&#39; with &#39;Reference Year 2012&#39;, &#39;Time Range 24.03.2011 - 15.09.2013&#39;, by &#39;CLC, European En...&#39;, Contact &#39;Matteo.Mattiuzzi...&#39;, &#39;Status PUBLISHED&#39;, and &#39;INSPIRE Themes Land use, Land cover&#39;. * &#39;Urban Atlas IBK_2018&#39;, created &#39;21.11.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;Austria/Österreich&#39; in &#39;Innsbruck&#39; with &#39;Time Range 26.06.2017 - 28.08.2018&#39;, by &#39;CLC, European En...&#39;, Contact &#39;Matteo.Mattiuzzi...&#39;, &#39;Status PROCESSING&#39;. * &#39;test_GRAMD&#39;, created &#39;05.09.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;Austria/Österreich&#39; with &#39;Status INGESTED_PREVIEW&#39;. * &#39;Test 2023_10_19&#39;, created &#39;19.10.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;Austria/Österreich&#39; in &#39;Linz-Wels&#39; with &#39;Status INGESTED_PREVIEW&#39;. * &#39;Test 2023_10_18&#39;, created &#39;18.10.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;Austria/Österreich&#39; with &#39;Status INGESTED_PREVIEW&#39;. * &#39;Test&#39;, created &#39;18.10.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;Austria/Österreich&#39; with &#39;Status INGESTED_PREVIEW&#39;. * &#39;Riparian Zones (RZ) 20...&#39;, created &#39;21.06.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;European Environ...&#39; with &#39;Reference Year 2018&#39;, &#39;Time Range 01.03.2018 - 31.07.2018&#39;, by &#39;CLC, European En...&#39;, Contact &#39;copernicus@eea...&#39;, &#39;Status USED&#39;, and &#39;INSPIRE Themes Land use, Land cover&#39;. * &#39;Riparian Zones (RZ) 20...&#39;, created &#39;21.02.2023&#39;, by &#39;CLC+ Core User Admin...&#39;, for &#39;European Environ...&#39; with &#39;Reference Year 2018&#39;, &#39;Time Range 01.03.2018 - 31.07.2018&#39;, by &#39;European Environ...&#39;, Contact &#39;copernicus@eea...&#39;, &#39;Status USED&#39;, and &#39;INSPIRE Themes Land use, Land cover&#39;. The table also includes a pagination control at the bottom, showing &#39;Items per page: 10&#39; and indicating &#39;1 - 10 of 32&#39; entries. The &#39;Type&#39; column uses a document icon to signify dataset files. The &#39;Status&#39; column shows various stages such as &#39;USED&#39;, &#39;PUBLISHED&#39;, &#39;PROCESSING&#39;, and &#39;INGESTED_PREVIEW&#39;, reflecting the lifecycle of data within the system." /><span id="_Ref151989171"
class="anchor"></span>

**Figure 3‑27: Example of different status of datasets in the CLC+
system**

<table style="width:100%;">
<caption><span id="_Ref98940657" class="anchor"></span>Table 3‑1: Status
of ingested datasets</caption>
<colgroup>
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"><strong>Status</strong> :==================
Uploading</td>
<td rowspan="2"><p><strong>Description</strong>
:===================================================================================================================================================================================================================================================================================================================================
Process, where all relevant information and their datasets are uploaded
to the system.</p>
<p><strong>Note: During this phase it is necessary to have a stable
internet connection and to keep the webpage open.</strong> As soon as
the status changes to “PROCESSING” the webpage can be
left/closed.</p></td>
<td></td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td>Uploading_Error</td>
<td colspan="2">An error occurred while uploading the dataset. By
clicking on the data catalogue entry, a pop-up window will help
indicating the error. | | <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image98.png"
style="width:5.57014in;height:2.60833in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core Data Catalogue web interface, displaying a list of data ingestions and an &#39;Uploading error&#39; modal dialog. The top navigation bar shows &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. The main view is titled &#39;Data Catalogue&#39; and includes filters for &#39;My organisation/s&#39;, &#39;My data&#39;, &#39;Ingestions&#39;, and &#39;Extractions&#39;, along with a search bar and an &#39;ADD INGESTION&#39; button. The main area lists several data ingestions with the following columns: &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39; (represented by a document icon), &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, and &#39;Status&#39;. Visible rows in the data table include: * &#39;HRL - Water and Wetnes...&#39; created &#39;06.09.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European Environ...&#39; in &#39;2018&#39;, time range &#39;01.01.2012 - 31.12.2018&#39;, organisation &#39;CLC, European Env...&#39;, contact &#39;info@eea.europa.eu&#39;, status &#39;USED&#39;. * &#39;N2K 2018&#39; created &#39;21.06.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European Environ...&#39; in &#39;2018&#39;, time range &#39;15.05.2017 - 14.09.2019&#39;, organisation &#39;CLC, European Env...&#39;, contact &#39;copernicus@eea.e...&#39;, status &#39;USED&#39;. * &#39;Riparian Zones (RZ) 2018&#39; created &#39;21.06.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European Environ...&#39; in &#39;2018&#39;, time range &#39;01.03.2018 - 31.07.2018&#39;, organisation &#39;CLC, European Env...&#39;, contact &#39;copernicus@eea.e...&#39;, status &#39;USED&#39;. * &#39;Riparian Zones (RZ) 2018&#39; created &#39;21.02.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European E[unreadable]&#39;, status &#39;USED&#39;. * &#39;Urban Atlas (UA) 2018&#39; created &#39;20.06.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European B[unreadable]&#39;, contact &#39;Matteo.Mattiuzzi@...&#39;, status &#39;USED&#39;. * &#39;Urban Atlas (UA) 2018&#39; created &#39;20.02.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European E[unreadable]&#39;, contact &#39;copernicus@eea.e...&#39;, status &#39;USED&#39;. * &#39;Urban_Atlas_IBK_2018&#39; created &#39;21.11.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;Austria/Öst[unreadable]&#39;, with a status of &#39;UPLOADING_ERROR&#39; indicated by a warning icon. * &#39;Coastal Zones (CZ) 2012&#39; created &#39;21.06.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European E[unreadable]&#39;, contact &#39;info@eea.europa.eu&#39;, status &#39;PUBLISHED&#39;. * &#39;Corine Land Cover (CLC)...&#39; created &#39;14.06.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European E[unreadable]&#39;, contact &#39;copernicus@eea.e...&#39;, status &#39;PUBLISHED&#39;. * &#39;HRL - Grassland 2018&#39; created &#39;10.03.2023&#39; by &#39;CLC+ Core User Admin...&#39; for &#39;European B[unreadable]&#39;, contact &#39;copernicus@eea.e...&#39;, status &#39;PUBLISHED&#39;. An &#39;Uploading error for ingestion: Urban_Atlas_IBK_2018&#39; modal dialog is superimposed, stating: &#39;The upload failed because the url directed to a file which is not supported for ingestion. It needs to contain a file of the type: tif, TIF, TIFF, tiff, ZIP, h5, gpkg. If the url opens a download page, please enter the download link you find there as the source for the upload. Contact admins and provide the error id: 84a7a295-53b7-42b1-87ba-b70d167c11f1. Please use the action &#39;Retry&#39; for making the needed changes or for retrying to add the Ingestion. Otherwise, please delete the Ingestion.&#39; The dialog offers four buttons: &#39;CLOSE&#39;, &#39;DELETE&#39;, &#39;RETRY&#39;, and &#39;RETRY MERGE&#39;. The table footer indicates &#39;Items per page: 10&#39;." />
| | - When ingesting a vector file, please check if the correct
attribute value is selected | | - Check if the provided upload link is
valid. In case the link is valid, a download should start by clicking on
it. If not, the download link might be expired (i.e. CLMS links expire
after 24h) | | - Retry or delete Ingestion | | Contact the <a
href="https://clcplus-core.land.copernicus.eu/">CLC+ Core support
team</a> |</td>
</tr>
<tr>
<td>Processing</td>
<td>The dataset is processed in the system (rasterized, reprojected and
aggregated, merged and their layers extracted into Input Classes). As
soon as an Ingestion is successfully processed, the status changes to
“DRAFT”.</td>
<td></td>
</tr>
<tr>
<td>Processing_Error</td>
<td colspan="2">An error occurred while processing the dataset. By
clicking on the data catalogue entry, a pop-up window will help
indicating the error. | | <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image99.png"
style="width:5.57014in;height:2.6625in"
data-fig-alt="A table showing datasets in the Copernicus Land Monitoring Service (CLMS) Data Catalogue, featuring metadata and current ingestion status for various land monitoring products. The table has columns: `EAGLE Approved` (all empty for visible rows), `Name`, `Type` (indicated by a document icon for all entries), `Created At`, `Created By`, `Country`, `Region`, `Reference Year`, `Time Range`, `Organisation/s`, `Contact Person`, and `Status`. Ten datasets are visible: 1. **HRL - Water and Wetness...**: Created on 06.09.2023 by CLC+ Core User Admin at European Environ..., Reference Year 2018, Time Range 01.01.2012 - 31.12.2018, Organisation/s CLC, European Env..., Contact Person info@eea.europa.eu, Status USED. 2. **N2K 2018** (Natura 2000): Created on 21.06.2023 by CLC+ Core User Admin at European Environ..., Reference Year 2018, Time Range 15.05.2017 - 14.09.2019, Organisation/s CLC, European Env..., Contact Person copernicus@eea.e..., Status USED. 3. **Riparian Zones (RZ) 2018**: Created on 21.06.2023 by CLC+ Core User Admin at European Environ..., Reference Year 2018, Time Range 01.03.2018 - 31.07.2018, Organisation/s CLC, European Env..., Contact Person copernicus@eea.e..., Status USED. 4. **Riparian Zones (RZ) 2018**: Created on 21.02.2023 by CLC+ Core User Admin at European Environ..., Reference Year 2018, Time Range 01.03.2018 - 31.07.2018, Organisation/s CLC, European Env..., Contact Person copernicus@eea.e..., Status USED. 5. **Urban Atlas (UA) 2018**: Created on 20.06.2023 by CLC+ Core User Admin at European Environ..., Reference Year 2018, Time Range 29.06.2017 - 01.09.2018, Organisation/s CLC, European Env..., Contact Person Matteo.Mattiuzzi@..., Status USED. 6. **Urban Atlas (UA) 2018**: Created on 20.02.2023 by CLC+ Core User Admin at European Environ..., Reference Year 2018, Time Range [partially obscured], Organisation/s [partially obscured], Status USED. 7. **UA_IBK_2018**: Created on 21.11.2023 by CLC+ Core User Admin at Austria/Österr..., Reference Year [partially obscured], Time Range [partially obscured], Organisation/s [partially obscured], Status PROCESSING_ERROR. A pop-up dialog is active for this entry. 8. **Coastal Zones (CZ) 2012**: Created on 21.06.2023 by CLC+ Core User Admin at European Environ..., Reference Year [partially obscured], Time Range [partially obscured], Organisation/s [partially obscured], Contact Person info@eea.europa.eu, Status PUBLISHED. 9. **Corine Land Cover (CLC)...**: Created on 14.06.2023 by CLC+ Core User Admin at European Environ..., Reference Year [partially obscured], Time Range [partially obscured], Organisation/s [partially obscured], Contact Person copernicus@eea.e..., Status PUBLISHED. 10. **HRL - Grassland 2018**: Created on 10.03.2023 by CLC+ Core User Admin at European Environ..., Reference Year [partially obscured], Time Range [partially obscured], Organisation/s [partially obscured], Contact Person copernicus@eea.e..., Status PUBLISHED. A &#39;Processing error for ingestion: UA_IBK_2018&#39; dialog box overlays the table. Its text states: &#39;Ingestion was cancelled manually. Please use the action &#39;Retry&#39; for making the needed changes or for retrying to add the Ingestion. Otherwise, please delete the Ingestion.&#39; The dialog offers four buttons: &#39;CLOSE&#39;, &#39;DELETE&#39;, &#39;RETRY&#39;, and &#39;RETRY MERGE&#39;. The table indicates user interface navigation options: &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39; in the top bar. Below the title &#39;Data Catalogue&#39;, filtering options include &#39;Filter&#39;, &#39;My organisation/s&#39;, &#39;My data&#39;, &#39;Ingestions&#39;, &#39;Extractions&#39;, and a &#39;Search&#39; bar. An &#39;ADD INGESTION&#39; button is on the far right. The table footer shows &#39;Items per page: 10&#39;. The table displays various statuses for datasets, including &#39;USED&#39;, &#39;PROCESSING_ERROR&#39;, and &#39;PUBLISHED&#39;, reflecting the lifecycle of data ingestion within the CLC+ system." />
| - Check if the provided upload link is valid. In case the link is
valid, a download should start by clicking on it. If not, the download
link might be expired (i.e. CLMS links expire after 24h) | | - Retry or
delete Ingestion | | Contact the <a
href="https://clcplus-core.land.copernicus.eu/">CLC+ Core support
team</a> |</td>
</tr>
<tr>
<td>Draft</td>
<td>Either the dataset was processed successfully and is newly ingested
in the system or changes were made to an existing Ingestion. The
Ingestion can now be edited by performing an EAGLE barcoding, changing
some of its ingesting information and many more.</td>
<td></td>
</tr>
<tr>
<td>Ingesting_Preview</td>
<td>The preview is executed for a smaller area in the map.</td>
<td></td>
</tr>
<tr>
<td>Ingesting</td>
<td>Ingestion is executed for the whole area</td>
<td></td>
</tr>
<tr>
<td>Ingesting_Error</td>
<td>An Error occurred during the INGESTING or INGESTING_PREVIEW step.
When opening the detail page of the Ingestion an error message with more
details is displayed. Do the required changes to resolve the error and
start the Ingestion again?</td>
<td></td>
</tr>
<tr>
<td>Ingested</td>
<td>Ingestion execution is finished for the whole area.</td>
<td></td>
</tr>
<tr>
<td>Published</td>
<td colspan="2">If the Ingestion is published, <strong>it can be made
available to other users and can thus be used for Extractions.</strong>
| | The user has several possibilities to publish the Ingestion.
Depending on what kind of visibility (private, public or national) you
have chosen, the Ingestion will then be available to either all users
(public), to all countries of the selected organisation (national), or
only to users within your organisation (private). | | <strong>Note: Once
the Ingestion is published, other users can perform Extractions with the
Ingestion, which changes the status to "used". In status USED, you can
no longer make changes to the Ingestion.</strong> | | <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image100.png"
style="width:2.56296in;height:1.4239in"
data-fig-alt="This image is a screenshot of a user interface modal dialog box titled &#39;Publish Ingestion &#39;UA18_IBK&#39;&#39;. The dialog explains that &#39;Publishing &#39;UA18_IBK&#39; will make it accessible for other users within CLC+ Core according to the visibility that you define - Please select the preferred visibility setting:&#39;. Below this, there is a dropdown menu labelled &#39;Visibility&#39;, which currently displays &#39;Public - All Organisations&#39;. A warning message states: &#39;Please be aware that it is possible to edit an Ingestion until it is used within an Extraction in status &#39;EXTRACTED&#39;. Once it is used in an Extraction, the status of the Ingestion will change to &#39;USED&#39;.&#39; The dialog box contains two action buttons: &#39;CANCEL&#39; and a green-highlighted &#39;PUBLISH&#39;." />
|</td>
</tr>
<tr>
<td>Used</td>
<td>The dataset is already used in an Extraction. <strong>Now it is no
longer possible to delete the dataset. The only further option is to
archive the dataset.</strong></td>
<td></td>
</tr>
<tr>
<td>Archived</td>
<td>The dataset is archived and thus <strong>no longer available /
usable for Extractions</strong>. Additionally, it is unpublished from
the geoserver, which means it cannot be viewed in the preview
anymore.</td>
<td></td>
</tr>
</tbody>
</table>

The status of an Ingestion is also displayed in the detail view next to
the Ingestion Name in the upper left corner (see [Figure
3‑28](#_Ref151989420)). The status of an Ingestion can be changed by
triggering some actions. E.g. by adding the EAGLE barcodes and pressing
preview for a small area, the status converts from ‘draft’ (see [Figure
3‑28](#_Ref151989420)) to ‘ingested_preview’.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image101.png"
style="width:6.925in;height:3.82014in"
data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) data ingestion interface for an Urban Atlas (UA) dataset named &#39;UA_IBK_2018&#39;, currently in &#39;DRAFT&#39; status. The interface includes: 1. **Top Navigation Bar**: Links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and &#39;CLC+ Core User Admin/Support&#39;. A red banner displays a warning: &#39;Please fill out all the required fields and save your changes! DISMISS&#39;. 2. **Ingestion Header**: Shows &#39;Ingestion &#39;UA_IBK_2018&#39;&#39; and provides action buttons: &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START INGESTION&#39;, and &#39;PUBLISH&#39;. An &#39;APPROVE EAGLE COMPLIANCE&#39; button is featured below the &#39;EAGLE Land Monitoring in Europe&#39; logo. 3. **General Information Section**: Contains input fields for dataset metadata. * &#39;Name *&#39;: &#39;UA_IBK_2018&#39; * &#39;Country *&#39;: &#39;AT Austria/Österreich&#39; * &#39;Region&#39;: &#39;AT332 Innsbruck&#39; * Required empty fields (with red text indicating unmet requirements): &#39;Reference Year *&#39;, &#39;Time Range of Ingested Data *&#39;, and &#39;INSPIRE Themes *&#39;. * &#39;Created By&#39;: &#39;CLC+ Core User Admin/Support&#39;. * &#39;Organisation/s *&#39;: &#39;CLC&#39; and &#39;European Environment Agency (EEA)&#39;. * Empty fields for &#39;Contact Person&#39; and &#39;Link to Document/s&#39;. * Action buttons: &#39;CANCEL&#39; and &#39;SAVE&#39;. 4. **Map Section**: Displays a satellite map with a pink-outlined region centred on Innsbruck, Austria, encompassing surrounding areas of Austria and Germany. Map controls include zoom (+/-), fullscreen, and layer options. A scale bar shows &#39;10 km&#39; and &#39;5 mi&#39;. An overlay message states, &#39;Your map is outdated! Please press &#39;PREVIEW&#39; to generate the map according to your new Input&#39;. Search fields for &#39;Country *&#39; and &#39;Region *&#39;, along with a &#39;PREVIEW&#39; button, are located above the map. Map attribution: &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. 5. **Input Classes Section**: A table-like list for managing classification codes and their properties, preceded by a &#39;DOWNLOAD EAGLE BARCODING&#39; button. Columns are &#39;Class Code&#39;, &#39;Name&#39;, &#39;EAGLE Elements&#39;, &#39;100% EAGLE compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39;. * Six rows are visible, listing Class Codes from &#39;11100&#39; to &#39;11300&#39;. * The &#39;Name&#39; column currently duplicates the &#39;Class Code&#39; (e.g., &#39;11100&#39;). * &#39;EAGLE Elements&#39; is marked with an asterisk. * &#39;100% EAGLE compliant&#39; checkboxes are unchecked. * The &#39;Colour&#39; column displays distinct colour swatches for each class: light blue (11100), dark blue (11210), light green (11220), medium green (11230), dark green (11240), and red (11300). * &#39;Show in Map&#39; toggle switches are all in the &#39;off&#39; position." />

This is a screenshot of the Copernicus Land Monitoring Service (CLMS)
data ingestion interface for an Urban Atlas (UA) dataset named
‘UA_IBK_2018’, currently in “DRAFT” status.

The interface includes: 1. **Top Navigation Bar**: Links to “Data
Catalogue”, “EAGLE Ontology”, “About EAGLE”, “Organisations”, “Users”,
and “CLC+ Core User Admin/Support”. A red banner displays a warning:
“Please fill out all the required fields and save your changes!
DISMISS”. 2. **Ingestion Header**: Shows “Ingestion ‘UA_IBK_2018’” and
provides action buttons: “REPUBLISH ON GEOSERVER”, “START INGESTION”,
and “PUBLISH”. An “APPROVE EAGLE COMPLIANCE” button is featured below
the “EAGLE Land Monitoring in Europe” logo. 3. **General Information
Section**: Contains input fields for dataset metadata. \* “Name *”:
”UA_IBK_2018”* ”Country *“:”AT Austria/Österreich”* “Region”: “AT332
Innsbruck” \* Required empty fields (with red text indicating unmet
requirements): “Reference Year *”, ”Time Range of Ingested Data* ”, and
“INSPIRE Themes *”.* ”Created By”: “CLC+ Core User Admin/Support”. \*
“Organisation/s *”: ”CLC” and ”European Environment Agency (EEA)”.*
Empty fields for”Contact Person” and “Link to Document/s”. \* Action
buttons: “CANCEL” and “SAVE”. 4. **Map Section**: Displays a satellite
map with a pink-outlined region centred on Innsbruck, Austria,
encompassing surrounding areas of Austria and Germany. Map controls
include zoom (+/-), fullscreen, and layer options. A scale bar shows “10
km” and “5 mi”. An overlay message states, “Your map is outdated! Please
press”PREVIEW” to generate the map according to your new Input”. Search
fields for “Country *” and ”Region* ”, along with a “PREVIEW” button,
are located above the map. Map attribution: “Leaflet \| © Core003
Mosaic, © OpenStreetMap contributors”. 5. **Input Classes Section**: A
table-like list for managing classification codes and their properties,
preceded by a “DOWNLOAD EAGLE BARCODING” button. Columns are “Class
Code”, “Name”, “EAGLE Elements”, “100% EAGLE compliant”, “Colour”, and
“Show in Map”. \* Six rows are visible, listing Class Codes from “11100”
to “11300”. \* The “Name” column currently duplicates the “Class Code”
(e.g., “11100”). \* “EAGLE Elements” is marked with an asterisk. \*
“100% EAGLE compliant” checkboxes are unchecked. \* The “Colour” column
displays distinct colour swatches for each class: light blue (11100),
dark blue (11210), light green (11220), medium green (11230), dark green
(11240), and red (11300). \* “Show in Map” toggle switches are all in
the “off” position.

<span id="_Ref151989420" class="anchor"></span>**Figure 3‑28: From draft
to ingested_preview (by adding EAGLE barcodes, Region and general
information like reference year, time range and INSPIRE theme)**

## Input Classes

**Input Classes** are representing detailed information about the
Ingestion and originating from the uploaded dataset for each Ingestion.
This also means that every Input Class is connected to an Ingestion.
Input Classes contain the information on how to interpret the class code
within the raster file and how they are mapped to the specific EAGLE
barcodes (compliance to EAGLE, factor of EAGLE barcode value). Input
Classes from the dataset layers are generated when adding a new
Ingestion to the system (see section[3.23.2](#add-ingestion)).
Furthermore, they are used when adding a new Extraction to the system in
case they are selected (see section [4.2](#add-extraction)). In the
example below (see [Figure 3‑29](#_Ref151640298)[Figure
3‑29](#_Ref151640298)) the Ingestion ‘HRL Forest Type’ has three input
classes. Besides the class code the class name and the EAGLE barcodes
per class are shown, as well as the colour code per class.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image2.jpg"
style="width:0.27165in;height:0.27165in"
data-fig-alt="A circular icon with a blue background and a white digit &#39;1&#39; centered within it. This icon typically indicates the first step in a sequential process or workflow, such as a data ingestion procedure within a technical document." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image102.png"
style="width:6.925in;height:3.80139in"
data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) data catalogue and ingestion interface for the High Resolution Layer (HRL) Forest Type (FTY) 2018 product. The interface shows general product information, a spatial distribution map of forest types across Europe, and a table detailing the input classification scheme based on EAGLE (EIONET Action Group Land Monitoring in Europe) elements. The &#39;General Information&#39; section provides metadata: - Name: HRL - Forest Type (FTY) 2018 - Country: European Environment Agency (EEA) (38+UK) - Region: European Environment Agency (EEA) (38+UK) - Reference Year: 2018 - Time Range of Ingested Data: 01.03.2018 - 31.10.2018 - INSPIRE Themes: LU Land use, LC Land cover - Created By: CLC+ Core User Admin/Support - Organisation/s: CLC, European Environment Agency - Visibility: Public - All Organisations - Contact Person: copernicus@eea.europa.eu - Link to Document/s: https://www.eea.europa.eu/about-us/tenders/eea-idm-r0-18-011 The right panel displays an interactive map of Europe showing the spatial distribution of forest types. Forested areas are depicted in shades of green, while non-forested areas are light grey/white. A scale bar indicates 300 km and 300 mi. Map controls include zoom in (+), zoom out (-), full extent, and layer toggle. Search boxes are present for &#39;Country *&#39; and &#39;Region *&#39;. The map attribution is &#39;© Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. Below the map, an &#39;Input Classes&#39; table defines the classification scheme: | Class Code | Name | EAGLE Elements | 100% EAGLE compliant | Colour | Show in Map | |:-----------|:--------------------|:--------------------------------|:---------------------|:-------------|:------------| | 0 | All non-forest areas | Trees (crossed out icon) | Yes | White | No | | 1 | Broadleaved forest | Trees (tree icon, plus 2) | Yes | Dark green | Yes | | 2 | Coniferous forest | Trees (tree icon, plus 1) | Yes | Darker green | Yes | The table indicates that &#39;All non-forest areas&#39; are represented by a crossed-out tree icon and are not shown on the map, while &#39;Broadleaved forest&#39; and &#39;Coniferous forest&#39; are represented by tree icons and shown in different shades of green on the map. All classes are marked as &#39;100% EAGLE compliant&#39;. The top of the page also features &#39;REPUBLISH ON GEOSERVER&#39; and &#39;ARCHIVE&#39; buttons, indicating data management functionalities." />

<span id="_Ref151640298" class="anchor"></span>**Figure 3‑29: Example of
Input Classes of the HRL Forest Type Ingestion**

## Edit Ingestion

To finally ingest your data to be able to use it, click on the required
Ingestion in the data catalogue table. You will be forwarded to a more
detailed view of the same Ingestion.

**Before an Ingestion can be previewed or published, you need to review
the Ingestion settings and map all Input Classes to EAGLE elements.** To
avoid mistakes, you can preview your Input Classes in the map. **Note:
The EAGLE barcoding is a mandatory task.**

You can **edit your Ingestion** as often as you like, also after the
status has change to Ingested or Published. If published, clicking
unpublish will set the status back to ingested and you are able to edit
your Ingestion again.

**Be aware that once the Ingestion is published and has been used for an
Extraction, it cannot be edited anymore**.

In the left section (**General Information**), you can review all
Ingestion information and edit them by clicking on the “**Edit**”
button. Reference year, time range and [INSPIRE
Themes](https://inspire.ec.europa.eu/Themes/Data-Specifications/2892)
are mandatory fields. In case a metadata file has been uploaded during
the Ingestion and the necessary data is available, this section will be
prefilled already. Save the changes by clicking on the “Save” button.
Before leaving the page without saving your edits the user will be
reminded to save the edits, otherwise all edits will not be saved when
returning to the page. Below the General Information the user can add
**additional documents** like the EAGLE barcoding file per drag and drop
or via uploading.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image103.png"
style="width:3.41965in;height:6.0025in"
data-fig-alt="A screenshot of a user interface form titled &#39;General Information,&#39; used for inputting metadata for a data ingestion process within the Copernicus Land Monitoring Service (CLMS) CLC+ Core system. The form displays various fields with pre-filled or selected values and blank input areas. The filled fields are: * `Name`: `UA_IBK_2018` (Urban Atlas Innsbruck 2018) * `Country`: `AT Austria/Österreich` * `Region`: `AT332 Innsbruck` * `Reference Year`: `2018` * `Time Range of Ingested Data`: `01.01.2018 – 31.12.2018` * `INSPIRE Themes`: `LU Land use` and `LC Land cover` (with a clickable link to an &#39;INSPIRE theme register&#39;). These themes align with Directive 2007/2/EC, the INSPIRE Directive. * `Created By`: `CLC+ Core User Admin/Support` * `Organisation/s`: `CLC` (CORINE Land Cover) and `European Environment Agency` (EEA) * `Initial Spatial Resolution`: `0 m` * `Initial Coordinate Reference System`: `EPSG:3035` * `Initial Type of Data`: `Vector` * `Attribute Name`: `code_2018` Fields that are currently empty for input include `Contact Person`, `Link to Document/s`, `Description`, and `Excluded Class Code`. In the top right corner, there are two action buttons: `CANCEL` and `SAVE`." />

A screenshot of a user interface form titled “General Information,” used
for inputting metadata for a data ingestion process within the
Copernicus Land Monitoring Service (CLMS) CLC+ Core system. The form
displays various fields with pre-filled or selected values and blank
input areas. The filled fields are: \* `Name`: `UA_IBK_2018` (Urban
Atlas Innsbruck 2018) \* `Country`: `AT Austria/Österreich` \* `Region`:
`AT332 Innsbruck` \* `Reference Year`: `2018` \*
`Time Range of Ingested Data`: `01.01.2018 – 31.12.2018` \*
`INSPIRE Themes`: `LU Land use` and `LC Land cover` (with a clickable
link to an “INSPIRE theme register”). These themes align with Directive
2007/2/EC, the INSPIRE Directive. \* `Created By`:
`CLC+ Core User Admin/Support` \* `Organisation/s`: `CLC` (CORINE Land
Cover) and `European Environment Agency` (EEA) \*
`Initial Spatial Resolution`: `0 m` \*
`Initial Coordinate Reference System`: `EPSG:3035` \*
`Initial Type of Data`: `Vector` \* `Attribute Name`: `code_2018` Fields
that are currently empty for input include `Contact Person`,
`Link to Document/s`, `Description`, and `Excluded Class Code`. In the
top right corner, there are two action buttons: `CANCEL` and `SAVE`.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image104.png"
style="width:4.1999in;height:2.539in"
data-fig-alt="Screenshot of a user interface section titled &#39;Additional Documents&#39; for uploading supplementary files. The interface presents two options for uploading: &#39;Drag and Drop&#39; files into a dashed-line boundary box, or click an &#39;UPLOAD DOCUMENT/S&#39; button with an upward arrow icon. A descriptive text below states: &#39;All documents that help to understand the content, including legend files which will be used to automatically create input classes and metadata files which will be used to automatically prefill the data description. (No file type restrictions)&#39;. Below this, a file named &#39;Urban_Atlas_2018_EAGLEBarcodingTemplate_3.1.2_23.12.2021_v3-F70...&#39; is listed, represented by a paperclip icon and followed by a trashcan icon for deletion. This document likely serves as an EAGLE (European Approach for Land-use/Land-cover mapping) barcoding template for Urban Atlas 2018 data." />

Screenshot of a user interface section titled “Additional Documents” for
uploading supplementary files. The interface presents two options for
uploading: “Drag and Drop” files into a dashed-line boundary box, or
click an “UPLOAD DOCUMENT/S” button with an upward arrow icon. A
descriptive text below states: “All documents that help to understand
the content, including legend files which will be used to automatically
create input classes and metadata files which will be used to
automatically prefill the data description. (No file type
restrictions)”. Below this, a file named
“Urban_Atlas_2018_EAGLEBarcodingTemplate_3.1.2_23.12.2021_v3-F70…” is
listed, represented by a paperclip icon and followed by a trashcan icon
for deletion. This document likely serves as an EAGLE (European Approach
for Land-use/Land-cover mapping) barcoding template for Urban Atlas 2018
data.

<span id="_Toc137576666" class="anchor"></span>**Figure 3‑30: Edit
Ingestion – Ingestion settings and possibility to add additional
documents**

**Note: Changes can only be done for unpublished datasets. As soon as a
dataset has been used in an Extraction, changes can no longer be made
while in use (by you or any other user).**

It is obligatory to map all ingested classes as **EAGLE elements** in
order to publish an Ingestion. It is recommended to upload the EAGLE
barcoding file (a detailed description is provided in section 2.3)
together with the data. You can do this already when defining the
settings for the Ingestion (see section [3.2](#add-ingestion)) or by
clicking on the EAGLE element picker. In case you use the picker,
continue with step 3 below, otherwise you can skip this and continue
with step 4.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image106.png"
style="width:6.925in;height:3.8125in"
data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core User Admin/Support interface, displaying detailed information for a data ingestion named &#39;UA_IBK_2018&#39;. The interface is structured into three main sections: General Information, a Map preview, and Input Classes. The &#39;General Information&#39; section on the left panel provides metadata for the &#39;UA_IBK_2018&#39; ingestion: * Name: UA_IBK_2018 * Country: Austria/Österreich * Region: Innsbruck * Reference Year: 2018 * Time Range of Ingested Data: 01.01.2018 - 31.12.2018 * INSPIRE (Infrastructure for Spatial Information in the European Community) Themes: LU Land use, LC Land cover * Created By: CLC+ Core User Admin/Support * Organisation/s: CLC (CORINE Land Cover), European Environment Agency (EEA) Action buttons at the top right of the interface include &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START INGESTION&#39;, and &#39;PUBLISH&#39;. A button labeled &#39;APPROVE EAGLE COMPLIANCE&#39; is also visible, associated with the EIONET Action Group EAGLE Land Monitoring in Europe logo. The central part of the interface features an interactive map displaying the geographic coverage of the &#39;UA_IBK_2018&#39; data for the Innsbruck region. The map shows a green overlay highlighting the data&#39;s extent over a mountainous topographic base map. Map controls include zoom functions (+/-), full screen toggle, and layer visibility. A scale bar shows &#39;10 km&#39; and &#39;5 mi&#39;. The map&#39;s attribution credits &#39;Leaflet | Core003 Mosaic, © OpenStreetMap contributors&#39;. Below the map, an &#39;Input Classes&#39; section presents a table detailing the classification scheme: * **Class Code:** 11100, 11210, 11220, 11230 * **Name:** 11100, 11210, 11220, 11230 * **EAGLE Elements:** All classes are mapped to &#39;Sealed Artificial Surfaces and Constructions&#39; with a factor of &#39;+10&#39; (for 11100, 11210) or &#39;+11&#39; (for 11220, 11230). * **100% EAGLE compliant:** All four listed classes are marked as compliant with a green checkmark. * **Colour:** Dark red for classes 11100, 11210, 11220; pink for class 11230. * **Show in Map:** Toggle switches are shown in the &#39;off&#39; position for all classes. A &#39;Download EAGLE Barcoding&#39; button is also present above this table." />

This is a screenshot of the Copernicus Land Monitoring Service (CLMS)
CLC+ Core User Admin/Support interface, displaying detailed information
for a data ingestion named ‘UA_IBK_2018’. The interface is structured
into three main sections: General Information, a Map preview, and Input
Classes.

The ‘General Information’ section on the left panel provides metadata
for the ‘UA_IBK_2018’ ingestion: \* Name: UA_IBK_2018 \* Country:
Austria/Österreich \* Region: Innsbruck \* Reference Year: 2018 \* Time
Range of Ingested Data: 01.01.2018 - 31.12.2018 \* INSPIRE
(Infrastructure for Spatial Information in the European Community)
Themes: LU Land use, LC Land cover \* Created By: CLC+ Core User
Admin/Support \* Organisation/s: CLC (CORINE Land Cover), European
Environment Agency (EEA)

Action buttons at the top right of the interface include “REPUBLISH ON
GEOSERVER”, “START INGESTION”, and “PUBLISH”. A button labeled “APPROVE
EAGLE COMPLIANCE” is also visible, associated with the EIONET Action
Group EAGLE Land Monitoring in Europe logo.

The central part of the interface features an interactive map displaying
the geographic coverage of the ‘UA_IBK_2018’ data for the Innsbruck
region. The map shows a green overlay highlighting the data’s extent
over a mountainous topographic base map. Map controls include zoom
functions (+/-), full screen toggle, and layer visibility. A scale bar
shows “10 km” and “5 mi”. The map’s attribution credits “Leaflet \|
Core003 Mosaic, © OpenStreetMap contributors”.

Below the map, an ‘Input Classes’ section presents a table detailing the
classification scheme: \* **Class Code:** 11100, 11210, 11220, 11230 \*
**Name:** 11100, 11210, 11220, 11230 \* **EAGLE Elements:** All classes
are mapped to “Sealed Artificial Surfaces and Constructions” with a
factor of “+10” (for 11100, 11210) or “+11” (for 11220, 11230). \*
**100% EAGLE compliant:** All four listed classes are marked as
compliant with a green checkmark. \* **Colour:** Dark red for classes
11100, 11210, 11220; pink for class 11230. \* **Show in Map:** Toggle
switches are shown in the ‘off’ position for all classes. A “Download
EAGLE Barcoding” button is also present above this table.

<span id="_Ref98941497" class="anchor"></span>**Figure 3‑31: Edit
Ingestion (step 3 is in [**Figure 3‑33**](#_Ref98941415))**

Further if the EAGLE barcoding was already uploaded or done manually the
number of used EAGLE elements per Input class is shown in the EAGLE
elements column. For example, + 10 for class 11100 in the example below
(see [Figure 3‑32](#_Ref152070629)) indicated that overall 11 EAGLE
elements are barcoded for this Input class (first element is written in
the column, the other 10 EAGLE elements are summarized as ‘+10’). By
hovering over the EAGLE element column for an input class all EAGLE
elements of this class including the applied barcoding is shown in the
dark grey box (see [Figure 3‑32](#_Ref152070629)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image107.png"
style="width:6.925in;height:5.73125in"
data-fig-alt="A screenshot of a web interface displaying a geographic map centered on the Innsbruck region (AT332) in Austria, overlaid with land cover classifications. The map uses an OpenStreetMap base layer and features a highlighted administrative boundary in pink. Land cover types are shown in green (likely vegetation/forest) and red/pink (likely artificial surfaces/urban). A scale bar indicates 10 km and 5 mi. A pop-up legend on the map lists &#39;11 elements&#39; including &#39;Sealed Artificial Surfaces and Constructions (3)&#39;, &#39;Biotic / Vegetation (1)&#39;, &#39;Agriculture (X)&#39;, &#39;Forestry (X)&#39;, &#39;Commercial Services (1)&#39;, &#39;Accommodation and Food Services (1)&#39;, &#39;Financial, Professional and Information Services (1)&#39;, &#39;Permanent Residential (2)&#39;, &#39;Residential Use With Other Compatible Uses (2)&#39;, &#39;City Street Blocks, Closed Front (3)&#39;, and &#39;Urban (5)&#39;. Below the map, an &#39;Input Classes&#39; table details the mapping of raw classification codes to harmonised EAGLE (EIONET Action Group on Land monitoring in Europe) elements for ingestion into the Copernicus Land Monitoring Service (CLMS). The table contains the following columns and data: | Class Code | Name | EAGLE Element | 100% EAGLE compliant | Colour | Show in Map | |:-----------|:------|:------------------------------------|:---------------------|:-----------|:------------| | 11100 | 11100 | Sealed Artificial Surfaces and Constructions +10 | ✓ | Dark Red | On | | 11210 | 11210 | Sealed Artificial Surfaces and Constructions +10 | ✓ | Dark Red | On | | 11220 | 11220 | Sealed Artificial Surfaces and Constructions +11 | ✓ | Dark Red | On | | 11230 | 11230 | Sealed Artificial Surfaces and Constructions +11 | ✓ | Light Red | On | Each row represents an input class, its name, the corresponding EAGLE Element, a compliance checkmark, the colour used for its representation on the map, and a toggle to show/hide it on the map. The interface also displays buttons for &#39;REPUBLISH ON GEOSERVER&#39;, &#39;UNPUBLISH&#39;, and &#39;DOWNLOAD EAGLE BARCODING&#39;, indicating data management functionalities within the CLC+ Core User Admin/Support system for High Resolution Layer (HRL) Forest Type Ingestion. The map shows the spatial distribution of these classified land cover types over the mountainous terrain around Innsbruck, with urban and sealed areas concentrated in valleys." />

A screenshot of a web interface displaying a geographic map centered on
the Innsbruck region (AT332) in Austria, overlaid with land cover
classifications. The map uses an OpenStreetMap base layer and features a
highlighted administrative boundary in pink. Land cover types are shown
in green (likely vegetation/forest) and red/pink (likely artificial
surfaces/urban). A scale bar indicates 10 km and 5 mi. A pop-up legend
on the map lists “11 elements” including “Sealed Artificial Surfaces and
Constructions (3)”, “Biotic / Vegetation (1)”, “Agriculture (X)”,
“Forestry (X)”, “Commercial Services (1)”, “Accommodation and Food
Services (1)”, “Financial, Professional and Information Services (1)”,
“Permanent Residential (2)”, “Residential Use With Other Compatible Uses
(2)”, “City Street Blocks, Closed Front (3)”, and “Urban (5)”.

Below the map, an “Input Classes” table details the mapping of raw
classification codes to harmonised EAGLE (EIONET Action Group on Land
monitoring in Europe) elements for ingestion into the Copernicus Land
Monitoring Service (CLMS). The table contains the following columns and
data:

| Class Code | Name | EAGLE Element | 100% EAGLE compliant | Colour | Show in Map |
|:---|:---|:---|:---|:---|:---|
| 11100 | 11100 | Sealed Artificial Surfaces and Constructions +10 | ✓ | Dark Red | On |
| 11210 | 11210 | Sealed Artificial Surfaces and Constructions +10 | ✓ | Dark Red | On |
| 11220 | 11220 | Sealed Artificial Surfaces and Constructions +11 | ✓ | Dark Red | On |
| 11230 | 11230 | Sealed Artificial Surfaces and Constructions +11 | ✓ | Light Red | On |

Each row represents an input class, its name, the corresponding EAGLE
Element, a compliance checkmark, the colour used for its representation
on the map, and a toggle to show/hide it on the map. The interface also
displays buttons for “REPUBLISH ON GEOSERVER”, “UNPUBLISH”, and
“DOWNLOAD EAGLE BARCODING”, indicating data management functionalities
within the CLC+ Core User Admin/Support system for High Resolution Layer
(HRL) Forest Type Ingestion. The map shows the spatial distribution of
these classified land cover types over the mountainous terrain around
Innsbruck, with urban and sealed areas concentrated in valleys.

<span id="_Ref152070629" class="anchor"></span>**Figure 3‑32: Summary of
EAGLE elements per Input class**

Even if it is recommended to upload the EAGLE barcoding file, the CLC+
Core system provides you with the EAGLE Picker\](see [Figure
3‑33](#_Ref98941415) and [Figure 3‑34](#_Ref98941416)) that allows you
to align the EAGLE elements with the Input Classes from an Ingestion. By
clicking on the EAGLE elements of one Input class a new window for the
EAGLE barcoding opens (see [Figure 3‑33](#_Ref98941415)). The picker
allows you to multi-select EAGLE elements that match the Input Classes,
select an EAGLE barcode (X-5 including a label, for a detailed
description of each barcode see the help function ([Figure
3‑34](#_Ref98941416)) or Annex Table 0‑1) and set a factor that defines
the coverage of the EAGLE element on the specific input class once an
EAGLE element has been added to an Input Class. Finally, you need to
check the checkbox whether it is 100% EAGLE compliant or not. The ‘100%
EAGLE compliant’ tick box is a flag indicating if the mapping to the
EAGLE language for one Input class is fully compliant or only partially
compliant. If it is only partially compliant it needs to be evaluated
within an Extraction then if the given gap causes issues in the specific
use case. Note that this tick box is not connected to the “Approved by
EAGLE” stamp for complete Ingestions.

Concerning the Help function, in the “Help- EAGLE Barcoding Manual”
there is also a direct link (see [Figure 3‑34](#_Ref98941416)) to the
[EAGLE homepage](https://land.copernicus.eu/en/eagle?tab=bar_coding),
which opens then in a separate tab.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image108.png"
style="width:6.925in;height:3.79722in"
data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, showing the &#39;Edit Ingestion&#39; page for &#39;Coastal Zones (CZ) 2012&#39;. An overlaying modal dialog, titled &#39;Select EAGLE Elements for Continuous urban fabric (Imperviousness Density (IMD) ≥80%) (9)&#39;, allows users to define classification rules. The main page displays &#39;General Information&#39; for the ingestion, including: - Name: Coastal Zones (CZ) - Country: European Environ[ment Agency] - Region: European Environ[ment Agency] - Reference Year: 2012 - Time Range of In[gestion]: 01.01.2010 - 31.1[unreadable] - INSPIRE Themes: LU Land use, LC Land cover - Created By: CLC+ Core User A[dmin] - Organisation/s: CLC, European Environ[ment Agency] - Contact Person: info@eea.europa[eu] - Link to Document/s: several URLs, including https://land.copernicus.eu/user-corner/technical-library/coastal-zone-monitoring The modal dialog is structured with expandable sections: - **Land Cover Components (LCC)**, which includes: - Abiotic / Non-Vegetated Surfaces and Objects (LCC-1), containing: - Artificial Surfaces and Constructions (LCC-1_1), further detailed into: - Sealed Artificial Surfaces and Constructions (LCC-1_1_1), with &#39;EAGLE Barcoding&#39;: 3 and &#39;Factor&#39;: 1.00. - Non-Sealed Artificial Surfaces (LCC-1_1_2), which includes: - Open Non-Sealed Artificial Surfaces (LCC-1_1_2_1), with &#39;EAGLE Barcoding&#39;: 1, a checked &#39;true&#39; box, and &#39;Factor&#39;: 1.00. - Waste Materials (LCC-1_1_2_2) (unchecked). - Natural Material Surfaces (LCC-1_2) (unchecked), with a dropdown showing options for &#39;EAGLE Barcoding&#39;: X (Excluded), 1 (Optional), 2 (One or more), 3 (All of them), 4 (At least two), and 5 (This one only). - Biotic / Vegetation (LCC-2) (checked). - Water (LCC-3) (checked). - **Land Use Attributes (LUA)**, which includes: - Primary Production Sector (LUA-1), containing: - Agriculture (LUA-1_1). Below the modal, partially visible table rows show: - Row 1: Code 11130, Name: Low density fabric (IMD &lt;30%), associated with &#39;Sealed Artificial Surfaces and Constructions&#39;, a value of +11, a green checkmark, and a red colour swatch. - Row 2: Code 11210, Name: Industrial, commercial, public and military, associated with &#39;Sealed Artificial Surfaces and Constructions&#39;, a value of +16, a green checkmark, and a purple colour swatch. The modal dialog has &#39;CANCEL&#39; and &#39;ADD TO INPUT CLASS&#39; buttons. A top menu bar displays &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. Buttons for &#39;PUBLISH&#39; and &#39;PREVIEW&#39; are visible on the right sidebar." /><span id="_Ref98941415"
class="anchor"></span>

**Figure 3‑33: Mapping Input Classes to EAGLE elements - Select EAGLE
elements**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image109.png"
style="width:3.87606in;height:2.05969in"
data-fig-alt="A screenshot of a help page titled &#39;Help - EAGLE Matrix Barcoding Manual&#39;, presenting the definitions of EAGLE Bar Code Values (BCV). The explanatory text states that BCVs are used to mark EAGLE matrix elements relevant to a given class definition from a nomenclature, expressing the role of the bar-coded element in fulfilling the targeted specific class definition. A &#39;List of Bar Code Values&#39; defines six types: * **X (Excluded)**: Element is excluded by definition. * **1 (Optional)**: An optional element that can be expected or occurs as typical, but is not mandatory for a class assignment. * **2 (One or more)**: A selective mandatory element, defining an OR-connection, where at least one (or several) of all elements with BCV 2 must be present. * **3 (All of them)**: A cumulative mandatory element, defining an AND-connection, where all elements with BC 3 must be present. * **4 (At least two)**: Multiple selective occurrence mandatory elements with an AND/OR connection, requiring at least two out of all elements with BCV 4 to be present. * **5 (This one only)**: An exclusive mandatory element that does not allow any other elements besides the single element with BC 5; only one BC 5 is allowed in each matrix block (LCC, LUA, LCH). The page also provides a link for more information about EAGLE Barcoding and includes a &#39;CLOSE&#39; button at the bottom right." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image110.png"
style="width:3.1216in;height:1.65998in"
data-fig-alt="This is a screenshot of a &#39;Help - Factor&#39; dialog box from a user interface, likely within a Copernicus Land Monitoring Service (CLMS) application like the CLC+ Core software. The dialog explains how a &#39;Factor&#39; is used to define the coverage of an EAGLE element for a given Input Class. The allowed value range for the Factor is 0.0 to 1.0. It states that the Factor, together with the percentage coverage of the Input Class for each cell, determines the coverage of the EAGLE element for that specific cell. An example calculation is provided: &#39;If an Input Class has got a percentage coverage of 80% for the specific cell and a factor of 0.5 is applied to the specific EAGLE element, the coverage of the EAGLE element for this cell is 40%.&#39; A &#39;CLOSE&#39; button is visible at the bottom right of the dialog." />

<span id="_Ref98941416" class="anchor"></span>**Figure 3‑34: Mapping
Input Classes to EAGLE elements – Help windows for barcoding and
factor**

Classes that have been already excluded from the dataset (e.g. NoData)
in the relevant steps before, will not be shown in the Input Classes
section anymore (see section [3.2](#add-ingestion) “exclude class
codes”). In case this has not been done yet, there is still the
opportunity to hide (not exclude!!!) specified/single classes before
finally ingesting the data. Therefore, just uncheck the ‘eye’ symbol at
the end of the row of the respective class ([Figure
3‑35](#_Ref100162670)). Note that the hidden classes will appear as “0”
in the Ingestion and not as NoData pixels. Hidden classes can be shown
again even after publishing the Ingestion by unpublishing the Ingestion
but only if the Ingestion is not in status “Used” yet.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image111.png"
style="width:3.98704in;height:2.05108in"
data-fig-alt="The table displays &#39;Input Classes&#39; for a Copernicus Land Monitoring Service (CLMS) dataset ingestion, showing the mapping of raw land cover classes to harmonised EAGLE elements. The table has six columns: &#39;Class Code&#39;, &#39;Name&#39;, &#39;EAGLE Elements&#39;, &#39;100% EAGLE compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39;. | Class Code | Name | EAGLE Elements | 100% EAGLE compliant | Colour | Show in Map | |:-----------|:-------------------------------|:------------------------------------|:----------------------|:-------|:------------| | 10 | Railway | Conventional Buildings (+7 additional) | Yes | Black | Yes | | 11 | Roads | Conventional Buildings (+5 additional) | No | Red | No | | 12 | Airport | Conventional Buildings (+8 additional) | Yes | Grey | Yes | | 20 | Residential area | Sealed Artificial Surfaces (+13 additional) | Yes | Yellow | Yes | | 21 | Retail trade, transport, and utilities | Sealed Artificial Surfaces (+5 additional) | Yes | Pink | Yes | The &#39;EAGLE Elements&#39; column indicates the primary EAGLE element mapped to the input class, followed by a count of additional mapped EAGLE elements (e.g., &#39;+7 additional&#39; means seven more elements are mapped besides the named one). The &#39;100% EAGLE compliant&#39; column uses a green checkmark for &#39;Yes&#39; and a grey checkmark for &#39;No&#39;. The &#39;Colour&#39; column shows a coloured square representing the assigned display colour. The &#39;Show in Map&#39; column uses a green checkmark for &#39;Yes&#39; and an empty box for &#39;No&#39;. Class 11 &#39;Roads&#39; is highlighted, showing &#39;No&#39; for &#39;100% EAGLE compliant&#39; and &#39;Show in Map&#39;, and a disabled edit icon, indicating that changes can no longer be made. This table details the configuration for different land cover input classes, their associated EAGLE element mappings, and their compliance status and display properties within the CLMS ingestion system." />

The table displays “Input Classes” for a Copernicus Land Monitoring
Service (CLMS) dataset ingestion, showing the mapping of raw land cover
classes to harmonised EAGLE elements. The table has six columns: “Class
Code”, “Name”, “EAGLE Elements”, “100% EAGLE compliant”, “Colour”, and
“Show in Map”.

| Class Code | Name | EAGLE Elements | 100% EAGLE compliant | Colour | Show in Map |
|:---|:---|:---|:---|:---|:---|
| 10 | Railway | Conventional Buildings (+7 additional) | Yes | Black | Yes |
| 11 | Roads | Conventional Buildings (+5 additional) | No | Red | No |
| 12 | Airport | Conventional Buildings (+8 additional) | Yes | Grey | Yes |
| 20 | Residential area | Sealed Artificial Surfaces (+13 additional) | Yes | Yellow | Yes |
| 21 | Retail trade, transport, and utilities | Sealed Artificial Surfaces (+5 additional) | Yes | Pink | Yes |

The “EAGLE Elements” column indicates the primary EAGLE element mapped
to the input class, followed by a count of additional mapped EAGLE
elements (e.g., “+7 additional” means seven more elements are mapped
besides the named one). The “100% EAGLE compliant” column uses a green
checkmark for “Yes” and a grey checkmark for “No”. The “Colour” column
shows a coloured square representing the assigned display colour. The
“Show in Map” column uses a green checkmark for “Yes” and an empty box
for “No”. Class 11 “Roads” is highlighted, showing “No” for “100% EAGLE
compliant” and “Show in Map”, and a disabled edit icon, indicating that
changes can no longer be made.

This table details the configuration for different land cover input
classes, their associated EAGLE element mappings, and their compliance
status and display properties within the CLMS ingestion system.

<span id="_Ref100162670" class="anchor"></span>**Figure 3‑35: Uncheck
‘eye’ to prevent values / classes to be ingested.**

Once all settings and Input Classes have been reviewed, you can start
the Ingestion for a small area / region that lies within the boundary of
the processed dataset by clicking on ‘**preview**’ (see [Figure
3‑36](#_Ref152070767)). If the preview was successful, you can now
inspect your Ingestion in the map and continue with step 6.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image112.png"
style="width:4.84595in;height:1.98851in"
data-fig-alt="This map displays a land cover classification focused on the AT33 Tirol region of Austria (Österreich), with surrounding areas of Liechtenstein and parts of Austria (Österreich). The base map is dark grey, indicating administrative boundaries and major roads. The main selected region, &#39;AT33 Tirol&#39;, is bordered in red and filled with a light grey-blue pattern. Within this region, a central area extending around Innsbruck, Schwaz, and towards Sölden is highlighted with a detailed land cover classification using shades of green and yellow. Darker green areas likely represent dense vegetation or forest, while lighter green and yellow areas may indicate sparser vegetation, grasslands, or other land uses. A notable white, unclassified linear feature runs through the green area, likely representing a major valley or infrastructure. Two additional areas within eastern Tyrol are outlined with a light green dashed border and shaded in a slightly darker green. User interface elements at the top right indicate selection filters for &#39;Country: AT Austria/Österreich&#39; and &#39;Region: AT33 Tirol&#39;. A &#39;PREVIEW&#39; button is visible to the right. The map includes zoom controls (+, -) and a full-screen toggle. A scale bar shows &#39;20 km&#39; and &#39;10 mi&#39;. The data source is attributed to &#39;Leaflet | German Aerospace Center (DLR) CC-BY 3.0&#39;. A blue circle with the number &#39;5&#39; is present in the top right." />

This map displays a land cover classification focused on the AT33 Tirol
region of Austria (Österreich), with surrounding areas of Liechtenstein
and parts of Austria (Österreich). The base map is dark grey, indicating
administrative boundaries and major roads. The main selected region,
“AT33 Tirol”, is bordered in red and filled with a light grey-blue
pattern. Within this region, a central area extending around Innsbruck,
Schwaz, and towards Sölden is highlighted with a detailed land cover
classification using shades of green and yellow. Darker green areas
likely represent dense vegetation or forest, while lighter green and
yellow areas may indicate sparser vegetation, grasslands, or other land
uses. A notable white, unclassified linear feature runs through the
green area, likely representing a major valley or infrastructure. Two
additional areas within eastern Tyrol are outlined with a light green
dashed border and shaded in a slightly darker green. User interface
elements at the top right indicate selection filters for “Country: AT
Austria/Österreich” and “Region: AT33 Tirol”. A “PREVIEW” button is
visible to the right. The map includes zoom controls (+, -) and a
full-screen toggle. A scale bar shows “20 km” and “10 mi”. The data
source is attributed to “Leaflet \| German Aerospace Center (DLR) CC-BY
3.0”. A blue circle with the number “5” is present in the top right.

<span id="_Ref152070767" class="anchor"></span>**Figure 3‑36: Map
preview**

Now, you can ‘**Start the Ingestion**’ for the full extent of your
Ingestion (see [Figure 3‑31](#_Ref98941497)). Afterwards you have the
choice to ‘Publish’ to use it for Extractions and to make it available
for other users (see [Figure 3‑39](#_Ref151639942)).

The clock symbol allows to view the **Ingestion history** (see [Figure
3‑37](#_Ref98877006)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image115.png"
style="width:6.925in;height:3.18333in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core system user interface, displaying the &#39;History of Ingestion &#39;Coastal Zones (CZ) 2012&#39;&#39; data product. The pop-up window shows a history log table with four columns: &#39;New Status&#39;, &#39;Changed At&#39;, &#39;Changed By&#39;, and &#39;Additional Information&#39;. The table lists 10 entries out of a total of 16, detailing the lifecycle of the data ingestion from initial upload to publication, spanning from 27.06.2023 to 23.11.2023. The history log entries are: | New Status | Changed At | Changed By | Additional Information | |:-----------|:---------------------|:-----------------------|:----------------------------| | PUBLISHED | 23.11.2023 09:30:20 | CLC+ Core User Admin | | | INGESTED | 23.11.2023 09:28:58 | CLC+ Core User Admin | | | PUBLISHED | 17.10.2023 09:49:19 | Lindmayer Amelie | | | USED | 17.10.2023 09:49:01 | Lindmayer Amelie | Used by: test error extraction | | PUBLISHED | 28.06.2023 07:24:40 | CLC+ Core User Admin | | | INGESTED | 28.06.2023 01:51:11 | CLC+ Core User Admin | | | INGESTING | 27.06.2023 20:01:46 | CLC+ Core User Admin | | | DRAFT | 27.06.2023 16:10:00 | CLC+ Core User Admin | | | PROCESSING | 27.06.2023 14:48:26 | CLC+ Core User Admin | | | UPLOADING | 27.06.2023 14:48:25 | CLC+ Core User Admin | | The main page, partially visible behind the pop-up, displays &#39;General Information&#39; for the &#39;Coastal Zones (CZ) 2012&#39; ingestion. This includes: Name &#39;Coastal Zones (CZ) 2012&#39;, Country &#39;European Environment Agency (38+UK)&#39;, Region &#39;European Environment Agency (38+UK)&#39;, Reference Year &#39;2012&#39;, and Time Range of Ingested Data &#39;01.01.2010 - 31.12.2014&#39;. It also lists INSPIRE Directive Themes &#39;LU Land use&#39; and &#39;LC Land cover&#39;, and credits &#39;CLC+ Core User Admin/Support&#39; and organisations &#39;CLC&#39; and &#39;European Environment Agency&#39;. A button labeled &#39;APPROVE EAGLE COM&#39; (presumably &#39;EAGLE Compliance&#39;) is visible, indicating the integration with the EIONET Action Group on Land monitoring in Europe (EAGLE) framework." />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) CLC+ Core system user interface, displaying the “History of
Ingestion ‘Coastal Zones (CZ) 2012’” data product. The pop-up window
shows a history log table with four columns: “New Status”, “Changed At”,
“Changed By”, and “Additional Information”. The table lists 10 entries
out of a total of 16, detailing the lifecycle of the data ingestion from
initial upload to publication, spanning from 27.06.2023 to 23.11.2023.

The history log entries are: \| New Status \| Changed At \| Changed By
\| Additional Information \| \|:———–\|:———————\|:———————–\|:—————————-\|
\| PUBLISHED \| 23.11.2023 09:30:20 \| CLC+ Core User Admin \| \| \|
INGESTED \| 23.11.2023 09:28:58 \| CLC+ Core User Admin \| \| \|
PUBLISHED \| 17.10.2023 09:49:19 \| Lindmayer Amelie \| \| \| USED \|
17.10.2023 09:49:01 \| Lindmayer Amelie \| Used by: test error
extraction \| \| PUBLISHED \| 28.06.2023 07:24:40 \| CLC+ Core User
Admin \| \| \| INGESTED \| 28.06.2023 01:51:11 \| CLC+ Core User Admin
\| \| \| INGESTING \| 27.06.2023 20:01:46 \| CLC+ Core User Admin \| \|
\| DRAFT \| 27.06.2023 16:10:00 \| CLC+ Core User Admin \| \| \|
PROCESSING \| 27.06.2023 14:48:26 \| CLC+ Core User Admin \| \| \|
UPLOADING \| 27.06.2023 14:48:25 \| CLC+ Core User Admin \| \|

The main page, partially visible behind the pop-up, displays “General
Information” for the ‘Coastal Zones (CZ) 2012’ ingestion. This includes:
Name “Coastal Zones (CZ) 2012”, Country “European Environment Agency
(38+UK)”, Region “European Environment Agency (38+UK)”, Reference Year
“2012”, and Time Range of Ingested Data “01.01.2010 - 31.12.2014”. It
also lists INSPIRE Directive Themes “LU Land use” and “LC Land cover”,
and credits “CLC+ Core User Admin/Support” and organisations “CLC” and
“European Environment Agency”. A button labeled “APPROVE EAGLE COM”
(presumably “EAGLE Compliance”) is visible, indicating the integration
with the EIONET Action Group on Land monitoring in Europe (EAGLE)
framework.

<span id="_Ref98877006" class="anchor"></span>**Figure 3‑37: History of
Ingestion for one layer**

Once an Ingestion is published (see next chapter) Input classes can
either be shown all in the map preview by activating the “Show in Map”
or be toggled on and off individually by selectin on Input class. Only
the selected Input class will then be shown in the map preview like for
example class “11210” in the example below (see [Figure
3‑38](#_Ref152248025)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image116.png"
style="width:6.925in;height:5.05556in"
data-fig-alt="This image is a screenshot of a Copernicus Land Monitoring Service (CLMS) user interface. The top section displays an interactive map of Innsbruck, Austria, identified by &#39;Country: AT Austria/Österreich&#39; and &#39;Region: AT332 Innsbruck&#39;. The map includes a scale bar showing &#39;1 km&#39; and &#39;1 mi&#39;, and is attributed to &#39;Leaflet | © OpenStreetMap contributors&#39;. Overlaid on the map are red-shaded areas representing selected land cover features, corresponding to one of the &#39;Input Classes&#39;. The bottom section of the screenshot is a control panel titled &#39;Input Classes&#39; and displays a URL: &#39;https://services.qa-clccore.cloudflight.host/clccore/9474ed82-9a79-4950-88d4-...&#39;. A button labeled &#39;DOWNLOAD EAGLE BARCODING&#39; is prominent. Below this, a table lists four input classes with the following columns: &#39;Class Code&#39;, &#39;Name&#39;, &#39;EAGLE Elements&#39;, &#39;100% EAGLE compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39;. The table details are: - **Class Code 11100, Name 11100:** Mapped to &#39;Sealed Artificial Surfaces and Constructions +10&#39;, marked as &#39;100% EAGLE compliant&#39; (checkbox checked), assigned a dark red colour, and its map visibility is off (toggle grey). - **Class Code 11210, Name 11210:** Mapped to &#39;Sealed Artificial Surfaces and Constructions +10&#39;, marked as &#39;100% EAGLE compliant&#39; (checkbox checked), assigned a dark red colour, and its map visibility is on (toggle green). The red areas on the map visually represent this class. - **Class Code 11220, Name 11220:** Mapped to &#39;Sealed Artificial Surfaces and Constructions +11&#39;, marked as &#39;100% EAGLE compliant&#39; (checkbox checked), assigned a dark red colour, and its map visibility is off (toggle grey). - **Class Code 11230, Name 11230:** Mapped to &#39;Sealed Artificial Surfaces and Constructions +11&#39;, marked as &#39;100% EAGLE compliant&#39; (checkbox checked), assigned a light red colour, and its map visibility is off (toggle grey)." />

This image is a screenshot of a Copernicus Land Monitoring Service
(CLMS) user interface. The top section displays an interactive map of
Innsbruck, Austria, identified by “Country: AT Austria/Österreich” and
“Region: AT332 Innsbruck”. The map includes a scale bar showing “1 km”
and “1 mi”, and is attributed to “Leaflet \| © OpenStreetMap
contributors”. Overlaid on the map are red-shaded areas representing
selected land cover features, corresponding to one of the “Input
Classes”.

The bottom section of the screenshot is a control panel titled “Input
Classes” and displays a URL:
“https://services.qa-clccore.cloudflight.host/clccore/9474ed82-9a79-4950-88d4-…”.
A button labeled “DOWNLOAD EAGLE BARCODING” is prominent. Below this, a
table lists four input classes with the following columns: “Class Code”,
“Name”, “EAGLE Elements”, “100% EAGLE compliant”, “Colour”, and “Show in
Map”.

The table details are: - **Class Code 11100, Name 11100:** Mapped to
“Sealed Artificial Surfaces and Constructions +10”, marked as “100%
EAGLE compliant” (checkbox checked), assigned a dark red colour, and its
map visibility is off (toggle grey). - **Class Code 11210, Name 11210:**
Mapped to “Sealed Artificial Surfaces and Constructions +10”, marked as
“100% EAGLE compliant” (checkbox checked), assigned a dark red colour,
and its map visibility is on (toggle green). The red areas on the map
visually represent this class. - **Class Code 11220, Name 11220:**
Mapped to “Sealed Artificial Surfaces and Constructions +11”, marked as
“100% EAGLE compliant” (checkbox checked), assigned a dark red colour,
and its map visibility is off (toggle grey). - **Class Code 11230, Name
11230:** Mapped to “Sealed Artificial Surfaces and Constructions +11”,
marked as “100% EAGLE compliant” (checkbox checked), assigned a light
red colour, and its map visibility is off (toggle grey).

<span id="_Ref152248025" class="anchor"></span>**Figure 3‑38: Show
selected Input classes in the map of published Ingestions.**

## Publish Ingestion

You can **publish an Ingestion** by clicking on the button ‘publish’ in
the Ingestion view (see at section [3.7](#edit-ingestion) and [Figure
3‑39](#_Ref151639942) below).

**Note: Depending on what kind of visibility (private, public or
national) you have chosen, the ingested data will then be available to
either all users (public), to the country of the selected organisation
(national), or only to users within your organisation (private).
Consider, that other users might use your data for Extractions. As
mentioned before, once your data has been used, it can no longer be
deleted or edited while in use by either you or other users.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image117.png"
style="width:6.925in;height:3.12778in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core User Admin/Support web interface, showing the ingestion management page for &#39;Coastal Zones (CZ) 2012&#39; data. The interface displays general information about the dataset, a geographic map preview, and an overlaid modal dialog for publishing the ingested data. The left panel provides &#39;General Information&#39; for the dataset: - Name: Coastal Zones (CZ) 2012 - Country: European Environment Agency (38+UK) - Region: European Environment Agency (38+UK) - Reference Year: 2012 - Time Range of Ingested Data: 01.01.2010 - 31.12.2014 - INSPIRE Themes: LU Land use, LC Land cover - Created By: CLC+ Core User Admin/Support - Organisation/s: CLC, European Environment Agency The top navigation bar features links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. An &#39;EIONET Action Group EAGLE Land Monitoring in Europe&#39; logo is displayed alongside an &#39;APPROVE EAGLE COMPLIANCE&#39; button. The right side of the interface contains a geographic map of Europe, with a basemap attributed to Leaflet, Core003 Mosaic, and OpenStreetMap contributors. The map shows parts of the United Kingdom, Ireland, Nordic countries, Central and Eastern Europe, and Turkey, overlaid with green and blue patterns representing ingested land cover data. Above the map are input fields for &#39;Country *&#39; and &#39;Region *&#39; and buttons labelled &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START INGESTION&#39;, &#39;PUBLISH&#39;, and &#39;PREVIEW&#39;. A &#39;DOWNLOAD EAGLE BARCODING&#39; button is visible below the map. A modal dialog titled &#39;Publish Ingestion &#39;Coastal Zones (CZ) 2012&#39;&#39; is overlaid in the center. It states that publishing makes the data accessible to other users within CLC+ Core based on selected visibility. The available visibility settings are: &#39;Public - All Organisations&#39;, &#39;National - Countries of selected Organisations&#39;, and &#39;Private - Selected Organisations&#39;. The dialog includes &#39;CANCEL&#39; and &#39;PUBLISH&#39; buttons. At the bottom, a partially visible table-like section lists input classes. Headers include &#39;Class Code ↑&#39;, &#39;Name *&#39;, &#39;EAGLE Elements *&#39;, &#39;100% EAGLE compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39;. The first visible entry shows Class Code &#39;11110&#39; for &#39;Continuous urban fabric (IMD ≥80%)&#39;, with &#39;Sealed Artificial Surfaces and Constructions +8&#39; as an EAGLE Element. This entry is marked as &#39;100% EAGLE compliant&#39; with a checkmark, has a red colour square, and its &#39;Show in Map&#39; toggle switch is off." />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) CLC+ Core User Admin/Support web interface, showing the ingestion
management page for ‘Coastal Zones (CZ) 2012’ data. The interface
displays general information about the dataset, a geographic map
preview, and an overlaid modal dialog for publishing the ingested data.

The left panel provides “General Information” for the dataset: - Name:
Coastal Zones (CZ) 2012 - Country: European Environment Agency (38+UK) -
Region: European Environment Agency (38+UK) - Reference Year: 2012 -
Time Range of Ingested Data: 01.01.2010 - 31.12.2014 - INSPIRE Themes:
LU Land use, LC Land cover - Created By: CLC+ Core User Admin/Support -
Organisation/s: CLC, European Environment Agency

The top navigation bar features links to “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”. An “EIONET
Action Group EAGLE Land Monitoring in Europe” logo is displayed
alongside an “APPROVE EAGLE COMPLIANCE” button.

The right side of the interface contains a geographic map of Europe,
with a basemap attributed to Leaflet, Core003 Mosaic, and OpenStreetMap
contributors. The map shows parts of the United Kingdom, Ireland, Nordic
countries, Central and Eastern Europe, and Turkey, overlaid with green
and blue patterns representing ingested land cover data. Above the map
are input fields for “Country *” and ”Region* ” and buttons labelled
“REPUBLISH ON GEOSERVER”, “START INGESTION”, “PUBLISH”, and “PREVIEW”. A
“DOWNLOAD EAGLE BARCODING” button is visible below the map.

A modal dialog titled “Publish Ingestion ‘Coastal Zones (CZ) 2012’” is
overlaid in the center. It states that publishing makes the data
accessible to other users within CLC+ Core based on selected visibility.
The available visibility settings are: “Public - All Organisations”,
“National - Countries of selected Organisations”, and “Private -
Selected Organisations”. The dialog includes “CANCEL” and “PUBLISH”
buttons.

At the bottom, a partially visible table-like section lists input
classes. Headers include “Class Code ↑”, “Name *”, ”EAGLE Elements* ”,
“100% EAGLE compliant”, “Colour”, and “Show in Map”. The first visible
entry shows Class Code “11110” for “Continuous urban fabric (IMD ≥80%)”,
with “Sealed Artificial Surfaces and Constructions +8” as an EAGLE
Element. This entry is marked as “100% EAGLE compliant” with a
checkmark, has a red colour square, and its “Show in Map” toggle switch
is off.

<span id="_Ref151639942" class="anchor"></span>Figure 3‑39: Publish
Ingestion – Select visibility (public or limited)

## Reuse Ingestion

Further, you can **reuse** an Ingestion by right clicking on the
Ingestion in the Data Catalogue a small windowsdialog with several
options opens (see [Figure 3‑40](#_Ref151639877)). Here, the Add
Ingestion dialog opens again (see [Figure 3‑41](#_Ref151639902)), with
all the fields containing the previous information entered such as name,
region, excluded values (section[3.2](#add-ingestion)). Please note that
by reusing an Ingestion the original raw data will not be available
anymore. Also, in case the “delete raw data” was not ticked for the
reused Ingestion the raw data is not accessible and reusable anymore.
The data needs to be uploaded as a file or via ULR again. Only the
information entered to the Ingestion before will be already filled in
when reusing an Ingestion.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image118.png"
style="width:0.46181in;height:0.52778in"
data-fig-alt="A screenshot displaying a vertical user interface menu with three options for managing Copernicus Land Monitoring Service (CLMS) data ingestions. Each option includes an icon and associated text: 1. An eye icon, labelled &#39;Open&#39;, suggesting an action to view or access an ingested data layer. 2. An overlapping squares icon, labelled &#39;Reuse&#39;, likely for reusing existing ingestion configurations or data. 3. An eye icon with a diagonal line through it, labelled &#39;Unpublish&#39;, indicating an action to make a previously published ingestion unavailable." />

A screenshot displaying a vertical user interface menu with three
options for managing Copernicus Land Monitoring Service (CLMS) data
ingestions. Each option includes an icon and associated text: 1. An eye
icon, labelled “Open”, suggesting an action to view or access an
ingested data layer. 2. An overlapping squares icon, labelled “Reuse”,
likely for reusing existing ingestion configurations or data. 3. An eye
icon with a diagonal line through it, labelled “Unpublish”, indicating
an action to make a previously published ingestion unavailable.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image119.png"
style="width:6.925in;height:3.10833in"
data-fig-alt="A user interface screenshot displaying a &#39;Data Catalogue&#39; table within the CLC+ Core system, listing various land monitoring data assets. The table is structured with columns: &#39;EAGLE Approved&#39; (empty for all visible entries), &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. The table lists 10 entries (21-30 of 41 total items displayed, showing 10 items per page): | Name | Type | Created At | Created By | Country | Region | Reference Year | Time Range | Organisation/s | Contact Person | Status | INSPIRE Themes | |---|---|---|---|---|---|---|---|---|---|---|---| | LULUCF Test | Extraction | 23.08.2023 | CLC+ Core User Admi... | Netherlands/Ned... | - | 2018 | 03.01.2017 - 02.01.2020 | CLC, European En... | [unreadable] | EXTRACTED_PREVIEW | Land use, Land cover | | CLC+ Core Review | Extraction | 16.08.2023 | CLC+ Core User Admi... | European Environ... | - | 2023 | 01.01.2022 - 31.12.2022 | CLC, European En... | [unreadable] | DRAFT | Land use, Land cover | | N2K 2012 | Ingestion | 21.06.2023 | CLC+ Core User Admi... | European Environ... | European Environ... | 2012 | 07.04.2010 - 06.08.2015 | CLC, European En... | copernicus@eea.... | PUBLISHED | Land use, Land cover | | N2K 2018 | Ingestion | 21.06.2023 | CLC+ Core User Admi... | European Environ... | European Environ... | 2018 | 15.05.2017 - 14.09.2019 | CLC, European En... | copernicus@eea.... | USED | Land use, Land cover | | Coastal Zones (CZ) 2012 | Ingestion | 21.06.2023 | CLC+ Core User Admi... | European Environ... | European Environ... | 2012 | 01.01.2010 - 31.12.2014 | CLC, European En... | info@eea.europa.... | PUBLISHED | Land use, Land cover | | Coastal Zones (CZ) 2018 | Ingestion | 21.06.2023 | CLC+ Core User Admi... | European Environ... | European Environ... | 2018 | 01.01.2017 - 31.12.2019 | CLC, European En... | info@eea.europa.... | USED | Land use, Land cover | | Riparian Zones (RZ) 2012 | Ingestion | 21.06.2023 | CLC+ Core User Admi... | European Environ... | European Environ... | 2012 | 14.07.2011 - 25.09.2014 | CLC, European En... | mpalacios@indra.... | PUBLISHED | Land use, Land cover | | Riparian Zones (RZ) 2018 | Ingestion" /><span id="_Ref151639877"
class="anchor"></span>

**Figure 3‑40: Reuse Ingestion**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image120.png"
style="width:6.925in;height:3.37917in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) Core system&#39;s &#39;Data Catalogue&#39; user interface, displaying a list of land cover/land use (LULC) datasets with an active &#39;Reuse Ingestion&#39; dialog box overlaid. The main &#39;Data Catalogue&#39; table shows columns for &#39;EAGLE Approved&#39;, &#39;Name&#39;, &#39;Type&#39;, &#39;Created At&#39;, &#39;Created By&#39;, &#39;Organisation/s&#39;, &#39;Contact Person&#39;, &#39;Status&#39;, and &#39;INSPIRE Themes&#39;. Visible dataset names include &#39;LULUCF Test&#39;, &#39;CLC+ Core Review&#39;, &#39;N2K 2012&#39;, &#39;N2K 2018&#39; (referring to Natura 2000), &#39;Coastal Zones (CZ) 20...&#39;, &#39;Riparian Zones (RZ) [unreadable]&#39;, and &#39;Urban Atlas (UA) 2012&#39; and &#39;Urban Atlas (UA) 2018&#39;. Creation dates range from &#39;20.06.2023&#39; to &#39;23.08.2023&#39;. Data statuses include &#39;EXTRACTED_PREVIEW&#39;, &#39;DRAFT&#39;, &#39;PUBLISHED&#39;, and &#39;USED&#39;. All listed datasets fall under the &#39;INSPIRE Themes&#39; category of &#39;Land use, Land cover&#39;. Pagination indicates &#39;Items per page: 10&#39; and &#39;21 – 30 of 41&#39; items. The &#39;Reuse Ingestion&#39; dialog is a two-step process, with &#39;1 Input Type Selection&#39; complete and &#39;2 &#39;Dataset Selection Upload Dataset - Vector&#39;&#39; active. It is pre-filled for a dataset named &#39;N2K 2018&#39;, associated with &#39;EEA-38+UK European Environment Agency (38+UK)&#39; for both &#39;Country&#39; and &#39;Region&#39;. Users can either &#39;File Upload&#39; or &#39;URL Upload&#39; data. The &#39;File Upload&#39; section shows instructions to &#39;Drag and Drop&#39; or &#39;UPLOAD DATASET/S&#39;, specifying accepted file formats as &#39;.tif, .TIF, .tiff, .TIFF, .zip, .h5, .gpkg&#39;. An &#39;Attribute Name&#39; field is present, pre-filled with &#39;CODE_4_18&#39;, with instructions to &#39;Enter Attribute Name from Dataset (column from the attribute table) which shall be used as Input Parameter for the Class Code. Values of the selected attribute column must only contain upper- and [partially obscured]&#39;." /><span id="_Ref151639902"
class="anchor"></span>

**Figure 3‑41: Reuse Ingestion – detailed view**

# Extraction

An **Extraction** will create new and independent data products that can
be used to generate Extractions for future CLC+ instances by selecting
Input Classes from available Ingestions in the CLC+ Core (section
[3.6](#input-classes)), define Class Conditions (section
[4.5.1](#some-definitions-for-a-better-understanding-also-see-glossary))
extracting the required information and thus, create new Output Classes
(section [4.5](#output-classes)), reuse an already available Extraction
(section [4.9](#reuse-extraction)) or delete an Extraction (section
[4.10](#delete-extraction)). To make the new Extraction available for
all or selected users in CLC+ Core, execute the Extraction, review and
validate the Extraction results and publish it (section
[4.8](#publish-extraction-and-download-result)). [Figure
4‑1](#_Ref100264486) provides a simplified overview of the Extraction
process.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image121.png"
style="width:5.73475in;height:4.50694in"
data-fig-alt="This diagram illustrates the workflow for managing an Extraction within a Copernicus Land Monitoring Service (CLMS) system, showing its lifecycle through creation, editing, and non-editable states. The workflow begins with the **Add Extraction** phase (orange box): 1. An Extraction process is initiated by selecting &#39;Add Extraction (Use published Ingestion)&#39;. 2. This leads to two parallel steps: &#39;Select Input Classes&#39; and &#39;Add rulesets&#39;. Both steps feed into the next phase. * At any point during the &#39;Add Extraction&#39; phase, the Extraction can be &#39;Deleted&#39;. The process then moves to the **Edit Extraction** phase (purple box), which includes several statuses: 3. **Status Draft**: * Users can &#39;Edit metadata&#39;, &#39;Add or remove Input Classes&#39;, &#39;Add and edit rulesets&#39;, and &#39;Add country and region for preview and click start preview&#39;. * Modifying &#39;Input Classes&#39; or &#39;rulesets&#39; loops back to the initial selection steps within the &#39;Add Extraction&#39; phase. * The Extraction can transition to &#39;Status Extracted_Preview&#39;. * At any point during the &#39;Edit Extraction&#39; phase (Draft, Extracted_Preview, or Extracted statuses), the Extraction can be &#39;Deleted&#39;. 4. **Status Extracted_Preview**: * Users can &#39;Click Start Extraction&#39; and &#39;Download Extraction result&#39;. * The Extraction can transition to &#39;Status Extracted&#39; or return to &#39;Status Draft&#39;. 5. **Status Extracted**: * Users can &#39;Click Publish&#39; and &#39;Download Extraction result&#39;. * The Extraction can transition to &#39;Status Published&#39; or return to &#39;Status Extracted_Preview&#39;. Finally, the process enters the **Non-editable Extraction** phase (green box): 6. **Status Published**: * Users can &#39;Click Archive&#39; to move the Extraction to &#39;Status Archived&#39;. * Users can also &#39;Click Unpublish&#39; to return the Extraction to &#39;Status Draft&#39; in the &#39;Edit Extraction&#39; phase, allowing further modifications. 7. **Status Archived**: This is a terminal state for the Extraction lifecycle. The process ends with either the Extraction being &#39;Deleted&#39; at an early stage or reaching &#39;Status Archived&#39;." />

This diagram illustrates the workflow for managing an Extraction within
a Copernicus Land Monitoring Service (CLMS) system, showing its
lifecycle through creation, editing, and non-editable states.

The workflow begins with the **Add Extraction** phase (orange box): 1.
An Extraction process is initiated by selecting “Add Extraction (Use
published Ingestion)”. 2. This leads to two parallel steps: “Select
Input Classes” and “Add rulesets”. Both steps feed into the next phase.
\* At any point during the “Add Extraction” phase, the Extraction can be
“Deleted”.

The process then moves to the **Edit Extraction** phase (purple box),
which includes several statuses: 3. **Status Draft**: \* Users can “Edit
metadata”, “Add or remove Input Classes”, “Add and edit rulesets”, and
“Add country and region for preview and click start preview”. \*
Modifying “Input Classes” or “rulesets” loops back to the initial
selection steps within the “Add Extraction” phase. \* The Extraction can
transition to “Status Extracted_Preview”. \* At any point during the
“Edit Extraction” phase (Draft, Extracted_Preview, or Extracted
statuses), the Extraction can be “Deleted”. 4. **Status
Extracted_Preview**: \* Users can “Click Start Extraction” and “Download
Extraction result”. \* The Extraction can transition to “Status
Extracted” or return to “Status Draft”. 5. **Status Extracted**: \*
Users can “Click Publish” and “Download Extraction result”. \* The
Extraction can transition to “Status Published” or return to “Status
Extracted_Preview”.

Finally, the process enters the **Non-editable Extraction** phase (green
box): 6. **Status Published**: \* Users can “Click Archive” to move the
Extraction to “Status Archived”. \* Users can also “Click Unpublish” to
return the Extraction to “Status Draft” in the “Edit Extraction” phase,
allowing further modifications. 7. **Status Archived**: This is a
terminal state for the Extraction lifecycle.

The process ends with either the Extraction being “Deleted” at an early
stage or reaching “Status Archived”.

<span id="_Ref100264486" class="anchor"></span>**Figure 4‑1: Simplified
Extraction workflow.**

Before starting with an Extraction, **it is recommended to already have
a concept in mind**. First of all, you need the **requirements** what
the Extraction is supposed to deliver (i.e. CLC+ legacy, LULUCF
instance, etc.). With this knowledge, the Data acquisition can start.
Before ingesting the data, the EAGLE barcoding needs to be performed,
also considering the planned Extraction output. As soon as the data is
ingested, the **selection of required input classes** can be done.
Afterwards the **definition of Output Classes including their Class
Condition** is conducted.

As a consequence of the aggregation to 100 m, **several thematic classes
share one 100 m pixel**. In an Extraction, this pixel is assigned to a
single class. This is accomplished by an algorithm which assigns the
class of a pixel by checking on Class Condition after the other. Pixels
that are shared by several thematic classes **are assigned to the first
output class that exceeds the threshold** and the pixel is no longer
available to any other class. The hierarchical processing of the
Extraction favours thus classes that are extracted early. Therefore, it
is immensely important to know the requirements you want to extract as
**the order of the Output classes is decisive**. Currently, this might
lead to a bias of the statistical estimates which could be avoided by
adapting the Extraction method such that it is insensitive to the
hierarchical order, for example by extracting the class with highest
fraction with highest priority. Another option could be to extract all
classes separately or by implementing a future update so that a
multiband raster Extraction can be the output.

## Status of an Extraction

The **status** indicates the current process of the Ingestion or
Extraction in the system. The status is displayed in the Data Catalogue
for each Ingestion and Extraction in the column ‘Status’ (see [Figure
3‑27](#_Ref151989171)). Table 4‑1 provides a detailed description of
possible status messages.

| Status | Description |
|----|----|
| Cancel | If you want to stop or cancel an extracted that you started, right click on the associated extraction in the Data Catalogue and click cancel. |
| Draft | Either the Extraction was newly created in the system or changes were made to an existing Extraction. The Extraction can now be edited by adding input- or output classes or changing some metadata fields. |
| Extracting | If an extraction has been started and the dataset is processing, the status is set to extracting. While extracting the data the dataset cannot be viewed. |
| Extracted_Preview | The preview is executed for smaller area in the map. |
| Extracted | The performed Extraction was successful and can now be published. |
| Extracting_Error | An error occurred while performing an Extraction. By clicking on the data catalogue entry, a pop-up window will help indicating the error. |
| Published | If the Extraction is published, **it can be made available to other users.** The user has several possibilities to publish the Extraction. Depending on what kind of visibility (private, public or national) you have chosen, the Extraction will then be available to either all users (public), to all countries of the selected organisation (national), or only to users within your organisation (private). **Note: Once the Extraction is published, it cannot be changed anymore!** |
| Archived | The Extraction is archived and thus it is unpublished from the geoserver, which means it cannot be viewed in the preview anymore. |

<span id="_Ref153954038" class="anchor"></span>Table 4‑1: Status of
Extraction datasets

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image122.png"
style="width:4.57692in;height:1.02299in"
data-fig-alt="A screenshot of the CLC+ Core Data Catalogue user interface, featuring a top navigation bar, filter options, and a data table listing &#39;Extractions&#39;. The top navigation bar includes &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. The main section is titled &#39;Data Catalogue&#39;. Filter buttons include &#39;Filter&#39;, &#39;My organisation/s&#39; (checked), &#39;My data&#39;, &#39;Ingestions&#39;, and &#39;Extractions&#39; (checked). A &#39;Search&#39; text field is present. Action buttons on the right are &#39;ADD INGESTION&#39; and another green button, partially obscured. The main content area displays a table with headers: &#39;Name&#39;, &#39;Type&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Time Range&#39;, and &#39;Status&#39;. Two rows of data are visible: 1. **Name:** &#39;Test Instances Issue with Eurolarge [partially obscured]&#39; **Type:** &#39;&gt;&#39; **Created By:** &#39;User Admin/Support CLC+ Core&#39; **Country:** &#39;Germany Deutschland&#39; **Time Range:** &#39;01.05.2023 - 31.05.2023&#39; **Status:** &#39;EXTRACTING&#39; 2. **Name:** &#39;LULUCF_Beta_1.1&#39; **Type:** &#39;&gt;&#39; **Created By:** &#39;User Admin/Support CLC+ Core&#39; **Country:** &#39;Netherlands Nederland&#39; **Time Range:** &#39;01.01.2017 - 01.01.2020&#39; **Status:** &#39;EXTRACTED_PREVIEW&#39; A &#39;Cancel&#39; button with an eye icon is shown as a hover action over the &#39;LULUCF_Beta_1.1&#39; row. The background of the interface shows a blurred aerial image of green agricultural fields." />

A screenshot of the CLC+ Core Data Catalogue user interface, featuring a
top navigation bar, filter options, and a data table listing
“Extractions”. The top navigation bar includes “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”. The main section
is titled “Data Catalogue”. Filter buttons include “Filter”, “My
organisation/s” (checked), “My data”, “Ingestions”, and “Extractions”
(checked). A “Search” text field is present. Action buttons on the right
are “ADD INGESTION” and another green button, partially obscured.

The main content area displays a table with headers: “Name”, “Type”,
“Created By”, “Country”, “Time Range”, and “Status”. Two rows of data
are visible: 1. **Name:** “Test Instances Issue with Eurolarge
\[partially obscured\]” **Type:** “\>” **Created By:** “User
Admin/Support CLC+ Core” **Country:** “Germany Deutschland” **Time
Range:** “01.05.2023 - 31.05.2023” **Status:** “EXTRACTING” 2. **Name:**
“LULUCF_Beta_1.1” **Type:** “\>” **Created By:** “User Admin/Support
CLC+ Core” **Country:** “Netherlands Nederland” **Time Range:**
“01.01.2017 - 01.01.2020” **Status:** “EXTRACTED_PREVIEW”

A “Cancel” button with an eye icon is shown as a hover action over the
“LULUCF_Beta_1.1” row. The background of the interface shows a blurred
aerial image of green agricultural fields.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image123.png"
style="width:5.55435in;height:2.61342in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core User web interface, displaying an &#39;Extraction&#39; task named &#39;TC18_Extraction_1&#39; in an error state. The left panel presents &#39;General Information&#39; for the extraction, including Name: &#39;TC18_Extraction_1&#39;, Country: &#39;Liechtenstein&#39;, Region: &#39;Liechtenstein&#39;, Reference Year: &#39;2021&#39;, and Time Range of Extracted Data: &#39;01.08.2021 - 28.08.2021&#39;. The task is associated with &#39;INSPIRE Themes: AC Atmospheric conditions&#39; and was created by &#39;Laurin Müller&#39; from the &#39;European Environment Agency (EEA)&#39;. An error pop-up titled &#39;Error: TC18_Extraction_1&#39; is overlaid on a map of Liechtenstein and surrounding areas. The error message states: &#39;EXTRACTING_ERROR: No output was generated. Please check your selected areas (country &amp; region) and try again! See log with id &#39;93e70da4-0a39-4d53-800e-f716cc54fb18&#39; for more details. Please refresh the page, check the status and if applicable, try again.&#39; The pop-up has a &#39;CLOSE&#39; button. Behind the pop-up, the map shows &#39;Country *&#39; as &#39;LI Liechtenstein&#39; and &#39;Region *&#39; as &#39;LI0 Liechtenstein&#39;, with a refresh icon indicating &#39;map is outdated! REVIEW to generate the to your new input&#39;. The map includes a scale bar of &#39;5 km&#39; or &#39;3 mi&#39; and is attributed to &#39;Leaflet | EEA Copernicus programme, German Aerospace Center (DLR) CC-BY 3.0&#39;. Below the map, a table header for &#39;Input Classes&#39; is partially visible, with columns: &#39;Class Code&#39;, &#39;Name&#39;, &#39;Ingestion&#39;, &#39;Eagle Elements&#39;, &#39;100% Eagle compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39;. The overall status of the extraction is marked by a prominent red &#39;EXTRACTING_ERROR&#39; banner in the header."
alt="Graphical user interface, website Description automatically generated" />

A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core
User web interface, displaying an “Extraction” task named
“TC18_Extraction_1” in an error state. The left panel presents “General
Information” for the extraction, including Name: “TC18_Extraction_1”,
Country: “Liechtenstein”, Region: “Liechtenstein”, Reference Year:
“2021”, and Time Range of Extracted Data: “01.08.2021 - 28.08.2021”. The
task is associated with “INSPIRE Themes: AC Atmospheric conditions” and
was created by “Laurin Müller” from the “European Environment Agency
(EEA)”.

An error pop-up titled “Error: TC18_Extraction_1” is overlaid on a map
of Liechtenstein and surrounding areas. The error message states:
“EXTRACTING_ERROR: No output was generated. Please check your selected
areas (country & region) and try again! See log with id
‘93e70da4-0a39-4d53-800e-f716cc54fb18’ for more details. Please refresh
the page, check the status and if applicable, try again.” The pop-up has
a “CLOSE” button.

Behind the pop-up, the map shows “Country *” as ”LI Liechtenstein” and
”Region* ” as “LI0 Liechtenstein”, with a refresh icon indicating “map
is outdated! REVIEW to generate the to your new input”. The map includes
a scale bar of “5 km” or “3 mi” and is attributed to “Leaflet \| EEA
Copernicus programme, German Aerospace Center (DLR) CC-BY 3.0”. Below
the map, a table header for “Input Classes” is partially visible, with
columns: “Class Code”, “Name”, “Ingestion”, “Eagle Elements”, “100%
Eagle compliant”, “Colour”, and “Show in Map”. The overall status of the
extraction is marked by a prominent red “EXTRACTING_ERROR” banner in the
header.

## Add Extraction

Clicking the ‘**Add Extraction’** button (section
[4.2](#add-extraction)) opens the ’Add Extraction’ dialog where you have
to enter a name and define a country. Optional you can also enter a
region. In the following example, an Extraction for the LULUCF case in
the Netherlands will be done ([Figure 4‑2](#_Ref100140157)).

By clicking on ‘ADD’, you will be forwarded to the ‘Edit Extraction’
view ([Figure 4‑3](#_Ref153438205), section [4.3](#edit-extraction)).
Further, a new entry in the Data Catalogue table was created with status
‘Draft’ ([Figure 4‑4](#_Ref100140139)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image124.png"
style="width:6.925in;height:3.34653in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) &#39;Data Catalogue&#39; user interface, displaying a list of data instances and an overlaying modal dialog titled &#39;Add Extraction&#39;. The top navigation bar includes links for &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, with &#39;User Admin/Support CLC+ Core&#39; visible on the far right. The main &#39;Data Catalogue&#39; section features a filter bar with options like &#39;Filter...&#39;, &#39;My organisation&#39;, &#39;Ingesti...&#39;, and &#39;Extracti...&#39;. The table shows columns for &#39;Name&#39;, &#39;Type&#39;, and &#39;Status&#39;. Examples of data instance names visible are &#39;CLC+_Instance_LULUCF_2018_alpha_1&#39;, &#39;CLC+_Instance_LULUCF_2018_beta_10&#39;, &#39;CLC+_Instances_alphaV2.0_TEST_GAF&#39;, and &#39;LULUCF_testcase_CLMS&#39;. Corresponding statuses include &#39;PUBLISHED&#39;, &#39;EXTRACTED&#39;, &#39;DRAFT&#39;, and &#39;EXTRACTED_PREVIEW&#39;. Further details for specific instances show &#39;Owner&#39;, &#39;Country&#39;, and &#39;Timeframe&#39;, such as &#39;LULUCF_testcase_CLMS&#39; for &#39;Austria/Österreich&#39; with timeframe &#39;01.01.2015 - 31.12.2019&#39; and &#39;LULUCF_testcase_NL&#39; for &#39;Netherlands/Nederland&#39; with timeframe &#39;01.01.2015 - 31.12.2018&#39;. The &#39;Add Extraction&#39; dialog box prompts for three fields: &#39;Name *&#39; (pre-filled with &#39;CLC+ Instance_LULUCF_2021_NL&#39;), &#39;Country *&#39; (pre-filled with &#39;NL Netherlands/Nederland&#39;), and &#39;Region&#39; (pre-filled with &#39;NL11 Groningen&#39;). It provides &#39;CANCEL&#39; and &#39;ADD&#39; buttons. The background shows a blurry aerial image of agricultural land." />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) “Data Catalogue” user interface, displaying a list of data
instances and an overlaying modal dialog titled “Add Extraction”. The
top navigation bar includes links for “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”, with “User
Admin/Support CLC+ Core” visible on the far right. The main “Data
Catalogue” section features a filter bar with options like “Filter…”,
“My organisation”, “Ingesti…”, and “Extracti…”. The table shows columns
for “Name”, “Type”, and “Status”. Examples of data instance names
visible are “CLC+\_Instance_LULUCF_2018_alpha_1”,
“CLC+\_Instance_LULUCF_2018_beta_10”,
“CLC+\_Instances_alphaV2.0_TEST_GAF”, and “LULUCF_testcase_CLMS”.
Corresponding statuses include “PUBLISHED”, “EXTRACTED”, “DRAFT”, and
“EXTRACTED_PREVIEW”. Further details for specific instances show
“Owner”, “Country”, and “Timeframe”, such as “LULUCF_testcase_CLMS” for
“Austria/Österreich” with timeframe “01.01.2015 - 31.12.2019” and
“LULUCF_testcase_NL” for “Netherlands/Nederland” with timeframe
“01.01.2015 - 31.12.2018”. The “Add Extraction” dialog box prompts for
three fields: “Name *” (pre-filled with ”CLC+ Instance_LULUCF_2021_NL”),
”Country* ” (pre-filled with “NL Netherlands/Nederland”), and “Region”
(pre-filled with “NL11 Groningen”). It provides “CANCEL” and “ADD”
buttons. The background shows a blurry aerial image of agricultural
land.

<span id="_Ref153438205" class="anchor"></span>**Figure 4‑2: Add
Extraction – Add Extraction Dialog.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image125.png"
style="width:6.925in;height:3.29583in"
data-fig-alt="This image is a screenshot of a web application interface for data extraction, specifically titled &#39;Extraction &#39;CLC+ Instance_LULUCF_2021_NL&#39;&#39;. The extraction request is currently in &#39;DRAFT&#39; status. The left panel displays &#39;General Information&#39; about the extraction, including: - **Name**: CLC+ Instance_LULUCF_2021_NL - **Country**: Netherlands/Nederland - **Region**: Groningen - **Reference Year**: - (empty) - **Time Range of Extracted Data**: - (empty) - **INSPIRE Themes**: - (empty) - **Created By**: User Admin/Support CLC+ Core - **Organisation/s**: European Environment Agency (EEA) - **Contact Person**: (empty) An &#39;EDIT&#39; button is available next to the &#39;General Information&#39; heading. The top right section contains action buttons: &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START EXTRACTION&#39;, and &#39;PUBLISH&#39;. The central and right-hand side of the interface features an interactive map. Above the map, selection filters are active for &#39;Country * NL Netherlands/Nederland&#39; and &#39;Region * NL11 Groningen&#39;. The map displays a basemap covering parts of the Netherlands and Germany, with the selected region of Groningen highlighted in red. Overlay text on the map states, &#39;Your map is outdated! Please press &#39;PREVIEW&#39; to generate the map according to your new input,&#39; next to a &#39;PREVIEW&#39; button. Map controls include zoom in/out, fullscreen toggle, and a layer stack icon. A scale bar indicates &#39;30 km&#39; and &#39;10 mi&#39;. The map&#39;s attribution credits &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. Below the map, a collapsed section titled &#39;Input Classes&#39; is visible. The top navigation bar of the application includes &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, alongside &#39;User Admin/Support CLC+ Core&#39; links and notifications." />

This image is a screenshot of a web application interface for data
extraction, specifically titled “Extraction ‘CLC+
Instance_LULUCF_2021_NL’”. The extraction request is currently in
“DRAFT” status.

The left panel displays “General Information” about the extraction,
including: - **Name**: CLC+ Instance_LULUCF_2021_NL - **Country**:
Netherlands/Nederland - **Region**: Groningen - **Reference Year**: -
(empty) - **Time Range of Extracted Data**: - (empty) - **INSPIRE
Themes**: - (empty) - **Created By**: User Admin/Support CLC+ Core -
**Organisation/s**: European Environment Agency (EEA) - **Contact
Person**: (empty) An “EDIT” button is available next to the “General
Information” heading.

The top right section contains action buttons: “REPUBLISH ON GEOSERVER”,
“START EXTRACTION”, and “PUBLISH”.

The central and right-hand side of the interface features an interactive
map. Above the map, selection filters are active for “Country \* NL
Netherlands/Nederland” and “Region \* NL11 Groningen”. The map displays
a basemap covering parts of the Netherlands and Germany, with the
selected region of Groningen highlighted in red. Overlay text on the map
states, “Your map is outdated! Please press”PREVIEW” to generate the map
according to your new input,” next to a “PREVIEW” button. Map controls
include zoom in/out, fullscreen toggle, and a layer stack icon. A scale
bar indicates “30 km” and “10 mi”. The map’s attribution credits
“Leaflet \| © Core003 Mosaic, © OpenStreetMap contributors”.

Below the map, a collapsed section titled “Input Classes” is visible.
The top navigation bar of the application includes “Data Catalogue”,
“EAGLE Ontology”, “About EAGLE”, “Organisations”, and “Users”, alongside
“User Admin/Support CLC+ Core” links and notifications.

<span id="_Ref100140157" class="anchor"></span>**Figure 4‑3: Add
Extraction – Edit Extraction View.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image126.png"
style="width:6.925in;height:1.4375in"
data-fig-alt="The table displays entries from a data catalogue within a Copernicus Land Monitoring Service (CLMS) user interface, detailing metadata and status for each. The user interface also shows navigation options including &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. Filters are applied for &#39;My organisation&#39; and &#39;Extracting&#39; data, with additional action buttons for &#39;ADD INGEST...&#39; and &#39;ADD EXTRACT...&#39;. The table columns are: Name, Type, Created By, Country, Time Range, and Status. | Name | Type | Created By | Country | Time Range | Status | |---|---|---|---|---|---| | CLC+ Instance_LULUCF_2021_NL | Extraction (icon) | User Admin/Support CLC+ Core | Netherlands/Nederland | - | DRAFT | | Test Instances Issue with Eurocrop = 0 | Extraction (icon) | User Admin/Support CLC+ Core | Germany/Deutschland | 01.08.2023 - 31.08.2023 | EXTRACTED | The first entry, &#39;CLC+ Instance_LULUCF_2021_NL&#39;, is for the Netherlands/Nederland and is in &#39;DRAFT&#39; status with no specified time range. The second entry, &#39;Test Instances Issue with Eurocrop = 0&#39;, is for Germany/Deutschland, covers the time range 01.08.2023 to 31.08.2023, and has an &#39;EXTRACTED&#39; status. Both entries are of &#39;Extraction&#39; type and were created by &#39;User Admin/Support CLC+ Core&#39;. The table is cut off, showing only these two entries." />

The table displays entries from a data catalogue within a Copernicus
Land Monitoring Service (CLMS) user interface, detailing metadata and
status for each. The user interface also shows navigation options
including “Data Catalogue”, “EAGLE Ontology”, “About EAGLE”,
“Organisations”, and “Users”. Filters are applied for “My organisation”
and “Extracting” data, with additional action buttons for “ADD INGEST…”
and “ADD EXTRACT…”. The table columns are: Name, Type, Created By,
Country, Time Range, and Status.

| Name | Type | Created By | Country | Time Range | Status |
|----|----|----|----|----|----|
| CLC+ Instance_LULUCF_2021_NL | Extraction (icon) | User Admin/Support CLC+ Core | Netherlands/Nederland | \- | DRAFT |
| Test Instances Issue with Eurocrop = 0 | Extraction (icon) | User Admin/Support CLC+ Core | Germany/Deutschland | 01.08.2023 - 31.08.2023 | EXTRACTED |

The first entry, “CLC+ Instance_LULUCF_2021_NL”, is for the
Netherlands/Nederland and is in ‘DRAFT’ status with no specified time
range. The second entry, “Test Instances Issue with Eurocrop = 0”, is
for Germany/Deutschland, covers the time range 01.08.2023 to 31.08.2023,
and has an ‘EXTRACTED’ status. Both entries are of “Extraction” type and
were created by “User Admin/Support CLC+ Core”. The table is cut off,
showing only these two entries.

<span id="_Ref100140139" class="anchor"></span>**Figure 4‑4: Add
Extraction – A new entry in the table was created with status ‘draft’.**

## Edit Extraction

Before an Extraction can be published you need to set the Extraction
settings, select the specific Input Classes and create Output Classes
with the help of Extraction rules. To prevent mistakes, you can preview
your results within a specific NUTS region in a Map Viewer. This view is
very similar to the Edit Ingestion (section [3.7](#edit-ingestion)) one.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image127.png"
style="width:6.925in;height:3.27153in"
data-fig-alt="This image is a screenshot of a web-based user interface for managing and previewing a Copernicus Land Monitoring Service (CLMS) &#39;Extraction&#39; of CLC+ (next-generation land cover/land use) data. The specific instance is named &#39;CLC+ Instance_LULUCF_2021_NL&#39; and is in a DRAFT state. The interface is structured into several sections: 1. **Top Navigation Bar**: Includes links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, along with user administration for &#39;CLC+ Core&#39;. 2. **Extraction Workflow Actions**: Buttons in the top right allow &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START EXTRACTION&#39;, and &#39;PUBLISH&#39;. 3. **General Information (left panel)**: * **Name**: CLC+ Instance_LULUCF_2021_NL * **Country**: Netherlands/Nederland * **Region**: Groningen * **Reference Year**: - * **Time Range of Extracted Data**: - * **INSPIRE Themes**: (link icon) * **Created By**: User Admin/Support CLC+ Core * **Organisation/s**: European Environment Agency (EEA) * **Contact Person**: - * **Link to Document/s**: - * **Description**: - An &#39;EDIT&#39; button is present to modify this information. 4. **Interactive Map (top right panel)**: Displays a base map of the Netherlands, with the region of Groningen highlighted. Filters for &#39;Country&#39; (NL Netherlands/Nederland) and &#39;Region&#39; (NL11 Groningen) are applied. A message overlay states &#39;Your map is outdated! Please press &#39;PREVIEW&#39; to generate the map according to your new input.&#39; The map includes zoom controls, a full-screen toggle, a layer control, a 30 km / 10 mi scale bar, and Leaflet, Core003 Mosaic, and OpenStreetMap attributions. 5. **Input Classes (middle right panel)**: A table defining input land cover classes. * **Rank**: 1. * **Class Code**: 3 * **Name**: Additional woody features * **Ingestion**: HRL - Small Woody Features (SWF) * **Eagle Elements**: Woody Vegetation * **100% Eagle compliant**: (checkbox) * **Colour**: Yellow square * **Show in Map**: Toggle switch (on) 6. **Output Classes (bottom right panel)**: A table for defining output land cover classes based on rulesets. * **Rank**: 1. * **Class Code ***: (input field for Class Code) * **Name ***: (input field for Name) * **Ruleset ***: (input field for Rule) * **Colour**: Green square * **Show in Map**: Toggle switch (on) 7. **Additional Documents (bottom left panel)**: Allows users to &#39;Drag and Drop&#39; or &#39;UPLOAD DOCUMENT/S&#39;." />

This image is a screenshot of a web-based user interface for managing
and previewing a Copernicus Land Monitoring Service (CLMS) “Extraction”
of CLC+ (next-generation land cover/land use) data. The specific
instance is named “CLC+ Instance_LULUCF_2021_NL” and is in a DRAFT
state.

The interface is structured into several sections: 1. **Top Navigation
Bar**: Includes links to “Data Catalogue”, “EAGLE Ontology”, “About
EAGLE”, “Organisations”, and “Users”, along with user administration for
“CLC+ Core”. 2. **Extraction Workflow Actions**: Buttons in the top
right allow “REPUBLISH ON GEOSERVER”, “START EXTRACTION”, and “PUBLISH”.
3. **General Information (left panel)**: \* **Name**: CLC+
Instance_LULUCF_2021_NL \* **Country**: Netherlands/Nederland \*
**Region**: Groningen \* **Reference Year**: - \* **Time Range of
Extracted Data**: - \* **INSPIRE Themes**: (link icon) \* **Created
By**: User Admin/Support CLC+ Core \* **Organisation/s**: European
Environment Agency (EEA) \* **Contact Person**: - \* **Link to
Document/s**: - \* **Description**: - An “EDIT” button is present to
modify this information. 4. **Interactive Map (top right panel)**:
Displays a base map of the Netherlands, with the region of Groningen
highlighted. Filters for “Country” (NL Netherlands/Nederland) and
“Region” (NL11 Groningen) are applied. A message overlay states “Your
map is outdated! Please press”PREVIEW” to generate the map according to
your new input.” The map includes zoom controls, a full-screen toggle, a
layer control, a 30 km / 10 mi scale bar, and Leaflet, Core003 Mosaic,
and OpenStreetMap attributions. 5. **Input Classes (middle right
panel)**: A table defining input land cover classes. \* **Rank**: 1. \*
**Class Code**: 3 \* **Name**: Additional woody features \*
**Ingestion**: HRL - Small Woody Features (SWF) \* **Eagle Elements**:
Woody Vegetation \* **100% Eagle compliant**: (checkbox) \* **Colour**:
Yellow square \* **Show in Map**: Toggle switch (on) 6. **Output Classes
(bottom right panel)**: A table for defining output land cover classes
based on rulesets. \* **Rank**: 1. \* **Class Code** *: (input field for
Class Code)* **Name** *: (input field for Name)* **Ruleset** *: (input
field for Rule)* **Colour**: Green square \* **Show in Map**: Toggle
switch (on) 7. **Additional Documents (bottom left panel)**: Allows
users to “Drag and Drop” or “UPLOAD DOCUMENT/S”.

<span id="_Ref153953950" class="anchor"></span>**Figure 4‑5: Edit
Extraction.**

In the left section (**General Information**) (see [Figure
4‑5](#_Ref153953950) and [Figure 4‑6](#_Ref153953951)) you can review
all Extraction settings and update them if necessary. Reference year,
Time range and [INSPIRE
Themes](https://inspire.ec.europa.eu/Themes/Data-Specifications/2892)
are mandatory.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image128.png"
style="width:2.95803in;height:4.06668in"
data-fig-alt="A screenshot of the &#39;General Information&#39; section within the &#39;Edit Extraction&#39; view of a Copernicus Land Monitoring Service (CLMS) CLC+ Core application. This user interface displays editable details about a specific data extraction. In the top right corner, there is a green &#39;EDIT&#39; button with a pencil icon. The fields and their current values are: - Name: &#39;CLC+ Instance_LULUCF_2021_NL&#39; - Country: &#39;Netherlands/Nederland&#39; - Region: &#39;Groningen&#39; - Reference Year: &#39;-&#39; - Time Range of Extracted Data: &#39;-&#39; (accompanied by a question mark icon for help) - INSPIRE Themes: &#39;-&#39; (accompanied by an external link icon) - Created By: &#39;User Admin/Support CLC+ Core&#39; (displayed as a clickable link) - Organisation/s: &#39;European Environment Agency&#39; (displayed as a clickable link) - Contact Person: &#39;-&#39; - Link to Document/s: &#39;-&#39; (accompanied by a question mark icon for help) - Description: &#39;-&#39;" />
<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image129.png"
style="width:2.96445in;height:4.03454in"
data-fig-alt="This image displays a screenshot of the &#39;General Information&#39; dialog box used for adding a new data &#39;Extraction&#39; within the Copernicus Land Monitoring Service (CLMS) CLC+ Core application. The dialog presents several input fields and their pre-filled values for defining extraction parameters. The fields shown are: - &#39;Name *&#39;: &#39;CLC+ Instance_LULUCF_2021_NL&#39; - &#39;Country *&#39;: &#39;NL Netherlands/Nederland&#39; - &#39;Region&#39;: &#39;NL11 Groningen&#39; - &#39;Reference Year *&#39;: &#39;2018&#39; - &#39;Time Range of Extracted Data *&#39;: &#39;01.01.2018 – 31.12.2018&#39;, accompanied by the descriptive text &#39;The time range of when the data was produced.&#39; - &#39;INSPIRE Themes *&#39;: Currently selected themes are &#39;LC Land cover&#39; and &#39;LU Land use&#39;. A hyperlink labeled &#39;INSPIRE theme register&#39; is provided for further details on Infrastructure for Spatial Information in the European Community (INSPIRE) themes. - &#39;Created By&#39;: &#39;User Admin/Support CLC+ Core&#39; (displayed as a clickable link) - &#39;Organisation/s *&#39;: &#39;European Environment Agency&#39; (EEA) Asterisks indicate mandatory fields. At the top right of the dialog, &#39;CANCEL&#39; and &#39;SAVE&#39; action buttons are visible. The populated fields specify an extraction related to Land Use, Land-Use Change and Forestry (LULUCF) data for the Netherlands, focusing on the Groningen region, with a reference year and data production time range of 2018." />

<span id="_Ref153953951" class="anchor"></span>**Figure 4‑6: Edit
Extraction - Review all Extraction settings and update them if
necessary. Reference year, Time range and INSPIRE Themes are
mandatory.**

Further, users are able to upload additional (already existing) datasets
such as EAGLE matrix or style files (CLR, QML) or metadata information
(txt, xml) ([Figure 4‑7](#_Ref153644917)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image130.png"
style="width:3.45744in;height:1.8518in"
data-fig-alt="This image is a screenshot of a user interface section titled &#39;Additional Documents&#39;. It displays a rectangular dashed-line box labeled &#39;Drag and Drop&#39; in the center, with &#39;OR&#39; below it. Underneath &#39;OR&#39;, there is a green-outlined button with a green upward arrow icon and the text &#39;UPLOAD DOCUMENT/S&#39;. Below the dashed box, explanatory grey text reads: &#39;All documents that help to understand the content. (No file type restrictions)&#39;. This interface provides two methods for users to add supplementary files to a system entry, likely within a Copernicus Land Monitoring Service (CLMS) data extraction or management process." />

This image is a screenshot of a user interface section titled
“Additional Documents”. It displays a rectangular dashed-line box
labeled “Drag and Drop” in the center, with “OR” below it. Underneath
“OR”, there is a green-outlined button with a green upward arrow icon
and the text “UPLOAD DOCUMENT/S”. Below the dashed box, explanatory grey
text reads: “All documents that help to understand the content. (No file
type restrictions)”. This interface provides two methods for users to
add supplementary files to a system entry, likely within a Copernicus
Land Monitoring Service (CLMS) data extraction or management process.

<span id="_Ref153644917" class="anchor"></span>**Figure 4‑7: Upload of
additional datasets such as EAGLE matrix or style files.**

In the next step, you need to **define the Input Classes** you want to
use for your Extraction. By clicking on the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image131.png"
style="width:0.16875in;height:0.16875in"
data-fig-alt="A grayscale user interface icon featuring a black plus sign (+) centered within a black circular outline. The icon has a slightly blurred or soft-edged appearance against a white background. In the context of the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover Plus) application, this icon typically represents an action to &#39;Add&#39; or &#39;Create New&#39; entries, such as a new Extraction or new Extraction settings, as suggested by its proximity to &#39;Add Extraction&#39; sections in the documentation." />
icon, in the area “**Input Classes**” you can **add Input Classes**
which are already ingested into CLC+ Core (see [Figure
4‑8](#_Ref153954099)). The **“Select Input Classes”** menu opens and the
dataset can be selected by checking the tick box. By clicking on the
**“Confirm Selection”** button, the data will be taken into the
Extraction view. Details about this step can be found at section [4.4
Add Input Classes to Extraction](#add-input-classes-to-extraction).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image132.png"
style="width:6.10264in;height:1.69875in"
data-fig-alt="This table displays the configuration settings for an Input Class within the Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation land cover/land use) Extraction user interface. The table includes eight columns: &#39;Rank&#39;, &#39;Class Code&#39;, &#39;Name&#39;, &#39;Ingestion&#39;, &#39;Eagle Elements&#39;, &#39;100% Eagle compliant&#39;, &#39;Colour&#39;, and &#39;Show in Map&#39;. The headers &#39;Rank&#39; and &#39;100% Eagle compliant&#39; have a question mark icon, indicating associated help text. The table contains one visible entry: | Rank | Class Code | Name | Ingestion | Eagle Elements | 100% Eagle compliant | Colour | Show in Map | |---|---|---|---|---|---|---|---| | 1. | 3 | Additional wood... | High Resolution Layer (HRL) - Small Woody Features | Woody Vegetation +3 | Yes | Yellow | Off | The &#39;Name&#39; column displays &#39;Additional wood...&#39;, which is a truncated label, and the &#39;Ingestion&#39; column specifies &#39;High Resolution Layer (HRL) - Small Woody Features&#39;, indicating the source data for this class. The &#39;Eagle Elements&#39; column shows an icon labelled &#39;Woody Vegetation&#39; followed by &#39;+3&#39;. The &#39;100% Eagle compliant&#39; status is checked (Yes). The &#39;Colour&#39; assigned for this class is yellow, and the &#39;Show in Map&#39; toggle switch is in the &#39;Off&#39; position. A plus icon within a circle is present below the table, indicating functionality to add new entries. This table details the selection and properties of an input class, likely for defining land cover extraction rules." />

This table displays the configuration settings for an Input Class within
the Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation land
cover/land use) Extraction user interface. The table includes eight
columns: “Rank”, “Class Code”, “Name”, “Ingestion”, “Eagle Elements”,
“100% Eagle compliant”, “Colour”, and “Show in Map”. The headers “Rank”
and “100% Eagle compliant” have a question mark icon, indicating
associated help text.

The table contains one visible entry: \| Rank \| Class Code \| Name \|
Ingestion \| Eagle Elements \| 100% Eagle compliant \| Colour \| Show in
Map \| \|—\|—\|—\|—\|—\|—\|—\|—\| \| 1. \| 3 \| Additional wood… \| High
Resolution Layer (HRL) - Small Woody Features \| Woody Vegetation +3 \|
Yes \| Yellow \| Off \|

The “Name” column displays “Additional wood…”, which is a truncated
label, and the “Ingestion” column specifies “High Resolution Layer
(HRL) - Small Woody Features”, indicating the source data for this
class. The “Eagle Elements” column shows an icon labelled “Woody
Vegetation” followed by “+3”. The “100% Eagle compliant” status is
checked (Yes). The “Colour” assigned for this class is yellow, and the
“Show in Map” toggle switch is in the ‘Off’ position. A plus icon within
a circle is present below the table, indicating functionality to add new
entries. This table details the selection and properties of an input
class, likely for defining land cover extraction rules.

<span id="_Ref153954099" class="anchor"></span>**Figure 4‑8: Add or
delete Input Classes.**

As a next step you need to create Output Classes and define Class
Conditions for them. Creating new Output Classes is possible by clicking
on in the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image131.png"
style="width:0.16875in;height:0.16875in"
data-fig-alt="A grayscale user interface icon featuring a black plus sign (+) centered within a black circular outline. The icon has a slightly blurred or soft-edged appearance against a white background. In the context of the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover Plus) application, this icon typically represents an action to &#39;Add&#39; or &#39;Create New&#39; entries, such as a new Extraction or new Extraction settings, as suggested by its proximity to &#39;Add Extraction&#39; sections in the documentation." />
icon in the area “**Output Classes**” (see [Figure
4‑9](#_Ref105168124)). Once you have triggered this action, a new and
Output Class will be added and you have to define the specific
attributes such as the class code, name and the Class Condition
(ruleset) ([Figure 4‑9](#_Ref105168124)). Further, you can specify a
class colour and if you want to have this Extraction displayed in the
Map preview or not. The class code is the value you assign to an Output
Class, the name should be class descriptive (i.e. class 1 – woodland
stands, 2 – unmanaged woodland, etc.).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image133.png"
style="width:6.35558in;height:1.75843in"
data-fig-alt="A user interface element for defining &#39;Output Classes&#39; within the Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation land cover/land use) Core User Manual&#39;s Edit Extraction section. The table-like structure allows users to define parameters for each output land cover class. The column headers are: | Rank | Class Code * | Name * | Ruleset * | Colour | Show In Map | |---|---|---|---|---|---| | 1. | 1 | Grassland | Rule * | &lt;square checkbox&gt; | &lt;toggle switch&gt; | Currently, one output class is defined: - **Rank:** 1. - **Class Code:** 1 (with placeholder text &#39;Class Code *&#39;) - **Name:** Grassland (with placeholder text &#39;Name *&#39;) - **Ruleset:** &#39;Rule *&#39; (accompanied by an icon for rule definition) - **Colour:** An empty square checkbox, indicating no specific colour is currently selected. - **Show In Map:** A grey toggle switch indicating the feature is currently turned off. An overall toggle switch for &#39;Show In Map&#39; is present in the header, shown in green (on state), potentially indicating a default setting or a global control for all classes. Below the single class entry, a circular icon with a plus sign (+) allows adding more output classes. This table allows users to select input classes and create output classes using extraction rules for land cover data." />

A user interface element for defining “Output Classes” within the
Copernicus Land Monitoring Service (CLMS) CLC+ (next-generation land
cover/land use) Core User Manual’s Edit Extraction section. The
table-like structure allows users to define parameters for each output
land cover class.

The column headers are: \| Rank \| Class Code \* \| Name \* \| Ruleset
\* \| Colour \| Show In Map \| \|—\|—\|—\|—\|—\|—\| \| 1. \| 1 \|
Grassland \| Rule \* \| <square checkbox> \| <toggle switch> \|

Currently, one output class is defined: - **Rank:** 1. - **Class Code:**
1 (with placeholder text “Class Code *”) - **Name:** Grassland (with
placeholder text ”Name* ”) - **Ruleset:** “Rule \*” (accompanied by an
icon for rule definition) - **Colour:** An empty square checkbox,
indicating no specific colour is currently selected. - **Show In Map:**
A grey toggle switch indicating the feature is currently turned off.

An overall toggle switch for “Show In Map” is present in the header,
shown in green (on state), potentially indicating a default setting or a
global control for all classes. Below the single class entry, a circular
icon with a plus sign (+) allows adding more output classes. This table
allows users to select input classes and create output classes using
extraction rules for land cover data.

<span id="_Ref105168124" class="anchor"></span>**Figure 4‑9: Add or
delete Output Classes.**

Once you have defined the specific attributes for the Output Classes,
you need to **add Class Conditions** to the Output Classes. You can do
that by clicking directly on the Class Condition (Rule) field at each
Output Classes row ([Figure 4‑9](#_Ref105168124)). Details about how to
create Class Conditions can be found at section
[4.5.1](#some-definitions-for-a-better-understanding-also-see-glossary).

Optionally, create a preliminary view of the Extraction by selecting a
certain NUTS region in the map and clicking the “**Preview**” button
(see [Figure 4‑10](#_Ref153954681) and section
[4.7](#preview-extraction-and-download-result)). Further, you are able
to download the result.

Once all settings and the test result have been reviewed you can start
the Extraction process by clicking on the “**start Extraction**” button
([Figure 4‑5](#_Ref153953950) and [Figure 4‑11](#_Ref153651792)). Once
the Extraction has already been processed, you can publish the
Extraction to make it available for other users. See also at section
**[4.8](#publish-extraction-and-download-result) [Publish
Extraction](#publish-extraction-and-download-result)**. Further, you are
able to download the result.

**After starting the Extraction, a pop-up window will appear asking if
you really want to proceed as the Extraction may take a while. Further,
it is indicating that EAGLE elements are used within the rules that are
not corresponding to the available Input Classes. Please check if the
correct EAGLE element and the correct barcode value is applied! The
warning can be ignored but may affect the result!** (see [Figure
4‑10](#_Ref153954681)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image134.png"
style="width:6.5652in;height:3.26614in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core web application interface, displaying an extraction configuration for &#39;CLC+ Instance_LULUCF_2021_NL&#39; in DRAFT status. The interface includes a header with navigation links such as &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. On the left, a &#39;General Information&#39; panel details: * Name: CLC+ Instance_LULUCF_2021_NL * Country: Netherlands/Nederland * Region: Groningen * Reference Year: 2018 * Time Range of Extracted Data: 01.12.2018 - 31.12.2018 * INSPIRE Themes: LU Land use, LC Land cover * Created By: User Admin/Support CLC+ Core * Organisation/s: European Environment Agency A central pop-up modal titled &#39;Start Extraction &#39;CLC+ Instance_LULUCF_2021_NL&#39;&#39; asks for confirmation to start the extraction, noting it may take time. It recommends selecting a smaller region for faster &#39;preview&#39; results. A warning states: &#39;EAGLE element used within rule, but no corresponding input class available&#39;, specifically mentioning &#39;Sealed Artificial Surfaces and Constructions with barcode 5&#39;, and advises adapting extraction rulesets or adding necessary input classes. The pop-up offers &#39;CANCEL&#39; and &#39;START EXTRACTING&#39; buttons. The right side of the screen shows a map interface with a selected region labeled &#39;NL11 Groningen&#39; and a &#39;PREVIEW&#39; button. A scale bar indicates &#39;30 km&#39; and &#39;10 mi&#39;. Map attribution is &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. Part of the map has overlaid text reading &#39;outdated! To generate the new input&#39;. A partially visible section at the bottom is labeled &#39;Input Classes&#39;." />

A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core
web application interface, displaying an extraction configuration for
“CLC+ Instance_LULUCF_2021_NL” in DRAFT status. The interface includes a
header with navigation links such as “Data Catalogue”, “EAGLE Ontology”,
“Organisations”, and “Users”.

On the left, a “General Information” panel details: \* Name: CLC+
Instance_LULUCF_2021_NL \* Country: Netherlands/Nederland \* Region:
Groningen \* Reference Year: 2018 \* Time Range of Extracted Data:
01.12.2018 - 31.12.2018 \* INSPIRE Themes: LU Land use, LC Land cover \*
Created By: User Admin/Support CLC+ Core \* Organisation/s: European
Environment Agency

A central pop-up modal titled “Start Extraction ‘CLC+
Instance_LULUCF_2021_NL’” asks for confirmation to start the extraction,
noting it may take time. It recommends selecting a smaller region for
faster “preview” results. A warning states: “EAGLE element used within
rule, but no corresponding input class available”, specifically
mentioning “Sealed Artificial Surfaces and Constructions with barcode
5”, and advises adapting extraction rulesets or adding necessary input
classes. The pop-up offers “CANCEL” and “START EXTRACTING” buttons.

The right side of the screen shows a map interface with a selected
region labeled “NL11 Groningen” and a “PREVIEW” button. A scale bar
indicates “30 km” and “10 mi”. Map attribution is “Leaflet \| © Core003
Mosaic, © OpenStreetMap contributors”. Part of the map has overlaid text
reading “outdated! To generate the new input”. A partially visible
section at the bottom is labeled “Input Classes”.

<span id="_Ref153954681" class="anchor"></span>**Figure 4‑10: Pop up
window asking to proceed. Indicating that EAGLE elements are used within
the rules that are not corresponding to the available Input Classes.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image135.png"
style="width:6.925in;height:3.28611in"
data-fig-alt="This is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core web application user interface, displaying an active data extraction process for a Land Use, Land-Use Change and Forestry (LULUCF) instance. The top navigation bar includes links to &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;, along with &#39;User Admin/Support CLC+ Core&#39;. The main panel shows &#39;Extraction &#39;CLC+ Instance_LULUCF_2021_NL&#39;&#39; with an &#39;EXTRACTING&#39; status and a clock icon, along with a &#39;REPUBLISH ON GEOSERVER&#39; button. A left-hand &#39;General Information&#39; sidebar provides details about the extraction: * **Name**: CLC+ Instance_LULUCF_2021_NL * **Country**: Netherlands/Nederland * **Region**: Groningen * **Reference Year**: 2018 * **Time Range of Extracted Data**: 01.12.2018 - 31.12.2018 * **INSPIRE Themes**: LU Land use, LC Land cover * **Created By**: User Admin/Support CLC+ Core * **Organisation/s**: European Environment Agency (EEA) The main content area features an interactive map displaying a greyscale basemap of the Netherlands and parts of Germany. Overlays indicate the selected &#39;Country: NL Netherlands/Nederland&#39; and &#39;Region: NL11 Groningen&#39;. A small green polygon highlights a specific area of interest on the map. Below the map controls (zoom, full extent, download envelope), a message states: &#39;The process is running. Once done, this page is refreshed. [Data preview is outdated!] Please press &#39;PREVIEW&#39; to generate the [new] map according to your new input.&#39; An &#39;OPEN DATA CATALOGUE&#39; button is present. The map attribution is &#39;Leaflet | © Core003 Mosaic. © OpenStreetMap contributors&#39;. A scale bar shows &#39;30 km&#39; and &#39;10 mi&#39;. The bottom left indicates &#39;Input Classes&#39; as a section header. A blue circular help icon is visible in the bottom right corner." />

This is a screenshot of the Copernicus Land Monitoring Service (CLMS)
CLC+ Core web application user interface, displaying an active data
extraction process for a Land Use, Land-Use Change and Forestry (LULUCF)
instance. The top navigation bar includes links to “Data Catalogue”,
“EAGLE Ontology”, “About EAGLE”, “Organisations”, and “Users”, along
with “User Admin/Support CLC+ Core”.

The main panel shows “Extraction ‘CLC+ Instance_LULUCF_2021_NL’” with an
“EXTRACTING” status and a clock icon, along with a “REPUBLISH ON
GEOSERVER” button.

A left-hand “General Information” sidebar provides details about the
extraction: \* **Name**: CLC+ Instance_LULUCF_2021_NL \* **Country**:
Netherlands/Nederland \* **Region**: Groningen \* **Reference Year**:
2018 \* **Time Range of Extracted Data**: 01.12.2018 - 31.12.2018 \*
**INSPIRE Themes**: LU Land use, LC Land cover \* **Created By**: User
Admin/Support CLC+ Core \* **Organisation/s**: European Environment
Agency (EEA)

The main content area features an interactive map displaying a greyscale
basemap of the Netherlands and parts of Germany. Overlays indicate the
selected “Country: NL Netherlands/Nederland” and “Region: NL11
Groningen”. A small green polygon highlights a specific area of interest
on the map. Below the map controls (zoom, full extent, download
envelope), a message states: “The process is running. Once done, this
page is refreshed. \[Data preview is outdated!\] Please press”PREVIEW”
to generate the \[new\] map according to your new input.” An “OPEN DATA
CATALOGUE” button is present. The map attribution is “Leaflet \| ©
Core003 Mosaic. © OpenStreetMap contributors”. A scale bar shows “30 km”
and “10 mi”. The bottom left indicates “Input Classes” as a section
header. A blue circular help icon is visible in the bottom right corner.

<span id="_Ref153651792" class="anchor"></span>**Figure 4‑11: After
starting the Extraction process.**

## Add Input Classes to Extraction

After you clicked on the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image131.png"
style="width:0.16875in;height:0.16875in"
data-fig-alt="A grayscale user interface icon featuring a black plus sign (+) centered within a black circular outline. The icon has a slightly blurred or soft-edged appearance against a white background. In the context of the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover Plus) application, this icon typically represents an action to &#39;Add&#39; or &#39;Create New&#39; entries, such as a new Extraction or new Extraction settings, as suggested by its proximity to &#39;Add Extraction&#39; sections in the documentation." />
icon within the area “**Input Classes**” the **“Select Input Classes”**
menu opens. You can select which are already ingested into CLC+ Core and
that you want to use for your Extraction by checking the tick box. You
can multi-select (more than one possible) Input Classes and also see
information about them within the table. Use the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image136.png"
style="width:0.40278in;height:0.17845in"
data-fig-alt="A graphical user interface icon, enclosed within a rounded rectangular border in light green. The icon itself is rendered in a darker shade of green. It depicts a stylized table (a rectangle with three vertical lines and one horizontal line at the top) on the left, and a downward-pointing chevron symbol on the right. This icon is used in the Copernicus Land Monitoring Service (CLMS) CLC+ Core software to add Input Classes or create Output Classes, initiating a selection menu." />
icon to add or remove columns for data information such as Name, Created
at/by, Reference Year, EAGLE comliance, etc ([Figure
4‑12](#_Ref153650700)).

Additionally, you have the possibility to **search** for specific Input
Classes using the search field and the filter panel. In the filter panel
([Figure 4‑13](#_Ref153649503)) you can sear for data matching your
criteria. Further, there is an option to toggle on/off “100 EAGLE
compliant” or “EAGLE approved”. The list on the right is updated
accordingly.

Further, you can reduce the list of data to data, ingested only by your
or your organisation ([Figure 4‑12](#_Ref153650700)).

By hovering the mouse over the EAGLE elements column, a tooltip dialog
opens, displaying all barcoded EAGLE elements for this Input Class
([Figure 4‑14](#_Ref153650770)). The EAGLE barcoding can be opened in a
new tab to be inspected in more detail by clicking on the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image137icon.png"
style="width:0.17361in;height:0.17361in"
data-fig-alt="A screenshot of a software interface displaying the &#39;Output Classes&#39; configuration section within the Copernicus Land Monitoring Service (CLMS) CLC+ Core User Manual. The interface features a table for defining output classes with the following columns: &#39;Code&#39;, &#39;Name&#39;, &#39;Class Condition (Rule)&#39;, &#39;Colour&#39;, and &#39;Display in Map&#39;. Two example output classes are shown: 1. **Code:** &#39;1&#39;, **Name:** &#39;Woodland stands&#39;, **Class Condition (Rule):** &#39;LC_NAME == &#39;Woodland stands&#39;&#39;, **Colour:** (green colour swatch), **Display in Map:** (checked checkbox). 2. **Code:** &#39;2&#39;, **Name:** &#39;Unmanaged woodland&#39;, **Class Condition (Rule):** &#39;LC_NAME == &#39;Unmanaged woodland&#39;&#39;, **Colour:** (darker green colour swatch), **Display in Map:** (checked checkbox). To the right of the &#39;Output Classes&#39; section title, there is an icon (plus sign) to add new output classes. Below the table, there are two buttons: &#39;Add new Output Class&#39; (with a plus icon) and &#39;Delete selected Output Class&#39; (with a minus icon)." />
icon ([Figure 4‑15](#_Ref153650763)).

In the last step you click on the **“Confirm Selection”** button in
order to apply them. The data will be taken into the Extraction view
([Figure 4‑12](#_Ref153650700)).

Back in the Extraction view, the selected data can be seen ([Figure
4‑16](#_Ref105172435)). By clicking on the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image131.png"
style="width:0.16875in;height:0.16875in"
data-fig-alt="A grayscale user interface icon featuring a black plus sign (+) centered within a black circular outline. The icon has a slightly blurred or soft-edged appearance against a white background. In the context of the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover Plus) application, this icon typically represents an action to &#39;Add&#39; or &#39;Create New&#39; entries, such as a new Extraction or new Extraction settings, as suggested by its proximity to &#39;Add Extraction&#39; sections in the documentation." />
icon at the end of the Input Classes, you are able to add more classes
and of course you can delete classes from your current selection by
clicking on the delete symbol ([Figure 4‑17](#_Ref105172428)). Same as
in the “Select Input Classes” View, hovering your mouse over the EAGLE
elements column, a tooltip dialog opens, displaying all barcoded EAGLE
elements for this Input Class ([Figure 4‑17](#_Ref105172428)). The EAGLE
barcoding can be opened in a new tab to be inspected in more detail by
clicking on the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image137icon.png"
style="width:0.17361in;height:0.17361in"
data-fig-alt="A screenshot of a software interface displaying the &#39;Output Classes&#39; configuration section within the Copernicus Land Monitoring Service (CLMS) CLC+ Core User Manual. The interface features a table for defining output classes with the following columns: &#39;Code&#39;, &#39;Name&#39;, &#39;Class Condition (Rule)&#39;, &#39;Colour&#39;, and &#39;Display in Map&#39;. Two example output classes are shown: 1. **Code:** &#39;1&#39;, **Name:** &#39;Woodland stands&#39;, **Class Condition (Rule):** &#39;LC_NAME == &#39;Woodland stands&#39;&#39;, **Colour:** (green colour swatch), **Display in Map:** (checked checkbox). 2. **Code:** &#39;2&#39;, **Name:** &#39;Unmanaged woodland&#39;, **Class Condition (Rule):** &#39;LC_NAME == &#39;Unmanaged woodland&#39;&#39;, **Colour:** (darker green colour swatch), **Display in Map:** (checked checkbox). To the right of the &#39;Output Classes&#39; section title, there is an icon (plus sign) to add new output classes. Below the table, there are two buttons: &#39;Add new Output Class&#39; (with a plus icon) and &#39;Delete selected Output Class&#39; (with a minus icon)." />
icon.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image138.png"
style="width:6.925in;height:3.28542in"
data-fig-alt="This is a screenshot of a web application interface within the Copernicus Land Monitoring Service (CLMS) for selecting input classes, specifically for a &#39;CLC+ Instance_LULUCF_2021_NL&#39; data extraction. The user interface features a top navigation bar with &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39; tabs, and a &#39;User Admin/Support CLC+ Core&#39; profile. Breadcrumbs indicate the current navigation path: &#39;Data Catalogue / Extraction &#39;CLC+ Instance_LULUCF_2021_NL&#39; / Select Input Classes&#39;. The main section is titled &#39;Select Input Classes (1)&#39;. It contains action buttons and a filter panel on the left, and a data table listing available input classes on the right. The top action bar includes &#39;Filter&#39; (with a funnel icon), &#39;My organisation/s&#39; (selected with a checkmark), &#39;My data&#39; buttons, and a search bar. On the right, &#39;CANCEL&#39; and &#39;CONFIRM SELECTION&#39; (highlighted green) buttons are present, along with a dropdown menu showing display/filter options. The &#39;Filter&#39; panel on the left allows users to filter by &#39;Country&#39;, &#39;Region&#39;, &#39;Reference Year&#39;, &#39;Time range&#39;, and &#39;EAGLE Elements&#39;, and includes a toggle for &#39;100% EAGLE Compliant&#39;. The main data table lists input classes with the following columns: an initial unchecked selection box, &#39;EAGLE Approved&#39; (with checkmarks for approved items), &#39;Name&#39;, &#39;Ingestion&#39;, &#39;Created By&#39;, &#39;Created At&#39;, &#39;EAGLE Elements&#39;, and a final checkbox for row selection. Example class names visible include &#39;Additional woody features&#39;, &#39;Small woody features&#39;, &#39;All non-forest type&#39;, &#39;Broadleaved forest type&#39;, &#39;Coniferous forest type&#39;, &#39;built-up&#39;, and &#39;non built-up&#39;. The &#39;Ingestion&#39; column specifies the High Resolution Layer (HRL) source, such as &#39;HRL - Small Woody Features&#39; or &#39;HRL - Forest Type (F...)&#39;. The &#39;Created At&#39; column uniformly shows &#39;27.11.2023&#39;. The &#39;EAGLE Elements&#39; column displays associated icons and values (e.g., &#39;Woody&#39;, &#39;Trees +2&#39;, &#39;Trees +1&#39;, &#39;Buildings +1&#39;). An open dropdown menu, accessed from the button next to &#39;CONFIRM SELECTION&#39;, displays options to show/hide columns or apply additional filters: &#39;Time Range&#39;, &#39;Organisation/s&#39;, &#39;EAGLE Elements&#39; (checked), &#39;100% EAGLE Compliant&#39; (checked), &#39;Extraction/s&#39;, and &#39;INSPIRE Themes&#39;." />

This is a screenshot of a web application interface within the
Copernicus Land Monitoring Service (CLMS) for selecting input classes,
specifically for a ‘CLC+ Instance_LULUCF_2021_NL’ data extraction. The
user interface features a top navigation bar with “Data Catalogue”,
“EAGLE Ontology”, “About EAGLE”, “Organisations”, and “Users” tabs, and
a “User Admin/Support CLC+ Core” profile. Breadcrumbs indicate the
current navigation path: “Data Catalogue / Extraction ‘CLC+
Instance_LULUCF_2021_NL’ / Select Input Classes”.

The main section is titled “Select Input Classes (1)”. It contains
action buttons and a filter panel on the left, and a data table listing
available input classes on the right. The top action bar includes
“Filter” (with a funnel icon), “My organisation/s” (selected with a
checkmark), “My data” buttons, and a search bar. On the right, “CANCEL”
and “CONFIRM SELECTION” (highlighted green) buttons are present, along
with a dropdown menu showing display/filter options.

The “Filter” panel on the left allows users to filter by “Country”,
“Region”, “Reference Year”, “Time range”, and “EAGLE Elements”, and
includes a toggle for “100% EAGLE Compliant”.

The main data table lists input classes with the following columns: an
initial unchecked selection box, “EAGLE Approved” (with checkmarks for
approved items), “Name”, “Ingestion”, “Created By”, “Created At”, “EAGLE
Elements”, and a final checkbox for row selection. Example class names
visible include “Additional woody features”, “Small woody features”,
“All non-forest type”, “Broadleaved forest type”, “Coniferous forest
type”, “built-up”, and “non built-up”. The “Ingestion” column specifies
the High Resolution Layer (HRL) source, such as “HRL - Small Woody
Features” or “HRL - Forest Type (F…)”. The “Created At” column uniformly
shows “27.11.2023”. The “EAGLE Elements” column displays associated
icons and values (e.g., “Woody”, “Trees +2”, “Trees +1”, “Buildings
+1”).

An open dropdown menu, accessed from the button next to “CONFIRM
SELECTION”, displays options to show/hide columns or apply additional
filters: “Time Range”, “Organisation/s”, “EAGLE Elements” (checked),
“100% EAGLE Compliant” (checked), “Extraction/s”, and “INSPIRE Themes”.

<span id="_Ref153650700" class="anchor"></span>**Figure 4‑12: Add Input
Classes to Extraction – selection of classes.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image139.png"
style="width:6.925in;height:3.45139in"
data-fig-alt="This image is a screenshot of a user interface for a data catalogue within the Copernicus Land Monitoring Service (CLMS) framework, likely for CORINE Land Cover (CLC+) data extraction. The interface displays data that has been filtered and is ready for an &#39;Extraction process&#39;, as referenced in the surrounding text. The top navigation bar features &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, &#39;Users&#39;, and &#39;User Admin/Support CLC+&#39;. Below this, tabs include &#39;Filter&#39; (active), &#39;My organisation/s&#39;, &#39;My data&#39;, and a search bar. The left-hand &#39;Filter&#39; panel, labelled &#39;CLOSE&#39;, shows the currently applied filters: * Country: &#39;European Union (27)&#39; * Region: (empty) * Reference Year: &#39;2018&#39; * Time range: (empty) * EAGLE Elements: &#39;Herbaceous Vegetation (Grass-Like, Fo...)&#39; [partially obscured] * A toggle switch for &#39;100% EAGLE Compliant&#39; is set to off. * &#39;INSPIRE Themes&#39; is partially visible at the bottom. The main content area on the right displays a table of data entries. The table columns are: * Checkbox for selection * &#39;EAGLE Approved&#39; (checkbox column header) * &#39;Name&#39; * &#39;Ingestion&#39; * &#39;Created By&#39; * &#39;Created At&#39; * &#39;Reference Year&#39; * &#39;EAGLE Elements&#39; * &#39;100% EAGLE Compliant&#39; (checkbox column header) Example rows from the table include: * **dry pulses:** Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +9&#39;, 100% EAGLE Compliant: (checked). * **fodder crops:** Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Herbaceous Veg...+22&#39; [partially obscured], 100% EAGLE Compliant: (checked). * **grasslands:** Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Trees +17&#39;, 100% EAGLE Compliant: (checked). * **other non pe...** [partially obscured]: Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +13&#39;, 100% EAGLE Compliant: (checked). * **other root cr...** [partially obscured]: Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +9&#39;, 100% EAGLE Compliant: (checked). * **Potatos:** Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +9&#39;, 100% EAGLE Compliant: (checked). * **Rape and tur...** [partially obscured]: Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +9&#39;, 100% EAGLE Compliant: (checked). * **soya:** Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +9&#39;, 100% EAGLE Compliant: (checked). * **Sugar beet:** Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +9&#39;, 100% EAGLE Compliant: (checked). * **sunflower** [partially visible]: Ingestion: &#39;Eurocrop&#39;, Created By: &#39;User Admin/Supp...&#39;, Created At: &#39;24.12.2022&#39;, Reference Year: &#39;2018&#39;, EAGLE Elements: &#39;Bare Soils +9&#39;, 100% EAGLE Compliant: (checked). Buttons &#39;CANCEL&#39; and &#39;CONFIRM SELECTION&#39; are visible in the top right." />

This image is a screenshot of a user interface for a data catalogue
within the Copernicus Land Monitoring Service (CLMS) framework, likely
for CORINE Land Cover (CLC+) data extraction. The interface displays
data that has been filtered and is ready for an “Extraction process”, as
referenced in the surrounding text.

The top navigation bar features “Data Catalogue”, “EAGLE Ontology”,
“About EAGLE”, “Organisations”, “Users”, and “User Admin/Support CLC+”.
Below this, tabs include “Filter” (active), “My organisation/s”, “My
data”, and a search bar.

The left-hand “Filter” panel, labelled “CLOSE”, shows the currently
applied filters: \* Country: “European Union (27)” \* Region: (empty) \*
Reference Year: “2018” \* Time range: (empty) \* EAGLE Elements:
“Herbaceous Vegetation (Grass-Like, Fo…)” \[partially obscured\] \* A
toggle switch for “100% EAGLE Compliant” is set to off. \* “INSPIRE
Themes” is partially visible at the bottom.

The main content area on the right displays a table of data entries. The
table columns are: \* Checkbox for selection \* “EAGLE Approved”
(checkbox column header) \* “Name” \* “Ingestion” \* “Created By” \*
“Created At” \* “Reference Year” \* “EAGLE Elements” \* “100% EAGLE
Compliant” (checkbox column header)

Example rows from the table include: \* **dry pulses:** Ingestion:
“Eurocrop”, Created By: “User Admin/Supp…”, Created At: “24.12.2022”,
Reference Year: “2018”, EAGLE Elements: “Bare Soils +9”, 100% EAGLE
Compliant: (checked). \* **fodder crops:** Ingestion: “Eurocrop”,
Created By: “User Admin/Supp…”, Created At: “24.12.2022”, Reference
Year: “2018”, EAGLE Elements: “Herbaceous Veg…+22” \[partially
obscured\], 100% EAGLE Compliant: (checked). \* **grasslands:**
Ingestion: “Eurocrop”, Created By: “User Admin/Supp…”, Created At:
“24.12.2022”, Reference Year: “2018”, EAGLE Elements: “Trees +17”, 100%
EAGLE Compliant: (checked). \* **other non pe…** \[partially obscured\]:
Ingestion: “Eurocrop”, Created By: “User Admin/Supp…”, Created At:
“24.12.2022”, Reference Year: “2018”, EAGLE Elements: “Bare Soils +13”,
100% EAGLE Compliant: (checked). \* **other root cr…** \[partially
obscured\]: Ingestion: “Eurocrop”, Created By: “User Admin/Supp…”,
Created At: “24.12.2022”, Reference Year: “2018”, EAGLE Elements: “Bare
Soils +9”, 100% EAGLE Compliant: (checked). \* **Potatos:** Ingestion:
“Eurocrop”, Created By: “User Admin/Supp…”, Created At: “24.12.2022”,
Reference Year: “2018”, EAGLE Elements: “Bare Soils +9”, 100% EAGLE
Compliant: (checked). \* **Rape and tur…** \[partially obscured\]:
Ingestion: “Eurocrop”, Created By: “User Admin/Supp…”, Created At:
“24.12.2022”, Reference Year: “2018”, EAGLE Elements: “Bare Soils +9”,
100% EAGLE Compliant: (checked). \* **soya:** Ingestion: “Eurocrop”,
Created By: “User Admin/Supp…”, Created At: “24.12.2022”, Reference
Year: “2018”, EAGLE Elements: “Bare Soils +9”, 100% EAGLE Compliant:
(checked). \* **Sugar beet:** Ingestion: “Eurocrop”, Created By: “User
Admin/Supp…”, Created At: “24.12.2022”, Reference Year: “2018”, EAGLE
Elements: “Bare Soils +9”, 100% EAGLE Compliant: (checked). \*
**sunflower** \[partially visible\]: Ingestion: “Eurocrop”, Created By:
“User Admin/Supp…”, Created At: “24.12.2022”, Reference Year: “2018”,
EAGLE Elements: “Bare Soils +9”, 100% EAGLE Compliant: (checked).

Buttons “CANCEL” and “CONFIRM SELECTION” are visible in the top right.

<span id="_Ref153649503" class="anchor"></span>**Figure 4‑13: Add Input
Classes to Extraction – filter panel.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image137.png"
style="width:6.72917in;height:3.20833in"
data-fig-alt="A screenshot of the CLC+ (next-generation land cover/land use) Core application&#39;s &#39;Select Input Classes&#39; user interface, showing a filter panel on the left and a data table on the right. The top navigation bar includes &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. The left-hand filter panel includes: * &#39;Country&#39; filter set to &#39;European Union (27)&#39;. * An empty &#39;Region&#39; filter. * &#39;Reference Year&#39; filter set to &#39;2018&#39;. * An empty &#39;Time range&#39; filter. * &#39;EAGLE Elements&#39; filter set to &#39;Herbaceous Vegetation (Grass-Like, Fo...)&#39;. * A toggle switch labelled &#39;100% EAGLE Compliant&#39;. * An empty &#39;INSPIRE Themes&#39; filter. * A &#39;CLEAR ALL FILTERS&#39; button. The right-hand data table displays 10 out of 11 available input classes with columns: &#39;EAGLE Approved&#39; (checkboxes), &#39;Name&#39;, &#39;Ingestion&#39;, &#39;Created By&#39;, &#39;Created At&#39;, &#39;Reference Year&#39;, &#39;EAGLE Elements&#39;, and &#39;100% EAGLE Compliant&#39; (checkboxes). All visible rows have both &#39;EAGLE Approved&#39; and &#39;100% EAGLE Compliant&#39; checkboxes ticked. Example data rows include: &#39;dry pulses&#39;, &#39;fodder crops&#39;, &#39;grasslands&#39;, &#39;other non pe...&#39;, &#39;other root cr...&#39;, &#39;Potatoes&#39;, &#39;Rape and tur...&#39;, &#39;soya&#39;, &#39;Sugar beet&#39;, and &#39;sunflower&#39;. For each row, &#39;Ingestion&#39; is &#39;Eurocrop&#39;, &#39;Created By&#39; is &#39;User Admin/Supp...&#39;, &#39;Created At&#39; is &#39;24.12.2022&#39;, and &#39;Reference Year&#39; is &#39;2018&#39;. The &#39;EAGLE Elements&#39; column typically shows &#39;Bare Soils +9&#39;, indicating 9 additional elements. For the &#39;grasslands&#39; row, hovering over &#39;EAGLE Elements&#39; reveals a popup listing &#39;10 elements&#39;: &#39;Bare Soils (2)&#39;, &#39;Herbaceous Vegetation (Grass-Like, Forbs, Ferns) (2)&#39;, &#39;Commercial Crop Production (5)&#39;, &#39;Production For Own Consumption (5)&#39;, &#39;Perennial Plant (5)&#39;, &#39;Arable Crop Land (5)&#39;, &#39;Kitchen Garden (1)&#39;, &#39;Alimentary Crop Production (1)&#39;, &#39;Kitchen Gardens (1)&#39;, and &#39;Dried Pulses and Protein Crops for The Production of Grain (5)&#39;." />

A screenshot of the CLC+ (next-generation land cover/land use) Core
application’s “Select Input Classes” user interface, showing a filter
panel on the left and a data table on the right. The top navigation bar
includes “Data Catalogue”, “EAGLE Ontology”, “About EAGLE”,
“Organisations”, and “Users”.

The left-hand filter panel includes: \* “Country” filter set to
“European Union (27)”. \* An empty “Region” filter. \* “Reference Year”
filter set to “2018”. \* An empty “Time range” filter. \* “EAGLE
Elements” filter set to “Herbaceous Vegetation (Grass-Like, Fo…)”. \* A
toggle switch labelled “100% EAGLE Compliant”. \* An empty “INSPIRE
Themes” filter. \* A “CLEAR ALL FILTERS” button.

The right-hand data table displays 10 out of 11 available input classes
with columns: “EAGLE Approved” (checkboxes), “Name”, “Ingestion”,
“Created By”, “Created At”, “Reference Year”, “EAGLE Elements”, and
“100% EAGLE Compliant” (checkboxes). All visible rows have both “EAGLE
Approved” and “100% EAGLE Compliant” checkboxes ticked. Example data
rows include: “dry pulses”, “fodder crops”, “grasslands”, “other non
pe…”, “other root cr…”, “Potatoes”, “Rape and tur…”, “soya”, “Sugar
beet”, and “sunflower”. For each row, “Ingestion” is “Eurocrop”,
“Created By” is “User Admin/Supp…”, “Created At” is “24.12.2022”, and
“Reference Year” is “2018”. The “EAGLE Elements” column typically shows
“Bare Soils +9”, indicating 9 additional elements. For the “grasslands”
row, hovering over “EAGLE Elements” reveals a popup listing “10
elements”: “Bare Soils (2)”, “Herbaceous Vegetation (Grass-Like, Forbs,
Ferns) (2)”, “Commercial Crop Production (5)”, “Production For Own
Consumption (5)”, “Perennial Plant (5)”, “Arable Crop Land (5)”,
“Kitchen Garden (1)”, “Alimentary Crop Production (1)”, “Kitchen Gardens
(1)”, and “Dried Pulses and Protein Crops for The Production of Grain
(5)”.

<span id="_Ref153650770" class="anchor"></span>**Figure 4‑14: Add Input
Classes to Extraction - EAGLE elements with tooltip dialog.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image140.png"
style="width:6.925in;height:3.32778in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, showing the &#39;Show EAGLE Elements&#39; menu for &#39;Input Class dry pulses (10)&#39;. The interface path is &#39;Data Catalogue / Ingestion &#39;Eurocrop&#39; / Input Class dry pulses / Show EAGLE Elements&#39;. A search bar is present at the top with a &#39;CLOSE&#39; button. The main content is structured into expandable sections: 1. **Land Cover Components (LCC)**: * **Abiotic / Non-Vegetated Surfaces and Objects (LCC-1)**: * **Natural Material Surfaces (LCC-1_2)**: * **Unconsolidated Surfaces (LCC-1_2_2)**: * &#39;Bare Soils (LCC-1_2_2_2)&#39; is checked, with &#39;EAGLE Barcoding&#39; value &#39;2&#39; and &#39;Factor&#39; value &#39;1,00&#39;. * **Biotic / Vegetation (LCC-2)**: * &#39;Herbaceous Vegetation (Grass-Like, Forbs, Ferns) (LCC-2_2)&#39; is checked, with &#39;EAGLE Barcoding&#39; value &#39;2&#39; and &#39;Factor&#39; value &#39;1,00&#39;. 2. **Land Use Attributes (LUA)**: * **Primary Production Sector (LUA-1)**: * **Agriculture (LUA-1_1)** (partially visible and collapsed). The interface allows users to select specific Land Cover Components and Land Use Attributes, and configure associated &#39;EAGLE Barcoding&#39; and &#39;Factor&#39; values for an input class." />

A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core
user interface, showing the “Show EAGLE Elements” menu for “Input Class
dry pulses (10)”. The interface path is “Data Catalogue / Ingestion
‘Eurocrop’ / Input Class dry pulses / Show EAGLE Elements”. A search bar
is present at the top with a “CLOSE” button.

The main content is structured into expandable sections: 1. **Land Cover
Components (LCC)**: \* **Abiotic / Non-Vegetated Surfaces and Objects
(LCC-1)**: \* **Natural Material Surfaces (LCC-1_2)**: \*
**Unconsolidated Surfaces (LCC-1_2_2)**: \* “Bare Soils (LCC-1_2_2_2)”
is checked, with “EAGLE Barcoding” value “2” and “Factor” value “1,00”.
\* **Biotic / Vegetation (LCC-2)**: \* “Herbaceous Vegetation
(Grass-Like, Forbs, Ferns) (LCC-2_2)” is checked, with “EAGLE Barcoding”
value “2” and “Factor” value “1,00”. 2. **Land Use Attributes (LUA)**:
\* **Primary Production Sector (LUA-1)**: \* **Agriculture (LUA-1_1)**
(partially visible and collapsed).

The interface allows users to select specific Land Cover Components and
Land Use Attributes, and configure associated “EAGLE Barcoding” and
“Factor” values for an input class.

<span id="_Ref153650763" class="anchor"></span>**Figure 4‑15: Add Input
Classes to Extraction - EAGLE barcoding opened in new window (here for
Input Class “dry pulses”).**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image141.png"
style="width:6.925in;height:2.94028in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, displaying an &#39;Extraction&#39; page for &#39;CLC+ Instance_LULUCF_2021_NL&#39;. The interface is divided into a left panel for &#39;General Information&#39; and &#39;Additional Documents&#39;, and a right panel containing a map viewer and an &#39;Input Classes&#39; table. The left &#39;General Information&#39; panel details the extraction parameters: * Name: CLC+ Instance_LULUCF_2021_NL * Country: Netherlands/Nederland * Region: Groningen * Reference Year: 2018 * Time Range of Extracted Data: 01.12.2018 - 31.12.2018 * INSPIRE Themes: LU Land use, LC Land cover * Created By: User Admin/Support CLC+ Core * Organisation/s: European Environment Agency (EEA) The top section of the right panel features a map viewer with controls for zoom, full extent, and layers. The map shows a region encompassing the Netherlands and parts of Germany, with &#39;NL Netherlands/Nederland&#39; and &#39;NL11 Groningen&#39; selected as geographical filters. The map displays a message &#39;Your map is outdated! Please press &#39;PREVIEW&#39; to generate the map according to your new input.&#39; The region of Groningen is outlined in dark red. A scale bar indicates &#39;30 km&#39; and &#39;10 mi&#39;. Map attribution states &#39;Leaflet | ©Core003 Mosaic, © OpenStreetMap contributors&#39;. Above the map, action buttons include &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START EXTRACTION&#39;, &#39;DOWNLOAD&#39;, and &#39;PUBLISH&#39;. Below the map, an &#39;Input Classes&#39; table lists four entries: | Rank | Class Code | Name | Ingestion | Eagle Elements | 100% Eagle compliant | Colour | Show In Map | |---|---|---|---|---|---|---|---| | 1. | 3 | Additional woody features | HRL - Small Woody Features | Woody Vegetation | +3 (checkbox checked) | (yellow square) | (toggle off) | | 2. | 1 | Small woody features | HRL - Small Woody Features | Woody Vegetation | +3 (checkbox checked) | (light green square) | (toggle off) | | 3. | 1 | Broadleaved forest | HRL - Forest Type (FTY) 2018 | Trees | +2 (checkbox checked) | (medium green square) | (toggle off) | | 4. | 2 | Coniferous forest | HRL - Forest Type (FTY) 2018 | Trees | +1 (checkbox checked) | (dark green square) | (toggle off) | HRL stands for High Resolution Layer. The &#39;100% Eagle compliant&#39; column indicates compliance with the EIONET Action Group on Land monitoring in Europe (EAGLE) methodology." />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) CLC+ Core user interface, displaying an “Extraction” page for
“CLC+ Instance_LULUCF_2021_NL”. The interface is divided into a left
panel for “General Information” and “Additional Documents”, and a right
panel containing a map viewer and an “Input Classes” table.

The left “General Information” panel details the extraction parameters:
\* Name: CLC+ Instance_LULUCF_2021_NL \* Country: Netherlands/Nederland
\* Region: Groningen \* Reference Year: 2018 \* Time Range of Extracted
Data: 01.12.2018 - 31.12.2018 \* INSPIRE Themes: LU Land use, LC Land
cover \* Created By: User Admin/Support CLC+ Core \* Organisation/s:
European Environment Agency (EEA)

The top section of the right panel features a map viewer with controls
for zoom, full extent, and layers. The map shows a region encompassing
the Netherlands and parts of Germany, with “NL Netherlands/Nederland”
and “NL11 Groningen” selected as geographical filters. The map displays
a message “Your map is outdated! Please press”PREVIEW” to generate the
map according to your new input.” The region of Groningen is outlined in
dark red. A scale bar indicates “30 km” and “10 mi”. Map attribution
states “Leaflet \| ©Core003 Mosaic, © OpenStreetMap contributors”. Above
the map, action buttons include “REPUBLISH ON GEOSERVER”, “START
EXTRACTION”, “DOWNLOAD”, and “PUBLISH”.

Below the map, an “Input Classes” table lists four entries: \| Rank \|
Class Code \| Name \| Ingestion \| Eagle Elements \| 100% Eagle
compliant \| Colour \| Show In Map \| \|—\|—\|—\|—\|—\|—\|—\|—\| \| 1.
\| 3 \| Additional woody features \| HRL - Small Woody Features \| Woody
Vegetation \| +3 (checkbox checked) \| (yellow square) \| (toggle off)
\| \| 2. \| 1 \| Small woody features \| HRL - Small Woody Features \|
Woody Vegetation \| +3 (checkbox checked) \| (light green square) \|
(toggle off) \| \| 3. \| 1 \| Broadleaved forest \| HRL - Forest Type
(FTY) 2018 \| Trees \| +2 (checkbox checked) \| (medium green square) \|
(toggle off) \| \| 4. \| 2 \| Coniferous forest \| HRL - Forest Type
(FTY) 2018 \| Trees \| +1 (checkbox checked) \| (dark green square) \|
(toggle off) \|

HRL stands for High Resolution Layer. The “100% Eagle compliant” column
indicates compliance with the EIONET Action Group on Land monitoring in
Europe (EAGLE) methodology.

<span id="_Ref105172435" class="anchor"></span>**Figure 4‑16: Add Input
Classes to Extraction – back in Edit Extraction view with the newly
added Input Classes.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image142.png"
style="width:6.71528in;height:3.22222in"
data-fig-alt="This image is a screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, displaying details for a data catalogue entry alongside selected &#39;Input Classes&#39; for data extraction. The left panel provides metadata for the data catalogue entry: - **Reference Year:** 2018 - **Time Range of Extracted Data:** 01.12.2018 - 31.12.2018 - **INSPIRE Themes:** LU Land use, LC Land cover - **Created By:** User Admin/Support CLC+ Core - **Organisation/s:** European Environment Agency (EEA) The central &#39;Input Classes&#39; panel presents a list of selected land cover classes with associated attributes in a table-like format: | Rank | Class Code | Name | Ingestion | Eagle Elements | 100% Eagle compliant | Colour | Show in Map | |---|---|---|---|---|---|---|---| | 1. | 3 | Additional wood... | HRL - Small Woody Features (SWF) 2015 | Woody Vegetation (+3) | ☑ | Yellow | ⚪ | | 2. | 1 | Small woody fea... | HRL - Small Woody Features (SWF) 2015 | Woody Veget... (+3) | ☑ | Green | ⚪ | | 3. | 1 | Broadleaved for... | HRL - Forest Type (FTY) 2018 | | ☑ | Dark Green | ⚪ | | 4. | 2 | Coniferous forest | HRL - Forest Type (FTY) 2018 | | ☑ | Dark Green | ⚪ | A tooltip is displayed for the &#39;Eagle Elements&#39; field in row 3, detailing &#39;4 elements&#39;: &#39;Woody Vegetation (5)&#39;, &#39;Mosaic (Clearly Distinct Patches) (5)&#39;, &#39;Hedge Rows (1)&#39;, and &#39;Rows of Trees (1)&#39;. The &#39;Ingestion&#39; column indicates the source data products as High Resolution Layer (HRL) &#39;HRL - Small Woody Features (SWF) 2015&#39; and &#39;HRL - Forest Type (FTY) 2018&#39;. An overlaid dropdown menu partially obscures the upper right map, showing selection options for &#39;Ingestion&#39;, &#39;Class&#39;, and &#39;Coverage&#39;. Visible selections include: &#39;HRL - Forest Type (FTY) 2018&#39; with &#39;Broadleaved forest&#39; at &#39;66 %&#39; coverage, and &#39;HRL - Small Woody Features (SWF) 2015&#39; with &#39;Additional woody features&#39; at &#39;50 %&#39; coverage. The right-hand map panel displays aerial imagery of an area with agricultural fields and scattered vegetation. It includes a scale bar indicating &#39;1 km&#39; and &#39;1 mi&#39;, and map attribution &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. White pixels are overlaid on the map, likely representing features corresponding to the selected input classes." />

This image is a screenshot of the Copernicus Land Monitoring Service
(CLMS) CLC+ Core user interface, displaying details for a data catalogue
entry alongside selected “Input Classes” for data extraction.

The left panel provides metadata for the data catalogue entry: -
**Reference Year:** 2018 - **Time Range of Extracted Data:**
01.12.2018 - 31.12.2018 - **INSPIRE Themes:** LU Land use, LC Land
cover - **Created By:** User Admin/Support CLC+ Core -
**Organisation/s:** European Environment Agency (EEA)

The central “Input Classes” panel presents a list of selected land cover
classes with associated attributes in a table-like format: \| Rank \|
Class Code \| Name \| Ingestion \| Eagle Elements \| 100% Eagle
compliant \| Colour \| Show in Map \| \|—\|—\|—\|—\|—\|—\|—\|—\| \| 1.
\| 3 \| Additional wood… \| HRL - Small Woody Features (SWF) 2015 \|
Woody Vegetation (+3) \| ☑ \| Yellow \| ⚪ \| \| 2. \| 1 \| Small woody
fea… \| HRL - Small Woody Features (SWF) 2015 \| Woody Veget… (+3) \| ☑
\| Green \| ⚪ \| \| 3. \| 1 \| Broadleaved for… \| HRL - Forest Type
(FTY) 2018 \| \| ☑ \| Dark Green \| ⚪ \| \| 4. \| 2 \| Coniferous
forest \| HRL - Forest Type (FTY) 2018 \| \| ☑ \| Dark Green \| ⚪ \|

A tooltip is displayed for the “Eagle Elements” field in row 3,
detailing “4 elements”: “Woody Vegetation (5)”, “Mosaic (Clearly
Distinct Patches) (5)”, “Hedge Rows (1)”, and “Rows of Trees (1)”. The
“Ingestion” column indicates the source data products as High Resolution
Layer (HRL) “HRL - Small Woody Features (SWF) 2015” and “HRL - Forest
Type (FTY) 2018”.

An overlaid dropdown menu partially obscures the upper right map,
showing selection options for “Ingestion”, “Class”, and “Coverage”.
Visible selections include: “HRL - Forest Type (FTY) 2018” with
“Broadleaved forest” at “66 %” coverage, and “HRL - Small Woody Features
(SWF) 2015” with “Additional woody features” at “50 %” coverage.

The right-hand map panel displays aerial imagery of an area with
agricultural fields and scattered vegetation. It includes a scale bar
indicating “1 km” and “1 mi”, and map attribution “Leaflet \| © Core003
Mosaic, © OpenStreetMap contributors”. White pixels are overlaid on the
map, likely representing features corresponding to the selected input
classes.

<span id="_Ref105172428" class="anchor"></span>**Figure 4‑17: Add or
delete Input Classes in the Extraction view and the EAGLE elements shown
in the tooltip dialog.**

**The Input Classes are following a hierarchical processing (from first
to last). But depending on the chosen Coverage Function, the order is
more or less important. First coverage function i.e. examines the Input
Classes from top to bottom until the first one is found that has a valid
value. Using the highest cov function, the order of the Classes is not
important.**

**There is also the possibility to change the order per ‘Drag & Drop’.**

## Output Classes

An **Output Class** represent detailed information about one
classification option of an Extraction (section [4](#extraction)).
Together with the class code and the name, it also contains the Class
Condition that specifies when the output class should be applied. Output
Classes can be found within the specific Extraction itself but are not
displayed separately within the Data Catalogue. Details about that can
be found at section [4.3 Edit Extraction](#edit-extraction).

### Some definitions for a better understanding (also see [Glossary](#glossary))

A **Rule** is a textual format of the specified Extraction syntax and is
displayed in the user interface as a structured expression. You can
relate EAGLE elements to other EAGLE elements, values (numbers) or
percentages, in order to define how a new Output Class should be
created. In other words, a **Rule** is simple comparison of a **Coverage
Function** against another coverage value. For example:

*The coverage of LCC-Water with barcode 5 must be greater than 50%.
cov(“LCC-Water”, 5) \> 50*

A **Ruleset** is a combination of **Rules or Rulesets** using Boolean
operators. Depending on the type of linking operator, the compound
expression is only true if both linked expressions are true
(AND-linkage) or if at least one of the linked expressions is true
(OR-linkage). For example:

*The coverage of LCC-Water/5 or LCC-Trees/5 must be greater than 50%.
cov(“LCC-Water”, 5) \> 50 **OR** cov(“LCC-Trees”, 5) \> 50*

The **Class Condition** specifies whether the Extraction Output Class to
which it belongs should be applied to a given pixel, given the coverage
values of Extraction Input Classes. Technically speaking, a Class
Condition is a Ruleset.

**Note: Currently it is not possible to save the rulesets outside of the
CLC+ Core System to reuse them for other Extractions. There is a
workaround, you can copy the rules (CTRL+C) from an existing rule and
paste it into another Extraction rule (CTRL+V) by using the text-field
for Extraction rules.**

### Create Output Classes

After you clicked on the <img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image131.png"
style="width:0.16875in;height:0.16875in"
data-fig-alt="A grayscale user interface icon featuring a black plus sign (+) centered within a black circular outline. The icon has a slightly blurred or soft-edged appearance against a white background. In the context of the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover Plus) application, this icon typically represents an action to &#39;Add&#39; or &#39;Create New&#39; entries, such as a new Extraction or new Extraction settings, as suggested by its proximity to &#39;Add Extraction&#39; sections in the documentation." />
icon within the area “**Output Classes**” a new entry will be added.
First, you have to define a name (here: FL Transitional woodland) and
Rule Class Code (here: 1) for the new Output Class. The Class Code is
automatically filled by the system, starting at 1, but could be adapted
to your needs ([Figure 4‑18](#_Ref153806764)).

The Output Classes are ranked according to their order. So, it is
following hierarchical processing (from first to last). That means that
the CLC+ Core System always favours the classes with a smaller order
number. If a pixel is then assigned to an Output Class, it cannot be
assigned to another class even if the coverage for this other class is
higher. There is also the possibility to change the order of the Output
Classes by Drag & Drop.

Furthermore, you can select a colour for your Output Class. And toggle
the visibility of this Output Class in the map. **Checking the eye icon
disables this Output Class from being extracted** ([Figure
4‑18](#_Ref153806764)).

Same as for the Input Classes, you are able to add further Output
Classes or delete the entry ([Figure 4‑18](#_Ref153806764)).

After you have clicked on the Class Condition of a specific Output Class
([Figure 4‑18](#_Ref153806764)), a new window opens (Query Builder,
[Figure 4‑19](#_Ref153808348)) and you can start creating or editing it
(see section [4.5.3 Create Class
Conditions/Rulesets](#create-class-conditionsrulesets)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image143.png"
style="width:6.22829in;height:1.44942in"
data-fig-alt="The table defines a single Output Class, likely within a Copernicus Land Monitoring Service (CLMS) Land Use / Land Cover (LULC) classification system, specifying its properties and rule-based condition. | Rank | Class Code | Name | Ruleset | Colour | Show in Map | |---|---|---|---|---|---| | 1. | 1 | FL Transitional woodland | cov(&#39;LCC-woody-vegetation&#39;, 5) &gt;= 30 | [Empty checkbox for colour selection] | [Toggle switch: ON] | The &#39;Class Code&#39;, &#39;Name&#39;, and &#39;Ruleset&#39; columns are marked as mandatory fields. The &#39;Ruleset&#39; defines the condition for applying the class: the coverage of &#39;LCC-woody-vegetation&#39; with barcode 5 must be greater than or equal to 30%. The &#39;Show in Map&#39; column indicates with an active toggle switch that this Output Class is configured to be visible on a map." />

The table defines a single Output Class, likely within a Copernicus Land
Monitoring Service (CLMS) Land Use / Land Cover (LULC) classification
system, specifying its properties and rule-based condition.

| Rank | Class Code | Name | Ruleset | Colour | Show in Map |
|----|----|----|----|----|----|
| 1\. | 1 | FL Transitional woodland | cov(“LCC-woody-vegetation”, 5) \>= 30 | \[Empty checkbox for colour selection\] | \[Toggle switch: ON\] |

The ‘Class Code’, ‘Name’, and ‘Ruleset’ columns are marked as mandatory
fields. The ‘Ruleset’ defines the condition for applying the class: the
coverage of ‘LCC-woody-vegetation’ with barcode 5 must be greater than
or equal to 30%. The ‘Show in Map’ column indicates with an active
toggle switch that this Output Class is configured to be visible on a
map.

<span id="_Ref153806764" class="anchor"></span>**Figure 4‑18: Create new
Output Class and other options.**

### Create Class Conditions/Rulesets

[Figure 4‑19](#_Ref153808348) shows an overview of the Query Builder
with all its options and functions which are explained in more details
in this section.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image147.png"
style="width:6.925in;height:3.33681in"
data-fig-alt="This is a rule definition interface, specifically the &#39;Query-Builder&#39; tab, for adding a rule to the &#39;Output Class &#39;2 - FL Deciduous&#39;&#39; within a Copernicus Land Monitoring Service (CLMS) CLC+ Core System. The interface allows users to construct complex logical conditions using nested &#39;And&#39; and &#39;Or&#39; operators. The top-level ruleset is an &#39;And&#39; linkage, indicating all primary conditions must be met. It includes a comment: &#39;Intersect HRL and CLC+ BB&#39; (High Resolution Layer and CORINE Land Cover Plus Basic Building blocks). The first active nested ruleset, also linked by &#39;And,&#39; defines two sub-conditions: 1. If the &#39;Total coverage&#39; of &#39;EAGLE-Element (LCC-2_1_1) Trees&#39; with &#39;Barcode 5&#39; is greater than or equal to &#39;30&#39;. 2. If the &#39;Total coverage&#39; of &#39;EAGLE-Element (LCH-3_1_2) Broad Leaved&#39; with &#39;Barcode 2&#39; is greater than or equal to &#39;30&#39;. Both of these sub-conditions must be true for this nested ruleset to be satisfied. An additional empty ruleset, also linked by &#39;And&#39;, is available for further conditions. Controls are present to add new rules or rulesets, and buttons for &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39; are at the top right. The process allows the user to either &#39;Cancel&#39; or &#39;Add&#39; the defined rule to the Output Class." />

This is a rule definition interface, specifically the “Query-Builder”
tab, for adding a rule to the “Output Class ‘2 - FL Deciduous’” within a
Copernicus Land Monitoring Service (CLMS) CLC+ Core System. The
interface allows users to construct complex logical conditions using
nested “And” and “Or” operators.

The top-level ruleset is an “And” linkage, indicating all primary
conditions must be met. It includes a comment: “Intersect HRL and CLC+
BB” (High Resolution Layer and CORINE Land Cover Plus Basic Building
blocks).

The first active nested ruleset, also linked by “And,” defines two
sub-conditions: 1. If the “Total coverage” of “EAGLE-Element (LCC-2_1_1)
Trees” with “Barcode 5” is greater than or equal to “30”. 2. If the
“Total coverage” of “EAGLE-Element (LCH-3_1_2) Broad Leaved” with
“Barcode 2” is greater than or equal to “30”.

Both of these sub-conditions must be true for this nested ruleset to be
satisfied. An additional empty ruleset, also linked by “And”, is
available for further conditions. Controls are present to add new rules
or rulesets, and buttons for “Computation manual” and “EAGLE-Elements”
are at the top right. The process allows the user to either “Cancel” or
“Add” the defined rule to the Output Class.

<span id="_Ref153808348" class="anchor"></span>**Figure 4‑19: Query
Builder with all its options and functions.**

Starting with a blank **Query Builder**, you are able to build up the
Class Condition by using single **Rules** or **Rulesets** (nested set of
rules). To decide between **Rule** and **Ruleset** you need to know how
the EAGLE elements you need for the **Extraction** relate to each other.
The relation is defined by **logical expressions (Boolean).**
**Depending on the type of linking operator, the compound expression is
only true, if both linked expressions are true (AND-linkage) or if at
least one of the linked expressions is true (OR-linkage).** You can add
as many **Rules** or **Rulesets** as needed. Of course, you can also
delete previously created Rule(sets).

So, in a first step decide on the structure you need and add Rules or
Rulesets according to your requirements as can be seen in [Figure
4‑20](#_Ref153873991). If you add a Ruleset, you need to add Rules to
it.

Example: For the Extraction of the deciduous forest class, I add two
Rulesets, one with two and one with three Rules, connected via an AND
operator. I want to make sure to only extract pixel that are covered in
all datasets ([Figure 4‑21](#_Ref153875245)). Once I have the structure,
I can start with entering the content.

Of course, there is the possibility to delete Rules or Rulesets.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image148.png"
style="width:6.48467in;height:3.14804in"
data-fig-alt="A screenshot of the &#39;Add Rule for Output Class &#39;2 - Deciduous&#39;&#39; interface within the Copernicus Land Monitoring Service (CLMS) CLC+ Core System&#39;s Query Builder. The interface features two tabs, &#39;Query-Builder&#39; (active) and &#39;Text&#39;, and buttons for &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39; in the top right. The main section allows users to define logical conditions for land cover classification. Each rule block begins with radio buttons for &#39;And&#39; or &#39;Or&#39; logic, and a &#39;Add comment&#39; button. Within each rule, users select one of three coverage options: &#39;Highest coverage&#39;, &#39;First coverage&#39;, or &#39;Total coverage&#39;. Input fields are provided for &#39;EAGLE-Element *&#39;, &#39;Barcode *&#39;, an &#39;Operator *&#39; (showing &#39;&gt;= as default), and &#39;Coverage Value *&#39;. Two icons (text and hash) appear next to the Coverage Value field. Buttons to &#39;+ Rule&#39;, &#39;+ Ruleset&#39;, and a minus sign for removing elements are present. Two of the rule blocks display an error message in red: &#39;A ruleset cannot be empty. Please add a rule or remove it all together.&#39; The interface allows for creating complex classification conditions that contribute to the hierarchical processing of land cover classes within the CLC+ Core System, where classes with smaller order numbers are favoured. At the bottom, &#39;CANCEL&#39; and &#39;ADD&#39; buttons are available to manage the rule definition process." />

A screenshot of the “Add Rule for Output Class ‘2 - Deciduous’”
interface within the Copernicus Land Monitoring Service (CLMS) CLC+ Core
System’s Query Builder. The interface features two tabs, “Query-Builder”
(active) and “Text”, and buttons for “Computation manual” and
“EAGLE-Elements” in the top right. The main section allows users to
define logical conditions for land cover classification.

Each rule block begins with radio buttons for “And” or “Or” logic, and a
“Add comment” button. Within each rule, users select one of three
coverage options: “Highest coverage”, “First coverage”, or “Total
coverage”. Input fields are provided for “EAGLE-Element *”, ”Barcode* ”,
an “Operator *” (showing ”\>= as default), and ”Coverage Value* ”. Two
icons (text and hash) appear next to the Coverage Value field. Buttons
to “+ Rule”, “+ Ruleset”, and a minus sign for removing elements are
present.

Two of the rule blocks display an error message in red: “A ruleset
cannot be empty. Please add a rule or remove it all together.” The
interface allows for creating complex classification conditions that
contribute to the hierarchical processing of land cover classes within
the CLC+ Core System, where classes with smaller order numbers are
favoured. At the bottom, “CANCEL” and “ADD” buttons are available to
manage the rule definition process.

<span id="_Ref153873991" class="anchor"></span>**Figure 4‑20: Create new
Rule for an Output Class – Query Builder**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image149.png"
style="width:6.56217in;height:3.14355in"
data-fig-alt="A screenshot of the &#39;Query-Builder&#39; interface for adding rules to &#39;Output Class &#39;2 - Deciduous&#39;&#39;. The interface is structured with a primary &#39;Query-Builder&#39; tab (active) and a &#39;Text&#39; tab. In the top right, there are buttons for &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39;. The main area allows users to construct classification rules using nested logical conditions. The top-level group uses &#39;And&#39; logic, containing two individual rules. Each rule can specify &#39;Highest coverage&#39; (selected), &#39;First coverage&#39;, or &#39;Total coverage&#39;. Rule conditions are defined by an &#39;EAGLE-Element *&#39;, &#39;Barcode *&#39;, an &#39;Operator *&#39; (defaulting to &#39;&gt;= &#39;), and a &#39;Coverage Value *&#39;. Icons next to the coverage value include a stylized &#39;XA&#39; and &#39;#&#39;. Below this, another top-level &#39;And&#39; logical group is partially visible, containing one rule. Users can add new &#39;+ Rule&#39; or &#39;+ Ruleset&#39; entries. Navigation buttons at the bottom are &#39;CANCEL&#39; and &#39;ADD&#39;. This interface is used to build Class Conditions or Rulesets for land cover classification within the Copernicus Land Monitoring Service (CLMS) framework." />

A screenshot of the “Query-Builder” interface for adding rules to
“Output Class ‘2 - Deciduous’”. The interface is structured with a
primary “Query-Builder” tab (active) and a “Text” tab. In the top right,
there are buttons for “Computation manual” and “EAGLE-Elements”. The
main area allows users to construct classification rules using nested
logical conditions. The top-level group uses “And” logic, containing two
individual rules. Each rule can specify “Highest coverage” (selected),
“First coverage”, or “Total coverage”. Rule conditions are defined by an
“EAGLE-Element *”, ”Barcode* ”, an “Operator *” (defaulting to ”\>= ”),
and a ”Coverage Value* ”. Icons next to the coverage value include a
stylized ‘XA’ and ‘\#’. Below this, another top-level “And” logical
group is partially visible, containing one rule. Users can add new “+
Rule” or “+ Ruleset” entries. Navigation buttons at the bottom are
“CANCEL” and “ADD”. This interface is used to build Class Conditions or
Rulesets for land cover classification within the Copernicus Land
Monitoring Service (CLMS) framework.

<span id="_Ref153875245" class="anchor"></span>**Figure 4‑21: Create new
Class Condition for Output Class “Deciduous Forest”.**

In the next steps, select the required EAGLE elements from the Query
Builder ([Figure 4‑22](#_Ref153876094)). The prefered option is to
select elements from the drop down menu but you can also write in the
text box.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image150.png"
style="width:6.53323in;height:3.15851in"
data-fig-alt="User interface for the Copernicus Land Monitoring Service (CLMS) Query Builder, titled &#39;Add Rule for Output Class &#39;2 - Deciduous&#39;&#39;. The interface is displayed with the &#39;Query-Builder&#39; tab active, alongside a &#39;Text&#39; tab. Rules and rulesets are constructed using logical Boolean &#39;And&#39; or &#39;Or&#39; operators; currently, &#39;And&#39; is selected for both the top-level and a nested ruleset. Options to &#39;Add comment&#39;, &#39;+ Rule&#39;, and &#39;+ Ruleset&#39; are available. Each rule configuration includes: 1. A selection for coverage type: &#39;Highest coverage&#39;, &#39;First coverage&#39;, or &#39;Total coverage&#39;. 2. An &#39;EAGLE-Element&#39; field, which, in the example, suggests &#39;LCC-2_1_1 Trees&#39; from &#39;EAGLE Elements from added Input Classes&#39; and &#39;All EAGLE Elements&#39; which also lists &#39;LCH-5_1_6_3_12 Christmas Trees&#39;. 3. A &#39;Barcode&#39; field. 4. An &#39;Operator&#39; selection, with &#39;&gt;=&#39; shown as the current value. 5. A &#39;Coverage Value&#39; field. The interface also provides access to a &#39;Computation manual&#39; and a list of &#39;EAGLE-Elements&#39;. The process is concluded with &#39;CANCEL&#39; or &#39;ADD&#39; buttons." />

User interface for the Copernicus Land Monitoring Service (CLMS) Query
Builder, titled “Add Rule for Output Class ‘2 - Deciduous’”. The
interface is displayed with the “Query-Builder” tab active, alongside a
“Text” tab. Rules and rulesets are constructed using logical Boolean
“And” or “Or” operators; currently, “And” is selected for both the
top-level and a nested ruleset. Options to “Add comment”, “+ Rule”, and
“+ Ruleset” are available. Each rule configuration includes: 1. A
selection for coverage type: “Highest coverage”, “First coverage”, or
“Total coverage”. 2. An “EAGLE-Element” field, which, in the example,
suggests “LCC-2_1_1 Trees” from “EAGLE Elements from added Input
Classes” and “All EAGLE Elements” which also lists “LCH-5_1_6_3_12
Christmas Trees”. 3. A “Barcode” field. 4. An “Operator” selection, with
“\>=” shown as the current value. 5. A “Coverage Value” field. The
interface also provides access to a “Computation manual” and a list of
“EAGLE-Elements”. The process is concluded with “CANCEL” or “ADD”
buttons.

<span id="_Ref153876094" class="anchor"></span>**Figure 4‑22: Select
EAGLE elements in the Query Builder.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image151.png"
style="width:6.58007in;height:3.16532in"
data-fig-alt="This image is a screenshot of a &#39;Query Builder&#39; interface used to define classification rules for an output class named &#39;2 - Deciduous&#39;. The interface is active under the &#39;Query-Builder&#39; tab, with a &#39;Text&#39; tab also visible. In the top right, there are buttons for &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39;. The core of the interface allows users to construct complex rulesets using Boolean logic. The main ruleset is configured with an &#39;And&#39; operator. Nested within it is a sub-ruleset, also configured with &#39;And&#39;. This sub-ruleset contains multiple rule lines. For each rule, the user can select a coverage type: &#39;Highest coverage&#39; (currently selected), &#39;First coverage&#39;, or &#39;Total coverage&#39;. A rule line consists of fields for: * &#39;EAGLE-Element *&#39;: An input field where &#39;mosa&#39; is partially typed. A dropdown list is open, showing &#39;EAGLE Elements from added Input Classes&#39; (with &#39;No elements found&#39;) and &#39;All EAGLE Elements&#39;, under which &#39;LCH-8_1_3 Mosaic Pattern&#39; is highlighted. * &#39;Barcode *&#39;: A dropdown menu. * &#39;Operator *&#39;: A dropdown menu, currently showing &#39;&gt;=&#39;. * &#39;Coverage Value *&#39;: An input field. Buttons to add &#39;+ Rule&#39; or &#39;+ Ruleset&#39; and to remove a rule or ruleset (&#39;-&#39;) are available at different nesting levels. At the bottom right of the interface are &#39;CANCEL&#39; and &#39;ADD&#39; buttons. This interface is designed for building class conditions or rulesets for land cover/land use (LULC) classification within the Copernicus Land Monitoring Service (CLMS) CLC+ framework." />

This image is a screenshot of a “Query Builder” interface used to define
classification rules for an output class named ‘2 - Deciduous’. The
interface is active under the “Query-Builder” tab, with a “Text” tab
also visible. In the top right, there are buttons for “Computation
manual” and “EAGLE-Elements”.

The core of the interface allows users to construct complex rulesets
using Boolean logic. The main ruleset is configured with an “And”
operator. Nested within it is a sub-ruleset, also configured with “And”.
This sub-ruleset contains multiple rule lines. For each rule, the user
can select a coverage type: “Highest coverage” (currently selected),
“First coverage”, or “Total coverage”.

A rule line consists of fields for: \* “EAGLE-Element *”: An input field
where ”mosa” is partially typed. A dropdown list is open, showing ”EAGLE
Elements from added Input Classes” (with ”No elements found”) and ”All
EAGLE Elements”, under which ”LCH-8_1_3 Mosaic Pattern” is highlighted.*
”Barcode *“: A dropdown menu. \*”Operator* ”: A dropdown menu, currently
showing “\>=”. \* “Coverage Value \*“: An input field.

Buttons to add “+ Rule” or “+ Ruleset” and to remove a rule or ruleset
(“-”) are available at different nesting levels. At the bottom right of
the interface are “CANCEL” and “ADD” buttons. This interface is designed
for building class conditions or rulesets for land cover/land use (LULC)
classification within the Copernicus Land Monitoring Service (CLMS) CLC+
framework.

<span id="_Ref153881096" class="anchor"></span>**Figure 4‑23: Select
EAGLE elements in the Query Builder. Information that LCH-8_1_3 is in
the list of EAGLE elements but does not occur in one of the Input
Classes.**

Next, select the barcode value from a drop-down list. There is also the
option to multiselect barcode values to cover more than one Input Class
having different barcodes mapped ([Figure 4‑24](#_Ref153876076)).

**Multi-selected barcodes are OR-connected. That means, that a rule with
multiple barcodes can be written as well as an OR-connected ruleset
containing an individual rule for each of the barcodes. The
multi-selection is only possible if an EAGLE Element is compared to a
value but not if two EAGLE Elements are compared (icon-toggle on the
right).**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image152.png"
style="width:6.58028in;height:3.16806in"
data-fig-alt="This image displays the Copernicus Land Monitoring Service (CLMS) CLC+ Query Builder interface, used to &#39;Add Rule for Output Class &#39;2 - Deciduous&#39;&#39;. The interface allows users to construct complex logical conditions for land cover classification by combining &#39;Rules&#39; and &#39;Rulesets&#39;. The top-level query structure is defined by an &#39;And&#39; or &#39;Or&#39; logical operator. Within this, nested Rulesets can be created, also linked by &#39;And&#39; or &#39;Or&#39; operators. Each Ruleset can contain one or more individual &#39;Rules&#39;. An example rule is shown for the &#39;EAGLE-Element (LCC-2_1_1) Trees&#39;. For this rule, &#39;Highest coverage&#39; is selected as the coverage type, and the &#39;Operator&#39; is set to &#39;&gt;=&#39;. A dropdown menu for the &#39;EAGLE-Element&#39; field is open, showing options for handling how the element is considered: &#39;X (Excluded)&#39;, &#39;1 (Optional)&#39;, &#39;2 (One or more)&#39;, &#39;3 (All of them)&#39;, &#39;4 (At least two)&#39;, and &#39;5 (This one only)&#39;. For the &#39;Trees&#39; element, &#39;5 (This one only)&#39; is selected. Another rule within the same nested Ruleset is partially configured, with &#39;Highest coverage&#39; selected and the &#39;Operator&#39; also set to &#39;&gt;=&#39;. The interface includes options to &#39;Add comment&#39;, &#39;+ Rule&#39;, &#39;+ Ruleset&#39;, and controls to delete elements. Ancillary information can be accessed via &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39; buttons. Final actions are &#39;CANCEL&#39; and &#39;ADD&#39;." />

This image displays the Copernicus Land Monitoring Service (CLMS) CLC+
Query Builder interface, used to “Add Rule for Output Class ‘2 -
Deciduous’”. The interface allows users to construct complex logical
conditions for land cover classification by combining “Rules” and
“Rulesets”.

The top-level query structure is defined by an “And” or “Or” logical
operator. Within this, nested Rulesets can be created, also linked by
“And” or “Or” operators. Each Ruleset can contain one or more individual
“Rules”.

An example rule is shown for the “EAGLE-Element (LCC-2_1_1) Trees”. For
this rule, “Highest coverage” is selected as the coverage type, and the
“Operator” is set to “\>=”. A dropdown menu for the “EAGLE-Element”
field is open, showing options for handling how the element is
considered: “X (Excluded)”, “1 (Optional)”, “2 (One or more)”, “3 (All
of them)”, “4 (At least two)”, and “5 (This one only)”. For the “Trees”
element, “5 (This one only)” is selected. Another rule within the same
nested Ruleset is partially configured, with “Highest coverage” selected
and the “Operator” also set to “\>=”.

The interface includes options to “Add comment”, “+ Rule”, “+ Ruleset”,
and controls to delete elements. Ancillary information can be accessed
via “Computation manual” and “EAGLE-Elements” buttons. Final actions are
“CANCEL” and “ADD”.

<span id="_Ref153876076" class="anchor"></span>**Figure 4‑24: Select the
barcode value from a drop-down list in the Query Builder.**

Then the comparison operators need to be selected from a drop-down list
([Figure 4‑25](#_Ref153876064)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image153.png"
style="width:6.53054in;height:3.16114in"
data-fig-alt="This is a screenshot of a software interface for the Copernicus Land Monitoring Service (CLMS) CLC+ Query Builder, used to define classification rules for an Output Class, specifically &#39;2 - Deciduous&#39;. The interface has two main tabs: &#39;Query-Builder&#39; (currently active) and &#39;Text&#39;. On the top right, there are buttons for &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39;. The Query Builder allows for nested logical conditions, starting with an outer &#39;And&#39; / &#39;Or&#39; / &#39;Add comment&#39; selection. Inside this, another nested &#39;And&#39; / &#39;Or&#39; / &#39;Add comment&#39; block is shown, which contains two individual rule lines. Each rule line includes radio button options for &#39;Highest coverage&#39;, &#39;First coverage&#39;, or &#39;Total coverage&#39;. The first rule line specifies: - &#39;EAGLE-Element&#39;: &#39;(LCC-2_1_1) Trees&#39; - &#39;Barcode&#39;: &#39;5&#39; - &#39;Operator&#39;: A dropdown menu is open, displaying options: &#39;&gt;= &#39;, &#39;&gt;&#39;, &#39;==&#39;, &#39;!=&#39;, &#39;&lt;=&#39;, &#39;&lt;&#39; - &#39;Coverage Value&#39; (an input field) The second rule line has empty input fields for &#39;EAGLE-Element&#39;, &#39;Barcode&#39;, &#39;Operator&#39;, and &#39;Coverage Value&#39;. Both rule lines include icons for text and number inputs (a &#39;text-A&#39; icon and a green &#39;#&#39; icon), and buttons to &#39;+ Rule&#39;, &#39;+ Ruleset&#39;, or &#39;-&#39; (delete) for individual rules or rule sets. At the bottom right, &#39;CANCEL&#39; and &#39;ADD&#39; buttons are present for managing the rule definition." />

This is a screenshot of a software interface for the Copernicus Land
Monitoring Service (CLMS) CLC+ Query Builder, used to define
classification rules for an Output Class, specifically ‘2 - Deciduous’.
The interface has two main tabs: “Query-Builder” (currently active) and
“Text”. On the top right, there are buttons for “Computation manual” and
“EAGLE-Elements”.

The Query Builder allows for nested logical conditions, starting with an
outer “And” / “Or” / “Add comment” selection. Inside this, another
nested “And” / “Or” / “Add comment” block is shown, which contains two
individual rule lines. Each rule line includes radio button options for
“Highest coverage”, “First coverage”, or “Total coverage”.

The first rule line specifies: - “EAGLE-Element”: “(LCC-2_1_1) Trees” -
“Barcode”: “5” - “Operator”: A dropdown menu is open, displaying
options: “\>=”, “\>”, “==”, “!=”, “\<=”, “\<” - “Coverage Value” (an
input field)

The second rule line has empty input fields for “EAGLE-Element”,
“Barcode”, “Operator”, and “Coverage Value”. Both rule lines include
icons for text and number inputs (a “text-A” icon and a green “\#”
icon), and buttons to “+ Rule”, “+ Ruleset”, or “-” (delete) for
individual rules or rule sets. At the bottom right, “CANCEL” and “ADD”
buttons are present for managing the rule definition.

<span id="_Ref153876064" class="anchor"></span>**Figure 4‑25: Select the
comparison operators in the Query Builder.**

The last step is setting the percentage coverage of the aggregated
value.

**Note: Aggregated means that for the i.e. 100 underlying 10 m pixel
values the arithmetic mean is calculated. As a consequence, several
thematic classes share one 100 m pixel and the coverage value indicates
the percentage of a pixel’s area that is covered by a barcoded EAGLE
element. In an Extraction, this pixel is assigned to a single class by
evaluating the Class Conditions of all Output Classes until one is found
whose ruleset matches.**

Subsequently, add other EAGLE elements to complete the Ruleset. Clicking
on “**ADD**” will save the Class Condition (see [Figure
4‑26](#_Ref153876041)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image155.png"
style="width:6.50905in;height:3.16575in"
data-fig-alt="This is a screenshot of a graphical user interface (GUI) titled &#39;Add Rule for Output Class &#39;2 - FL Deciduous&#39;&#39;, showcasing the Query-Builder tab. The interface allows users to define rules based on EAGLE (EIONET Action Group on Land monitoring in Europe) elements and associated values. The top section indicates a global logic with &#39;And&#39; (selected) and &#39;Or&#39; radio buttons, along with an &#39;Add comment&#39; button. On the right, there are links for &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39; along with buttons to add a &#39;+ Rule&#39; or &#39;+ Ruleset&#39;. Below this, the interface displays nested rule sets. The first main rule set is active, starting with an &#39;And&#39; (selected) / &#39;Or&#39; choice, and an &#39;Add comment&#39; button. Inside this set, two individual rules are defined: 1. For &#39;EAGLE-Element *&#39; identified as &#39;(LCC-2_1_1) Trees&#39;, with &#39;Total coverage&#39; selected, a &#39;Barcode *&#39; of &#39;5&#39;, an &#39;Operator *&#39; of &#39;&gt;=&#39;, and a &#39;Coverage Value *&#39; of &#39;30&#39;. 2. For &#39;EAGLE-Element *&#39; identified as &#39;(LCH-3_1_2) Broad Leaved&#39;, with &#39;Total coverage&#39; selected, a &#39;Barcode *&#39; of &#39;2&#39;, an &#39;Operator *&#39; of &#39;&gt;=&#39;, and a &#39;Coverage Value *&#39; of &#39;30&#39;. A second, similar rule set is partially visible below the first, also starting with &#39;And&#39; (selected) / &#39;Or&#39; and &#39;Add comment&#39;. It contains one visible rule: 1. For &#39;EAGLE-Element *&#39; identified as &#39;(LCC-2_1_1) Trees&#39;, with &#39;Total coverage&#39; selected, a &#39;Barcode *&#39; of &#39;5&#39;, an &#39;Operator *&#39; of &#39;&gt;=&#39;, and a &#39;Coverage Value *&#39; of &#39;30&#39;. The bottom right corner shows &#39;CANCEL&#39; and &#39;ADD&#39; buttons to manage the rule definition." />

This is a screenshot of a graphical user interface (GUI) titled “Add
Rule for Output Class ‘2 - FL Deciduous’”, showcasing the Query-Builder
tab. The interface allows users to define rules based on EAGLE (EIONET
Action Group on Land monitoring in Europe) elements and associated
values.

The top section indicates a global logic with “And” (selected) and “Or”
radio buttons, along with an “Add comment” button. On the right, there
are links for “Computation manual” and “EAGLE-Elements” along with
buttons to add a “+ Rule” or “+ Ruleset”.

Below this, the interface displays nested rule sets. The first main rule
set is active, starting with an “And” (selected) / “Or” choice, and an
“Add comment” button. Inside this set, two individual rules are
defined: 1. For “EAGLE-Element *” identified as ”(LCC-2_1_1) Trees”,
with ”Total coverage” selected, a ”Barcode* ” of “5”, an “Operator *” of
”\>=”, and a ”Coverage Value* ” of “30”. 2. For “EAGLE-Element *”
identified as ”(LCH-3_1_2) Broad Leaved”, with ”Total coverage”
selected, a ”Barcode* ” of “2”, an “Operator *” of ”\>=”, and a
”Coverage Value* ” of “30”.

A second, similar rule set is partially visible below the first, also
starting with “And” (selected) / “Or” and “Add comment”. It contains one
visible rule: 1. For “EAGLE-Element *” identified as ”(LCC-2_1_1)
Trees”, with ”Total coverage” selected, a ”Barcode* ” of “5”, an
“Operator *” of ”\>=”, and a ”Coverage Value* ” of “30”.

The bottom right corner shows “CANCEL” and “ADD” buttons to manage the
rule definition.

<span id="_Ref153876041" class="anchor"></span>**Figure 4‑26: Class
Condition for Output Class “Deciduous Forest” set up in the Query
Builder.**

You also have the option to add comments to your Class Conditions (see
[Figure 4‑27](#_Ref153958528)). Especially, if the Rulesets are getting
more complex, the commenting function might be very helpful. You can use
it to document your intentions because due to the usage of the EAGLE
elements, the connection to the Ingestions and/or Input Classes gets
lost or difficult to keep track. There is of course also the possibility
to delete the comments.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image156.png"
style="width:6.50611in;height:3.13496in"
data-fig-alt="This is a user interface diagram of a Query Builder for adding a rule for the Output Class &#39;2 - FL Deciduous&#39; within a Copernicus Land Monitoring Service (CLMS) application, likely for CORINE Land Cover (CLC+) or High Resolution Layer (HRL) processing. The interface allows users to construct complex logical rules based on EAGLE (European Approach for Geographical Information Layering) elements. The rule definition workflow is as follows: 1. Users define a rule or ruleset with an optional comment, selecting either &#39;And&#39; or &#39;Or&#39; logic for combining conditions. 2. The top-level rule group is configured with &#39;And&#39; logic and the comment &#39;Intersect HRL with CLC+ BB classes&#39;. 3. Nested within this, a second rule group is also configured with &#39;And&#39; logic and the comment &#39;HRL Forest broadleaved classes&#39;. 4. This nested group contains two specific rule conditions, both using &#39;Total coverage&#39; as the selected criterion: * **Condition 1:** The &#39;EAGLE-Element&#39; &#39;(LCC-2_1_1) Trees&#39; with &#39;Barcode&#39; 5 and &#39;Operator&#39; `&gt;=` for a &#39;Coverage Value&#39; of 30. * **Condition 2:** The &#39;EAGLE-Element&#39; &#39;(LCH-3_1_2) Broad Leaved&#39; with &#39;Barcode&#39; 2 and &#39;Operator&#39; `&gt;=` for a &#39;Coverage Value&#39; of 30. 5. Users can add more individual rules (&#39;+ Rule&#39;) or rule groups (&#39;+ Ruleset&#39;) at any level, and remove existing rules using a trashcan icon. 6. The interface also includes buttons for a &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39; information. 7. The process concludes with &#39;CANCEL&#39; or &#39;ADD&#39; actions to either discard or save the defined rule." />

This is a user interface diagram of a Query Builder for adding a rule
for the Output Class ‘2 - FL Deciduous’ within a Copernicus Land
Monitoring Service (CLMS) application, likely for CORINE Land Cover
(CLC+) or High Resolution Layer (HRL) processing. The interface allows
users to construct complex logical rules based on EAGLE (European
Approach for Geographical Information Layering) elements.

The rule definition workflow is as follows: 1. Users define a rule or
ruleset with an optional comment, selecting either “And” or “Or” logic
for combining conditions. 2. The top-level rule group is configured with
“And” logic and the comment “Intersect HRL with CLC+ BB classes”. 3.
Nested within this, a second rule group is also configured with “And”
logic and the comment “HRL Forest broadleaved classes”. 4. This nested
group contains two specific rule conditions, both using “Total coverage”
as the selected criterion: \* **Condition 1:** The “EAGLE-Element”
“(LCC-2_1_1) Trees” with “Barcode” 5 and “Operator” `>=` for a “Coverage
Value” of 30. \* **Condition 2:** The “EAGLE-Element” “(LCH-3_1_2) Broad
Leaved” with “Barcode” 2 and “Operator” `>=` for a “Coverage Value” of
30. 5. Users can add more individual rules (“+ Rule”) or rule groups (“+
Ruleset”) at any level, and remove existing rules using a trashcan icon.
6. The interface also includes buttons for a “Computation manual” and
“EAGLE-Elements” information. 7. The process concludes with “CANCEL” or
“ADD” actions to either discard or save the defined rule.

<span id="_Ref153958528" class="anchor"></span>**Figure 4‑27: Add
comments to the Rulesets.**

If you are familiar with query language, you are also able to use the
“Text field”. In [Figure 4‑28](#_Ref105174879), you can see the Class
Condition and its rules in an **expression language** in the Text tab.
If you have added a comment, this is also shown here. If you want to
reuse a created Class Condition or parts of it in a different class,
copy the respective text and paste it in a different Output Classes
Class Condition text editor.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image157.png"
style="width:6.46142in;height:1.7926in"
data-fig-alt="This image is a screenshot of a CLC+ (Copernicus Land Monitoring Service CORINE Land Cover Plus) Query Builder interface, displaying the &#39;Text&#39; tab for adding a rule to an output land cover class. The interface title is &#39;Add Rule for Output Class &#39;2 - FL Deciduous&#39;&#39;. Below the title, two tabs are visible: &#39;Query-Builder&#39; and &#39;Text&#39;, with the &#39;Text&#39; tab actively selected and highlighted by a green underline. On the right side of the header, two buttons are displayed: &#39;Computation manual&#39; and &#39;EAGLE-Elements&#39; (with a leaf-like icon). The main content area under the &#39;Text&#39; tab contains a text editor box labeled &#39;Insert your rule here&#39;. The rule defines classification conditions in a programmatic format: ``` # Intersect HRL with CLC+ BB classes ( # HRL Forest broadleaved classes sumCov(&#39;LCC-trees&#39;, 5) &gt;= 30&amp;&amp; sumCov(&#39;LCH-broad-leaved&#39;, 2) &gt;= 30 )&amp;&amp; ( sumCov(&#39;LCC-trees&#39;, 5) &gt;= 30&amp;&amp; sumCov(&#39;LCH-deciduous&#39;, 5) &gt;= 30&amp;&amp; sumCov(&#39;LCH-broad-leaved&#39;, 5) &gt;= 30 ) ``` This rule specifies conditions for an aggregated pixel to be classified as &#39;FL Deciduous&#39; (Forest Deciduous). It requires the logical AND (`&amp;&amp;`) of two main condition groups. The first group, commented as `# HRL Forest broadleaved classes`, requires the `sumCov` (sum of coverage) of the `EAGLE Element` &#39;LCC-trees&#39; with barcode `5` to be greater than or equal to 30%, AND the `sumCov` of &#39;LCH-broad-leaved&#39; with barcode `2` to be greater than or equal to 30%. This entire group is then ANDed with a second group of conditions: `sumCov` of &#39;LCC-trees&#39; with barcode `5` &gt;= 30% AND `sumCov` of &#39;LCH-deciduous&#39; with barcode `5` &gt;= 30% AND `sumCov` of &#39;LCH-broad-leaved&#39; with barcode `5` &gt;= 30%. The `sumCov` function indicates the percentage of an aggregated pixel&#39;s area covered by the specified `EAGLE Element` barcode. Below the rule content, a section titled &#39;Rule Structure&#39; is visible, stating &#39;(i) No comments&#39;." />

This image is a screenshot of a CLC+ (Copernicus Land Monitoring Service
CORINE Land Cover Plus) Query Builder interface, displaying the “Text”
tab for adding a rule to an output land cover class. The interface title
is “Add Rule for Output Class ‘2 - FL Deciduous’”. Below the title, two
tabs are visible: “Query-Builder” and “Text”, with the “Text” tab
actively selected and highlighted by a green underline. On the right
side of the header, two buttons are displayed: “Computation manual” and
“EAGLE-Elements” (with a leaf-like icon).

The main content area under the “Text” tab contains a text editor box
labeled “Insert your rule here”. The rule defines classification
conditions in a programmatic format:

    # Intersect HRL with CLC+ BB classes
    (
        # HRL Forest broadleaved classes
        sumCov('LCC-trees', 5) >= 30&&
        sumCov('LCH-broad-leaved', 2) >= 30
    )&&
    (
        sumCov('LCC-trees', 5) >= 30&&
        sumCov('LCH-deciduous', 5) >= 30&&
        sumCov('LCH-broad-leaved', 5) >= 30
    )

This rule specifies conditions for an aggregated pixel to be classified
as ‘FL Deciduous’ (Forest Deciduous). It requires the logical AND (`&&`)
of two main condition groups. The first group, commented as
`# HRL Forest broadleaved classes`, requires the `sumCov` (sum of
coverage) of the `EAGLE Element` ‘LCC-trees’ with barcode `5` to be
greater than or equal to 30%, AND the `sumCov` of ‘LCH-broad-leaved’
with barcode `2` to be greater than or equal to 30%. This entire group
is then ANDed with a second group of conditions: `sumCov` of ‘LCC-trees’
with barcode `5` \>= 30% AND `sumCov` of ‘LCH-deciduous’ with barcode
`5` \>= 30% AND `sumCov` of ‘LCH-broad-leaved’ with barcode `5` \>= 30%.
The `sumCov` function indicates the percentage of an aggregated pixel’s
area covered by the specified `EAGLE Element` barcode. Below the rule
content, a section titled “Rule Structure” is visible, stating “(i) No
comments”.

<span id="_Ref105174879" class="anchor"></span>**Figure 4‑28: Class
Condition in expression language.**

Further, there are two information boxes at the top right. By clicking
on “Computational Manual”, a window next to the Query Builder appears
([Figure 4‑29](#_Ref153880313)). It explains how the Extraction result
is computes by explaining the details about which Input Classes’
coverages are considered during the calculation of Coverage Functions.
In section [4.6](#how-is-the-extraction-result-computed), the whole
process and the single Coverage Functions are described in more detail.

You need to select either of the three options which might fit best to
your requirements. Highest Coverage is the default and is recommended.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image158.png"
style="width:6.56569in;height:3.15051in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover Plus) &#39;Query-Builder&#39; interface, titled &#39;Add Rule for Output Class &#39;2 - FL Deciduous&#39;&#39; (Forest Land Deciduous). The interface allows users to construct hierarchical rules for land cover classification using &#39;And&#39; or &#39;Or&#39; logical operators. The main rule shown is commented &#39;Intersect HRL with CLC+ BB classes&#39; (likely Broadleaved). Nested within this, using an &#39;And&#39; operator, is a condition commented &#39;HRL Forest broadleaved classes&#39;. This nested condition comprises two sub-conditions, both configured for &#39;Total coverage&#39;: 1. **EAGLE-Element:** &#39;(LCC-2_2_1_1) Trees&#39;, with Barcode &#39;5&#39;, using an Operator &#39;&gt;=&#39; for a Coverage Value of &#39;30&#39;. 2. **EAGLE-Element:** &#39;(LCH-3_1_2) Broad Leaved&#39;, with Barcode &#39;2&#39;, using an Operator &#39;&gt;=&#39; for a Coverage Value of &#39;30&#39;. On the right side, a &#39;Computation manual&#39; sidebar is open, containing collapsible sections for &#39;How is the extraction result computed?&#39;, &#39;Highest Coverage / maxCov(...)&#39;, &#39;First Coverage / firstCov(...)&#39;, &#39;Total Coverage / sumCov(...)&#39;, &#39;Examples&#39;, &#39;Glossary&#39;, and &#39;Aggregation rules&#39;. The interface includes &#39;CANCEL&#39; and &#39;ADD&#39; buttons at the bottom." />

A screenshot of the Copernicus Land Monitoring Service (CLMS) CLC+
(CORINE Land Cover Plus) “Query-Builder” interface, titled “Add Rule for
Output Class ‘2 - FL Deciduous’” (Forest Land Deciduous). The interface
allows users to construct hierarchical rules for land cover
classification using “And” or “Or” logical operators.

The main rule shown is commented “Intersect HRL with CLC+ BB classes”
(likely Broadleaved). Nested within this, using an “And” operator, is a
condition commented “HRL Forest broadleaved classes”. This nested
condition comprises two sub-conditions, both configured for “Total
coverage”: 1. **EAGLE-Element:** “(LCC-2_2_1_1) Trees”, with Barcode
“5”, using an Operator “\>=” for a Coverage Value of “30”. 2.
**EAGLE-Element:** “(LCH-3_1_2) Broad Leaved”, with Barcode “2”, using
an Operator “\>=” for a Coverage Value of “30”.

On the right side, a “Computation manual” sidebar is open, containing
collapsible sections for “How is the extraction result computed?”,
“Highest Coverage / maxCov(…)”, “First Coverage / firstCov(…)”, “Total
Coverage / sumCov(…)”, “Examples”, “Glossary”, and “Aggregation rules”.
The interface includes “CANCEL” and “ADD” buttons at the bottom.

<span id="_Ref153880313" class="anchor"></span>**Figure 4‑29:
Computational Manual.**

## How is the extraction result computed?

Each pixel of the output raster is assigned to the first output class
whose **Class Condition** is fulfilled. If none of the class conditions
are fulfilled for a given pixel, it remains unclassified (i.e. its value
is *No-Data)*. This computation is done independently for each pixel,
which means that a pixel is never influenced by its neighbors.

**Class Conditions** consist at the core of **Rules,** which perform a
comparison of the **Coverage** value of a barcoded EAGLE elements
against a threshold. The coverage value of a barcoded EAGLE element is
computed with a **Coverage Function.** This computation works by:

1.  Selecting the **Input Classes** that were explicitly mapped with the
    given EAGLE element and barcode during the ingestion process or that
    are mapped with a direct child in the EAGLE ontology (aggregation
    rule 5),

2.  Further restricting this selection based on the type of **Coverage
    Function** (aggregation rule 3)

3.  Calculating the **Coverage** sum of all selected **Input Classes**
    (aggregation rule 2).

You can choose between three types of **Coverage Function** in your
rules. They differ only in which of the matching input classes are
chosen and aggregated (i.e. step 2). The selection of matching input
classes (step 1) and the final aggregation (step 3) are always the same.
In the following the different **Coverage Functions** are described in
more detail:

**Highest Coverage / maxCov(...)**

This function groups the matching **Input Classes** by **Ingestion**,
selects the group that has the highest **Coverage** sum for the current
pixel, and returns that coverage sum. If no **Input Class** has a value,
the result is NO DATA.

This choice of **Coverage Function** makes sense if you want to know
whether at least one of your chosen **Ingestions** reaches a given
minimum **Coverage** for a certain EAGLE-element-barcode-combination.

**First Coverage / firstCov(...)**

This function examines the **Input Classes** from top to bottom until
the first one is found that has a value (not *NO DATA*) for the current
pixel. It selects this class and all the other matching **Input
Classes** of the same **Ingestion** and returns their sum of
**Coverages**. If none of the classes have a value, it returns *NO
DATA*.

For this function the ordering of **Input Classes** is relevant for the
result, so make sure that they are sorted by their priority.

This choice of **Coverage Function** makes sense when aggregating
datasets that describe the same features but have different quality and
spatial extent. The first **Coverage Function** allows you to prioritize
the high-quality **Ingestion** wherever it’s available and fall back to
the low-quality one otherwise.

**Total Coverage / sumCov(…)**

This function selects all the matching **Input Classes** independent of
which **Ingestion** they belong to and returns their coverage sum, or
NO-DATA if none of them has a value.

This choice of **Coverage Function** can make sense if you need to sum
up coverages of **Input Classes** that belong to different Ingestions,
which is not possible with the two other function types. However, sumCov
comes with the risk of producing **Coverage** values bigger than a
hundred percent if Input Classes are summed up which are not
semantically disjunct.

**Examples**

Consider the following ranked **Input Classes** that have a matching
EAGLE barcoding of LCC-Water with barcode 5.

| **Extraction Input Class** | **Ingestion** | **Mapping**       | **Value**   |
|----------------------------|---------------|-------------------|-------------|
| **A1**                     | **A**         | **LCC-Water / 5** | **NO-DATA** |
| B1                         | B             | LCC-Trees / 5     | 80 %        |
| **B2**                     | **B**         | **LCC-Water / 5** | **15 %**    |
| **B3**                     | **B**         | **LCC-Water / 5** | **5 %**     |
| **C1**                     | **C**         | **LCC-Water / 5** | **40%**     |
| C2                         | C             | LCC-Trees / 5     | 60 %        |

Assume a rule that checks that the coverage value of *LCC-Water* with
Barcode 5 is greater or equals 50. Let’s look at the results of the
different **Coverage Functions** in this case:

- **maxCov(“LCC-Water”, 5)** returns the highest coverage sum of
  matching **Input Classes** within any **Ingestion**, which is in this
  case the **Coverage** of C1 (40%). That’s smaller than 50 % so the
  rule is *false*.

- **firstCov(“LCC-Water”, 5)** looks for the first matching **Input
  Class** with a value (B2) and returns all the matching classes of that
  **Ingestion** (B2 + B3 = 20%). 20 % is smaller than 50 %, so the rule
  is *false*.

- **sumCov(“LCC-Water”, 5)** returns the **Coverage** sum of all
  matching **Input Classes** independent of which **Ingestion** they
  belong to (B2 + B3 + C1 = 60%). That’s bigger than 50 %, so the rule
  is *true.*

Using the EAGLE elements information box will list all the relevant
EAGLE elements and show the Input Classes, Ingestions and the barcode
value ([Figure 4‑30](#_Ref153880277)). So, in this example: EAGLE
element “Trees” with barcode 5 is included in the following Information:
i.e. Broadleaved class from DLT 2018, broadleaved, deciduous trees from
CLC+ BB 2018, etc. By clicking on the Ingestion link, you will be
transferred to the Ingestion view of this dataset.

This will help users to avoid errors and get a better overview and
understanding of the used EAGLE elements.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image159.png"
style="width:6.52019in;height:3.14306in"
data-fig-alt="This diagram illustrates a rule definition interface titled &#39;Add Rule for Output Class &#39;2 - FL Deciduous&#39;&#39; within a Query-Builder tab. The interface allows users to construct complex logical conditions using &#39;And&#39; and &#39;Or&#39; operators to define land cover classes based on EAGLE-Elements. The primary rule structure is as follows: 1. The top-level rule starts with an &#39;And&#39; operator and a comment: &#39;Intersect HRL with CLC+ BB classes&#39;. 2. Nested within this is a sub-rule block also beginning with an &#39;And&#39; operator and a comment: &#39;HRL Forest broadleaved classes&#39;. * This block contains two conditions: * Condition 1: &#39;EAGLE-Element&#39; is &#39;(LCC-2_1_1) Trees&#39;, &#39;Barcode&#39; is &#39;5&#39;, and &#39;Operator&#39; is &#39;&gt;=&#39; with a &#39;Value&#39; of &#39;30&#39;. * Condition 2: &#39;EAGLE-Element&#39; is &#39;(LCH-3_1_2) Broad Leaved&#39;, &#39;Barcode&#39; is &#39;2&#39;, and &#39;Operator&#39; is &#39;&gt;=&#39; with a &#39;Value&#39; of &#39;30&#39;. 3. A second, partially visible, sub-rule block also begins with an &#39;And&#39; operator and a comment: &#39;Add comment&#39;. * This block contains two partially visible conditions: * Condition 1: &#39;EAGLE-Element&#39; is &#39;(LCC-2_1_1) Trees&#39;, &#39;Barcode&#39; is &#39;5&#39;, and &#39;Operator&#39; is &#39;&gt;=&#39; with a &#39;Value&#39; of &#39;30&#39;. * Condition 2: &#39;EAGLE-Element&#39; is &#39;(LCH-3_2_2) Deciduous&#39;, &#39;Barcode&#39; is &#39;5&#39;, and &#39;Operator&#39; is &#39;&gt;=&#39; with a &#39;Value&#39; of &#39;[unreadable]&#39;. On the right side of the interface, an &#39;EAGLE-Elements&#39; selection panel is open, displaying a hierarchical list of elements: * &#39;Natural Material Surfaces (LCC-1_2)&#39; * &#39;Trees (LCC-2_1_1)&#39; * &#39;Barcode 5&#39; * &#39;Broadleaved (HRL - Dominant Leaf Type (DLT) 2018)&#39; * &#39;Woody - broadleaved, deciduous trees (CLC+Backbone (2018))&#39; * &#39;Coniferous (HRL - Dominant Leaf Type (DLT) 2018)&#39; (partially visible) The interface includes options for &#39;Aggregation rules&#39; and allows adding new rules or rulesets, editing comments, and deleting elements. Final actions are &#39;CANCEL&#39; or &#39;ADD&#39; the rule." />

This diagram illustrates a rule definition interface titled “Add Rule
for Output Class ‘2 - FL Deciduous’” within a Query-Builder tab. The
interface allows users to construct complex logical conditions using
“And” and “Or” operators to define land cover classes based on
EAGLE-Elements.

The primary rule structure is as follows: 1. The top-level rule starts
with an “And” operator and a comment: “Intersect HRL with CLC+ BB
classes”. 2. Nested within this is a sub-rule block also beginning with
an “And” operator and a comment: “HRL Forest broadleaved classes”. \*
This block contains two conditions: \* Condition 1: “EAGLE-Element” is
“(LCC-2_1_1) Trees”, “Barcode” is “5”, and “Operator” is “\>=” with a
“Value” of “30”. \* Condition 2: “EAGLE-Element” is “(LCH-3_1_2) Broad
Leaved”, “Barcode” is “2”, and “Operator” is “\>=” with a “Value” of
“30”. 3. A second, partially visible, sub-rule block also begins with an
“And” operator and a comment: “Add comment”. \* This block contains two
partially visible conditions: \* Condition 1: “EAGLE-Element” is
“(LCC-2_1_1) Trees”, “Barcode” is “5”, and “Operator” is “\>=” with a
“Value” of “30”. \* Condition 2: “EAGLE-Element” is “(LCH-3_2_2)
Deciduous”, “Barcode” is “5”, and “Operator” is “\>=” with a “Value” of
“\[unreadable\]”.

On the right side of the interface, an “EAGLE-Elements” selection panel
is open, displaying a hierarchical list of elements: \* “Natural
Material Surfaces (LCC-1_2)” \* “Trees (LCC-2_1_1)” \* “Barcode 5” \*
“Broadleaved (HRL - Dominant Leaf Type (DLT) 2018)” \* “Woody -
broadleaved, deciduous trees (CLC+Backbone (2018))” \* “Coniferous
(HRL - Dominant Leaf Type (DLT) 2018)” (partially visible)

The interface includes options for “Aggregation rules” and allows adding
new rules or rulesets, editing comments, and deleting elements. Final
actions are “CANCEL” or “ADD” the rule.

<span id="_Ref153880277" class="anchor"></span>**Figure 4‑30: EAGLE
elements.**

[Table 0‑5](#_Ref105175205) in the Annex shows as an example of LC
category “Forest” with its sublevels and the applied rulesets.

## Preview Extraction and download result

Analog to the Ingestion section, you can run a preview of your
Extraction for a small extent by clicking **Preview** in the Map Viewer.
By doing so, your Extraction result can be visually inspected in the
map. If the preview was successful and the result satisfying, continue
with ‘Start Extraction’ to apply the ruleset for the full extent
([Figure 4‑31](#_Ref153652241)).

By inspecting the data in the map and clicking on the
classification/pixel, a tooltip dialog opens. Under Output Class the
assigned Output Class (here Grassland) is indicated ([Figure
4‑31](#_Ref153652241)). By clicking on the Output Class in the window
the Class unfolds and the result of all the rules of the selected output
class is shown. Here you find the information which rule was true and
which rules was false and the reason why ([Figure
4‑32](#_Ref153972958)). By checking the show all box, all Output Classes
are shown, even the ones that have been ignored because a True condition
was found ([Figure 4‑32](#_Ref153972958)).

The used Input Classes in the section below ([Figure
4‑31](#_Ref153652241)). Further, the coverage of each individual class
is shown. By clicking on the Input Class in the window the Class unfolds
and further information is shown in [Figure 4‑32](#_Ref153972958). Per
default, all Input Classes covering 0% are not shown but this feature
can be enabled by checking the tick box.

Further, you can **download** the dataset (geotiff) and the metadata
(geojson) to be able to inspect and validate your data in more detail in
a GIS program on your local computer ([Figure 4‑31](#_Ref153652241)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image160.png"
style="width:6.5046in;height:3.10749in"
data-fig-alt="A screenshot of the Copernicus Land Monitoring Service (CLMS) web interface for an &#39;Extraction &#39;LULUCF maxCov&#39;&#39; process, showing details for a land cover/land use (LULUCF) data extraction in the Netherlands. The page displays &#39;General Information&#39; on the left panel, including: Name &#39;LULUCF maxCov&#39;, Country &#39;Netherlands/Nederland&#39;, Reference Year &#39;2018&#39;, and Time Range of Extracted Data &#39;2017-01-03 - 2020-01-02&#39;. It indicates compliance with INSPIRE Themes &#39;LU Land use&#39; and &#39;LC Land cover&#39;, and credits &#39;CLC+ Core User Admin/Support&#39;, &#39;CLC&#39; (CORINE Land Cover), and the &#39;European Environment Agency&#39; (EEA) as creators/organisations. The main content area features an interactive map centered on the region &#39;NL11 Groningen&#39; in the Netherlands, with a scale bar showing &#39;500 m&#39; or &#39;3000 ft&#39;. An overlay window on the map details the extraction configuration: &#39;Output Classes&#39; are &#39;GL Pastures&#39;, and &#39;Input Classes&#39; include &#39;Corine Land Cover (CLC) 2018&#39; (Class: &#39;231 - Pastures&#39;, Coverage: &#39;100%&#39;) and &#39;CLC+Backbone (2018)&#39; (Class: &#39;Permanent herbaceous (i.e. grasslands)&#39;, Coverage: &#39;100%&#39;). The top banner includes navigation links: &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. Available actions for the extracted data are &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START EXTRACTION&#39;, &#39;DOWNLOAD&#39;, and &#39;PUBLISH&#39;. A partially visible table at the bottom suggests further details about the &#39;Input Classes&#39;, with headers like &#39;Rank&#39;, &#39;Class Code&#39;, &#39;Name&#39;, &#39;Ingestion&#39;, and &#39;Eagle Elements&#39;." />

A screenshot of the Copernicus Land Monitoring Service (CLMS) web
interface for an “Extraction ‘LULUCF maxCov’” process, showing details
for a land cover/land use (LULUCF) data extraction in the Netherlands.
The page displays “General Information” on the left panel, including:
Name “LULUCF maxCov”, Country “Netherlands/Nederland”, Reference Year
“2018”, and Time Range of Extracted Data “2017-01-03 - 2020-01-02”. It
indicates compliance with INSPIRE Themes “LU Land use” and “LC Land
cover”, and credits “CLC+ Core User Admin/Support”, “CLC” (CORINE Land
Cover), and the “European Environment Agency” (EEA) as
creators/organisations. The main content area features an interactive
map centered on the region “NL11 Groningen” in the Netherlands, with a
scale bar showing “500 m” or “3000 ft”. An overlay window on the map
details the extraction configuration: “Output Classes” are “GL
Pastures”, and “Input Classes” include “Corine Land Cover (CLC) 2018”
(Class: “231 - Pastures”, Coverage: “100%”) and “CLC+Backbone (2018)”
(Class: “Permanent herbaceous (i.e. grasslands)”, Coverage: “100%”). The
top banner includes navigation links: “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”. Available
actions for the extracted data are “REPUBLISH ON GEOSERVER”, “START
EXTRACTION”, “DOWNLOAD”, and “PUBLISH”. A partially visible table at the
bottom suggests further details about the “Input Classes”, with headers
like “Rank”, “Class Code”, “Name”, “Ingestion”, and “Eagle Elements”.

<span id="_Ref153652241" class="anchor"></span>**Figure 4‑31: Preview
Extraction and download result.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image161.png"
style="width:6.24756in;height:2.86816in"
data-fig-alt="A geographic map displaying land cover patterns in the NL Netherlands/Nederland, specifically the region NL11 Groningen, with an interactive overlay detailing EAGLE element rule evaluations and input classes. The map includes named roads such as &#39;Munnikeweg&#39;, &#39;Mersumaweg&#39;, &#39;Hoofdstraat&#39;, &#39;Hooiweg&#39;, &#39;Gawe en Munnik&#39;, and settlement names like &#39;Boerakker&#39; and &#39;Oostwold&#39;. Land cover is shown with a dominant green colour, interspersed with red, brown, yellow, and blue rectangular parcels. A pink line outlines a boundary on the eastern side. A scale bar indicates 500 m and 3000 ft. The map&#39;s data source is Leaflet | Core003 Mosaic, © OpenStreetMap contributors. An interactive panel, labelled &#39;GL F&#39;, overlays the map. It presents the result of rules applied to a selected output class. Two rules are shown: 1. `maxCov(&#39;LUA-commercial-crop-production&#39;, 5) &gt;= 30.0`, which evaluates to `True`. 2. `maxCov(&#39;LCH-managed-permanent-grassland&#39;, 5) &gt;= 30.0`, which also evaluates to `True`. The `maxCov` function, as per Copernicus Land Monitoring Service (CLMS) documentation, returns the highest coverage sum of matching input classes within any ingestion for a specific EAGLE element (represented by barcode &#39;5&#39; in this context). The panel also lists the input classes used for evaluation in a table: | Rank | Ingestion | Input Class | Coverage | | :--- | :-------------------------------- | :------------- | :------- | | 47 | Corine Land Cover (CLC) 2018 | 231 - Pastures | 100 % | This table confirms that the evaluation is based on 100% coverage of &#39;231 - Pastures&#39; from the CORINE Land Cover (CLC) 2018 dataset." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image162.png"
style="width:6.31865in;height:2.86151in"
data-fig-alt="This image is a screenshot of a Copernicus Land Monitoring Service (CLMS) user interface displaying a geographic map overlaid with an interactive rule evaluation panel. The interface is set for &#39;Country: NL Netherlands/Nederland&#39; and &#39;Region: NL11 Groningen&#39;. The map shows a patchwork of land cover/land use types, with prominent areas in green, brown, red, and dark blue, indicative of an agricultural landscape. Place names visible on the map include &#39;Munninkweg&#39;, &#39;Mensumaweg&#39;, &#39;Bakkerom&#39;, &#39;Hoolweg&#39;, &#39;Boerakker&#39;, &#39;Hoofdweg&#39;, &#39;Oostwold&#39;, and &#39;Hoendiep&#39;. A scale bar indicates 500 m / 3000 ft. The map is credited to &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors&#39;. The central overlay panel, titled &#39;The following table shows the result of all the rules of the selected output class,&#39; lists five evaluation rules. Each rule uses the `maxCov` function (indicating maximum coverage of matching input classes) with a specific Land Cover Class (LCC), Land Use Activity (LUA), or Land Cover Hierarchical (LCH) element, a barcode value of &#39;5&#39;, and a threshold of 30.0%. - Two rules evaluate to `True`: - `maxCov(&#39;LCC-herbaceous-vegetation&#39;, 5) &gt;= 30.0` - `maxCov(&#39;LUA-commercial-crop-production&#39;, 5) &gt;= 30.0` - Three rules evaluate to `False`: - `maxCov(&#39;LCH-arable-crop-land&#39;, 5) &gt;= 30.0` - `maxCov(&#39;LCH-crop-rotation&#39;, 5) &gt;= 30.0` - `maxCov(&#39;LCH-no-irrigation&#39;, 5) &gt;= 30.0` The panel also includes a &#39;PREVIEW&#39; button." /><img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image163.png"
style="width:6.57644in;height:3.00068in"
data-fig-alt="This map displays land cover information for the NL11 Groningen region in the Netherlands, viewed through a Copernicus Land Monitoring Service (CLMS) interface for selecting EAGLE elements. The geographic map shows a detailed mosaic of various land cover / land use (LULC) types, with predominant colours including green, red, dark brown/orange, black, blue, and light yellow, representing an agricultural landscape with features like waterways (e.g., &#39;Hoendiep&#39;) and settlements (e.g., &#39;Boerakker,&#39; &#39;Oostwold,&#39; &#39;Midwolde&#39;). A scale bar in the bottom left indicates distances of &#39;500 m&#39; and &#39;3000 ft.&#39; Map attribution is &#39;Leaflet | © Core003 Mosaic, © OpenStreetMap contributors.&#39; An interactive overlay window, implied to be an &#39;EAGLE elements&#39; selection tool based on surrounding text, lists several land cover classification options with their selection status: * &#39;CL Annual crops&#39; is marked with a red cross (rejected). * &#39;CL Perennial crops&#39; is marked with a red cross (rejected). * &#39;GL Burnt areas&#39; is marked with a red cross (rejected). * &#39;GL Pastures&#39; is marked with a green checkmark (accepted). * &#39;GL Shrubs&#39; is marked with a question mark (status pending/uncertain). * &#39;GL natural grasslands&#39; is marked with a question mark (status pending/uncertain). A scrollbar indicates that more options are available within this list. The top bar of the interface includes dropdown selectors for &#39;Country *&#39; showing &#39;NL Netherlands/Nederland&#39; and &#39;Region *&#39; showing &#39;NL11 Groningen&#39;, alongside a &#39;PREVIEW&#39; button. Zoom controls and a layer icon are visible in the top left corner." /><span id="_Ref153972958"
class="anchor"></span>

**Figure 4‑32: Output Class extraction information.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image164.png"
style="width:6.63608in;height:3.00726in"
data-fig-alt="An interactive geographic map interface showing land cover data for a selected region, NL11 Groningen in the Netherlands, with an overlaid information box detailing Copernicus Land Monitoring Service (CLMS) EAGLE elements. The map displays land cover categories using various colours: large green areas representing vegetation or agricultural land (consistent with grasslands/pastures in the popup), brown areas possibly indicating cultivated fields or bare soil, red areas indicating artificial surfaces or built-up zones, and dark blue/purple areas representing water bodies. Specific place names visible include Oostwold, Boerakker, Hoofdweg, Munnikeweg, and Hoendiep. A scale bar at the bottom left indicates 500 m and 3000 ft. Map controls for zooming, full-screen view, and layer toggling are present on the left. Data attribution at the bottom right states &#39;Leaflet | Core003 Mosaic, © OpenStreetMap contributors&#39;. Input fields at the top allow selection of &#39;Country&#39; (NL Netherlands/Nederland) and &#39;Region&#39; (NL11 Groningen), alongside a &#39;PREVIEW&#39; button. An overlaid information dialog box, identified as &#39;EAGLE elements&#39;, displays land cover classifications and their coverage: * Under &#39;Ingestion&#39; for &#39;CLC+Backbone (2018)&#39;, the &#39;Class&#39; is &#39;Permanent herbaceous (i.e. grasslands)&#39; with a &#39;Coverage&#39; of &#39;100 %&#39;. * Under &#39;Ingestion&#39; for &#39;Corine Land Cover (CLC) 2018&#39;, the &#39;Class&#39; is &#39;231 - Pastures&#39; with a &#39;Coverage&#39; of &#39;100 %&#39;. Below these, a list of individual EAGLE elements is shown, each with a barcode and a coverage value (represented as a decimal proportion of 1.00): * Boulders, Stones: 1 / 1.00 * Trees: 1 / 1.00 * Regular Bushes: 1 / 1.00 * Grasses, Sedges, Rushes, Cereals: 3 / 1.00 * Non-Graminoids, Forbs, Ferns: 1 / 1.00 * Commercial Crop Production: 5 / 1.00 * Managed Permanent Grassland: 5 / 1.00 * No Crop Rotation: 5 / 1.00 (partially cut off)" /><span id="_Ref153972533"
class="anchor"></span>

**Figure 4‑33: Input Class extraction information.**

## Publish Extraction and download result

You can publish an Extraction by clicking on the ‘**publish**’ button in
the detail view. Similar to the IngestionI, you can choose the
Visibility of your Extraction (public/private/national) ([Figure
4‑34](#_Ref153652068)).

Further, you can download the dataset (geotiff) and the metadata
(geojson) to be able to inspect your data in more detail in a GIS
program on your local computer ([Figure 4‑34](#_Ref153652068)).

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image166.png"
style="width:6.77917in;height:3.22917in"
data-fig-alt="This image is a screenshot of a web interface for publishing an extracted dataset within the Copernicus Land Monitoring Service (CLMS) CLC+ (CORINE Land Cover+) Core system. The interface displays &#39;General Information&#39; for an extraction named &#39;CLC+ Instance_LULUCF_2021_NL&#39; for the &#39;Netherlands/Nederland&#39; in the &#39;Groningen&#39; region (NUTS code NL11 visible on the map) with a &#39;Reference Year&#39; of &#39;2018&#39; and &#39;Time Range of Extracted Data&#39; from &#39;01.12.2018 - 31.12.2018&#39;. It is associated with INSPIRE (Infrastructure for Spatial Information in the European Community) Themes &#39;LU Land use&#39; and &#39;LC Land cover&#39;, created by &#39;User Admin/Support CLC+ Core&#39;, and managed by the &#39;European Environment Agency&#39; (EEA). The main part of the screenshot features a &#39;Publish Extraction &#39;CLC+ Instance_LULUCF_2021_NL&#39;&#39; modal dialog overlaying the page. The dialog explains: &#39;Publishing &#39;CLC+ Instance_LULUCF_2021_NL&#39; will make it accessible for other users within CLC+ Core according to the visibility that you define - Please select the preferred visibility setting:&#39;. Three visibility options are presented: &#39;Public - All Organisations&#39; (highlighted), &#39;National - Countries of selected Organisations&#39;, and &#39;Private - Selected Organisations&#39;. The dialog also includes &#39;CANCEL&#39; and &#39;PUBLISH&#39; buttons (partially visible). The background of the interface shows navigational elements: &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. Action buttons include &#39;EXTRACTED&#39;, &#39;REPUBLISH ON GEOSERVER&#39;, &#39;START EXTRACTION&#39;, &#39;DOWNLOAD&#39;, and &#39;PUBLISH&#39;. A map viewer on the right displays the highlighted &#39;NL11 Groningen&#39; region within the Netherlands, with a scale bar indicating &#39;50 km&#39; and &#39;30 mi&#39;, and attribution to &#39;Leaflet | Core003 Mosaic, © OpenStreetMap contributors&#39;. A label for &#39;Input Classes&#39; is partially visible at the bottom." />

This image is a screenshot of a web interface for publishing an
extracted dataset within the Copernicus Land Monitoring Service (CLMS)
CLC+ (CORINE Land Cover+) Core system. The interface displays “General
Information” for an extraction named “CLC+ Instance_LULUCF_2021_NL” for
the “Netherlands/Nederland” in the “Groningen” region (NUTS code NL11
visible on the map) with a “Reference Year” of “2018” and “Time Range of
Extracted Data” from “01.12.2018 - 31.12.2018”. It is associated with
INSPIRE (Infrastructure for Spatial Information in the European
Community) Themes “LU Land use” and “LC Land cover”, created by “User
Admin/Support CLC+ Core”, and managed by the “European Environment
Agency” (EEA).

The main part of the screenshot features a “Publish Extraction ‘CLC+
Instance_LULUCF_2021_NL’” modal dialog overlaying the page. The dialog
explains: “Publishing ‘CLC+ Instance_LULUCF_2021_NL’ will make it
accessible for other users within CLC+ Core according to the visibility
that you define - Please select the preferred visibility setting:”.
Three visibility options are presented: “Public - All Organisations”
(highlighted), “National - Countries of selected Organisations”, and
“Private - Selected Organisations”. The dialog also includes “CANCEL”
and “PUBLISH” buttons (partially visible).

The background of the interface shows navigational elements: “Data
Catalogue”, “EAGLE Ontology”, “About EAGLE”, “Organisations”, and
“Users”. Action buttons include “EXTRACTED”, “REPUBLISH ON GEOSERVER”,
“START EXTRACTION”, “DOWNLOAD”, and “PUBLISH”. A map viewer on the right
displays the highlighted “NL11 Groningen” region within the Netherlands,
with a scale bar indicating “50 km” and “30 mi”, and attribution to
“Leaflet \| Core003 Mosaic, © OpenStreetMap contributors”. A label for
“Input Classes” is partially visible at the bottom.

<span id="_Ref153652068" class="anchor"></span>**Figure 4‑34: Publish
Extraction and download result.**

## Reuse Extraction

Further, you can **reuse** an Extraction. By right clicking on the
Extraction in the Data Catalogue, a small window with several options
opens (see [Figure 4‑35](#_Ref153652480)). Here, the Add Extraction
dialog opens again, with all the fields containing the previous
information entered such as name, country, region (see [Figure
4‑36](#_Ref153652678)). This is only true, if the user does share the
same organisation with the entry or is a USER_ADMIN. Otherwise, the
entry will either way is not visible to the user.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image167.png"
style="width:6.72917in;height:3.20139in"
data-fig-alt="This image displays a data catalogue table from a Copernicus Land Monitoring Service (CLMS) web interface, showing details of various CLC+ data extractions. The table contains 10 rows of data with the following columns: &#39;Name&#39;, &#39;Type&#39;, &#39;Created By&#39;, &#39;Country&#39;, &#39;Time Range&#39;, and &#39;Status&#39;. The table data is as follows: | Name | Type | Created By | Country | Time Range | Status | |---|---|---|---|---|---| | CLC+_Instance_LULUCF_2021_NI | [action icon] | User Admin/Support CLC+ Core |" />

This image displays a data catalogue table from a Copernicus Land
Monitoring Service (CLMS) web interface, showing details of various CLC+
data extractions. The table contains 10 rows of data with the following
columns: “Name”, “Type”, “Created By”, “Country”, “Time Range”, and
“Status”.

The table data is as follows: \| Name \| Type \| Created By \| Country
\| Time Range \| Status \| \|—\|—\|—\|—\|—\|—\| \|
CLC+\_Instance_LULUCF_2021_NI \| \[action icon\] \| User Admin/Support
CLC+ Core \|

<span id="_Ref153652480" class="anchor"></span>**Figure 4‑35: Reuse
Extraction.**

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image168.png"
style="width:6.925in;height:3.87292in"
data-fig-alt="This image displays a screenshot of a web interface for a Data Catalogue, focusing on an &#39;Add Extraction&#39; modal dialog. The main interface shows a header navigation bar with &#39;Data Catalogue&#39;, &#39;EAGLE Ontology&#39;, &#39;About EAGLE&#39;, &#39;Organisations&#39;, and &#39;Users&#39;. Below this, the &#39;Data Catalogue&#39; section features filters (&#39;Filter&#39;, &#39;My organisati...&#39;, &#39;My d...&#39;, &#39;Ingesti...&#39;, &#39;Extracti...&#39;, &#39;Search&#39;) and buttons (&#39;ADD INGES...&#39;, &#39;ADD E...&#39;). A table in the background is partially visible, displaying columns &#39;Name&#39;, &#39;Type&#39;, and &#39;Status&#39;. Selected rows include: * &#39;CLC+_Instance_LULUCF_2021_NL&#39; with Status &#39;EXTRACTED&#39;. * &#39;Test Instances Issue with Eurocrop = ...&#39; with Status &#39;EXTRACTED&#39;. * &#39;LULUCF_beta_1.1_backup&#39; with Status &#39;EXTRACTED_PREVIEW&#39;. * &#39;CLC+_Instance_LULUCF_2018_beta_1...&#39; with Status &#39;EXTRACTED_PREVIEW&#39;. * &#39;CLC+_Instance_LULUCF_2018_alpha_...&#39; with Status &#39;DRAFT&#39;. * &#39;CLC+_Instances_alphaV2.0_TEST_GAF&#39; with Status &#39;EXTRACTED_PREVIEW&#39;. * &#39;CLC+_Instance_LULUCF_2018_alpha_...&#39; by &#39;User Admin/Support CLC+ Core&#39; for &#39;Ireland/Éire&#39; with date range &#39;01.01.2017 - 31.12.2019&#39; and Status &#39;EXTRACTED&#39;. * &#39;CLC+_Instance_LULUCF_2018_alpha_...&#39; by &#39;User Admin/Support CLC+ Core&#39; for &#39;Spain/España&#39; with date range &#39;02.01.2023 - 13.01.2023&#39; and Status &#39;PUBLISHED&#39;. * &#39;workshop_example_extraction_GRA&#39; by &#39;User Admin/Support CLC+ Core&#39; for &#39;Denmark/Danmark&#39; with date range &#39;01.01.2018 - 31.12.2018&#39; and Status &#39;EXTRACTED_PREVIEW&#39;. * &#39;workshop_example_extraction_urban&#39; by &#39;User Admin/Support CLC+ Core&#39; for &#39;Denmark/Danmark&#39; with date range &#39;01.01.2018 - 31.12.2018&#39; and Status &#39;EXTRACTED_PREVIEW&#39;. The modal dialog titled &#39;Add Extraction&#39; is overlaid on the Data Catalogue. It contains three input fields: 1. &#39;Name *&#39; (required): pre-filled with &#39;CLC+ Instance_LULUCF_2021_DE&#39;. 2. &#39;Country *&#39; (required): pre-filled with &#39;DE Germany/Deutschland&#39;. 3. &#39;Region&#39; (optional): an empty text field. Buttons at the bottom of the dialog are &#39;CANCEL&#39; and &#39;ADD&#39;." />

This image displays a screenshot of a web interface for a Data
Catalogue, focusing on an ‘Add Extraction’ modal dialog. The main
interface shows a header navigation bar with “Data Catalogue”, “EAGLE
Ontology”, “About EAGLE”, “Organisations”, and “Users”. Below this, the
“Data Catalogue” section features filters (“Filter”, “My organisati…”,
“My d…”, “Ingesti…”, “Extracti…”, “Search”) and buttons (“ADD INGES…”,
“ADD E…”).

A table in the background is partially visible, displaying columns
“Name”, “Type”, and “Status”. Selected rows include: \*
“CLC+\_Instance_LULUCF_2021_NL” with Status “EXTRACTED”. \* “Test
Instances Issue with Eurocrop = …” with Status “EXTRACTED”. \*
“LULUCF_beta_1.1_backup” with Status “EXTRACTED_PREVIEW”. \*
“CLC+\_Instance_LULUCF_2018_beta_1…” with Status “EXTRACTED_PREVIEW”. \*
“CLC+*Instance_LULUCF_2018_alpha*…” with Status “DRAFT”. \*
“CLC+\_Instances_alphaV2.0_TEST_GAF” with Status “EXTRACTED_PREVIEW”. \*
“CLC+*Instance_LULUCF_2018_alpha*…” by “User Admin/Support CLC+ Core”
for “Ireland/Éire” with date range “01.01.2017 - 31.12.2019” and Status
“EXTRACTED”. \* “CLC+*Instance_LULUCF_2018_alpha*…” by “User
Admin/Support CLC+ Core” for “Spain/España” with date range
“02.01.2023 - 13.01.2023” and Status “PUBLISHED”. \*
“workshop_example_extraction_GRA” by “User Admin/Support CLC+ Core” for
“Denmark/Danmark” with date range “01.01.2018 - 31.12.2018” and Status
“EXTRACTED_PREVIEW”. \* “workshop_example_extraction_urban” by “User
Admin/Support CLC+ Core” for “Denmark/Danmark” with date range
“01.01.2018 - 31.12.2018” and Status “EXTRACTED_PREVIEW”.

The modal dialog titled “Add Extraction” is overlaid on the Data
Catalogue. It contains three input fields: 1. “Name *” (required):
pre-filled with ”CLC+ Instance_LULUCF_2021_DE”. 2. ”Country* ”
(required): pre-filled with “DE Germany/Deutschland”. 3. “Region”
(optional): an empty text field. Buttons at the bottom of the dialog are
“CANCEL” and “ADD”.

<span id="_Ref153652678" class="anchor"></span>**Figure 4‑36: Reuse
Extraction – detailed view.**

## Delete Extraction

Further, you can **delete** an Extraction. By right clicking on the
Extraction in the Data Catalogue, a small window with several options
opens (see [Figure 4‑35](#_Ref153652480)). By clicking on “**Delete**”,
a pop-up window prevents you from accidentally deleting a dataset (see
[Figure 4‑37](#_Ref153956701)). By clicking Delete in the window, the
dataset will be ultimately removed from the data catalogue. This is only
true, if the user does share the same organisation with the entry or is
a USER_ADMIN. Otherwise, the entry will either way is not visible to the
user.

<img
src="./clcplus-core_CLC+Core_User_Manual_Issue_4.0_v1-media/image169.png"
style="width:2.96528in;height:1.42465in"
data-fig-alt="Screenshot of a modal dialog box within the Copernicus Land Monitoring Service (CLMS) CLC+ Core user interface, prompting confirmation for deleting an &#39;Extraction&#39;. The dialog is titled &#39;Delete Extraction &#39;CLC+ Instance_LULUCF_2021_NL&#39;&#39;. The primary text asks: &#39;Are you sure you want to delete Extraction &#39;CLC+ Instance_LULUCF_2021_NL&#39;?&#39; A warning message states: &#39;Deleting this Extraction will also delete all uploaded files and configurations.&#39; The user is presented with two action buttons: &#39;CANCEL&#39; (light grey) and &#39;DELETE&#39; (green, indicating the affirmative action). The background of the screenshot shows a portion of a data table or list, with visible entries including a user &#39;Lindmayer Amelie&#39;, country &#39;Ireland/Éire&#39;, and a date range &#39;01.01.2017 - 31.12.2019&#39;." />

Screenshot of a modal dialog box within the Copernicus Land Monitoring
Service (CLMS) CLC+ Core user interface, prompting confirmation for
deleting an ‘Extraction’. The dialog is titled “Delete Extraction ‘CLC+
Instance_LULUCF_2021_NL’”. The primary text asks: “Are you sure you want
to delete Extraction ‘CLC+ Instance_LULUCF_2021_NL’?” A warning message
states: “Deleting this Extraction will also delete all uploaded files
and configurations.” The user is presented with two action buttons:
“CANCEL” (light grey) and “DELETE” (green, indicating the affirmative
action). The background of the screenshot shows a portion of a data
table or list, with visible entries including a user “Lindmayer Amelie”,
country “Ireland/Éire”, and a date range “01.01.2017 - 31.12.2019”.

<span id="_Ref153956701" class="anchor"></span>**Figure 4‑37: Delete
Extraction**

## Recommendations and lessons learned

Since the creation of the rulesets is a very complex task that must be
carried out with great attention and precision, it is advisable to add
each rule individually, then execute it and examine the result in a GIS
program. Especially when creating the Extraction rules (wrong barcode
value or wrong logical operator) an error can occur very quickly and
debugging in the CLC+ Core System is sometimes difficult. Please
consider that that step will take quite some time. With the
implementation of the new map pop up described in section
[4.7](#preview-extraction-and-download-result) it becomes easier for the
user to debug and find out why a certain Output Class are extracted like
that a s all the background information why a Class Condition was
applied or not becomes visible in the map pop up.

Furthermore, it should be noted that due to some additional
rules/Aggregation rules (see Annex) implemented in the system, the
creation of Extraction rules and understanding their output is further
complicated.

# FAQ (Frequently Asked Questions)

In this section you can find the most frequently asked questions about
CLC+ Core. Of course, this section will be extended on demand.

**Where can I find more information about CLMS products?**

In general, you can find more about CLMS products on EEAs official
homepage <https://land.copernicus.eu/>.

**Where can I find more information About EAGLE?**

Within CLC+ Core we have directly linked the EAGLE homepage in our
Navigation Menu at “About EAGLE” (see also section 9 - About EAGLE
within this documentation). There you can find additional material About
EAGLE. There is also a FAQ section and the possibility to get in touch
with the EAGLE group.

**Where can I download the latest EAGLE barcoding template?**

You can download the matrix under menu item “EAGLE ontology” and then
click on “Download barcoding template”

**Can I find word definitions of CLC+ Core System?**

Yes, you can find them in the [Glossary](#glossary).

**Where do I get user credentials for using the system?**

If you do not have an EIONET account yet, please contact the [Eionet
Helpdesk](https://www.eionet.europa.eu/about/helpdesk?msclkid=265000d2aa8b11ec89be0ad26fcd73b0)
and create one.

**What to do if my Ingestion / Extraction fails?**

1.  If ingesting a vector file, please check if the correct attribute
    value is selected

2.  Check if the provided upload link is valid. It is valid if a file
    download is automatically started immediately after clicking on the
    link. If not, the download link might be expired (i.e. CLMS links
    expire after 24h)

3.  Retry or delete Ingestion

4.  Contact the [CLC+ Core support
    team](https://clcplus-core.land.copernicus.eu/) (us the help
    function ‘?’ on the webpage or
    <https://land.copernicus.eu/en/contact-service-helpdesk>)

**Is it possible to upload data from my local premises?**

Yes, you are able to upload your locally stored data but due to
performance issues, especially for large datasets, it is recommended to
upload the data using an URL.

**What if my dataset has more than \>100 classes – do I need to perform
the EAGLE barcoding for all classes?**

In general yes, you need to map all classes if you want to use them
within the system. But you could consider the possibility to
re-structure / aggregate your classes to a less detailed level before
uploading them to the system.

**Will my dataset automatically be reprojected, rasterized (for vector
datasets) and aggregated to 100 m or do I have to pre-process
anything?**

No, everything will be performed automatically.

**Can I always make changes to my ingested dataset?**

Most of the times - yes. However, if your dataset is published and used,
no more changes can be made while in use (by you or another user).

**How can I prevent my data from being seen by all users?**

Depending on what kind of visibility (private or public) you have
chosen, the ingested data will then be available to either all users
(public), to the country of the selected organisation (national), or
only to users within your organisation (private). So, to prevent your
data to be seen by others choose the private option.

**I uploaded an ArcGIS Layer (.lyr) file for the symbology of my vector
dataset but it is not working?**

The CLC+ Core system only recognizes and supports the following
legend/symbology files: QGIS layer style file (.qml) or SLD (Styled
Layer Descriptor) file (.sld). Text files and ArcGIS Layer Files (.lyr)
are not supported.

**Which raster and vector file formats are supported by CLC+ Core to
ingest data?**

- shapefile (shp as zip)

- geopackage (gpkg)

- file geodatabases (gdb)

- Hierarchical Data Format (HDF5)

- Geotiff (tif/tiff)

**What if there is a new version of the EAGLE barcoding file, is it
necessary to update all my datasets? And what if an Extraction was
already used?**

If the new version of the EAGLE barcoding file only contains new EAGLE
elements or has some updates on existing ones, no Extractions need to be
update (unless you want to also add the newly created EAGLE elements in
you EAGLE mapping).

If EAGLE elements do no longer exist in the newer version of the EAGLE
barcoding file, please check all your Ingestions and Extractions which
are not published yet. For these Ingestions and Extractions please
update the EAGLE barcoding.

For all published Ingestions and Extractions, the EAGLE barcoding cannot
be changed anymore.

**I have trouble with the EAGLE mapping of my dataset, where can I get
support?**

Relevant contact details are provided in the portal.

# Admin User only - see separate Annex

# Glossary

**Ingestion**  
An Ingestion is the original input dataset uploaded to the CLC+ Core
system. Each uploaded dataset gets resampled / aggregated to 100 x 100 m
spatial resolution. Each Ingestion consists of one or more classes.
These classes, so called **Input Classes** in CLC+ Core, can then be
used as input for **Extractions**. CLC+ Core supports the following
raster and vector file formats to ingest data: shapefile (shp as zip),
geopackage (gpkg), file geodatabases (gdb), Hierarchical Data Format
(HDF5) or Geotiff (tif/tiff).

**Extraction**  
An Extraction will create new and independent data products (100x100m
raster) by combining data from several **Extraction Input Classes.**
Every pixel of the raster is classified as one **Extraction Output
Class**, based on its **Class Condition**, or remains unclassified, if
none of the conditions apply.

**Extraction Input Class**  
Extraction Input classes are **Input classes** of **Ingestions** used in
an **Extraction**. They are selected by the user from all published
**Ingestions** in the CLC+ Core system. They need to be selected for
each Extraction because they define the input data which is needed to
evaluate the **Class Condition** of each **Extraction Output Class**.

**Coverage**  
The percentage of the area of a given pixel that an **Input Class**
covers is called the coverage. Pixel values are not binary because the
raw input data is reprojected to the EPSG:3035 coordinate reference
system and resampled to a 100m x 100m pixel size if they are not given
in this format already. Therefore, it can happen that multiple **Input
Classes** from the same **Ingestion** apply to the same raster pixel,
but don’t cover the full extent of the pixel.

A coverage can also be *No-Data* if the whole area of the pixel is
unclassified in the **Ingestion**.

**Extraction Output Class**  
Represents one classification option of an **Extraction**. It has a
name, an identifying class code and a C**lass Condition** that specifies
when the output class should be applied.

**Class Condition**  
Specifies whether the **Extraction Output Class** to which it
belongs should be applied to a given pixel, given the **coverage**
values of **Extraction Input Classes**. Technically speaking, a class
condition is a **Ruleset** (consisting of nested **Rules** and
**Rulesets).**

**Ruleset**   
A combination of **Rules** *or* **Rulesets** using Boolean
operators[^10]. Depending on the type of linking operator, the compound
expression is only true if both linked expressions are true
(AND-linkage) or if at least one of the linked expressions is true
(OR-linkage). Consequently, the result of a ruleset is also always
*true* or *false.* For example:

> *The coverage of LCC-Water/5 or LCC-Trees/5 must be greater than
> 50%.   
> **cov(“LCC-Water”, 5) \> 50*** ***   OR*** ***  cov(“LCC-Trees”, 5) \>
> 50** *

The top-level ruleset of an output class is called the **Class
Condition.** 

**Rule**  
A simple comparison of a **Coverage Function** (i.e. the coverage of a
barcoded EAGLE element) against another coverage value. For example: 

> *The coverage of LCC-Water with barcode 5 must be greater than 50%.   
> **cov(“LCC-Water”, 5) \> 50** *

When evaluating a **rule** on a given pixel, the result is always either
*true* or *false.* Comparing a *No-Data* value against any other value
produces the result *false.*

**Coverage Function**  
A function that computes the **Coverage** of a barcoded EAGLE element
for the selected **Extraction Input Classes** for a given pixel. This
computation works by:

1.  Selecting the **Extraction Input Classes** that were explicitly
    mapped with the given EAGLE element and barcode during the Ingestion
    process or that are mapped with a direct child in the EAGLE ontology
    (aggregation rule 5),

2.  Further restricting this selection based on the type of Coverage
    Function (aggregation rule 3)

3.  Calculating the **Coverage** sum of all selected **Extraction Input
    Classes** (aggregation rule 2).

# List of abbreviations

| Abbreviation | Name | Reference |
|----|----|----|
| **ADs** | Applicable Documents |  |
| **AI** | Action Item |  |
| **API** | Application Programming Interface |  |
| **CLC** | CORINE Land Cover | <https://land.copernicus.eu/en/products/corine-land-cover> |
| **CLC+** | CORINE Land Cover + | <https://land.copernicus.eu/en/products/clc-a-new-generation-land-information-system-for-europe> |
| **CLMS** | Copernicus Land Monitoring Service | <https://land.copernicus.eu/en> |
| **COG** | Cloud-optimized GIF |  |
| **CORINE** | Coordination of information on the environment |  |
| **CZ** | Coastal Zones |  |
| **DB** | Database |  |
| **DIAS** | Copernicus Data and Information Access Services |  |
| **EAGLE** | Eionet Action Group on Land monitoring in Europe | <https://land.copernicus.eu/en/eagle> |
| **EC** | European Commission | <https://commission.europa.eu/> |
| **EEA** | European Environment Agency | <https://www.eea.europa.eu> |
| **EEA39** | The 33 member and 6 cooperating countries of the EEA |  |
| **EEA38+UK** | The 32 member and 6 cooperating countries of the EEA + United Kingdom |  |
| **EO** | Earth Observation |  |
| **ESA** | European Space Agency | <https://www.esa.int> |
| **ETC** | European Topic Centre | <https://www.eionet.europa.eu/etcs> |
| **EU** | European Union |  |
| **EU27** | The 27 Member States of the European Union |  |
| **FM** | Final Meeting |  |
| **FWC** | Framework Contract |  |
| **GDAL** | Geospatial Data Abstraction Library |  |
| **GDB** | Geodatabase |  |
| **GIO** | GMES Initial Operations |  |
| **GPKG** | GeoPackage |  |
| **HDF5** | Hierarchical Data Format |  |
| **HRL / HRLs** | High Resolution Layer / High Resolution Layers |  |
| **IaaS** | Infrastructure-as-a-Service |  |
| **ID** | Identification Number |  |
| **INSPIRE** | Infrastructure for Spatial Information in Europe | <https://knowledge-base.inspire.ec.europa.eu/index_en> |
| **ISO** | International Organisation for Standardization |  |
| **ITT** | Invitation to Tender |  |
| **JDBC** | Java Database Connectivity |  |
| **JWT** | JSON Web Token |  |
| **KOM** | Kick-Off Meeting |  |
| **LC** | Land Cover |  |
| **LCC** | Land Cover Component |  |
| **LCH** | Land Characteristics |  |
| **LC/LU** | Land Cover / Land Use |  |
| **LCC** | Land Cover Component |  |
| **LU** | Land Use |  |
| **LUA** | Land Use Attribute |  |
| **LULUCF** | Land Use, Land Use Change and Forestry |  |
| **LYR** | ArcGIS Layer File |  |
| **MMU** | Minimum Mapping Unit |  |
| **MS** | Member States |  |
| **NFRs** | Non-Functional-Requirements |  |
| **NRC** | National Reference Centre |  |
| **NUTS** | Nomenclature of Territorial Units for Statistics |  |
| **N2K** | Natura 2000 |  |
| **OBDC** | Open Database Connectivity |  |
| **PDF** | Portable Document Format |  |
| **PM** | Progress Meeting |  |
| **PMP** | Project Management Plan |  |
| **PoC** | Proof of Concept |  |
| **QA** | Quality Assurance |  |
| **QC** | Quality Control |  |
| **QM** | Quality Management |  |
| **QML** | QGIS Style file |  |
| **REST** | Representational State Transfer |  |
| **RZ** | Riparian Zones |  |
| **SC** | Specific Contract |  |
| **SHP** | ESRI Shapefile |  |
| **SLD** | Styled Layer Descriptor |  |
| **SQL** | Structured Query Language |  |
| **UA** | Urban Atlas |  |
| **UI** | User Interface |  |
| **URI** | Uniform Resource Identifier |  |
| **URL** | Uniform Resource Locator |  |
| **UUID** | Universally Unique Identifier |  |
| **VM** | Virtual Machine |  |
| **WBS** | Work Breakdown Structure |  |
| **WEkEO** | Copernicus DIAS reference service for environmental data, virtual environments for data processing | <https://www.wekeo.eu/> |
| **WP** | Work Package |  |
| **ZIP** | ZIP Format |  |

# Annex

**Barcoding**

The ‘barcoding’ method is referring to the process of selecting and
assigning a value to relevant LCC, LUA and LCH elements from the matrix
to describe a class. The aim of bar-coding is to create a standardized
and concise representation of the class using a sequence of numerical
codes.

The EAGLE matrix elements initially have no specific bar code value
(BCV) and are considered neutral. During the bar-coding exercise for a
targeted class or landscape situation, these elements get assigned a
certain BCV (Table 1) according to their importance and logic
relationship within a given class definition. The resulting sequence of
numerical codes assigned to the matrix elements serves as a descriptive
summary of the class.

This bar-coding approach streamlines the process of representing complex
information about different classes, making it easier to handle and to
compare among them and with other classification systems. When working
with the barcoding exercise, different classes require the EAGLE
elements to take different roles, according to the targeted definitions.
Similar class definitions should reflect in also similar barcoding
results.[^11].

| **Barcode Value** | **Definition** |
|----|----|
| X | Element is excluded by definition |
| 1 | An optional element, it can occur as typical but not necessarily as mandatory |
| 2 | Selective mandatory element, EITHER-AND/OR logic, at least two or more of all elements with assigned BCV 2 must be present |
| 3 | Cumulative mandatory element, AND-logic, all elements with assigned BCV 3 must be present |
| 4 | Paired mandatory element, two of all elements with assigned BCV 4 must be present |
| 5 | Exclusive mandatory element, NOTHING-BUT-logic, practically allows only the one element with assigned BCV 5 and excludes any other element from its parent matrix block |

<span id="_Ref152071020" class="anchor"></span>Table 0‑1: List of
Bar-code value meanings. The BCVs define the role of EAGLE elements to
fulfil a given mapping rule, class definition or landscape situation.

**Aggregation Rules**

In the **current version of the CLC+ Core system**, for the creation of
an Extraction, the **following rules** were applied:

1.  Apply the coverage of the Input Class multiplied by the specified
    factor to the specified barcoded EAGLE element.

2.  If there is more than one coverage information for a certain
    barcoded EAGLE element originating from different Input Classes of
    the same Ingestion the coverage values are added up.

3.  If there is more than one coverage information for a certain EAGLE
    element originating from different data sets, the result depends on
    the choice of Coverage Function:

    1.  For *maxCov* the highest coverage sum of matching Input Classes
        within any Ingestion in the list of inputs is chosen.

    2.  For *firstCov* the first matching Input Class in the list of
        inputs has priority - so the order of the Input Classes is
        relevant here. More important classes should be ranked first.

    3.  For *sumCov* the coverages of all matching Input Classes are
        summed up, even if they belong to different Ingestions.

4.  Coverage values do NOT propagate to child elements of the EAGLE
    hierarchy. If an Input Class maps to EAGLE “buildings” the system
    does not give any information about “Specific buildings”.

5.  Coverage values are propagated to its parent elements by default.

6.  If several values must be combined (several contributions are coming
    from children) they are NOT added up if they originate from the same
    Input Class.

  

<table style="width:98%;">
<caption><span id="_Ref151628372" class="anchor"></span>Table 0‑2:
Datasets used for Ingestion into the CLC+ Core System by the CLC+ Core
Consortium.</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 31%" />
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Product Category</strong></th>
<th style="text-align: left;"><strong>Product Name (long)</strong></th>
<th style="text-align: left;"><strong>Product Name (short)</strong></th>
<th style="text-align: left;"><strong>Reference year</strong></th>
<th style="text-align: left;"><strong>Data format</strong></th>
<th style="text-align: left;"><strong>comments</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: left;">HRLs</td>
</tr>
<tr>
<td style="text-align: left;">Imperviousness</td>
<td style="text-align: left;">Built up</td>
<td style="text-align: left;">IBU_010m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Imperviousness</td>
<td style="text-align: left;">Degree of Imperviousness</td>
<td style="text-align: left;">IMD_010m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Forest</td>
<td style="text-align: left;">Tree Cover Density</td>
<td style="text-align: left;">TCD_010m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Forest</td>
<td style="text-align: left;">Forest Type</td>
<td style="text-align: left;">FTY_010m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Forest</td>
<td style="text-align: left;">Dominant Leaf Type</td>
<td style="text-align: left;">DLT_010m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Grassland</td>
<td style="text-align: left;">Grassland</td>
<td style="text-align: left;">GRA_010m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Water and Wetness</td>
<td style="text-align: left;">Water and Wetness</td>
<td style="text-align: left;">WAW_010m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Small Woody Feature</td>
<td style="text-align: left;">Small Woody Feature</td>
<td style="text-align: left;">SWF_005m_15</td>
<td style="text-align: left;">HRL 2015</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Small Woody Feature</td>
<td style="text-align: left;">Small Woody Feature</td>
<td style="text-align: left;">SWF_005m_18</td>
<td style="text-align: left;">HRL 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">CLC / CLC+ Backbone</td>
</tr>
<tr>
<td style="text-align: left;">CLC raster</td>
<td style="text-align: left;">Corine Land Cover</td>
<td style="text-align: left;">CLC_100m_18</td>
<td style="text-align: left;">CLC 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">CLC+ Backbone</td>
<td style="text-align: left;">Corine Land Cover Plus Backbone</td>
<td style="text-align: left;">CLC+BB_010m_18</td>
<td style="text-align: left;">CLC+ BB 2018</td>
<td style="text-align: left;">Raster</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">Priority Area Monitoring</td>
</tr>
<tr>
<td style="text-align: left;">Urban Atlas</td>
<td style="text-align: left;">Urban Atlas LC/LU</td>
<td style="text-align: left;">UA LC/LU 18</td>
<td style="text-align: left;">Hotspot 2018</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Urban Atlas</td>
<td style="text-align: left;">Urban Atlas LC/LU</td>
<td style="text-align: left;">UA LC/LU 12</td>
<td style="text-align: left;">Hotspot 2012</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Riparian Zones</td>
<td style="text-align: left;">Riparian Zones LC/LU</td>
<td style="text-align: left;">RZ LC/LU 18</td>
<td style="text-align: left;">Hotspot 2018</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Riparian Zones</td>
<td style="text-align: left;">Riparian Zones LC/LU</td>
<td style="text-align: left;">RZ LC/LU 12</td>
<td style="text-align: left;">Hotspot 2012</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Natura 2000</td>
<td style="text-align: left;">Natura 2000 LC/LU</td>
<td style="text-align: left;">N2K LC/LU 18</td>
<td style="text-align: left;">Hotspot 2018</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Natura 2000</td>
<td style="text-align: left;">Natura 2000 LC/LU</td>
<td style="text-align: left;">N2K LC/LU 12</td>
<td style="text-align: left;">Hotspot 2012</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Coastal Zones</td>
<td style="text-align: left;">Coastal Zones LC/LU</td>
<td style="text-align: left;">CZ LC/LU 18</td>
<td style="text-align: left;">Hotspot 2018</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">Coastal Zones</td>
<td style="text-align: left;">Coastal Zones LC/LU</td>
<td style="text-align: left;">CZ LC/LU 12</td>
<td style="text-align: left;">Hotspot 2012</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;">National Datasets</td>
</tr>
<tr>
<td style="text-align: left;">National dataset NL</td>
<td style="text-align: left;">Bestand Bodemgebruik</td>
<td style="text-align: left;">BBG 15</td>
<td style="text-align: left;">2015</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;">Aggregated to less classes by
consortium</td>
</tr>
<tr>
<td style="text-align: left;">National dataset NL</td>
<td style="text-align: left;">BRP Agricultural Parcels
(Gewasparcelen)</td>
<td style="text-align: left;">BRP 18</td>
<td style="text-align: left;">2018</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;">Aggregated to less classes by
consortium</td>
</tr>
<tr>
<td style="text-align: left;">National dataset ES</td>
<td style="text-align: left;">National Land Cover and Land Use System
(SIOSE) - Land Cover</td>
<td style="text-align: left;">SIOSE - Land Cover</td>
<td style="text-align: left;">2017</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">National dataset ES</td>
<td style="text-align: left;">National Land Cover and Land Use System
(SIOSE) - Land Use</td>
<td style="text-align: left;">SIOSE - Land Use</td>
<td style="text-align: left;">2017</td>
<td style="text-align: left;">Vector</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

Source: <https://land.copernicus.eu/> and national authorities

<table style="width:98%;">
<caption><span id="_Ref149045139" class="anchor"></span>Table 0‑3:
Excerpt of the LC/LU classes (here Grassland) with sub stratification
and corresponding EAGLE elements relevant for Extraction. Proposal EAGLE
Group [AD11] supplemented by consortium. The procedure must be done for
all the remaining classes as well.</caption>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 2%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Level 1</th>
<th style="text-align: center;">Level 2</th>
<th style="text-align: center;">Level 3</th>
<th style="text-align: left;">dataset</th>
<th style="text-align: left;"><strong>LCC</strong></th>
<th style="text-align: left;"><strong>LUA</strong></th>
<th style="text-align: left;"><strong>LCH</strong></th>
<th style="text-align: left;"><strong>code CLMS</strong></th>
<th style="text-align: left;"><strong>code ES</strong></th>
<th style="text-align: left;"><strong>code NL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="21"
style="text-align: center;"><strong>Grassland</strong></td>
<td rowspan="14" style="text-align: center;">Agriculture Use</td>
<td rowspan="7" style="text-align: center;">Pasture Use</td>
<td style="text-align: left;">CLC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1_1_1 commercial crop production</td>
<td style="text-align: left;">5_1_2_2 no crop rotation<br />
5_1_6_2 Pasture-meadow</td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=50&amp;&amp;</em></p>
<p><em>cov("LCC-herbaceous-vegetation", 5)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-commercial-crop-production", 5)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LCH-no-crop-rotation", 5)&gt;=30||</em></p>
<p><em>cov("LCH-pasture-meadow", 5)&gt;=30</em></p>
<p><em>)</em></p></td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=30||</em></p>
<p><em>cov("LCC-graminoids", 3)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-other-primary-production", 3)&gt;=30</em></p>
<p><em>)</em></p></td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=30&amp;&amp;</em></p>
<p><em>cov("LCC-herbaceous-vegetation", 2)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-commercial-crop-production", 5)&gt;=30</em></p>
<p><em>)</em></p></td>
</tr>
<tr>
<td style="text-align: left;">SIOSE LU</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">1_5 other primary production</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">SIOSE LC</td>
<td style="text-align: left;">2_2_1 graminiods</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BRP</td>
<td style="text-align: left;">2_2_1 graminiods</td>
<td style="text-align: left;">1_1_1 commercial crop production</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BBG</td>
<td style="text-align: left;">2_2 herbaceous_vegetation</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">CLC+</td>
<td style="text-align: left;">2_2 herbaceous_vegetation</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">GRA</td>
<td style="text-align: left;">2_2_1 graminiods</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="7" style="text-align: center;">Managed Grassland</td>
<td style="text-align: left;">CLC</td>
<td style="text-align: left;">2_2_1_1 grasses</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">5_1_2_2 no crop rotation<br />
5_1_1_2 managed grassland</td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=50&amp;&amp;</em></p>
<p><em>cov("LCC-herbaceous-vegetation", 5)&gt;=50</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-commercial-crop-production", 5)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LCH-no-crop-rotation", 5)&gt;=30&amp;&amp;</em></p>
<p><em>cov("LCH-pasture-meadow", 5)&gt;=30&amp;&amp;</em></p>
<p><em>cov("LCH-managed-permanent-grassland", 5)&gt;=30</em></p>
<p><em>)</em></p></td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=30||</em></p>
<p><em>cov("LCC-graminoids", 3)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-commercial-crop-production", 5)&gt;=30</em></p>
<p><em>)</em></p></td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=30&amp;&amp;</em></p>
<p><em>cov("LCC-herbaceous-vegetation", 2)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-commercial-crop-production", 5)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LCH-managed-permanent-grassland", 5)&gt;=30</em></p>
<p><em>)</em></p></td>
</tr>
<tr>
<td style="text-align: left;">SIOSE LU</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"> 1_1_1 commercial crop production</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">SIOSE LC</td>
<td style="text-align: left;"> 2_2_1 graminiods, 2_2
herbaceous_vegetation</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BRP</td>
<td style="text-align: left;">2_2_1 graminiods</td>
<td style="text-align: left;">1_1_1 commercial crop production</td>
<td style="text-align: left;">5_1_1_2 managed permanent grassland</td>
</tr>
<tr>
<td style="text-align: left;">BBG</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">CLC+</td>
<td style="text-align: left;">2_2 herbaceous_vegetation</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">GRA</td>
<td style="text-align: left;">2_2_1 graminiods</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td rowspan="7" style="text-align: center;">Non Agriculture Use</td>
<td rowspan="7" style="text-align: center;">Natural/Semi-natural
grassland</td>
<td style="text-align: left;">CLC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">6_3_1 Land areas not in other economic
use</td>
<td style="text-align: left;">5_1_4_1_1 no ploughing<br />
5_1_4_5_1 no irrigation<br />
5_1_4_2_1 no fertilizing<br />
5_1_4_3_1 no weed control<br />
5_1_4_4_1 no pest control<br />
5_1_4_7_1 no drainage</td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=50&amp;&amp;</em></p>
<p><em>cov("LCC-herbaceous-vegetation", 5)&gt;=50</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-land-areas-not-in-other-economic-use",
2)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LCH-no-ploughing", 5)&gt;=30||</em></p>
<p><em>cov("LCH-no-irrigation", 5)&gt;=30||</em></p>
<p><em>cov("LCH-no-fertilizing", 5)&gt;=30||</em></p>
<p><em>cov("LCH-no-weed-control", 5)&gt;=30||</em></p>
<p><em>cov("LCH-no-pest-control", 5)&gt;=30||</em></p>
<p><em>cov("LCH-no-drainage", 5)&gt;=30</em></p>
<p><em>)</em></p></td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=50||</em></p>
<p><em>cov("LCC-grasses_sedges_rushes_cereals ", 3)&gt;=50</em></p>
<p><em>)</em></p></td>
<td rowspan="7" style="text-align: left;"><p><em>(</em></p>
<p><em>cov("LCC-graminoids", 5)&gt;=30</em></p>
<p><em>)&amp;&amp;</em></p>
<p><em>(</em></p>
<p><em>cov("LUA-land-areas-not-in-other-economic-use",
5)&gt;=30</em></p>
<p><em>)</em></p></td>
</tr>
<tr>
<td style="text-align: left;">SIOSE LU</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">SIOSE LC</td>
<td style="text-align: left;"> 2_2_1_1 Grasses, Sedges, Rushes,
Cereals</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BRP</td>
<td style="text-align: left;">2_2_1 graminiods</td>
<td style="text-align: left;"> 6_3_1 Land areas not in other economic
use</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">BBG</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">CLC+</td>
<td style="text-align: left;">2_2 herbaceous_vegetation</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">GRA</td>
<td style="text-align: left;">2_2_1 graminiods</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

| 2056 | 5015  |
|------|-------|
| 2059 | 5016  |
| 2100 | 5325  |
| 2154 | 5514  |
| 2157 | 5514  |
| 2169 | 6204  |
| 2180 | 23033 |
| 2462 | 23700 |
| 3006 | 25830 |
| 3059 | 25832 |
| 3067 | 25833 |
| 3301 | 25834 |
| 3346 | 25834 |
| 3763 | 28992 |
| 3765 | 31287 |
| 3812 | 32628 |
| 3844 | 32632 |
| 3909 | 32632 |
| 3912 | 32635 |
| 5014 | 32636 |

<span id="_Ref151967307" class="anchor"></span>Table 0‑4: supported
national EPSG codes in the CLC+ Core system

<span id="_Ref105175205" class="anchor"></span>

<table style="width:99%;">
<caption><span id="_Toc154038182" class="anchor"></span>Table 0‑5:
Excerpt of the LC/LU classes (here Forest) with sub stratification and
applied rulesets done by the CLC+ Instances consortium.</caption>
<colgroup>
<col style="width: 0%" />
<col style="width: 2%" />
<col style="width: 50%" />
<col style="width: 3%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 1%" />
<col style="width: 0%" />
<col style="width: 20%" />
<col style="width: 4%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;">Output Classes</th>
<th colspan="6" style="text-align: left;">Input Classes</th>
<th colspan="2" style="text-align: left;">CLC+ Core Ruleset</th>
</tr>
<tr>
<th style="text-align: center;">Class code</th>
<th style="text-align: center;">Output classes</th>
<th style="text-align: center;">Output Class description</th>
<th style="text-align: left;">Input classes</th>
<th style="text-align: center;">Reference year</th>
<th style="text-align: center;">Temp resolution</th>
<th style="text-align: center;">Spatial resolution</th>
<th style="text-align: center;">MMU</th>
<th style="text-align: left;">Class description</th>
<th style="text-align: left;">CLC+ Core Ruleset</th>
<th style="text-align: left;">CLC+ Core Ruleset Intention</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: center;"><strong>21</strong></td>
<td rowspan="2" style="text-align: center;"><strong>FL Burnt
areas</strong></td>
<td rowspan="2" style="text-align: center;">The Burnt Area products map
burn scars, surfaces which have been sufficiently affected by fire to
display significant changes in the vegetation cover (destruction of dry
material, reduction or loss of green material) and in the ground surface
(temporarily darker because of ash, destroyed buildings). In this case
it maps burnt forest areas and woody plants such as coniferous and
broad-leaved trees; etc</td>
<td style="text-align: left;">EFFIS for year 2018</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">n/a</td>
<td style="text-align: left;"><a
href="https://effis-gwis-cms.s3-eu-west-1.amazonaws.com/effis/reports-and-publications/effis-related-publications/eudb_tech_spec_final_2register.pdf"><u>https://effis-gwis-cms.s3-eu-west-1.amazonaws.com/effis/reports-and-publications/effis-related-publications/eudb_tech_spec_final_2register.pdf</u></a></td>
<td rowspan="2" style="text-align: left;">cov("LCC-trees",
5)&gt;=30&amp;&amp;<br />
cov("LCH-forest-fire-wildfire", 5)&gt;=30</td>
<td rowspan="2" style="text-align: left;">Effis dataset (2018) is
combined with all forest classes that are mapped with the EAGLE element
"trees"==5 (HRL TCD, DLT, CLC+ BB) via an AND operator</td>
</tr>
<tr>
<td style="text-align: left;">All HRLs/CLC+BB forest classes mapped with
trees==5</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">2/3</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">0.01ha</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras"><u>https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras</u></a></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;"><strong>22</strong></td>
<td rowspan="2" style="text-align: center;"><strong>FL Transitional
woodland</strong></td>
<td rowspan="2" style="text-align: center;">Transitional bushy and
herbaceous vegetation with occasional scattered trees. Can represent
woodland degradation, forest regeneration / recolonization or natural
succession. Areas representing natural development of forest formations,
consisting of young plants of broad–leaved and coniferous species, with
herbaceous vegetation and dispersed solitary adult trees. Transitional
process can be for instance natural succession on abandoned agricultural
land, regeneration of forest after damages of various origin
(e.g. storm, avalanche), stages of forest degeneration caused by natural
or anthropogenic stress factors (e.g. drought, pollution), reforestation
after clearcutting, afforestation on formerly non-forested natural or
semi-natural areas etc.<br />
<strong>Includes:</strong><br />
- young broad-leaved and/or coniferous trees;<br />
- damaged or dead trees and shrubs;<br />
- fully grown trees, covering &lt; 30% of area;<br />
shrubs;<br />
- herbaceous vegetation (grasses and herbs);<br />
- bare soil or natural bare surfaces.</td>
<td style="text-align: left;">CLC 324 Transitional woodland/shrub</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">100</td>
<td style="text-align: center;">25ha</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/corine-land-cover-nomenclature-guidelines/html/index-clc-324.html"><u>https://land.copernicus.eu/user-corner/technical-library/corine-land-cover-nomenclature-guidelines/html/index-clc-324.html</u></a></td>
<td rowspan="2" style="text-align: left;">(<br />
cov("LCC-regular-bushes", 2)&gt;=30&amp;&amp;<br />
cov("LUA-forestry", 2)&gt;=30&amp;&amp;<br />
cov("LCH-abandoned", 2)&gt;=30&amp;&amp;<br />
cov("LCH-clear-cut", 2)&gt;=30&amp;&amp;<br />
cov("LCH-collapsed-destroyed-damaged", 2)&gt;=30&amp;&amp;<br />
cov("LCH-woodland-forest-and-other-wooded-land", 5)&gt;=30<br />
)&amp;&amp;<br />
cov("LCC-trees", 5)&gt;=30</td>
<td rowspan="2" style="text-align: left;">All forest classes that are
mapped with the EAGLE element "trees"==5 (HRL TCD, DLT, CLC+ BB) are
combined with CLC trans wood class via an AND operator</td>
</tr>
<tr>
<td style="text-align: left;">All HRLs/CLC+BB forest classes mapped with
trees==5</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">2/3</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">0.01ha</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras"><u>https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras</u></a></td>
</tr>
<tr>
<td rowspan="3" style="text-align: center;"><strong>23</strong></td>
<td rowspan="3" style="text-align: center;"><strong>FL
Deciduous</strong></td>
<td rowspan="3" style="text-align: center;">Perennial woody plants with
single, self-supporting main stem or trunk, containing woody tissue and
branching into smaller branches and shoots.<br />
<strong>Includes:</strong><br />
- referring to trees of the botanical group Angiospermae, with the
exception of ginkgo (Ginkgo biloba), which belongs to the Gymnospermae
taxonomically.<br />
- trees which are leafless for a certain period during the year<br />
<strong>Excludes:</strong><br />
- Pinus mugo and Alnus vidris<br />
- Ephedra<br />
- Shrub forms of Taxus, Juniperus and Betula<br />
- Musa</td>
<td style="text-align: left;">HRL Forest TCD</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">/</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/forest-2018-user-manual.pdf"><u>Forest
2018 user manual (copernicus.eu)</u></a></td>
<td rowspan="3" style="text-align: left;">(<br />
cov("LCC-trees", 5)&gt;=30&amp;&amp;<br />
cov("LCH-broad-leaved", 2)&gt;=30<br />
)&amp;&amp;<br />
(<br />
cov("LCC-trees", 5)&gt;=30&amp;&amp;<br />
cov("LCH-deciduous", 5)&gt;=30&amp;&amp;<br />
cov("LCH-broad-leaved", 5)&gt;=30<br />
)</td>
<td rowspan="3" style="text-align: left;">Combination of the
broadleaved/deciduous forest classes via an AND operator</td>
</tr>
<tr>
<td style="text-align: left;">HRL Forest DLT broadleaved</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">/</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/forest-2018-user-manual.pdf"><u>Forest
2018 user manual (copernicus.eu)</u></a></td>
</tr>
<tr>
<td style="text-align: left;">CLC+BB Broadl deciduous</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">0.01ha</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras"><u>https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras</u></a></td>
</tr>
<tr>
<td rowspan="4" style="text-align: center;"><strong>24</strong></td>
<td rowspan="4" style="text-align: center;"><strong>FL
Coniferous/Evergreen</strong></td>
<td rowspan="4" style="text-align: center;">Perennial woody plants with
single, self-supporting main stem or trunk, containing woody tissue and
branching into smaller branches and shoots.<br />
**Includes:** - Needle leaved trees: referring to trees of the botanical
group Gymnospermae (Ford-Robertson, 1971) carrying typical needle-shaped
leaves. An exception is Ginkgo biloba which belongs to the Gymnospermae
but is considered here as Broadleaved deciduous tree.<br />
- trees that are never entirely without green foliage (includes
palm-leaved species)</td>
<td style="text-align: left;">HRL Forest TCD</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">/</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/forest-2018-user-manual.pdf"><u>Forest
2018 user manual (copernicus.eu)</u></a></td>
<td rowspan="4" style="text-align: left;">(<br />
cov("LCC-trees", 5)&gt;=30&amp;&amp;<br />
(<br />
cov("LCH-needle-leaved", 5)&gt;=30||<br />
cov("LCH-evergreen", 5)&gt;=30<br />
)<br />
)</td>
<td rowspan="4" style="text-align: left;">Combination of theHRL TCD via
an AND operator,with the other needle/coniferous/evergreen classes.
These are connected via an OR operator as evergreen class is only common
in southern Europe.</td>
</tr>
<tr>
<td style="text-align: left;">HRL Forest DLT coniferous</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">/</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/forest-2018-user-manual.pdf"><u>Forest
2018 user manual (copernicus.eu)</u></a></td>
</tr>
<tr>
<td style="text-align: left;">CLC+BB needle leaved</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">0.01ha</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras"><u>https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras</u></a></td>
</tr>
<tr>
<td style="text-align: left;">CLC+BB Broadl evergreen</td>
<td style="text-align: center;">2018</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">0.01ha</td>
<td style="text-align: left;"><a
href="https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras"><u>https://land.copernicus.eu/user-corner/technical-library/clc-bb_user_manual_ras</u></a></td>
</tr>
</tbody>
</table>

[^1]: [clcplus-core.land.copernicus.eu](https://urldefense.com/v3/__https:/eur02.safelinks.protection.outlook.com/?url=https*3A*2F*2Furldefense.com*2Fv3*2F__https*3A*2Feur02.safelinks.protection.outlook.com*2F*3Furl*3Dhttps*3A*2F*2Furldefense.com*2Fv3*2F__https*3A*2F*2Feur02.safelinks.protection.outlook.com*2F*3Furl*3Dhttps*3A*2F*2Furldefense.com*2Fv3*2F__http*3A*2Fclcplus-core.land.copernicus.eu__*3B!!OepYZ6Q!vOjXaYPuONheDubX7TP8vlAB4HsNJN6FhNzsvqHkg48gGOpCiRnh1azddHGtV3Q8bU1s*24*26data*3D04*7C01*7CEugenija.Schuren*40eea.europa.eu*7C6f421a51adb245e0345308da11596ea5*7Cbe2e7beab4934de5bbc58b4a6a235600*7C1*7C0*7C637841373076254170*7CUnknown*7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0*3D*7C3000*26sdata*3Df*2By2Icsr881iMH4*2Fy4XqZL21MYo1U6rS*2FCjZy5q*2FpGQ*3D*26reserved*3D0__*3BJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSU!!OepYZ6Q!u-9fn2l19QpUDeQxuJjOpS3JsdMpopBHv_AL7TvwMKWhE5kg4Acj4zHlXO1YGA_Uya9h*24*26data*3D04*7C01*7CEugenija.Schuren*40eea.europa.eu*7C032e79d3f38e4414f98208da116dcd40*7Cbe2e7beab4934de5bbc58b4a6a235600*7C1*7C0*7C637841460556907216*7CUnknown*7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0*3D*7C3000*26sdata*3DvbJoKgAIl4Eavm8tJQxNqg03N4OUVcsiyGGM7EEFBeU*3D*26reserved*3D0__*3BJSUlJSUlJSUlJSUqKioqKioqKiolJSoqKioqKioqKioqKiUlKioqKiolJSUlJSUlJSUlJSUlJSUlJQ!!OepYZ6Q!q5qrniOv8p1iIfZjis3w329hIAadz9WRg40QUHKftwrQTJmA9rOYSiJwW14coqosJtkr*24&data=04*7C01*7CEugenija.Schuren*40eea.europa.eu*7Ced4a17eba3f84c759e1f08da1602dbae*7Cbe2e7beab4934de5bbc58b4a6a235600*7C1*7C0*7C637846498797154873*7CUnknown*7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0*3D*7C3000&sdata=OnVb26TUT97Ab*2BT4tcGZJLsOyrS1tZFQaunm67nD7D0*3D&reserved=0__;JSUlJSUlJSUlJSoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiUlKioqKioqKioqKioqJSUqJSUlJSUlJSUlJSUlJSUlJSUl!!OepYZ6Q!40atOGXaqdeEoJ_GcIGYMO63a2RM3Pvq1R4AZoytOQKlw-W_0eTXi0SexpK7ZkDuC3Tnf1gCekFB7R2NH6xjfl7QsBXT23nxVQFp$)

[^2]: <https://land.copernicus.eu/en/eagle?tab=main>

[^3]: <https://land.copernicus.eu/en/eagle?tab=document_archive>

[^4]: [https://land.copernicus.eu/en/technical-library/explanatory-documentation-of-the-eagle-concept-3_2/@@download/file](https://land.copernicus.eu/en/eagle?tab=introduction_and_context)
    (Version 3.2, 2023)

[^5]: <https://land.copernicus.eu/en/eagle?tab=document_archive>
    (Version 3.2, 2023)
    <https://land.copernicus.eu/eagle/files/documents-and-reports/eagle-matrix-t2-2_bar-coding-manual>

[^6]: https://land.copernicus.eu/eagle/files/explanatory-documentation/eagle-docu
    (Version 3.1.2, 2021)

[^7]: Rasterization to 10 m resolution for <u>vector</u> products first

[^8]: <https://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/discrete-and-continuous-data.htm>

[^9]: <https://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/discrete-and-continuous-data.htm>

[^10]: <https://de.wikipedia.org/wiki/Logischer_Operator>

[^11]: <https://land.copernicus.eu/en/eagle?tab=bar_coding>
