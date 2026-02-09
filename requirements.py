import React, { useState } from 'react';
import { Download, FileSpreadsheet, ChevronDown, ChevronRight } from 'lucide-react';

const RequirementsExcel = () => {
  const [expandedSections, setExpandedSections] = useState({});

  const toggleSection = (id) => {
    setExpandedSections(prev => ({
      ...prev,
      [id]: !prev[id]
    }));
  };

  const requirements = [
    {
      id: 'REQ-001',
      module: 'Common Document Repository',
      priority: 'High',
      feature: 'Unified Document Storage',
      description: 'Single centralized repository for all documents feeding NextGen Data Sites, Coordination Platform, and UNHCR.org',
      technicalSpecs: [
        'Design central document storage database with fields: doc_id, title, description, file_path, version, created_date, modified_date',
        'Implement cloud storage integration (Azure Blob Storage or AWS S3) for document files',
        'Create REST API endpoints: POST /documents/upload, GET /documents/{id}, PUT /documents/{id}, DELETE /documents/{id}',
        'Build content distribution service to sync documents across NextGen sites',
        'Implement versioning system with rollback capability'
      ],
      acceptance: 'Documents uploaded to central repository appear on all connected platforms within 5 minutes',
      dependencies: 'Cloud storage infrastructure, API gateway'
    },
    {
      id: 'REQ-002',
      module: 'Common Document Repository',
      priority: 'High',
      feature: 'Rich Document Metadata and Taxonomy',
      description: 'Structured metadata system aligned with ODP, UNHCR.org, and ReliefWeb taxonomies',
      technicalSpecs: [
        'Create metadata schema with fields: document_type, publication_date, coverage_date, country_id, region_id, situation_id, population_group[], sector[], language[]',
        'Build taxonomy management tables: doc_types, sectors, population_groups, languages with parent-child relationships',
        'Implement metadata validation rules and constraints',
        'Create taxonomy mapping service to align ODP → UNHCR.org → ReliefWeb',
        'Build admin interface for taxonomy management with CRUD operations'
      ],
      acceptance: 'All mandatory metadata fields enforced before document publication; taxonomy aligned across all three systems',
      dependencies: 'Reference data from UNHCR.org and ReliefWeb APIs'
    },
    {
      id: 'REQ-003',
      module: 'Common Document Repository',
      priority: 'Medium',
      feature: 'AI-Assisted Document Upload',
      description: 'Automated metadata extraction and document summarization using AI',
      technicalSpecs: [
        'Integrate Azure OpenAI or Claude API for document analysis',
        'Build document processing pipeline: file upload → text extraction (OCR if needed) → AI analysis → metadata suggestion',
        'Implement prompt engineering for: title extraction, description generation, tag suggestion, sector classification, language detection',
        'Create metadata review UI with suggested vs. user-edited fields clearly marked',
        'Add confidence scoring for AI suggestions',
        'Build feedback loop to improve AI accuracy over time'
      ],
      acceptance: 'AI correctly suggests metadata with >80% accuracy; users can review and edit all suggestions before publishing',
      dependencies: 'AI API access, OCR service for scanned documents'
    },
    {
      id: 'REQ-004',
      module: 'Common Document Repository',
      priority: 'High',
      feature: 'Document Review and Approval Workflow',
      description: 'Human-in-the-loop review process with notifications and version control',
      technicalSpecs: [
        'Design workflow state machine: Draft → Pending Review → Approved/Rejected → Published',
        'Create workflow tables: document_submissions, review_history, approver_assignments',
        'Implement role-based permissions: Uploader, Reviewer, Approver, Admin',
        'Build notification service (email + Teams webhook) for review requests',
        'Create approval dashboard showing pending reviews, history, and comments',
        'Add comment/feedback system for reviewer-uploader communication',
        'Implement audit trail logging all workflow actions'
      ],
      acceptance: 'Reviewers notified within 2 minutes of submission; complete audit trail maintained for all documents',
      dependencies: 'Email service, Microsoft Teams integration, user authentication system'
    },
    {
      id: 'REQ-005',
      module: 'Common Document Repository',
      priority: 'High',
      feature: 'Search and Discovery',
      description: 'Advanced search with free-text and faceted filtering capabilities',
      technicalSpecs: [
        'Implement Elasticsearch or Azure Cognitive Search for full-text indexing',
        'Index fields: title, description, content (extracted text), all metadata fields',
        'Build search API with support for: boolean operators, phrase matching, fuzzy search, relevance ranking',
        'Create faceted filter interface for: country, region, situation, document_type, sector, population_group, date_range',
        'Implement filter persistence and shareable search URLs',
        'Add search analytics to track popular queries and improve results'
      ],
      acceptance: 'Search returns relevant results in <2 seconds; users can apply multiple filters simultaneously; search relevance score >85%',
      dependencies: 'Search engine infrastructure, document text extraction service'
    },
    {
      id: 'REQ-006',
      module: 'Common Document Repository',
      priority: 'Medium',
      feature: 'Document Presentation and Access',
      description: 'Dedicated landing pages with previews, metadata display, and download options',
      technicalSpecs: [
        'Build document landing page template with sections: thumbnail/preview, metadata panel, download button, share options, edit button (role-based)',
        'Implement thumbnail generation service for PDFs, Word docs, images',
        'Create document preview component using PDF.js or Office Online',
        'Build social sharing functionality with OpenGraph meta tags',
        'Implement download tracking and analytics',
        'Add print-friendly view option'
      ],
      acceptance: 'Each document has unique URL with preview; metadata clearly displayed; download and share buttons functional',
      dependencies: 'Document preview libraries, thumbnail generation service'
    },
    {
      id: 'REQ-007',
      module: 'Common Document Repository',
      priority: 'Medium',
      feature: 'Role-Based Access and Upload Rights',
      description: 'Granular permissions for IM, Protection, External Relations, and Comm focal points',
      technicalSpecs: [
        'Design role hierarchy: Admin → Regional Focal Point → Country Focal Point → Contributor',
        'Create permissions matrix: roles × actions (upload, edit, delete, approve, publish)',
        'Implement Azure AD or OAuth integration for authentication',
        'Build role assignment interface in admin console',
        'Create scope-based permissions (e.g., country-level, region-level, global)',
        'Implement delegation feature for temporary role assignment'
      ],
      acceptance: 'Users can only perform actions permitted by their role; IM focal points can delegate upload rights to Protection/ER/Comm staff',
      dependencies: 'Identity provider (Azure AD), authorization service'
    },
    {
      id: 'REQ-008',
      module: 'Common Document Repository',
      priority: 'Medium',
      feature: 'Legacy ODP Document Migration',
      description: 'Automated migration with filtering to exclude irrelevant legacy content',
      technicalSpecs: [
        'Build migration extraction service to connect to ODP database',
        'Create filtering rules: exclude documents with tags [signpost, waypoint, directory], exclude docs older than 10 years unless flagged',
        'Implement data transformation pipeline: ODP schema → NextGen schema',
        'Build migration dashboard showing progress, errors, validation issues',
        'Create archive database for excluded documents with searchable index',
        'Implement rollback mechanism in case of migration errors',
        'Add post-migration validation reports'
      ],
      acceptance: 'All relevant ODP documents migrated with correct metadata; filtered documents archived but accessible; migration report shows 100% completion with <1% errors',
      dependencies: 'Access to ODP database, ETL tools, archive storage'
    },
    {
      id: 'REQ-009',
      module: 'Operational Population Data',
      priority: 'High',
      feature: 'Unified Population Data Module',
      description: 'Standardized data module for refugee, IDP, returnee, and mixed movement populations',
      technicalSpecs: [
        'Design unified data schema: population_id, country_id, situation_id, population_group, demographic_breakdown (age/gender), date, source, frequency',
        'Build data ingestion API accepting CSV, JSON, Excel formats',
        'Implement data validation rules: required fields, value ranges, consistency checks',
        'Create data routing logic: Refugee data → WS2, Context-specific data → WS3, Both → WS2 + WS3',
        'Build automated data quality checks and flagging system',
        'Implement exception handling for non-standard data structures'
      ],
      acceptance: 'System accepts population data from all sources; automatically routes to correct platform; validates data with 95% accuracy',
      dependencies: 'Common data layer database, data validation engine'
    },
    {
      id: 'REQ-010',
      module: 'Operational Population Data',
      priority: 'Medium',
      feature: 'Exception Handling for Legacy Data',
      description: 'Flexible import rules for countries with incomplete or non-standard data',
      technicalSpecs: [
        'Create exception rules engine with configurable minimum required fields',
        'Build exception configuration interface: define country-specific rules, minimum fields, data granularity levels',
        'Implement metadata capture for exceptions: reason, source limitations, caveats, explanatory notes',
        'Create exception documentation system visible to future IM focal points',
        'Build exception approval workflow requiring regional office sign-off',
        'Add exception monitoring dashboard showing all active exceptions by country'
      ],
      acceptance: 'Countries can import partial data with documented exceptions; future users can understand historical data limitations; exceptions require approval',
      dependencies: 'Workflow system, documentation storage'
    },
    {
      id: 'REQ-011',
      module: 'AI-Enabled Data Exploration',
      priority: 'High',
      feature: 'Natural Language Query Interface',
      description: 'AI assistant for asking questions about operational data in plain English',
      technicalSpecs: [
        'Integrate LLM (Claude/GPT-4) with function calling to query data layer',
        'Build query parser to convert natural language → SQL/API calls',
        'Create data context injection: provide LLM with schema, available data ranges, metadata',
        'Implement query safeguards: prevent data modification, limit query complexity, timeout after 30s',
        'Build conversational memory to handle follow-up questions',
        'Add query logging and analytics to improve NL understanding'
      ],
      acceptance: 'Users can ask questions in plain English; system responds with accurate data in <5 seconds; handles 90% of common query types',
      dependencies: 'LLM API access, data layer query service'
    },
    {
      id: 'REQ-012',
      module: 'AI-Enabled Data Exploration',
      priority: 'High',
      feature: 'Automated Insight Generation',
      description: 'AI-generated summaries of trends, patterns, and changes in displacement data',
      technicalSpecs: [
        'Build trend analysis engine: calculate month-over-month, year-over-year changes',
        'Implement pattern detection algorithms: identify sudden spikes, sustained trends, seasonal patterns',
        'Create insight generation prompts for LLM: "Summarize key trends for {country} in the past 6 months"',
        'Build insight caching system to avoid regenerating unchanged summaries',
        'Add confidence indicators for insights based on data completeness',
        'Implement insight versioning when underlying data updates'
      ],
      acceptance: 'System generates accurate insights highlighting increasing/decreasing/stable trends; insights update when new data arrives',
      dependencies: 'Statistical analysis libraries, LLM API'
    },
    {
      id: 'REQ-013',
      module: 'AI-Enabled Data Exploration',
      priority: 'High',
      feature: 'Data Source Attribution and Limitations',
      description: 'Clear indication of data sources, update dates, and known limitations',
      technicalSpecs: [
        'Design data lineage tracking: source_id, collection_date, update_date, methodology, limitations, caveats',
        'Build attribution display component showing source, date, and confidence level',
        'Create limitation flagging system: data gaps, estimation methods, known issues',
        'Implement "data not available" messaging for missing data scenarios',
        'Add data quality indicators: complete, partial, estimated, outdated',
        'Build data freshness monitoring with alerts for stale data'
      ],
      acceptance: 'All data responses include clear source attribution; limitations prominently displayed; users understand data quality',
      dependencies: 'Data provenance system, metadata storage'
    },
    {
      id: 'REQ-014',
      module: 'RRP Coordination Data',
      priority: 'High',
      feature: 'Common RRP Data Template',
      description: 'Standardized data structure for Refugee Response Plans (RRP/JRP/RMRP)',
      technicalSpecs: [
        'Design RRP data schema: plan_id, country_ids[], plan_type (RRP/JRP/RMRP), financial_requirements, population_targeted, funding_received, funding_gap, partners[], sectors[]',
        'Build ActivityInfo integration connector to pull standardized data',
        'Create data transformation service: ActivityInfo format → Common data layer format',
        'Implement data aggregation logic: by sector, by organization, by country',
        'Build data validation against agreed inter-agency standards',
        'Create API endpoints for NextGen sites to consume RRP data'
      ],
      acceptance: 'RRP data from all countries automatically ingested; standardized across all response plans; accessible via API',
      dependencies: 'ActivityInfo API access, inter-agency data standards documentation'
    },
    {
      id: 'REQ-015',
      module: 'Standard Taxonomies',
      priority: 'High',
      feature: 'Population Group Taxonomy',
      description: 'Controlled vocabulary aligned with UNHCR Annual Statistics Report',
      technicalSpecs: [
        'Create population_groups reference table with 17 standard categories',
        'Implement taxonomy enforcement in data entry forms (dropdown with no free-text)',
        'Build mapping service for context-specific terms → standard categories',
        'Create taxonomy governance workflow: only HQ NextGen admins can modify',
        'Implement taxonomy versioning for historical data compatibility',
        'Build taxonomy API for consumption by all NextGen sites',
        'Add taxonomy documentation with official UNHCR definitions'
      ],
      acceptance: 'All population data uses standard taxonomy; no custom categories allowed; mappings documented and governed',
      dependencies: 'Reference to UNHCR Refugee Data Finder definitions'
    },
    {
      id: 'REQ-016',
      module: 'Admin Console',
      priority: 'High',
      feature: 'Situation Definition Interface',
      description: 'Admin tool to create and manage situations with metadata and country linkages',
      technicalSpecs: [
        'Build admin console situation management module with CRUD operations',
        'Create situation data model: situation_id, name, description, type (emergency/protracted), start_date, end_date, impacted_countries[], population_groups[], categories[]',
        'Implement UNHCR emergency alignment: pull L2/L3 data from UNHCR.org API, match by geography',
        'Build country impact configuration: origin countries, transit countries, destination countries (for mixed movements)',
        'Create situation categorization: RRP, Fundraising, Advocacy (multi-select)',
        'Implement visibility rules: public/internal flag for sensitive data',
        'Build situation validation rules and conflict detection'
      ],
      acceptance: 'Admins can create situations aligned with emergencies; situations properly categorized; country relationships defined',
      dependencies: 'UNHCR.org emergencies API, country reference data'
    },
    {
      id: 'REQ-017',
      module: 'Admin Console',
      priority: 'High',
      feature: 'Data Automation Configuration',
      description: 'Configure automatic data pulls from common data layer (funding, indicators, partners)',
      technicalSpecs: [
        'Build data source configuration interface: select data types, configure refresh frequency, map fields',
        'Create country ID mapping tool: NextGen country_id ↔ Compass country_id ↔ Oracle ID',
        'Implement automated data sync jobs with scheduling (hourly, daily, weekly)',
        'Build data transformation rules engine for different source formats',
        'Create sync monitoring dashboard: status, last update, errors, data quality metrics',
        'Implement manual override and emergency data push capabilities'
      ],
      acceptance: 'Funding and indicator data automatically updated; country mappings configured; sync runs reliably with <2% failure rate',
      dependencies: 'Compass API, Oracle database access, scheduling service'
    },
    {
      id: 'REQ-018',
      module: 'Content Presentation',
      priority: 'High',
      feature: 'Flexible Widget Library',
      description: 'Reusable content widgets for text, maps, documents, tables, and charts',
      technicalSpecs: [
        'Build widget framework with standard interface: render(), configure(), getData()',
        'Create 8 widget types: Text Widget (rich text editor), Map Widget (Mapbox integration), Document Widget (featured docs), Table Widget (population data), Chart Widget (trend graphs), Demographic Widget (age/gender), iFrame Widget (external dashboards), Custom HTML Widget',
        'Implement drag-and-drop page builder interface',
        'Create widget configuration panels with widget-specific settings',
        'Build widget data binding: connect widgets to common data layer or static content',
        'Implement widget templates for common use cases',
        'Add responsive design support for all widgets'
      ],
      acceptance: 'Users can build custom page layouts; all 8 widget types functional; pages render correctly on desktop and mobile',
      dependencies: 'Frontend framework (React), Mapbox API, chart libraries'
    },
    {
      id: 'REQ-019',
      module: 'Content Presentation',
      priority: 'Medium',
      feature: 'External Dashboard Embedding',
      description: 'Support for embedding Power BI, ArcGIS, and other external visualizations',
      technicalSpecs: [
        'Build iFrame widget with security controls: CSP headers, sandboxing, whitelist of allowed domains',
        'Implement responsive iFrame resizing based on content',
        'Create embed code generator for common tools (Power BI, Tableau, ArcGIS)',
        'Add authentication pass-through for secured dashboards (where possible)',
        'Build fallback messaging for failed embeds',
        'Implement embed performance monitoring'
      ],
      acceptance: 'External dashboards embed correctly; responsive on all devices; secured against XSS attacks',
      dependencies: 'External dashboard services, security review'
    },
    {
      id: 'REQ-020',
      module: 'Content Presentation',
      priority: 'High',
      feature: 'Situation View Template',
      description: 'Standardized template for situation pages with automated content aggregation',
      technicalSpecs: [
        'Design situation page template with sections: Header (name, description), Key Figures (population aggregated), Funding Overview (visual chart), Documents (filtered by situation_id), Related Countries (links)',
        'Build content aggregation service: query all data/content tagged with situation_id',
        'Implement dynamic content injection based on situation categories (RRP shows appeals data, Advocacy shows policy docs)',
        'Create automated population aggregation across impacted countries',
        'Build funding visualization component pulling from RRP data',
        'Implement "last updated" timestamps for each section'
      ],
      acceptance: 'Situation pages automatically populate with relevant content; population totals calculated correctly; funding data current',
      dependencies: 'Common data layer, content tagging system'
    },
    {
      id: 'REQ-021',
      module: 'Content Presentation',
      priority: 'Medium',
      feature: 'Country-Situation Integration',
      description: 'Link country pages with related situations for seamless navigation',
      technicalSpecs: [
        'Build relationship mapping: country ↔ situations (many-to-many)',
        'Create "Related Situations" widget for country pages',
        'Implement situation data snippets on country pages: latest figures from linked situations',
        'Build bidirectional navigation: country page → situation pages, situation page → impacted country pages',
        'Create breadcrumb navigation showing relationship hierarchy',
        'Implement smart content recommendations based on user navigation patterns'
      ],
      acceptance: 'Users can navigate between country and situation views; related content clearly linked; navigation intuitive',
      dependencies: 'Country-situation relationship data, navigation framework'
    },
    {
      id: 'REQ-022',
      module: 'Partner Management',
      priority: 'High',
      feature: 'Consolidated Partner Database',
      description: 'Unified partner registry merging ActivityInfo, UN Partner Portal, and ODP partner data',
      technicalSpecs: [
        'Design consolidated partner schema: partner_id, unpp_id, compass_id, legal_name, short_name, acronym, partner_type, offices[]',
        'Build data consolidation service: merge ActivityInfo + UNPP + ODP partner records',
        'Implement deduplication algorithm: match by name similarity, UNPP ID, contact details',
        'Create partner record enrichment: if UNPP ID exists, pull full data from UNPP API',
        'Build partner office management: office_id, city, country, contact_details, active_status',
        'Implement partner data quality scoring and flagging for missing UNPP links',
        'Create partner reference API for use across all platforms'
      ],
      acceptance: 'All partners from 3 sources consolidated; duplicates merged; UNPP-linked partners fully enriched; single source of truth established',
      dependencies: 'ActivityInfo API, UN Partner Portal API, ODP database access'
    },
    {
      id: 'REQ-023',
      module: 'Coordination Platform',
      priority: 'Medium',
      feature: 'Partner Space',
      description: 'Dedicated pages for partners showing 3W, contacts, funding, and documents',
      technicalSpecs: [
        'Build partner profile page template with sections: Overview, 3W Activities, Contact Details, Funding (from RRP), Related Content, Documents',
        'Implement data aggregation by partner_id from multiple sources',
        'Create 3W activity display pulling from ActivityInfo',
        'Build funding breakdown visualization by sector and country',
        'Implement document filtering to show partner-specific content',
        'Add "Partner in other situations" section with cross-references',
        'Create partner contact directory integration'
      ],
      acceptance: 'Each partner has profile page; 3W data displays correctly; funding and documents aggregated by partner',
      dependencies: 'Consolidated partner database, 3W data from ActivityInfo'
    },
    {
      id: 'REQ-024',
      module: 'Coordination Platform',
      priority: 'High',
      feature: 'Contact List Module',
      description: 'Searchable directory of coordination contacts with role-based access',
      technicalSpecs: [
        'Design contact schema: contact_id, name, role, organization, sector, coordination_role, email, phone, country, admin_level (province/district), office_location, public_flag, active_until',
        'Build ActivityInfo integration to import existing contact data',
        'Create standard contact form template for ActivityInfo databases',
        'Implement search and filter API: by country, situation, organization, sector, role, public/private',
        'Build contact management UI with add/edit/deactivate functions',
        'Implement contact expiry system with notifications 30 days before active_until date',
        'Create role-based access: IM/coordination focal points can edit, others read-only'
      ],
      acceptance: 'Contact list searchable and filterable; contacts auto-expire when active_until date passes; role-based editing enforced',
      dependencies: 'ActivityInfo template design, user role management'
    },
    {
      id: 'REQ-025',
      module: 'Coordination Platform',
      priority: 'Medium',
      feature: 'Service Mapping Tool',
      description: 'Interactive map of services for refugees, IDPs, and persons of concern',
      technicalSpecs: [
        'Design service data model: service_id, provider_id, service_name, description, category, sector, location (lat/long), address, contact, operating_hours, eligibility',
        'Build service taxonomy management: categories hierarchy, sector classification',
        'Implement Mapbox integration for interactive map display',
        'Create service entry form with location picker and bulk upload template',
        'Build responsive mobile interface optimized for smartphone access',
        'Implement search and filter: by location (proximity), category, sector, provider',
        'Add service verification workflow: submitted → verified → published',
        'Create public-facing map interface for beneficiaries'
      ],
      acceptance: 'Services displayed on interactive map; searchable by location and category; mobile-responsive; beneficiaries can find services easily',
      dependencies: 'Mapbox API, geolocation services, service taxonomy definition'
    },
    {
      id: 'REQ-026',
      module: 'Multilingual Support',
      priority: 'Medium',
      feature: 'Language Selection and Translation',
      description: 'Support for UN languages and local languages with translation utilities',
      technicalSpecs: [
        'Implement language selector UI component (dropdown or flag icons)',
        'Create language preference storage: session-based and user account-based',
        'Build translation database: translations table (content_id, language_code, translated_text)',
        'Implement 6 UN official languages: EN, FR, ES, AR, ZH, RU',
        'Create translation management interface for content editors',
        'Build machine translation integration (Azure Translator) with human review workflow',
        'Implement language-specific content fallback: show English if translation unavailable',
        'Add translation coverage reporting by content type and language'
      ],
      acceptance: 'Language switcher functional; core content available in all 6 UN languages; local language support configurable per country',
      dependencies: 'Translation management system, Azure Translator API'
    },
    {
      id: 'REQ-027',
      module: 'Data Migration',
      priority: 'High',
      feature: 'ODP Content Decomposition and Routing',
      description: 'Automated routing of ODP content to NextGen sites based on content type and audience',
      technicalSpecs: [
        'Build content analysis service to classify ODP content by type, audience, purpose',
        'Create routing decision engine with rules: Refugee data → WS2, Coordination content → WS3, Policy/advocacy → UNHCR.org, Overlapping content → multiple destinations',
        'Implement content transformation pipelines for each destination',
        'Build migration dashboard showing routing decisions with manual override capability',
        'Create validation reports: content integrity checks, broken link detection, missing metadata',
        'Implement phased migration: test → validate → production with rollback points',
        'Build migration documentation system explaining routing decisions'
      ],
      acceptance: 'ODP content correctly routed to appropriate platforms; migration dashboard shows 100% completion; validation reports show <2% errors',
      dependencies: 'Access to ODP database, NextGen sites ingestion APIs'
    },
    {
      id: 'REQ-028',
      module: 'Platform Architecture',
      priority: 'High',
      feature: 'Common Data Layer',
      description: 'Enterprise data platform serving all NextGen sites with standardized schemas',
      technicalSpecs: [
        'Design common data layer architecture: data lake (raw data) + data warehouse (transformed) + data marts (topic-specific)',
        'Implement core schemas: documents, population_data, situations, countries, partners, funding, indicators, contacts, services',
        'Build ETL pipelines for data ingestion from multiple sources',
        'Create data quality framework: validation rules, completeness checks, consistency monitoring',
        'Implement data access layer with REST APIs and GraphQL endpoints',
        'Build data catalog and metadata management',
        'Create data governance policies and access controls',
        'Implement data lineage tracking for audit and compliance'
      ],
      acceptance: 'Common data layer operational; all data schemas implemented; APIs functional with 99.5% uptime; data quality >95%',
      dependencies: 'Cloud infrastructure (Azure/AWS), data integration tools, API management'
    }
  ];

  const downloadCSV = () => {
    const headers = ['Req ID', 'Module', 'Priority', 'Feature', 'Description', 'Technical Specifications', 'Acceptance Criteria', 'Dependencies'];
    
    const csvContent = [
      headers.join(','),
      ...requirements.map(req => [
        req.id,
        `"${req.module}"`,
        req.priority,
        `"${req.feature}"`,
        `"${req.description}"`,
        `"${req.technicalSpecs.join(' | ')}"`,
        `"${req.acceptance}"`,
        `"${req.dependencies}"`
      ].join(','))
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'ODP_NextGen_Requirements.csv';
    a.click();
  };

  const priorityColors = {
    High: 'bg-red-100 text-red-800 border-red-300',
    Medium: 'bg-yellow-100 text-yellow-800 border-yellow-300',
    Low: 'bg-green-100 text-green-800 border-green-300'
  };

  const moduleColors = {
    'Common Document Repository': 'bg-blue-50',
    'Operational Population Data': 'bg-purple-50',
    'AI-Enabled Data Exploration': 'bg-indigo-50',
    'RRP Coordination Data': 'bg-pink-50',
    'Standard Taxonomies': 'bg-teal-50',
    'Admin Console': 'bg-orange-50',
    'Content Presentation': 'bg-cyan-50',
    'Partner Management': 'bg-lime-50',
    'Coordination Platform': 'bg-amber-50',
    'Multilingual Support': 'bg-emerald-50',
    'Data Migration': 'bg-violet-50',
    'Platform Architecture': 'bg-rose-50'
  };

  const groupedRequirements = requirements.reduce((acc, req) => {
    if (!acc[req.module]) acc[req.module] = [];
    acc[req.module].push(req);
    return acc;
  }, {});

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <FileSpreadsheet className="w-12 h-12 text-blue-600" />
              <div>
                <h1 className="text-3xl font-bold text-gray-900">ODP NextGen Business Requirements</h1>
                <p className="text-gray-600 mt-1">Detailed specifications for development team</p>
              </div>
            </div>
            <button
              onClick={downloadCSV}
              className="flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors shadow-md"
            >
              <Download className="w-5 h-5" />
              Download CSV
            </button>
          </div>
          
          <div className="grid grid-cols-3 gap-4 mt-6">
            <div className="bg-blue-50 p-4 rounded-lg">
              <div className="text-2xl font-bold text-blue-900">{requirements.length}</div>
              <div className="text-sm text-blue-700">Total Requirements</div>
            </div>
            <div className="bg-red-50 p-4 rounded-lg">
              <div className="text-2xl font-bold text-red-900">
                {requirements.filter(r => r.priority === 'High').length}
              </div>
              <div className="text-sm text-red-700">High Priority</div>
            </div>
            <div className="bg-purple-50 p-4 rounded-lg">
              <div className="text-2xl font-bold text-purple-900">
                {Object.keys(groupedRequirements).length}
              </div>
              <div className="text-sm text-purple-700">Modules</div>
            </div>
          </div>
        </div>

        {/* Requirements by Module */}
        <div className="space-y-4">
          {Object.entries(groupedRequirements).map(([module, reqs]) => (
            <div key={module} className={`rounded-lg shadow-md overflow-hidden ${moduleColors[module]}`}>
              <button
                onClick={() => toggleSection(module)}
                className="w-full p-4 flex items-center justify-between hover:bg-opacity-80 transition-colors"
              >
                <div className="flex items-center gap-3">
                  {expandedSections[module] ? (
                    <ChevronDown className="w-5 h-5" />
                  ) : (
                    <ChevronRight className="w-5 h-5" />
                  )}
                  <h2 className="text-xl font-bold text-gray-900">{module}</h2>
                  <span className="bg-white px-3 py-1 rounded-full text-sm font-semibold">
                    {reqs.length} requirements
                  </span>
                </div>
              </button>

              {expandedSections[module] && (
                <div className="p-4 bg-white space-y-4">
                  {reqs.map(req => (
                    <div key={req.id} className="border border-gray-200 rounded-lg p-5 hover:shadow-md transition-shadow">
                      <div className="flex items-start justify-between mb-3">
                        <div className="flex items-center gap-3">
                          <span className="bg-gray-800 text-white px-3 py-1 rounded font-mono text-sm">
                            {req.id}
                          </span>
                          <h3 className="text-lg font-semibold text-gray-900">{req.feature}</h3>
                        </div>
                        <span className={`px-3 py-1 rounded-full text-sm font-semibold border ${priorityColors[req.priority]}`}>
                          {req.priority}
                        </span>
                      </div>

                      <p className="text-gray-700 mb-4">{req.description}</p>

                      <div className="space-y-4">
                        <div>
                          <h4 className="font-semibold text-gray-900 mb-2 flex items-center gap-2">
                            <span className="w-2 h-2 bg-blue-600 rounded-full"></span>
                            Technical Specifications for Developers
                          </h4>
                          <ul className="space-y-2">
                            {req.technicalSpecs.map((spec, idx) => (
                              <li key={idx} className="flex gap-3">
                                <span className="text-blue-600 font-semibold mt-1">{idx + 1}.</span>
                                <span className="text-gray-700 flex-1">{spec}</span>
                              </li>
                            ))}
                          </ul>
                        </div>

                        <div className="bg-green-50 border-l-4 border-green-500 p-3 rounded">
                          <h4 className="font-semibold text-green-900 mb-1">Acceptance Criteria</h4>
                          <p className="text-green-800 text-sm">{req.acceptance}</p>
                        </div>

                        <div className="bg-amber-50 border-l-4 border-amber-500 p-3 rounded">
                          <h4 className="font-semibold text-amber-900 mb-1">Dependencies</h4>
                          <p className="text-amber-800 text-sm">{req.dependencies}</p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Summary Footer */}
        <div className="bg-white rounded-lg shadow-lg p-6 mt-6">
          <h3 className="text-lg font-bold text-gray-900 mb-4">Implementation Notes</h3>
          <div className="grid grid-cols-2 gap-4 text-sm text-gray-700">
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Development Phases</h4>
              <ol className="list-decimal list-inside space-y-1">
                <li>Phase 1: Common Data Layer & Document Repository "(REQ-001 to REQ-008)"</li>
                <li>Phase 2: Population Data & Taxonomies "(REQ-0o to REQ-016)"</li>
                <li>Phase 3: Content Presentation & Widgets "(REQ-017 to REQ-021)"</li>
                <li>Phase 4: Partner & Coordination Platform "(REQ-022 to REQ-025)"</li>
                <li>Phase 5: AI Features & Multilingual "(REQ-011 to REQ-013, REQ-026)"</li>
                <li>Phase 6: Data Migration "(REQ-027 to REQ-028)"</li>
              </ol>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Key Technologies</h4>
              <ul className="space-y-1">
                <li>"• Backend: .NET Core / Node.js, REST APIs, GraphQL"</li>
                <li>"• Frontend: React, Tailwind CSS, Responsive Design"</li>
                <li>"• Database: SQL Server / PostgreSQL, Azure Blob Storage"</li>
                <li>"• AI/ML: Azure OpenAI / Claude API, NLP Services"</li>
                <li>"• Maps: Mapbox, GeoJSON"</li>
                <li>"• Search: Elasticsearch / Azure Cognitive Search"</li>
                <li>"• Integration: ActivityInfo API, UNPP API, Compass API"</li>
                <li>"• Authentication: Azure AD, OAuth 2.0, Role-Based Access"</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RequirementsExcel;