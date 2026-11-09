# Product Name – Algorithm Theoretical Basis Document (ATBD)

2026-11-05

- [<span class="toc-section-number">1</span> Executive summary
  <span class="yellow-box" custom-style="yellow-box-line">(mandatory
  chapter)</span>](#executive-summary-mandatory-chapter)
- [<span class="toc-section-number">2</span> Background of the document
  <span class="yellow-box" custom-style="yellow-box-line">(mandatory
  chapter)</span>](#background-of-the-document-mandatory-chapter)
  - [<span class="toc-section-number">2.1</span> Scope and objectives
    <span class="yellow-box" custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#scope-and-objectives-mandatory-subchapter)
  - [<span class="toc-section-number">2.2</span> Content and structure
    <span class="yellow-box" custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#content-and-structure-mandatory-subchapter)
- [<span class="toc-section-number">3</span> Methodology
  <span class="yellow-box" custom-style="yellow-box-line">(mandatory
  chapter)</span>](#methodology-mandatory-chapter)
  - [<span class="toc-section-number">3.1</span> Theoretical Background
    <span class="yellow-box" custom-style="yellow-box-line">(optional
    subchapter)</span>](#theoretical-background-optional-subchapter)
  - [<span class="toc-section-number">3.2</span> Methodology and
    workflow <span class="yellow-box"
    custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#methodology-and-workflow-mandatory-subchapter)
  - [<span class="toc-section-number">3.3</span> Source data
    <span class="yellow-box" custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#source-data-mandatory-subchapter)
  - [<span class="toc-section-number">3.4</span> Pre-processing
    <span class="yellow-box" custom-style="yellow-box-line">(optional
    subchapter)</span>](#pre-processing-optional-subchapter)
    - [<span class="toc-section-number">3.4.1</span> Pre-processing
      overview <span class="yellow-box"
      custom-style="yellow-box-line">(optional
      subchapter)</span>](#pre-processing-overview-optional-subchapter)
    - [<span class="toc-section-number">3.4.2</span> Input data for
      pre-processing <span class="yellow-box"
      custom-style="yellow-box-line">(optional
      subchapter)</span>](#input-data-for-pre-processing-optional-subchapter)
    - [<span class="toc-section-number">3.4.3</span> Pre-processing
      methodology <span class="yellow-box"
      custom-style="yellow-box-line">(optional
      subchapter)</span>](#pre-processing-methodology-optional-subchapter)
    - [<span class="toc-section-number">3.4.4</span> Intermediate
      outputs <span class="yellow-box"
      custom-style="yellow-box-line">(optional
      subchapter)</span>](#intermediate-outputs-optional-subchapter)
  - [<span class="toc-section-number">3.5</span> Processing
    <span class="yellow-box" custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#processing-mandatory-subchapter)
    - [<span class="toc-section-number">3.5.1</span> Processing overview
      <span class="yellow-box" custom-style="yellow-box-line">(optional
      subchapter)</span>](#processing-overview-optional-subchapter)
    - [<span class="toc-section-number">3.5.2</span> Input data for
      processing <span class="yellow-box"
      custom-style="yellow-box-line">(optional
      subchapter)</span>](#input-data-for-processing-optional-subchapter)
    - [<span class="toc-section-number">3.5.3</span> Processing
      methodology <span class="yellow-box"
      custom-style="yellow-box-line">(optional
      subchapter)</span>](#processing-methodology-optional-subchapter)
    - [<span class="toc-section-number">3.5.4</span> Algorithm
      descriptions <span class="yellow-box"
      custom-style="yellow-box-line">(optional
      subchapter)</span>](#algorithm-descriptions-optional-subchapter)
  - [<span class="toc-section-number">3.6</span> Post-processing
    <span class="yellow-box" custom-style="yellow-box-line">(optional
    subchapter)</span>](#post-processing-optional-subchapter)
  - [<span class="toc-section-number">3.7</span> Output products
    <span class="yellow-box" custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#output-products-mandatory-subchapter)
- [<span class="toc-section-number">4</span> Quality control and
  production verification <span class="yellow-box"
  custom-style="yellow-box-line">(mandatory
  subchapter)</span>](#quality-control-and-production-verification-mandatory-subchapter)
- [<span class="toc-section-number">5</span> Recognized technical issues
  <span class="yellow-box" custom-style="yellow-box-line">(mandatory
  chapter)</span>](#recognized-technical-issues-mandatory-chapter)
- [<span class="toc-section-number">6</span> Terms of use and product
  technical support <span class="yellow-box"
  custom-style="yellow-box-line">(mandatory
  chapter)</span>](#terms-of-use-and-product-technical-support-mandatory-chapter)
  - [<span class="toc-section-number">6.1</span> Terms of use
    <span class="yellow-box" custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#terms-of-use-mandatory-subchapter)
  - [<span class="toc-section-number">6.2</span> Citation
    <span class="yellow-box" custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#citation-mandatory-subchapter)
  - [<span class="toc-section-number">6.3</span> Product technical
    support <span class="yellow-box"
    custom-style="yellow-box-line">(mandatory
    subchapter)</span>](#product-technical-support-mandatory-subchapter)
- [<span class="toc-section-number">7</span> List of abbreviations &
  acronyms <span class="yellow-box"
  custom-style="yellow-box-line">(mandatory
  chapter)</span>](#list-of-abbreviations--acronyms-mandatory-chapter)
- [<span class="toc-section-number">8</span> References
  <span class="yellow-box" custom-style="yellow-box-line">(mandatory
  chapter)</span>](#references-mandatory-chapter)
- [<span class="toc-section-number">9</span> Annexes
  <span class="yellow-box" custom-style="yellow-box-line">(optional
  chapter)</span>](#annexes-optional-chapter)

# IMPORTANT: Please read this section then delete before submitting your report

## How to use the CLMS Algorithm Theoretical Basis Document template

This is the Algorithm Theoretical Basis Document (ATBD) template. You
should use it to write the ATBD reports for the Copernicus Land
Monitoring Service. The template provides the structure and guidelines
as you develop your report.

For more information about the design and style, please refer to the
“CLMS Word template CLMS_February” and the CLMS Brand Guidelines or
contact the communications team at the EEA.

The ATBD template is organised into a set of chapters and subchapters
that are mandatory or optional.

You may insert a new subchapter (not described in the current structure)
if you deem it necessary.

If any of the mandatory sections of the ATBD cannot be described or are
not applicable, please include a statement in the corresponding section
explaining the reason.

The ATBD template contains the following information:

- The structure of chapters and subchapters that must be used when
  editing the report.

- Instructions (e.g. an overview of the content that should be followed
  when editing the section). This information is presented in
  <span class="yellow-box" custom-style="yellow-box-line">yellow
  boxes</span> and must be deleted and replaced with your content
  (e.g. text, tables, figures).

- Examples of standard text and tables for chapters or subchapters
  (these examples are presented in <span class="grey-box"
  custom-style="grey-box-line">grey boxes</span>) that can be adapted
  accordingly.

For visual insets such as charts, graphs, diagrams, tables, maps and
photos, follow these guidelines:

- Assign each inset a numbered caption with a clear and descriptive
  title (follow the design and style instructions given in the “CLMS
  Word template CLMS_February”).Use automatic numbering for insets, to
  ensure that insets are numbered sequentially in **bold** (e.g.,
  **Figure 1**, **Table 1**).

- In the body text, refer to the inset's caption number in **bold**,
  explaining the visual's content (e.g., “As shown in **Inset 1**, the
  data highlights the following trend…”). Always use Word’s
  cross-reference tool for referencing insets, ensuring that references
  update automatically if numbers change.

- Label all units clearly (e.g., x and y axes, legends, column headers,
  parts of graphs and diagrams).

- Include the source of the data or image if you did not create it
  yourself.

- Ensure that the data or image is not distorted in any way.

A guide on best practices and principles for data visualisation, is
available at the URL
"<https://data.europa.eu/apps/data-visualisation-guide/>".

# End of instructions. Delete up to here.



# Executive summary <span class="yellow-box" custom-style="yellow-box-line">(mandatory chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Presents an overview of the product, including purpose and main
features.

An executive summary should concisely communicate the key points of the
CLMS product to decision-makers and stakeholders. It should provide an
overview of the CLMS, highlight the products generated, and summarize
what the ATBD presents. To achieve this, consider the following
suggestions:

1.  **Know the audience**: Write with executives and stakeholders in
    mind. Focus on what they need to know to make informed decisions and
    avoid unnecessary details.

2.  **Highlight key points**: Clearly summarize the most important
    aspects of the product, including objectives, key findings, and
    recommendations, being direct and to the point.

3.  **Be clear and concise**: Use straightforward language, aiming for
    sentences to be no longer than 20–25 words whenever possible. This
    executive summary should not exceed two pages.

4.  **Prioritize Information**: Lead with the most critical information
    and ensure that the most important details are easily accessible.
    Use bullet points or subheadings to break down complex information.

5.  **Use active voice**: Make your writing more engaging by using
    active voice. Focus on actions and outcomes, emphasizing what has
    been done and what is recommended.

6.  **Minimize jargon**: Use technical terms only when necessary, and
    ensure they are clearly explained, and avoid industry-specific
    jargon that might be unfamiliar to a broader audience.

</div>



# Background of the document <span class="yellow-box" custom-style="yellow-box-line">(mandatory chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Details the scope, the intended audience, content, and structure of the
document.

</div>

## Scope and objectives <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Explains the primary purpose and coverage of the document.

</div>

<div class="grey-box" custom-style="grey-box">

Here an example:

This Algorithm Theoretical Basis Document summarizes the product
characteristics and describes production methodologies and workflows of
“PRODUCT SHORT NAME”.

</div>

## Content and structure <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Outlines the document's structure, including chapters on product
descriptions, quality, access, and references.

In detail, the document is structured as follows:

</div>

<div class="grey-box" custom-style="grey-box">

- Chapter 1 provides the executive summary of the project along with a
  general information about European Union's Earth Observation Programme
  and Copernicus Land Monitoring Service (CLMS).

- Chapter 2 outlines the scope, content and structure of this document.

- Chapter 3 details the general thematic content and product
  descriptions with the methodology, workflows and internal quality
  control processes.

- Chapter 4 discusses know issues of the current methodology and the
  product.

- Chapter 5 presents the terms of use, citation guidelines, and
  technical support for the product.

- Chapter 6 defines key terms used in the document.

- and the Abbreviations & Acronyms, References, Annex, and Appendices
  Chapters provide citations, supplementary information, and additional
  reference materials.

</div>



# Methodology <span class="yellow-box" custom-style="yellow-box-line">(mandatory chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Describes the workflow, input datasets, production methodology including
data pre-processing, processing, post-processing and quality control and
product verification.

In the “Methodology Description” chapter, some of the subchapters are
classified as mandatory, but only if they are relevant to the
methodology being described. Optional subchapters can be included or
omitted, allowing flexibility to adapt the structure to the specific
characteristics of the product.

If any of the following mandatory sections cannot be described or are
not applicable, please include a statement in the corresponding section
explaining the reason.

Provide an overview table of methodology. Follow the example below:

</div>

<div class="tbl-caption">

Table 3.1 Example of an overview table of methodology (insert your
caption here, delete feature and insert your feature)

</div>

| Category Title | Description/Details |
|----|----|
| Retrieval Methodology | Example: Convolutional Neural Network (CNN), Time Series Analysis, Change Detection, etc. |
| Input Data | Example: Sentinel-2 (S2A, S2B), Level-2ª (processing baseline 05.11), retrieved via ESA Copernicus Open Access Hub |
| Ancillary Data | Example: OSM: Open Street Map roads, parking lots, runways and building footprints, CLC: CORINE Land Cover 2018 (1.2.2 Road and rail networks and associated land) |
| Processing Workflow | Example: Cloud masking, atmospheric correction, radiometric calibration, temporal compositing |
| Spatial/Temporal Resolution | Example: 10m spatial resolution |
| Verification and Accuracy | Example: Product verification using ground-based reference, accuracy assessment with RMSE calculations. |



## Theoretical Background <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Provides an overview of concepts, common definitions and assumptions of
the product and links it to related previous studies and work to allow
an understanding of the product and applied methodology.

</div>

## Methodology and workflow <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Provides an overview of the product generation, highlighting the
workflow, the input datasets, key processes involved, and algorithms
used. Ideally, the description is complemented by a traceability diagram
that allows users to understand the uncertainty budget of the product as
a result of its inputs and workflow (if needed, add subchapter).

Below is a generic example that should be adapted to the specific needs
of the product to provide an overview of the production process
workflow.

</div>

<img src="templates_CLMS_ATBD_Template_v1-media/figure_1.png"
style="width:100.0%"
data-fig-alt="This diagram illustrates a generic production process workflow for Copernicus Land Monitoring Service (CLMS) products, detailing five sequential stages: Input data, Pre-processing, Processing, Post-processing, and Output products. 1. **Input data**: This stage involves sourcing data from Sentinel-x, Copernicus Land Monitoring Service (CLMS) specific datasets, Ancillary data, and other unspecified data sources. 2. **Pre-processing**: This stage includes multiple concurrent or sequential activities: &#39;Scene selection, check and correction&#39;, &#39;Extraction, quality control and calibration&#39;, and &#39;Classification and optimization&#39;. 3. **Processing**: This core stage encompasses &#39;Metrics generation, classification (e.g. threshold tunning, visual interpretation) data fusion processing&#39;. During this processing phase, &#39;Quality control and product verification&#39; is also conducted. 4. **Post-processing**: This stage focuses on refining the processed data through &#39;Filtering and harmonization, integration of ancillary data, classification improvements, product preparation&#39;. 5. **Output products**: The final outputs generated are a &#39;Status layer&#39;, a &#39;Change, auxiliary, reference layer&#39;, and &#39;Other datasets&#39;."
alt="Figure 1.1 Example of a generic workflow (insert your caption here, delete feature and insert your feature)" />

This diagram illustrates a generic production process workflow for
Copernicus Land Monitoring Service (CLMS) products, detailing five
sequential stages: Input data, Pre-processing, Processing,
Post-processing, and Output products.

1.  **Input data**: This stage involves sourcing data from Sentinel-x,
    Copernicus Land Monitoring Service (CLMS) specific datasets,
    Ancillary data, and other unspecified data sources.
2.  **Pre-processing**: This stage includes multiple concurrent or
    sequential activities: “Scene selection, check and correction”,
    “Extraction, quality control and calibration”, and “Classification
    and optimization”.
3.  **Processing**: This core stage encompasses “Metrics generation,
    classification (e.g. threshold tunning, visual interpretation) data
    fusion processing”. During this processing phase, “Quality control
    and product verification” is also conducted.
4.  **Post-processing**: This stage focuses on refining the processed
    data through “Filtering and harmonization, integration of ancillary
    data, classification improvements, product preparation”.
5.  **Output products**: The final outputs generated are a “Status
    layer”, a “Change, auxiliary, reference layer”, and “Other
    datasets”.



## Source data <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Explain which datasets (e.g., Sentinel-x, DEM, or other CLMS products)
serve as input for the product. Clarify internal dependencies within the
product, such as primary data used to generate secondary outputs.
Reference external thematic data where applicable and ensure the
workflow diagram illustrates the connections between different datasets.

</div>

## Pre-processing <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Details the initial steps taken to prepare the data for further
processing, including corrections and adjustments to raw data.
Sub-chapter structure optional.

</div>

### Pre-processing overview <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Introduces the pre-processing stage, outlining its purpose and
significance in the overall methodology.

</div>

### Input data for pre-processing <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Lists the various input datasets used in the pre-processing stage.

</div>

### Pre-processing methodology <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Describes the specific workflow and steps involved in pre-processing the
input data, including correction (e.g. atmospheric, topographic,
geometric corrections) and cleaning operations within the project
activities.

</div>

### Intermediate outputs <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Specifies the types of output data generated from the pre-processing
stage, which will be used in subsequent processing steps.

</div>

## Processing <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Details the core processing steps that transform pre-processed data into
the final products, and the configuration of the tools used for
corrections. Product derivation tasks, such as aggregation rules and
change layer calculation can be described in this section.

The subchapter structure is optional.

</div>

### Processing overview <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Summarizes the main goals and components of the processing stage.

</div>

### Input data for processing <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Identifies the input data required for the processing stage, including
pre-processed datasets and additional ancillary data.

</div>

### Processing methodology <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Outlines the workflow and methods used during the processing stage,
detailing each step.

</div>

### Algorithm descriptions <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Provides detailed descriptions of the algorithms used in the processing
stage.

</div>

## Post-processing <span class="yellow-box" custom-style="yellow-box-line">(optional subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Presents tasks typically involved in the refinement, quality assurance
and control, and finalization of the datasets such has manual steps,
filtering and smoothing, integration of ancillary data, reprojecting,
resampling or merging, classification improvements and preparing data
for end-users. A subchapter structure as suggested with previous
sections may be introduced if necessary.

</div>

## Output products <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Specifies the types of output products generated (e.g., status
layer/change/auxiliary layer, reference layer, near-real time).

</div>



# Quality control and production verification <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Discusses the methods and criteria used to assess the internal quality
assurance and control process as well as production verification, the
quality and accuracy of the products, ensuring they meet the required
standards and specifications.

</div>



# Recognized technical issues <span class="yellow-box" custom-style="yellow-box-line">(mandatory chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Discusses any challenges or limitations of the current methodology,
algorithm, input and reference data or technical aspects relevant to the
product that might influence its quality, validity or reliability. At
the same time, any foreseeable planned developments could be mentioned
here.

</div>



# Terms of use and product technical support <span class="yellow-box" custom-style="yellow-box-line">(mandatory chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Presents information on the terms of use, citation guidelines, and
technical support for the products.

</div>

## Terms of use <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Presents information on the legal use of data for added products or
derivative works.

Here an example of a standard text.

</div>

<div class="grey-box" custom-style="grey-box">

The Terms of Use for the product(s) described in this document,
acknowledge the following:  
Free, full and open access to the products and services of the
Copernicus Land Monitoring Service is made on the conditions that:

1.  When distributing or communicating Copernicus Land Monitoring
    Service products and services (data, software scripts, web services,
    user and methodological documentation and similar) to the public,
    users shall inform the public of the source of these products and
    services and shall acknowledge that the Copernicus Land Monitoring
    Service products and services were produced “with funding by the
    European Union”.

2.  Where the Copernicus Land Monitoring Service products and services
    have been adapted or modified by the user, the user shall clearly
    state this.

3.  Users shall make sure not to convey the impression to the public
    that the user's activities are officially endorsed by the European
    Union.

The user has all intellectual property rights to the products he/she has
created based on the Copernicus Land Monitoring Service products and
services.

[Consult Data policy — Copernicus Land Monitoring Service for further
details](https://land.copernicus.eu/en/data-policy)

</div>

## Citation <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Presents guidelines on how to properly cite and reference the products
and services of the CLMS.

Here are examples of standard text to be used according to the
situation:

</div>

<div class="grey-box" custom-style="grey-box">

When **planning to publish a publication (scientific, commercial,
etc.)**, it shall explicitly mention:

> “This publication has been prepared using European Union's Copernicus
> Land Monitoring Service information; \<insert all relevant DOI links
> here, if applicable\>”

When developing a **product or service using the products or services of
the Copernicus Land Monitoring Service**, it shall explicitly mention:

> “Generated using European Union's Copernicus Land Monitoring Service
> information; \<insert all relevant DOI links here, if applicable\>”

When **redistributing a part of the Copernicus Land Monitoring Service
(product, dataset, documentation, picture, web service, etc.)**, it
shall explicitly mention:

> “European Union's Copernicus Land Monitoring Service information;
> \<insert all relevant DOI links here, if applicable\>”

[Consult Data policy — Copernicus Land Monitoring Service for further
details](https://land.copernicus.eu/en/data-policy)

</div>

## Product technical support <span class="yellow-box" custom-style="yellow-box-line">(mandatory subchapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Presents information on the support available for users of the product,
including contact details.

Here an example of a standard text.

</div>

<div class="grey-box" custom-style="grey-box">

Product technical support is provided by the product custodian through
[Copernicus Land Monitoring Service – Service
desk](https://land.copernicus.eu/en/data-policy). Product technical
support does not include software specific user support or general GIS
or remote sensing support.  
More information on the products can be found on the Copernicus Land
Monitoring Service website (https://land.copernicus.eu/)

</div>



# List of abbreviations & acronyms <span class="yellow-box" custom-style="yellow-box-line">(mandatory chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Lists abbreviations and acronyms used throughout the document.

</div>

| Abbreviation | Name                                 | Reference         |
|--------------|--------------------------------------|-------------------|
| ATBD         | Algorithm Theoretical Basis Document |                   |
| DOI          | Digital Object Identifier            |                   |
| EEA          | European Environment Agency          | www.eea.europa.eu |
| PUM          | Product User Manual                  |                   |



# References <span class="yellow-box" custom-style="yellow-box-line">(mandatory chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Lists references cited throughout the document.

</div>



# Annexes <span class="yellow-box" custom-style="yellow-box-line">(optional chapter)</span>

<div class="yellow-box" custom-style="yellow-box">

Annexes should be kept to a minimum but can be placed as needed to
present technical details, data and information repository, resources on
product development.

</div>
