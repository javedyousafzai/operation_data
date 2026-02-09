import React, { useState } from 'react';
import { Database, FileText, Users, Globe, Settings, ArrowRight, Filter, CheckCircle, XCircle, RefreshCw } from 'lucide-react';

const MigrationDiagram = () => {
  const [activeView, setActiveView] = useState('overview');

  const OverviewDiagram = () => (
    <div className="w-full h-full p-8 bg-gradient-to-br from-blue-50 to-indigo-50">
      <h2 className="text-2xl font-bold mb-6 text-center text-indigo-900">ODP Decomposition Architecture</h2>
      
      {/* Current ODP */}
      <div className="flex items-start justify-between gap-8">
        <div className="flex-1 bg-white rounded-lg shadow-lg p-6 border-2 border-gray-300">
          <div className="flex items-center gap-3 mb-4">
            <Database className="w-8 h-8 text-blue-600" />
            <h3 className="text-xl font-bold text-gray-800">Operational Data Portal (ODP)</h3>
          </div>
          
          <div className="space-y-3">
            <div className="bg-blue-50 p-3 rounded border border-blue-200">
              <div className="font-semibold text-blue-900 mb-2">Content Types:</div>
              <ul className="text-sm space-y-1 text-gray-700">
                <li>&#8226; Documents (90,000+)</li>
                <li>&#8226; Population Data</li>
                <li>&#8226; Funding Information</li>
                <li>&#8226; Working Groups</li>
                <li>&#8226; Partner Data</li>
                <li>&#8226; News & Highlights</li>
                <li>&#8226; Indicators</li>
              </ul>
            </div>
            
            <div className="bg-amber-50 p-3 rounded border border-amber-200">
              <div className="font-semibold text-amber-900 mb-2">Coverage:</div>
              <ul className="text-sm space-y-1 text-gray-700">
                <li>&#8226; Situations (50+)</li>
                <li>&#8226; Countries (100+)</li>
                <li>&#8226; Regional Pages</li>
                <li>&#8226; MCO Offices</li>
              </ul>
            </div>
          </div>
        </div>

        <div className="flex flex-col items-center justify-center gap-4 py-12">
          <ArrowRight className="w-12 h-12 text-indigo-600 animate-pulse" />
          <div className="text-center">
            <div className="font-bold text-indigo-900">Decomposition</div>
            <div className="text-sm text-gray-600">& Migration</div>
          </div>
          <ArrowRight className="w-12 h-12 text-indigo-600 animate-pulse" />
        </div>

        {/* Target Systems */}
        <div className="flex-1 space-y-4">
          {/* Common Data Layer */}
          <div className="bg-white rounded-lg shadow-lg p-4 border-2 border-purple-400">
            <div className="flex items-center gap-2 mb-3">
              <Database className="w-6 h-6 text-purple-600" />
              <h4 className="font-bold text-gray-800">Common Data Layer (Orion)</h4>
            </div>
            <div className="text-sm text-gray-700 space-y-1">
              <div>&#8226; Population Data Module</div>
              <div>&#8226; RRP Data Template</div>
              <div>&#8226; Funding Data</div>
              <div>&#8226; Indicator Data</div>
              <div>&#8226; Partner Data</div>
            </div>
          </div>

          {/* Document Repository */}
          <div className="bg-white rounded-lg shadow-lg p-4 border-2 border-green-400">
            <div className="flex items-center gap-2 mb-3">
              <FileText className="w-6 h-6 text-green-600" />
              <h4 className="font-bold text-gray-800">Document Repository</h4>
            </div>
            <div className="text-sm text-gray-700 space-y-1">
              <div>&#8226; AI-Assisted Upload</div>
              <div>&#8226; Unified Taxonomy</div>
              <div>&#8226; Approval Workflow</div>
              <div>&#8226; Serves all platforms</div>
            </div>
          </div>

          {/* NextGen Sites */}
          <div className="bg-white rounded-lg shadow-lg p-4 border-2 border-blue-400">
            <div className="flex items-center gap-2 mb-3">
              <Globe className="w-6 h-6 text-blue-600" />
              <h4 className="font-bold text-gray-800">NextGen Data Sites (WS2)</h4>
            </div>
            <div className="text-sm text-gray-700 space-y-1">
              <div>&#8226; Refugee Data Portal</div>
              <div>&#8226; UNHCR.org</div>
              <div>&#8226; ASR-aligned data</div>
            </div>
          </div>

          {/* Coordination Platform */}
          <div className="bg-white rounded-lg shadow-lg p-4 border-2 border-orange-400">
            <div className="flex items-center gap-2 mb-3">
              <Users className="w-6 h-6 text-orange-600" />
              <h4 className="font-bold text-gray-800">Coordination Platform (WS3)</h4>
            </div>
            <div className="text-sm text-gray-700 space-y-1">
              <div>&#8226; Inter-agency content</div>
              <div>&#8226; Ad-hoc population data</div>
              <div>&#8226; Working Groups</div>
              <div>&#8226; Contact Lists</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const DataFlowDiagram = () => (
    <div className="w-full h-full p-8 bg-gradient-to-br from-green-50 to-teal-50">
      <h2 className="text-2xl font-bold mb-6 text-center text-teal-900">Population Data Migration Flow</h2>
      
      <div className="grid grid-cols-3 gap-6">
        {/* Source Data */}
        <div className="bg-white rounded-lg shadow-lg p-6 border-2 border-gray-300">
          <h3 className="font-bold text-lg mb-4 text-gray-800">ODP Population Data</h3>
          <div className="space-y-3">
            <div className="bg-blue-50 p-3 rounded">
              <div className="font-semibold text-blue-900 mb-1">ASR-Aligned Data</div>
              <div className="text-xs text-gray-600">
                Refugees, Asylum-seekers, IDPs, Returnees
              </div>
            </div>
            <div className="bg-amber-50 p-3 rounded">
              <div className="font-semibold text-amber-900 mb-1">Ad-hoc Data</div>
              <div className="text-xs text-gray-600">
                Arrivals, Departures, Flow data
              </div>
            </div>
            <div className="bg-purple-50 p-3 rounded">
              <div className="font-semibold text-purple-900 mb-1">Context-Specific</div>
              <div className="text-xs text-gray-600">
                Exception handling cases
              </div>
            </div>
          </div>
        </div>

        {/* Processing */}
        <div className="bg-white rounded-lg shadow-lg p-6 border-2 border-indigo-400">
          <h3 className="font-bold text-lg mb-4 text-indigo-900">Data Classification</h3>
          <div className="space-y-4">
            <div className="border-l-4 border-green-500 pl-3">
              <div className="font-semibold text-green-700 mb-1">Route 1: Enterprise Data</div>
              <div className="text-xs text-gray-600">
                → Common Data Layer<br/>
                → NextGen Sites (WS2)
              </div>
            </div>
            <div className="border-l-4 border-orange-500 pl-3">
              <div className="font-semibold text-orange-700 mb-1">Route 2: Coordination Data</div>
              <div className="text-xs text-gray-600">
                → Common Data Layer<br/>
                → Coordination Platform (WS3)
              </div>
            </div>
            <div className="border-l-4 border-purple-500 pl-3">
              <div className="font-semibold text-purple-700 mb-1">Route 3: Dual Platform</div>
              <div className="text-xs text-gray-600">
                → Both WS2 & WS3<br/>
                → Shared visibility
              </div>
            </div>
          </div>
        </div>

        {/* Destination */}
        <div className="bg-white rounded-lg shadow-lg p-6 border-2 border-gray-300">
          <h3 className="font-bold text-lg mb-4 text-gray-800">Data Consumption</h3>
          <div className="space-y-3">
            <div className="bg-blue-50 p-3 rounded border border-blue-200">
              <div className="font-semibold text-blue-900 mb-1">NextGen Sites</div>
              <div className="text-xs text-gray-600">
                • Country pages<br/>
                • Situation views<br/>
                • AI-enabled exploration
              </div>
            </div>
            <div className="bg-orange-50 p-3 rounded border border-orange-200">
              <div className="font-semibold text-orange-900 mb-1">Coordination Platform</div>
              <div className="text-xs text-gray-600">
                • RRP dashboards<br/>
                • Partner visibility<br/>
                • Real-time updates
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Data Templates */}
      <div className="mt-6 bg-white rounded-lg shadow-lg p-6 border-2 border-teal-400">
        <h3 className="font-bold text-lg mb-4 text-teal-900">Data Collection Tools</h3>
        <div className="grid grid-cols-3 gap-4">
          <div className="bg-teal-50 p-4 rounded">
            <div className="font-semibold mb-2">ActivityInfo Template</div>
            <div className="text-sm text-gray-700">
              &#8226; Standard operational data<br/>
              &#8226; RRP coordination data<br/>
              &#8226; Contact lists
            </div>
          </div>
          <div className="bg-teal-50 p-4 rounded">
            <div className="font-semibold mb-2">Exception Handler</div>
            <div className="text-sm text-gray-700">
              &#8226; Political sensitivities<br/>
              &#8226; Incomplete datasets<br/>
              &#8226; Requires caveats
            </div>
          </div>
          <div className="bg-teal-50 p-4 rounded">
            <div className="font-semibold mb-2">Data Validation</div>
            <div className="text-sm text-gray-700">
              &#8226; Human-in-the-loop<br/>
              &#8226; Quality checks<br/>
              &#8226; Approval workflow
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const DocumentFlowDiagram = () => (
    <div className="w-full h-full p-8 bg-gradient-to-br from-amber-50 to-yellow-50">
      <h2 className="text-2xl font-bold mb-6 text-center text-amber-900">Document Repository Migration</h2>
      
      <div className="space-y-6">
        {/* Migration Process */}
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="font-bold text-lg mb-4 text-gray-800">Document Migration Process</h3>
          <div className="grid grid-cols-5 gap-3">
            <div className="bg-blue-50 p-4 rounded text-center">
              <Filter className="w-8 h-8 mx-auto mb-2 text-blue-600" />
              <div className="font-semibold text-sm mb-1">1. Filter</div>
              <div className="text-xs text-gray-600">Apply exclusion criteria</div>
            </div>
            <ArrowRight className="w-6 h-6 mx-auto my-auto text-gray-400" />
            <div className="bg-green-50 p-4 rounded text-center">
              <CheckCircle className="w-8 h-8 mx-auto mb-2 text-green-600" />
              <div className="font-semibold text-sm mb-1">2. AI Process</div>
              <div className="text-xs text-gray-600">Auto-generate metadata</div>
            </div>
            <ArrowRight className="w-6 h-6 mx-auto my-auto text-gray-400" />
            <div className="bg-purple-50 p-4 rounded text-center">
              <RefreshCw className="w-8 h-8 mx-auto mb-2 text-purple-600" />
              <div className="font-semibold text-sm mb-1">3. Review</div>
              <div className="text-xs text-gray-600">Human approval</div>
            </div>
          </div>
        </div>

        {/* Document Filtering */}
        <div className="grid grid-cols-2 gap-6">
          <div className="bg-white rounded-lg shadow-lg p-6 border-2 border-red-400">
            <h3 className="font-bold text-lg mb-4 text-red-900 flex items-center gap-2">
              <XCircle className="w-5 h-5" />
              Exclude from Migration
            </h3>
            <ul className="space-y-2 text-sm text-gray-700">
              <li className="flex items-start gap-2">
                <span className="text-red-500 font-bold">×</span>
                <span>Signpost documents (toilets, directions)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-red-500 font-bold">×</span>
                <span>Document catalogues (link collections)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-red-500 font-bold">×</span>
                <span>Very old documents (case-by-case with operations)</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-red-500 font-bold">×</span>
                <span>Hidden documents without clear history</span>
              </li>
            </ul>
          </div>

          <div className="bg-white rounded-lg shadow-lg p-6 border-2 border-green-400">
            <h3 className="font-bold text-lg mb-4 text-green-900 flex items-center gap-2">
              <CheckCircle className="w-5 h-5" />
              Include in Migration
            </h3>
            <ul className="space-y-2 text-sm text-gray-700">
              <li className="flex items-start gap-2">
                <span className="text-green-500 font-bold">✓</span>
                <span>Operational reports & factsheets</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500 font-bold">✓</span>
                <span>Protection monitoring documents</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500 font-bold">✓</span>
                <span>Inter-agency coordination products</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-green-500 font-bold">✓</span>
                <span>RRP/JRP related documents</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Document Distribution */}
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="font-bold text-lg mb-4 text-gray-800">Document Distribution to Platforms</h3>
          <div className="grid grid-cols-3 gap-4">
            <div className="bg-blue-50 p-4 rounded border-2 border-blue-300">
              <div className="font-semibold text-blue-900 mb-2">NextGen Sites (WS2)</div>
              <ul className="text-xs text-gray-700 space-y-1">
                <li>&#8226; UNHCR-specific documents</li>
                <li>&#8226; Protection reports</li>
                <li>&#8226; Policy papers</li>
                <li>&#8226; Statistical reports</li>
              </ul>
            </div>
            <div className="bg-orange-50 p-4 rounded border-2 border-orange-300">
              <div className="font-semibold text-orange-900 mb-2">Coordination Platform (WS3)</div>
              <ul className="text-xs text-gray-700 space-y-1">
                <li>&#8226; Inter-agency products</li>
                <li>&#8226; Working group documents</li>
                <li>&#8226; 3W/4W reports</li>
                <li>&#8226; Joint assessments</li>
              </ul>
            </div>
            <div className="bg-purple-50 p-4 rounded border-2 border-purple-300">
              <div className="font-semibold text-purple-900 mb-2">Both Platforms</div>
              <ul className="text-xs text-gray-700 space-y-1">
                <li>&#8226; Situation updates</li>
                <li>&#8226; Regional appeals</li>
                <li>&#8226; RRP documents</li>
                <li>&#8226; Factsheets</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const SituationDiagram = () => (
    <div className="w-full h-full p-8 bg-gradient-to-br from-purple-50 to-pink-50">
      <h2 className="text-2xl font-bold mb-6 text-center text-purple-900">Situation Definition & Content Aggregation</h2>
      
      <div className="space-y-6">
        {/* Admin Console */}
        <div className="bg-white rounded-lg shadow-lg p-6 border-2 border-purple-400">
          <div className="flex items-center gap-3 mb-4">
            <Settings className="w-8 h-8 text-purple-600" />
            <h3 className="font-bold text-lg text-gray-800">NextGen Admin Console - Situation Definition</h3>
          </div>
          <div className="grid grid-cols-4 gap-4">
            <div className="bg-purple-50 p-3 rounded">
              <div className="font-semibold text-sm mb-2">Situation Metadata</div>
              <ul className="text-xs text-gray-700 space-y-1">
                <li>&#8226; Name & Description</li>
                <li>&#8226; Start/End Dates</li>
                <li>&#8226; Emergency Status (L2/L3)</li>
                <li>&#8226; Visibility Rules</li>
              </ul>
            </div>
            <div className="bg-blue-50 p-3 rounded">
              <div className="font-semibold text-sm mb-2">Countries Impacted</div>
              <ul className="text-xs text-gray-700 space-y-1">
                <li>&#8226; Origin countries</li>
                <li>&#8226; Transit countries</li>
                <li>&#8226; Arrival/destination</li>
                <li>&#8226; Hosting countries</li>
              </ul>
            </div>
            <div className="bg-green-50 p-3 rounded">
              <div className="font-semibold text-sm mb-2">Population Groups</div>
              <ul className="text-xs text-gray-700 space-y-1">
                <li>&#8226; Refugees</li>
                <li>&#8226; Asylum-seekers</li>
                <li>&#8226; IDPs</li>
                <li>&#8226; Mixed movements</li>
              </ul>
            </div>
            <div className="bg-amber-50 p-3 rounded">
              <div className="font-semibold text-sm mb-2">Categories</div>
              <ul className="text-xs text-gray-700 space-y-1">
                <li>&#8226; RRP/JRP/RMRP</li>
                <li>&#8226; Fundraising</li>
                <li>&#8226; Advocacy</li>
                <li>&#8226; Protracted</li>
              </ul>
            </div>
          </div>
        </div>

        {/* Example Situations */}
        <div className="grid grid-cols-3 gap-4">
          <div className="bg-white rounded-lg shadow-lg p-4 border-l-4 border-red-500">
            <h4 className="font-bold mb-3 text-red-900">Sudan Situation</h4>
            <div className="space-y-2 text-sm">
              <div><strong>Type:</strong> Emergency (L2)</div>
              <div><strong>Countries:</strong> Egypt, Chad, CAR, Ethiopia, South Sudan</div>
              <div><strong>Population:</strong> Refugees, Asylum-seekers</div>
              <div><strong>Category:</strong> RRP, Fundraising</div>
            </div>
          </div>
          
          <div className="bg-white rounded-lg shadow-lg p-4 border-l-4 border-blue-500">
            <h4 className="font-bold mb-3 text-blue-900">Venezuela Situation</h4>
            <div className="space-y-2 text-sm">
              <div><strong>Type:</strong> Regional Response</div>
              <div><strong>Countries:</strong> 17 LAC countries</div>
              <div><strong>Population:</strong> Mixed refugees & migrants</div>
              <div><strong>Category:</strong> RMRP, R4V Platform</div>
            </div>
          </div>
          
          <div className="bg-white rounded-lg shadow-lg p-4 border-l-4 border-purple-500">
            <h4 className="font-bold mb-3 text-purple-900">Route-Based Approach</h4>
            <div className="space-y-2 text-sm">
              <div><strong>Type:</strong> Mixed Movement</div>
              <div><strong>Routes:</strong> Mediterranean, Atlantic</div>
              <div><strong>Population:</strong> Arrivals, Departures, Dead & Missing</div>
              <div><strong>Category:</strong> Protection, DIP</div>
            </div>
          </div>
        </div>

        {/* Content Aggregation */}
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="font-bold text-lg mb-4 text-gray-800">Automated Content Aggregation by Situation</h3>
          <div className="grid grid-cols-4 gap-4">
            <div className="bg-indigo-50 p-4 rounded text-center">
              <div className="font-semibold mb-2">Population Data</div>
              <div className="text-xs text-gray-600">Aggregate by countries + population groups</div>
            </div>
            <div className="bg-green-50 p-4 rounded text-center">
              <div className="font-semibold mb-2">Funding Data</div>
              <div className="text-xs text-gray-600">Pull from Common Data Layer</div>
            </div>
            <div className="bg-amber-50 p-4 rounded text-center">
              <div className="font-semibold mb-2">Documents</div>
              <div className="text-xs text-gray-600">Filter by situation tags</div>
            </div>
            <div className="bg-blue-50 p-4 rounded text-center">
              <div className="font-semibold mb-2">RRP Activities</div>
              <div className="text-xs text-gray-600">Link ActivityInfo data</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="w-full h-screen flex flex-col bg-gray-100">
      {/* Navigation */}
      <div className="bg-indigo-900 text-white p-4 shadow-lg">
        <h1 className="text-2xl font-bold mb-3">ODP to NextGen Sites Migration Architecture</h1>
        <div className="flex gap-2">
          <button
            onClick={() => setActiveView('overview')}
            className={`px-4 py-2 rounded transition-colors ${
              activeView === 'overview'
                ? 'bg-indigo-600 font-semibold'
                : 'bg-indigo-800 hover:bg-indigo-700'
            }`}
          >
            Overview
          </button>
          <button
            onClick={() => setActiveView('dataflow')}
            className={`px-4 py-2 rounded transition-colors ${
              activeView === 'dataflow'
                ? 'bg-indigo-600 font-semibold'
                : 'bg-indigo-800 hover:bg-indigo-700'
            }`}
          >
            Data Flow
          </button>
          <button
            onClick={() => setActiveView('documents')}
            className={`px-4 py-2 rounded transition-colors ${
              activeView === 'documents'
                ? 'bg-indigo-600 font-semibold'
                : 'bg-indigo-800 hover:bg-indigo-700'
            }`}
          >
            Documents
          </button>
          <button
            onClick={() => setActiveView('situations')}
            className={`px-4 py-2 rounded transition-colors ${
              activeView === 'situations'
                ? 'bg-indigo-600 font-semibold'
                : 'bg-indigo-800 hover:bg-indigo-700'
            }`}
          >
            Situations
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        {activeView === 'overview' && <OverviewDiagram />}
        {activeView === 'dataflow' && <DataFlowDiagram />}
        {activeView === 'documents' && <DocumentFlowDiagram />}
        {activeView === 'situations' && <SituationDiagram />}
      </div>

      {/* Footer */}
      <div className="bg-gray-800 text-white p-3 text-center text-sm">
        <p>UNHCR NextGen Data Portals Project - ODP Decomposition Requirements (January 2026)</p>
      </div>
    </div>
  );
};

export default MigrationDiagram;