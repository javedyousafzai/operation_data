```mermaid
flowchart TB

    %% Core Concepts
    ODP[ODP Situation]
    Emergency[UNHCR.org Emergency]
    NextGen[NextGen Situation Definition]
    DataLayer[Common Data Layer]

    %% Relationships
    ODP -->|aligns with| Emergency
    Emergency -->|indicators for| NextGen
    NextGen -->|pulls data from| DataLayer

    %% Situation Types
    subgraph Situation_Types [Types of Situations]
        SC[Single-country crisis<br/>Sudan - Afghanistan - DRC]
        MM[Mixed movement / regional flows<br/>Horn of Africa to Europe]
    end

    ODP --> SC
    ODP --> MM

    %% Sudan Example
    subgraph Sudan_Example [Sudan Situation - Data Views]
        SudanSit[Sudan Situation]
        EgyptPage[Egypt Country Page<br/>822,337 refugees from Sudan]
        SudanPage[Sudan Situation Page - Egypt<br/>1.5M arrivals<br/>795,299 registered refugees]
    end

    SudanSit --> EgyptPage
    SudanSit --> SudanPage

    %% Parameters
    subgraph Parameters [Situation Definition Parameters]
        P1[Emergency declared on UNHCR.org]
        P2[L2 declaration date]
        P3[Emergency active period]
        P4[Countries impacted]
        P5[Situation matches emergency]
        P6[Population groups - Refugees IDPs Mixed]
        P7[RRP countries]
        P8[Advocacy and funding gaps]
    end

    NextGen --> P1
    NextGen --> P2
    NextGen --> P3
    NextGen --> P4
    NextGen --> P5
    NextGen --> P6
    NextGen --> P7
    NextGen --> P8

    %% Taxonomy and Aggregation
    subgraph Taxonomy [Situation Taxonomy and Aggregation]
        Cat[Situation categories]
        Agg[Aggregation rules for data and content]
        Ctry[Countries involved or affected]
    end

    NextGen --> Cat
    NextGen --> Agg
    NextGen --> Ctry
