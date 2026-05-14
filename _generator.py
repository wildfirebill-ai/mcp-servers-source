#!/usr/bin/env python3
"""Generate 100 custom MCP servers - each unique, with skills, ports, Docker, and start/stop scripts."""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

SERVERS = [
    (1, "code-architect", 25000, [
        "Software Architecture Design", "Design Pattern Implementation",
        "Code Structure Refactoring", "Technical Debt Analysis",
        "UML & Architecture Documentation", "API Contract Design",
        "SOLID Principles Application", "Architecture Decision Records"
    ]),
    (2, "python-weaver", 25001, [
        "Python Scripting & Automation", "Async Programming with asyncio",
        "Type Hinting & Pydantic", "Package Management with pip/poetry",
        "Virtual Environment Management", "Testing with pytest",
        "Python Performance Optimization", "Cython & Extensions"
    ]),
    (3, "web-sculptor", 25002, [
        "Full-Stack Web Development", "REST API Integration",
        "Frontend-Backend Architecture", "Web Security Best Practices",
        "Performance Optimization", "Responsive Web Design",
        "Server-Side Rendering", "API Versioning Strategies"
    ]),
    (4, "design-crafter", 25003, [
        "UI/UX Design Principles", "Color Theory & Palettes",
        "Typography Selection", "Layout Composition",
        "Design System Creation", "Prototyping & Wireframing",
        "User Flow Optimization", "Visual Hierarchy Design"
    ]),
    (5, "browser-engineer", 25004, [
        "Browser Extension Development", "DOM Manipulation Mastery",
        "Browser DevTools Expertise", "Cross-Browser Compatibility",
        "Web Performance Optimization", "Browser Storage APIs",
        "Service Worker Architecture", "Web Authentication Flows"
    ]),
    (6, "devops-pilot", 25005, [
        "CI/CD Pipeline Design", "Infrastructure as Code",
        "Container Orchestration", "Monitoring & Alerting",
        "Incident Response Planning", "Environment Management",
        "Release Strategy Design", "SLA & SLO Engineering"
    ]),
    (7, "data-alchemist", 25006, [
        "Data Pipeline Architecture", "ETL Process Design",
        "Data Cleaning & Transformation", "Batch Processing Systems",
        "Stream Processing with Kafka", "Data Warehousing Concepts",
        "OLAP vs OLTP Design", "Data Governance Practices"
    ]),
    (8, "api-builder", 25007, [
        "REST API Design Principles", "GraphQL Schema Design",
        "API Versioning Strategies", "OpenAPI/Swagger Documentation",
        "API Rate Limiting", "Request Validation & Sanitization",
        "API Authentication Methods", "Webhook Implementation"
    ]),
    (9, "css-artisan", 25008, [
        "CSS Selectors Mastery", "Flexbox Layout Design",
        "CSS Grid Architecture", "CSS Animations & Transitions",
        "Responsive Design Breakpoints", "CSS Custom Properties",
        "Preprocessor Expertise (Sass/Less)", "CSS Methodologies (BEM/SMACSS)"
    ]),
    (10, "js-virtuoso", 25009, [
        "JavaScript ES6+ Features", "Closures & Scope Mastery",
        "Event Loop Understanding", "Promise & Async Patterns",
        "Prototypal Inheritance", "Module Systems (ESM/CJS)",
        "Functional Programming in JS", "JavaScript Memory Management"
    ]),
    (11, "ts-master", 25010, [
        "TypeScript Type System", "Generic Types & Utilities",
        "Type Inference Techniques", "Declaration File Creation",
        "Conditional & Mapped Types", "Strict Mode Configuration",
        "TypeScript with React", "Migration from JavaScript"
    ]),
    (12, "react-forger", 25011, [
        "React Component Architecture", "Hooks & Custom Hooks",
        "State Management Patterns", "Server Components",
        "React Suspense & Streaming", "React Performance Optimization",
        "Component Testing with RTL", "Context API & Composition"
    ]),
    (13, "vue-sage", 25012, [
        "Vue 3 Composition API", "Reactivity System Deep Dive",
        "Vue Router & Navigation", "Pinia State Management",
        "Vue Component Design Patterns", "Transition & Animation",
        "Server-Side Rendering with Nuxt", "Vue Ecosystem Integration"
    ]),
    (14, "angular-weaver", 25013, [
        "Angular Module Architecture", "RxJS Observable Patterns",
        "Dependency Injection", "Angular Forms (Template/Reactive)",
        "Angular Routing & Guards", "Change Detection Strategy",
        "Angular Universal SSR", "NgRx State Management"
    ]),
    (15, "node-crafter", 25014, [
        "Node.js Event Loop", "Streams & Buffers",
        "Express/Koa/Fastify Routing", "Middleware Architecture",
        "File System Operations", "Child Process Management",
        "Cluster Mode & Load Balancing", "npm Package Publishing"
    ]),
    (16, "flask-artist", 25015, [
        "Flask Application Design", "Jinja2 Template Mastery",
        "SQLAlchemy ORM Integration", "Flask Extension Ecosystem",
        "Blueprint Module Organization", "REST API with Flask",
        "Flask Authentication Patterns", "Testing Flask Applications"
    ]),
    (17, "django-master", 25016, [
        "Django MTV Architecture", "Django ORM Mastery",
        "Class-Based Views", "Django REST Framework",
        "Authentication & Permissions", "Django Admin Customization",
        "Management Commands", "Django Signals & Tasks"
    ]),
    (18, "fastapi-ace", 25017, [
        "FastAPI Application Design", "Pydantic Model Validation",
        "Async Endpoint Patterns", "OpenAPI Auto-Generation",
        "Dependency Injection System", "WebSocket Support",
        "Background Task Management", "FastAPI Testing Strategies"
    ]),
    (19, "sql-wizard", 25018, [
        "SQL Query Optimization", "Database Schema Design",
        "Indexing Strategies", "Query Plan Analysis",
        "Stored Procedure Development", "Transaction Management",
        "ACID Compliance Understanding", "Database Migration Tools"
    ]),
    (20, "nosql-expert", 25019, [
        "MongoDB Document Design", "Redis Caching Patterns",
        "Cassandra Data Modeling", "Elasticsearch Indexing",
        "DynamoDB Single-Table Design", "CouchDB Replication",
        "Neo4j Graph Modeling", "CosmosDB Partitioning"
    ]),
    (21, "git-guru", 25020, [
        "Git Branching Strategies", "Rebase vs Merge Mastery",
        "Interactive Rebase Techniques", "Git Hooks Automation",
        "Submodule & Subtree Management", "Git Workflow Design",
        "Cherry-Pick & Bisect", "Git LFS Large File Handling"
    ]),
    (22, "docker-maestro", 25021, [
        "Dockerfile Optimization", "Multi-Stage Builds",
        "Docker Compose Architecture", "Container Networking",
        "Volume & Mount Management", "Image Security Scanning",
        "Registry & Tag Management", "Docker Swarm Orchestration"
    ]),
    (23, "kubernetes-captain", 25022, [
        "Pod & Deployment Design", "Service & Ingress Configuration",
        "ConfigMap & Secret Management", "Helm Chart Development",
        "Kubernetes RBAC Security", "Horizontal Pod Autoscaling",
        "Persistent Volume Claims", "Operator Pattern Design"
    ]),
    (24, "ci-cd-engineer", 25023, [
        "GitHub Actions Workflows", "Jenkins Pipeline Design",
        "GitLab CI Configuration", "Azure DevOps Pipelines",
        "ArgoCD GitOps Strategy", "Artifact Management",
        "Environment Promotion", "Rollback Strategy Design"
    ]),
    (25, "test-architect", 25024, [
        "Unit Testing Strategies", "Integration Testing Patterns",
        "End-to-End Testing with Playwright", "Test-Driven Development",
        "Behavior-Driven Development", "Mocking & Stubbing",
        "Code Coverage Optimization", "Performance & Load Testing"
    ]),
    (26, "debug-detectiv", 25025, [
        "Debugging Methodologies", "Stack Trace Analysis",
        "Memory Leak Detection", "Race Condition Identification",
        "Log Analysis Techniques", "Performance Profiling",
        "Network Request Inspection", "Error Boundary Design"
    ]),
    (27, "perf-tuner", 25026, [
        "Performance Audit Methods", "Lighthouse Optimization",
        "Lazy Loading Strategies", "Bundle Size Reduction",
        "Image Optimization Techniques", "Critical CSS Extraction",
        "Caching Strategy Design", "Database Query Optimization"
    ]),
    (28, "security-sentinel", 25027, [
        "OWASP Top 10 Mitigation", "Input Validation & Sanitization",
        "Authentication Security", "Authorization Best Practices",
        "Encryption Implementation", "Secure Session Management",
        "XSS & CSRF Prevention", "Security Headers Configuration"
    ]),
    (29, "auth-guardian", 25028, [
        "OAuth 2.0 Flow Implementation", "OpenID Connect Integration",
        "JWT Token Design & Validation", "Session Management Patterns",
        "Multi-Factor Authentication", "SSO Architecture Design",
        "Password Hashing & Storage", "RBAC & Permission Systems"
    ]),
    (30, "ml-practitioner", 25029, [
        "Scikit-Learn Pipeline Design", "Feature Engineering Methods",
        "Model Evaluation Techniques", "Hyperparameter Tuning",
        "Cross-Validation Strategies", "Ensemble Learning Methods",
        "Dimensionality Reduction", "Model Serialization & Deployment"
    ]),
    (31, "ai-architect", 25030, [
        "LLM Integration Patterns", "RAG Architecture Design",
        "Prompt Engineering Techniques", "Agent Framework Design",
        "Vector Database Selection", "Embedding Model Selection",
        "Fine-Tuning Strategy", "AI Safety & Alignment"
    ]),
    (32, "algorithm-master", 25031, [
        "Sorting & Searching Algorithms", "Graph Algorithm Design",
        "Dynamic Programming Patterns", "Greedy Algorithm Analysis",
        "Divide & Conquer Strategies", "Backtracking Techniques",
        "Time Complexity Analysis", "Space Complexity Optimization"
    ]),
    (33, "data-struct-wiz", 25032, [
        "Array & Linked List Operations", "Tree & Graph Structures",
        "Hash Table Design", "Heap & Priority Queue",
        "Trie & Suffix Array", "Bloom Filter Implementation",
        "LRU Cache Design", "Union-Find & Disjoint Sets"
    ]),
    (34, "regex-ranger", 25033, [
        "Regex Pattern Design", "Lookahead & Lookbehind",
        "Regex Performance Optimization", "Named Capture Groups",
        "Pattern Debugging Techniques", "Regex for Data Extraction",
        "Replacement & Substitution", "Language-Specific Regex Differences"
    ]),
    (35, "cli-commander", 25034, [
        "CLI Application Design", "Argument Parsing Patterns",
        "Command Tree Architecture", "Terminal UI Development",
        "Shell Completion Scripts", "Exit Code Conventions",
        "Pipeline-Friendly Design", "Cross-Platform CLI Considerations"
    ]),
    (36, "graphql-ninja", 25035, [
        "GraphQL Schema Design", "Resolver Architecture",
        "N+1 Query Prevention", "Subscription Implementation",
        "Federation & Gateway Patterns", "Input Validation via GraphQL",
        "GraphQL Security Best Practices", "Apollo & Relay Integration"
    ]),
    (37, "rest-api-pro", 25036, [
        "RESTful Resource Design", "HATEOAS Implementation",
        "HTTP Status Code Usage", "Pagination Strategies",
        "Content Negotiation", "Error Response Formatting",
        "API Deprecation Strategies", "Idempotency & Safe Methods"
    ]),
    (38, "websocket-mage", 25037, [
        "WebSocket Protocol Understanding", "Real-Time Architecture",
        "Connection Lifecycle Management", "Broadcast & Room Patterns",
        "Reconnection Strategies", "WebSocket Security Measures",
        "Scalability with WebSockets", "Fallback to Long-Polling"
    ]),
    (39, "grpc-builder", 25038, [
        "Protocol Buffer Design", "gRPC Service Definition",
        "Unary & Streaming Patterns", "Interceptor Implementation",
        "gRPC Gateway Setup", "Load Balancing with gRPC",
        "Deadline & Cancellation", "gRPC Web Integration"
    ]),
    (40, "microservice-arch", 25039, [
        "Service Decomposition Strategies", "Inter-Service Communication",
        "Event-Driven Architecture", "Saga Pattern Implementation",
        "Service Mesh Integration", "API Gateway Design",
        "Observability in Microservices", "Distributed Tracing"
    ]),
    (41, "queue-master", 25040, [
        "RabbitMQ Exchange Design", "Kafka Topic Architecture",
        "Message Serialization", "Dead Letter Queue Management",
        "Consumer Group Patterns", "At-Least-Once Delivery Guarantees",
        "Backpressure Handling", "Queue Monitoring & Alerting"
    ]),
    (42, "cache-wizard", 25041, [
        "Cache Strategy Design", "Redis Data Structures",
        "CDN Caching Configuration", "HTTP Caching Headers",
        "Cache Invalidation Patterns", "Distributed Caching",
        "Write-Through & Write-Behind", "Cache Warming Strategies"
    ]),
    (43, "search-engineer", 25042, [
        "Elasticsearch Mapping Design", "Full-Text Search Optimization",
        "Query DSL Mastery", "Indexing Strategy Design",
        "Search Relevance Tuning", "Aggregation & Faceting",
        "Autocomplete Implementation", "Search Performance Tuning"
    ]),
    (44, "log-analyst", 25043, [
        "Log Aggregation Architecture", "Log Parsing Patterns",
        "Structured Logging Design", "Log Retention Strategies",
        "Real-Time Log Monitoring", "Log Correlation Techniques",
        "ELK Stack Implementation", "Log-Based Alerting"
    ]),
    (45, "deploy-captain", 25044, [
        "Deployment Strategy Design", "Blue-Green Deployment",
        "Canary Release Patterns", "Rolling Update Management",
        "Feature Flag Implementation", "A/B Testing Infrastructure",
        "Rollback Automation", "Immutable Infrastructure Design"
    ]),
    (46, "cloud-architect", 25045, [
        "Cloud Migration Strategy", "Multi-Cloud Architecture",
        "Cloud Cost Optimization", "Availability Zone Design",
        "Disaster Recovery Planning", "Cloud Security Best Practices",
        "Serverless Architecture Design", "Cloud-Native Application Design"
    ]),
    (47, "aws-specialist", 25046, [
        "AWS Service Selection", "VPC Network Architecture",
        "IAM Policy Design", "Lambda Function Optimization",
        "S3 Storage Strategies", "ECS/EKS Container Orchestration",
        "CloudFormation & CDK", "AWS Well-Architected Framework"
    ]),
    (48, "azure-pro", 25047, [
        "Azure Resource Management", "Azure Active Directory",
        "Azure DevOps Pipelines", "Azure Functions Development",
        "Azure Kubernetes Service", "Azure Storage Solutions",
        "Azure Networking Architecture", "ARM & Bicep Templates"
    ]),
    (49, "gcp-expert", 25048, [
        "GCP Project Organization", "Google Kubernetes Engine",
        "Cloud Run Serverless", "BigQuery Data Analysis",
        "Cloud Storage Design", "VPC Network Configuration",
        "IAM & Service Accounts", "Cloud Function Development"
    ]),
    (50, "terraform-builder", 25049, [
        "Terraform State Management", "Module Design Patterns",
        "Resource Graph Understanding", "Provider Development",
        "Remote State Configuration", "Terraform Workspace Strategy",
        "Policy as Code with Sentinel", "Infrastructure Testing"
    ]),
    (51, "ansible-crafter", 25050, [
        "Ansible Playbook Design", "Role-Based Architecture",
        "Inventory Management", "Jinja2 Template Integration",
        "Ansible Vault Secrets", "Custom Module Development",
        "Idempotent Automation Design", "AWX/Tower Automation"
    ]),
    (52, "vim-master", 25051, [
        "Vim Modal Editing Mastery", "Custom Keybinding Design",
        "Vimscript Plugin Development", "Buffer & Window Management",
        "Macro Recording & Playback", "Vim Configuration Optimization",
        "Plugin Manager Usage (vim-plug)", "Quickfix & Location Lists"
    ]),
    (53, "emacs-sage", 25052, [
        "Emacs Lisp Programming", "Buffer & Major Modes",
        "Org-Mode Mastery", "Package Configuration with use-package",
        "Evil Mode Integration", "Magit Git Interface",
        "Dired File Management", "Emacs Performance Tuning"
    ]),
    (54, "shell-weaver", 25053, [
        "Bash Scripting Mastery", "Zsh Configuration & Themes",
        "POSIX Compliance Understanding", "Command Pipeline Design",
        "Shell Variable Expansion", "Error Handling in Shell Scripts",
        "Shell Built-in Commands", "Cross-Platform Shell Scripting"
    ]),
    (55, "powershell-pro", 25054, [
        "PowerShell Pipeline Design", "Cmdlet Development",
        "PowerShell Remoting", "Desired State Configuration",
        "PowerShell Module Creation", "Error Handling with Try/Catch",
        "PowerShell Workflows", "Active Directory Automation"
    ]),
    (56, "network-engineer", 25055, [
        "TCP/IP Protocol Understanding", "DNS Configuration & Troubleshooting",
        "HTTP/2 & HTTP/3 Protocols", "Load Balancer Configuration",
        "Firewall Rule Design", "Subnet & CIDR Planning",
        "SSL/TLS Certificate Management", "Network Performance Monitoring"
    ]),
    (57, "encoding-expert", 25056, [
        "Base64 Encoding/Decoding", "URL Encoding Best Practices",
        "JSON Serialization Patterns", "XML Parsing Techniques",
        "CSV File Processing", "Binary Data Handling",
        "Character Encoding (UTF-8/ASCII)", "MessagePack & Protocol Buffers"
    ]),
    (58, "compression-wiz", 25057, [
        "Gzip & Deflate Algorithms", "Image Compression Methods",
        "Lossless vs Lossy Compression", "Video Codec Understanding",
        "Archive Format Design (ZIP/TAR)", "Compression Ratio Optimization",
        "Stream Compression Patterns", "Content-Encoding Negotiation"
    ]),
    (59, "image-processor", 25058, [
        "Image Filtering Techniques", "Color Space Conversion",
        "Image Resize & Crop Algorithms", "Exif Data Handling",
        "Image Format Conversion", "Batch Processing Pipelines",
        "Face Detection Integration", "OCR Text Extraction"
    ]),
    (60, "animation-crafter", 25059, [
        "CSS Animation Keyframes", "JavaScript Animation Libraries",
        "Timing Function Design", "Performance-Conscious Animations",
        "SVG Animation Techniques", "Canvas Animation Loop",
        "Scroll-Triggered Animations", "Web Animation API"
    ]),
    (61, "game-dev-builder", 25060, [
        "Game Loop Architecture", "Sprite Management",
        "Collision Detection Algorithms", "State Machine Design",
        "Asset Pipeline Management", "Input Handling Systems",
        "Tile Map Design", "Game Performance Optimization"
    ]),
    (62, "mobile-dev-artist", 25061, [
        "Responsive Mobile Layouts", "Touch Gesture Handling",
        "Mobile-First Design Principles", "App Shell Architecture",
        "Offline-First Strategies", "Push Notification Implementation",
        "Mobile Performance Optimization", "Cross-Platform Development"
    ]),
    (63, "responsive-master", 25062, [
        "Mobile-First CSS Design", "Media Query Mastery",
        "Fluid Typography Systems", "Container Query Usage",
        "Viewport Unit Strategies", "Responsive Image Handling",
        "Breakpoint Planning", "Device Testing Methodologies"
    ]),
    (64, "a11y-advocate", 25063, [
        "WCAG 2.1 Compliance Check", "Screen Reader Optimization",
        "Keyboard Navigation Design", "ARIA Attribute Mastery",
        "Color Contrast Validation", "Focus Management Patterns",
        "Semantic HTML Structure", "Accessible Form Design"
    ]),
    (65, "seo-specialist", 25064, [
        "On-Page SEO Optimization", "Technical SEO Auditing",
        "Structured Data Markup (Schema.org)", "Meta Tag Optimization",
        "Sitemap Generation & Management", "Robots.txt Configuration",
        "Core Web Vitals Optimization", "Canonical URL Management"
    ]),
    (66, "analytics-guru", 25065, [
        "Google Analytics 4 Setup", "Event Tracking Design",
        "Conversion Funnel Analysis", "Custom Dashboard Creation",
        "A/B Testing Implementation", "User Segmentation Strategies",
        "Data Privacy Compliance", "Attribution Model Design"
    ]),
    (67, "i18n-master", 25066, [
        "Internationalization Architecture", "Locale File Management",
        "Pluralization Rules Handling", "RTL Layout Support",
        "Date/Time Formatting Patterns", "Number & Currency Formatting",
        "Translation Workflow Design", "i18n Library Integration"
    ]),
    (68, "l10n-expert", 25067, [
        "Localization Workflow Design", "Translation Memory Management",
        "Cultural Adaptation Strategies", "Localization Testing Methods",
        "Pseudo-Localization Techniques", "Content Management for L10n",
        "Regional Format Compliance", "Language Fallback Strategies"
    ]),
    (69, "component-designer", 25068, [
        "Component API Design", "Props Interface Definition",
        "Composition vs Inheritance", "Stateful vs Stateless Components",
        "Component Testing Patterns", "Reusable Component Libraries",
        "Compound Component Pattern", "Render Props & HOCs"
    ]),
    (70, "design-system-arch", 25069, [
        "Design Token Architecture", "Theme System Design",
        "Component Library Organization", "Documentation with Storybook",
        "Visual Regression Testing", "Design System Versioning",
        "Cross-Framework Components", "Accessibility in Design Systems"
    ]),
    (71, "color-theorist", 25070, [
        "Color Wheel & Harmony", "Accessible Color Palette Creation",
        "Color Psychology Understanding", "Brand Color System Design",
        "Dark Mode Color Design", "Gradient & Color Effect Design",
        "Color Contrast Calculations", "Color Naming & Organization"
    ]),
    (72, "typography-master", 25071, [
        "Font Selection Principles", "Type Scale Establishment",
        "Line Height & Spacing Design", "Web Font Loading Optimization",
        "Variable Font Configuration", "Kerning & Tracking Adjustment",
        "Responsive Typography Design", "Font Pairing Techniques"
    ]),
    (73, "layout-artist", 25072, [
        "Page Layout Architecture", "Flexbox Layout Mastery",
        "CSS Grid Template Design", "Multi-Column Layout Patterns",
        "Positioning & Z-Index Management", "Overflow & Scroll Patterns",
        "Aspect Ratio Box Model", "Logical Properties & Values"
    ]),
    (74, "svg-artist", 25073, [
        "SVG Path Command Mastery", "Scalable Icon Design",
        "SVG Animation with SMIL", "SVG Filter Effects",
        "Responsive SVG Techniques", "Inline SVG Optimization",
        "SVG Accessibility Practices", "SVG Sprite Systems"
    ]),
    (75, "canvas-wizard", 25074, [
        "Canvas 2D Rendering", "Pixel Manipulation Techniques",
        "Canvas Animation Loop", "Coordinate System Mastery",
        "Canvas Image Processing", "OffscreenCanvas Usage",
        "High-DPI Canvas Rendering", "Canvas Performance Optimization"
    ]),
    (76, "webgl-builder", 25075, [
        "WebGL Shader Programming", "3D Scene Construction",
        "Texture Mapping Techniques", "Lighting & Material Models",
        "Three.js Integration", "WebGL Performance Optimization",
        "GLSL Vertex & Fragment Shaders", "GPU Memory Management"
    ]),
    (77, "wasm-specialist", 25076, [
        "WebAssembly Module Design", "Rust-to-WASM Compilation",
        "C/C++ Emscripten Integration", "WASI System Interface",
        "JS-WASM Interop Patterns", "Memory Management in WASM",
        "WebAssembly Performance Tuning", "WAT Text Format Understanding"
    ]),
    (78, "pwa-architect", 25077, [
        "Service Worker Lifecycle", "Cache Storage Strategies",
        "Offline Experience Design", "Web App Manifest Configuration",
        "Background Sync Patterns", "Push Notification Architecture",
        "App Shell Model Implementation", "PWA Installation Flow"
    ]),
    (79, "meta-tag-master", 25078, [
        "Open Graph Protocol Implementation", "Twitter Card Design",
        "Meta Description Optimization", "Viewport Meta Configuration",
        "Social Media Preview Design", "Canonical Tag Management",
        "Refresh & Redirect Meta Tags", "Theme-Color & Meta Theme"
    ]),
    (80, "html-craftsman", 25079, [
        "Semantic HTML Structure", "Form Design & Validation",
        "Table Accessibility Mastery", "Embedded Content Management",
        "HTML5 API Integration", "Template & Slot Elements",
        "Custom Data Attributes", "Progressive Enhancement Patterns"
    ]),
    (81, "http-protocol-pro", 25080, [
        "HTTP Request/Response Lifecycle", "Status Code Best Practices",
        "Header Configuration Guide", "CORS Policy Design",
        "Cookie Management Strategies", "HTTP Caching Directives",
        "Content-Type Negotiation", "HTTP Security Headers"
    ]),
    (82, "json-validator", 25081, [
        "JSON Schema Design", "JSON Path Query Mastery",
        "JSON Parsing Performance", "Nested JSON Handling",
        "JSON Patch Operations", "JSON Merge Patch Patterns",
        "Circular Reference Detection", "Streaming JSON Processing"
    ]),
    (83, "yaml-tamer", 25082, [
        "YAML Structure Design", "Multi-Document YAML",
        "Anchor & Alias Mastery", "YAML Schema Validation",
        "YAML vs JSON Conversion", "Complex Nested Configurations",
        "YAML Security Best Practices", "YAML Merge Keys"
    ]),
    (84, "markdown-scribe", 25083, [
        "Markdown Extended Syntax", "Documentation Structure Design",
        "Code Block Formatting", "Table & List Organization",
        "Link & Image Management", "Front Matter Configuration",
        "Mermaid Diagram Integration", "Documentation Versioning"
    ]),
    (85, "openapi-designer", 25084, [
        "OpenAPI 3.1 Specification", "Endpoint Path Design",
        "Request/Response Schema Design", "Security Scheme Configuration",
        "API Documentation Generation", "Mock Server Implementation",
        "API Client Code Generation", "OpenAPI Validation Tools"
    ]),
    (86, "proto-compiler", 25085, [
        "Protocol Buffer Schema Design", "Message Type Definition",
        "Service Definition Patterns", "Proto File Organization",
        "Backward Compatibility Strategies", "Custom Options & Extensions",
        "Multi-Language Code Generation", "Proto Linting & Validation"
    ]),
    (87, "code-formatter", 25086, [
        "Prettier Configuration Mastery", "ESLint Rule Design",
        "EditorConfig Standardization", "Language-Specific Formatters",
        "Format-on-Save Workflow", "Style Guide Enforcement",
        "Husky & Lint-Staged Setup", "Custom Formatter Development"
    ]),
    (88, "static-site-gen", 25087, [
        "Static Site Architecture", "SSG vs SSR Trade-offs",
        "Markdown-to-HTML Pipeline", "Asset Pipeline Management",
        "Incremental Static Regeneration", "Headless CMS Integration",
        "Static Site Deployment", "Build Performance Optimization"
    ]),
    (89, "jamstack-dev", 25088, [
        "JAMstack Architecture Design", "Pre-rendering Strategies",
        "Serverless Function Development", "API Integration Patterns",
        "Headless CMS Selection", "CDN Deployment Strategy",
        "Atomic Deployments", "Edge Function Implementation"
    ]),
    (90, "cdn-specialist", 25089, [
        "CDN Configuration Design", "Edge Caching Strategies",
        "Purge & Invalidation Methods", "Origin Shield Architecture",
        "CDN Security Features (WAF)", "Geo-Routing Configuration",
        "Custom Domain SSL Setup", "CDN Performance Monitoring"
    ]),
    (91, "webhook-builder", 25090, [
        "Webhook Payload Design", "Delivery Retry Strategies",
        "Webhook Signature Verification", "Event Subscription Management",
        "Idempotent Webhook Handling", "Rate Limiting Webhooks",
        "Webhook Monitoring & Logging", "Consumer SDK Generation"
    ]),
    (92, "sse-crafter", 25091, [
        "Server-Sent Events Protocol", "Event Stream Format Design",
        "Reconnection Logic Implementation", "Event ID Tracking",
        "SSE vs WebSocket Comparison", "Auto-Retry Headers",
        "Polyfill for Older Browsers", "SSE Scalability Patterns"
    ]),
    (93, "oauth-guardian", 25092, [
        "OAuth 2.0 Authorization Flows", "Authorization Code + PKCE",
        "Client Credentials Grant", "Refresh Token Rotation",
        "Token Revocation Strategies", "OpenID Connect Discovery",
        "Scopes & Consent Design", "OAuth Security Best Practices"
    ]),
    (94, "jwt-master", 25093, [
        "JWT Structure & Claims", "Token Signing Algorithms",
        "JWT Verification Pipeline", "Key Rotation Strategies",
        "JWT Expiration & Refresh", "Payload Best Practices",
        "Stateless Session Design", "JWT Security Vulnerabilities"
    ]),
    (95, "rate-limiter", 25094, [
        "Rate Limiting Algorithm Design", "Token Bucket Implementation",
        "Sliding Window Patterns", "Leaky Bucket Algorithm",
        "Distributed Rate Limiting", "Rate Limit Header Format",
        "Backoff Strategy Design", "Rate Limit Monitoring"
    ]),
    (96, "proxy-engineer", 25095, [
        "Reverse Proxy Architecture", "Nginx Configuration Mastery",
        "HAProxy Load Balancing", "Proxy Protocol Handling",
        "SSL Termination Configuration", "Request Rewriting Rules",
        "Proxy Cache Configuration", "WebSocket Proxy Support"
    ]),
    (97, "load-balancer", 25096, [
        "Load Balancing Algorithms", "Health Check Design",
        "Session Persistence Strategies", "Weighted Distribution",
        "Geographic Load Balancing", "Circuit Breaker Pattern",
        "Failover Configuration", "Traffic Splitting Techniques"
    ]),
    (98, "db-migrator", 25097, [
        "Schema Migration Strategy", "Alembic & Flyway Configuration",
        "Rollback Planning & Execution", "Data Migration Patterns",
        "Zero-Downtime Migration", "Version-Controlled Schemas",
        "Seed Data Management", "Migration Testing Strategies"
    ]),
    (99, "seed-data-pro", 25098, [
        "Test Data Generation Patterns", "Realistic Dataset Creation",
        "Database Seeding Workflows", "Factory Pattern for Data",
        "Anonymous Data Generation", "Relationship Graph Seeding",
        "Large-Scale Data Generation", "Environment-Specific Seeds"
    ]),
    (100, "fullstack-dev", 25099, [
        "Frontend-Backend Integration", "API Client Generation",
        "State Synchronization Patterns", "Authentication Flow Design",
        "Data Validation Architecture", "Full-Stack Testing Strategy",
        "Build & Bundle Configuration", "Dev Environment Setup"
    ]),
]

# ── Template ──────────────────────────────────────────────────────────

DOCKERFILE = """\
FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py skills.md ./
COPY data ./data
EXPOSE {port}
CMD ["python", "server.py"]
"""

REQUIREMENTS_TXT = "mcp>=1.0.0,<2.0.0\n"

START_BAT = """\
@echo off
cd /d "%~dp0"
start /B python server.py > NUL 2>&1
echo {name} started on port {port}
"""

STOP_BAT = """\
@echo off
set "port={port}"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c":%%port%% "') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo {name} on port {port} stopped.
"""

COMPOSE_YML = """\
services:
  {name}:
    build: .
    ports:
      - "{port}:{port}"
    environment:
      - MCP_PORT={port}
    volumes:
      - ./data:/app/data
    restart: unless-stopped
"""

SKILLS_MD = """\
# {title}

## Skills

{skills}
"""

SERVER_PY = """\
#!/usr/bin/env python3
\"\"\"{name} MCP Server — port {port}\"\"\"

import base64 as _b64
import datetime
import functools
import hashlib
import json
import logging
import os
import random
import string
import subprocess
import uuid as _uuid
from pathlib import Path

from mcp.server.fastmcp import FastMCP

SERVER_NAME = "{name}"
PORT = {port}
HOST = "0.0.0.0"

LOG_DIR = Path(__file__).parent / "data"
LOG_DIR.mkdir(parents=True, exist_ok=True)

_log_fh = logging.FileHandler(LOG_DIR / "server.log", encoding="utf-8", mode="a")
_log_fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
_log_sh = logging.StreamHandler()
_log_sh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(_log_fh)
root.addHandler(_log_sh)

logger = logging.getLogger(SERVER_NAME)
logger.info("Server starting — %s:%s", SERVER_NAME, PORT)


def _log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("TOOL %s args=%s", func.__name__, kwargs)
        try:
            result = func(*args, **kwargs)
            logger.info("TOOK %s OK", func.__name__)
            return result
        except Exception as e:
            logger.error("TOOL %s FAILED: %s", func.__name__, e)
            raise
    return wrapper


mcp = FastMCP(SERVER_NAME, host=HOST, port=PORT)


def _load_skills() -> str:
    p = Path(__file__).parent / "skills.md"
    return p.read_text() if p.exists() else "Skills file not found."

MEMORY_FILE = Path(__file__).parent / "data" / "memory.json"


def _read_memory() -> dict:
    if MEMORY_FILE.exists():
        try:
            return json.loads(MEMORY_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {{}}


def _write_memory(data: dict) -> None:
    MEMORY_FILE.write_text(json.dumps(data, indent=2))


@mcp.tool()
@_log_call
def ping() -> str:
    \"\"\"Health check.\"\"\"
    return "pong"


@mcp.tool()
@_log_call
def echo(text: str) -> str:
    \"\"\"Echo back the input text.\"\"\"
    return text


@mcp.tool()
@_log_call
def get_skills() -> str:
    \"\"\"Return the skills defined for this server.\"\"\"
    return _load_skills()


@mcp.tool()
@_log_call
def get_server_info() -> str:
    \"\"\"Return metadata about this server.\"\"\"
    return json.dumps({{
        "name": SERVER_NAME,
        "port": PORT,
        "host": HOST,
        "protocol": "MCP (Model Context Protocol)",
        "transport": "SSE"
    }}, indent=2)


@mcp.tool()
@_log_call
def read_file(path: str) -> str:
    \"\"\"Read a file from the filesystem.\"\"\"
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception as e:
        return f"Error: {{e}}"


@mcp.tool()
@_log_call
def write_file(path: str, content: str) -> str:
    \"\"\"Write content to a file (creates parent dirs).\"\"\"
    try:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return f"Wrote {{len(content)}} bytes to {{path}}"
    except Exception as e:
        return f"Error: {{e}}"


@mcp.tool()
@_log_call
def list_files(path: str = ".") -> str:
    \"\"\"List directory contents.\"\"\"
    try:
        p = Path(path)
        if not p.exists():
            return f"Path not found: {{path}}"
        items = []
        for e in sorted(p.iterdir()):
            kind = "<DIR>" if e.is_dir() else "<FILE>"
            items.append(f"{{kind}} {{e.name}}")
        return "\\n".join(items) if items else "(empty)"
    except Exception as e:
        return f"Error: {{e}}"


@mcp.tool()
@_log_call
def execute_command(command: str) -> str:
    \"\"\"Execute a shell command (30 s timeout).\"\"\"
    try:
        r = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )
        out = r.stdout or ""
        err = r.stderr or ""
        if r.returncode != 0:
            return f"exit {{r.returncode}}\\n{{err}}\\n{{out}}"
        return out or "(done)"
    except subprocess.TimeoutExpired:
        return "Error: command timed out"
    except Exception as e:
        return f"Error: {{e}}"


@mcp.tool()
@_log_call
def analyze_code(code: str, language: str = "python") -> str:
    \"\"\"Basic code statistics.\"\"\"
    lines = code.splitlines()
    non_empty = [l for l in lines if l.strip()]
    return json.dumps({{
        "language": language,
        "total_lines": len(lines),
        "non_empty_lines": len(non_empty),
        "characters": len(code),
        "words": len(code.split()),
    }}, indent=2)


@mcp.tool()
@_log_call
def validate_json(text: str) -> str:
    \"\"\"Check whether a string is valid JSON.\"\"\"
    try:
        obj = json.loads(text)
        return f"Valid JSON — {{type(obj).__name__}}"
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {{e}}"


@mcp.tool()
@_log_call
def encode_base64(text: str) -> str:
    \"\"\"Encode text to base64.\"\"\"
    return _b64.b64encode(text.encode()).decode()


@mcp.tool()
@_log_call
def decode_base64(encoded: str) -> str:
    \"\"\"Decode base64 to text.\"\"\"
    try:
        return _b64.b64decode(encoded).decode()
    except Exception as e:
        return f"Error: {{e}}"


@mcp.tool()
@_log_call
def get_time() -> str:
    \"\"\"Return current UTC timestamp.\"\"\"
    return datetime.datetime.now(datetime.UTC).isoformat()


@mcp.tool()
@_log_call
def generate_uuid() -> str:
    \"\"\"Generate a random UUID.\"\"\"
    return str(_uuid.uuid4())


@mcp.tool()
@_log_call
def count_words(text: str) -> int:
    \"\"\"Return word count.\"\"\"
    return len(text.split())


@mcp.tool()
@_log_call
def calculate(expression: str) -> str:
    \"\"\"Evaluate a mathematical expression (digits + - * / ( ) . only).\"\"\"
    allowed = set("0123456789+-*/.() ")
    if not all(c in allowed for c in expression):
        return "Error: invalid characters"
    try:
        return str(eval(expression, {{"__builtins__": {{}}}}, {{}}))
    except Exception as e:
        return f"Error: {{e}}"


@mcp.tool()
@_log_call
def hash_text(text: str, algorithm: str = "sha256") -> str:
    \"\"\"Hash text (md5, sha1, sha256, sha512).\"\"\"
    alg = algorithm.lower()
    h = hashlib.new(alg, text.encode())
    return h.hexdigest()


@mcp.tool()
@_log_call
def generate_password(length: int = 16) -> str:
    \"\"\"Generate a secure random password.\"\"\"
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.SystemRandom().choice(chars) for _ in range(length))


@mcp.tool()
@_log_call
def search_files(pattern: str, path: str = ".") -> str:
    \"\"\"Recursively search for a pattern in text files.\"\"\"
    try:
        root = Path(path)
        matches = []
        for f in root.rglob("*"):
            if f.is_file():
                try:
                    if pattern in f.read_text(encoding="utf-8", errors="ignore"):
                        matches.append(str(f))
                except Exception:
                    pass
        return "\\n".join(matches) if matches else "No matches"
    except Exception as e:
        return f"Error: {{e}}"


@mcp.tool()
@_log_call
def random_number(min_val: int = 0, max_val: int = 100) -> int:
    \"\"\"Return a random integer in [min_val, max_val].\"\"\"
    return random.randint(min_val, max_val)


@mcp.tool()
@_log_call
def format_json(text: str) -> str:
    \"\"\"Pretty-print JSON text.\"\"\"
    try:
        obj = json.loads(text)
        return json.dumps(obj, indent=2)
    except Exception as e:
        return f"Error: {{e}}"


# ── Memory (persistent key-value storage) ────────────────────────────

@mcp.tool()
@_log_call
def memory_set(key: str, value: str) -> str:
    \"\"\"Store a value in persistent memory.\"\"\"
    data = _read_memory()
    data[key] = value
    _write_memory(data)
    return f"Stored key '{{key}}' ({{len(value)}} chars)"


@mcp.tool()
@_log_call
def memory_get(key: str) -> str:
    \"\"\"Retrieve a value from persistent memory.\"\"\"
    data = _read_memory()
    if key not in data:
        return f"Key '{{key}}' not found"
    val = data[key]
    return val if isinstance(val, str) else json.dumps(val)


@mcp.tool()
@_log_call
def memory_delete(key: str) -> str:
    \"\"\"Delete a key from persistent memory.\"\"\"
    data = _read_memory()
    if key not in data:
        return f"Key '{{key}}' not found"
    del data[key]
    _write_memory(data)
    return f"Deleted key '{{key}}'"


@mcp.tool()
@_log_call
def memory_list() -> str:
    \"\"\"List all keys in persistent memory.\"\"\"
    data = _read_memory()
    if not data:
        return "(memory is empty)"
    keys = "\\n".join(f"- {{k}}" for k in data)
    return f"Memory keys ({{len(data)}}):\\n{{keys}}"


@mcp.tool()
@_log_call
def memory_clear() -> str:
    \"\"\"Clear all data from persistent memory.\"\"\"
    _write_memory({{}})
    return "Memory cleared"


@mcp.tool()
@_log_call
def memory_stats() -> str:
    \"\"\"Show memory usage statistics.\"\"\"
    data = _read_memory()
    total_chars = sum(len(v) if isinstance(v, str) else len(json.dumps(v)) for v in data.values())
    return json.dumps({{
        "total_keys": len(data),
        "total_chars": total_chars,
        "file_size_bytes": MEMORY_FILE.stat().st_size if MEMORY_FILE.exists() else 0,
    }}, indent=2)


if __name__ == "__main__":
    mcp.run(transport="sse")
"""


def main():
    for num, name, port, skills in SERVERS:
        folder = os.path.join(BASE, f"{num:03d}-{name}")
        os.makedirs(folder, exist_ok=True)

        # skills.md
        bullet_skills = "\n".join(f"- {s}" for s in skills)
        title = name.replace("-", " ").title()
        skills_content = SKILLS_MD.format(title=title, skills=bullet_skills)
        with open(os.path.join(folder, "skills.md"), "w", encoding="utf-8") as f:
            f.write(skills_content)

        # server.py
        server_content = SERVER_PY.format(name=name, port=port)
        with open(os.path.join(folder, "server.py"), "w", encoding="utf-8") as f:
            f.write(server_content)

        # Dockerfile
        docker_content = DOCKERFILE.format(port=port)
        with open(os.path.join(folder, "Dockerfile"), "w", encoding="utf-8") as f:
            f.write(docker_content)

        # requirements.txt  (identical for every server)
        with open(os.path.join(folder, "requirements.txt"), "w", encoding="utf-8") as f:
            f.write(REQUIREMENTS_TXT)

        # start.bat
        start_content = START_BAT.format(name=name, port=port)
        with open(os.path.join(folder, "start.bat"), "w", encoding="utf-8") as f:
            f.write(start_content)

        # stop.bat
        stop_content = STOP_BAT.format(name=name, port=port)
        with open(os.path.join(folder, "stop.bat"), "w", encoding="utf-8") as f:
            f.write(stop_content)

        # data/memory.json (persistent store, bind-mount friendly)
        data_dir = os.path.join(folder, "data")
        os.makedirs(data_dir, exist_ok=True)
        with open(os.path.join(data_dir, "memory.json"), "w", encoding="utf-8") as f:
            f.write("{}\n")

        # docker-compose.yml (per-server)
        compose_content = COMPOSE_YML.format(name=name, port=port)
        with open(os.path.join(folder, "docker-compose.yml"), "w", encoding="utf-8") as f:
            f.write(compose_content)

        print(f"  [{num:3d}] {name:<25s}  port {port}")

    # ── root-level files ───────────────────────────────────────────────

    # docker-compose.yml
    compose_lines = [
        'services:',
    ]
    for num, name, port, _ in SERVERS:
        compose_lines.append(f'  {name}:')
        compose_lines.append(f'    build: ./{num:03d}-{name}')
        compose_lines.append(f'    ports:')
        compose_lines.append(f'      - "{port}:{port}"')
        compose_lines.append(f'    environment:')
        compose_lines.append(f'      - MCP_PORT={port}')
        compose_lines.append(f'    restart: unless-stopped')

    with open(os.path.join(BASE, "docker-compose.yml"), "w", encoding="utf-8") as f:
        f.write("\n".join(compose_lines) + "\n")

    # root requirements.txt
    with open(os.path.join(BASE, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write(REQUIREMENTS_TXT)

    # root start-all.bat
    start_all = ["@echo off"]
    for num, name, port, _ in SERVERS:
        start_all.append(f'start /B python "{BASE}\\{num:03d}-{name}\\server.py" > NUL 2>&1')
    start_all.append("echo All 100 servers started.")
    with open(os.path.join(BASE, "start-all.bat"), "w", encoding="utf-8") as f:
        f.write("\n".join(start_all) + "\n")

    # root stop-all.bat
    stop_all = ["@echo off"]
    for _, name, port, _ in SERVERS:
        stop_all.append(
            f'for /f "tokens=5" %%a in (\'netstat -ano ^| findstr /c":{port} "\') do ('
        )
        stop_all.append("    taskkill /F /PID %%a >nul 2>&1")
        stop_all.append(")")
    stop_all.append("echo All 100 servers stopped.")
    with open(os.path.join(BASE, "stop-all.bat"), "w", encoding="utf-8") as f:
        f.write("\n".join(stop_all) + "\n")

    print(f"\nDone — {len(SERVERS)} servers generated.")


if __name__ == "__main__":
    main()
