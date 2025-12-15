# Firebase Prototype Deployment Plan
## Generative AI Portal - Stakeholder Preview Version

**Version:** 1.0
**Date:** December 15, 2024
**Status:** Ready for Stakeholder Review
**Estimated Deployment Time:** 2-3 weeks

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Prototype Scope & Objectives](#2-prototype-scope--objectives)
3. [Firebase Architecture Overview](#3-firebase-architecture-overview)
4. [Prototype Features](#4-prototype-features)
5. [Technology Stack](#5-technology-stack)
6. [Firebase Services Configuration](#6-firebase-services-configuration)
7. [Step-by-Step Deployment Guide](#7-step-by-step-deployment-guide)
8. [Security & Access Control](#8-security--access-control)
9. [Testing & Validation Plan](#9-testing--validation-plan)
10. [Stakeholder Demo Environment](#10-stakeholder-demo-environment)
11. [Cost Estimation](#11-cost-estimation)
12. [Migration Path to Production](#12-migration-path-to-production)
13. [Timeline & Milestones](#13-timeline--milestones)
14. [Risk Mitigation](#14-risk-mitigation)
15. [Approval Checklist](#15-approval-checklist)

---

## 1. Executive Summary

### Purpose
This document outlines the complete plan for deploying a **functional prototype** of the Generative AI Portal on Firebase. This prototype will enable stakeholders to interact with the core features, evaluate the user experience, and approve the solution before full-scale production deployment.

### Why Firebase for Prototype?
- **Rapid Deployment**: Get a working demo live in days, not months
- **Zero Infrastructure Management**: No servers to configure or maintain
- **Built-in Security**: Authentication, hosting, and API security out-of-the-box
- **Cost-Effective**: Pay only for actual usage; free tier covers most prototype needs
- **Easy Stakeholder Access**: Simple URLs, no VPN or complex setup required
- **Seamless Migration**: Can migrate to production environment (Azure, AWS, or on-premise) later

### What Stakeholders Will Experience
A fully functional web application where they can:
- Log in using email authentication
- Browse the AI tool catalog
- Interact with AI models (OpenAI GPT-4, Claude)
- View their chat history
- Experience the UI/UX of the final product
- Test on any device (desktop, tablet, mobile)

### Success Criteria for Prototype
✅ Stakeholders can access the portal via a public URL
✅ Authentication works smoothly
✅ At least 2 AI models are functional (GPT-4 and Claude)
✅ UI is responsive and intuitive
✅ Response time < 5 seconds for typical queries
✅ All demo scenarios work without errors

---

## 2. Prototype Scope & Objectives

### What's INCLUDED in the Prototype

#### Core Features (MVP)
1. **User Authentication**
   - Email/password login
   - Google Sign-In (optional)
   - Password reset functionality
   - User profile management

2. **AI Tool Catalog**
   - Display 3-5 AI tools with descriptions
   - Tool categorization (Text, Code, Research)
   - Visual cards with capability badges

3. **Chat Interface**
   - Clean, modern chat UI
   - Support for GPT-4 and Claude models
   - Real-time streaming responses
   - Conversation history (last 10 chats)

4. **Basic Governance**
   - Content filtering for sensitive keywords
   - Usage logging (who used what, when)
   - Simple rate limiting (10 requests/minute per user)

5. **Responsive Design**
   - Works on desktop, tablet, mobile
   - Dark/light mode toggle
   - Accessible UI components

### What's EXCLUDED from Prototype (Production Features)

The following will be implemented after stakeholder approval:
- ❌ SSO/SAML integration with corporate directory
- ❌ Role-based access control (RBAC) with complex permissions
- ❌ Advanced analytics dashboard
- ❌ Multi-language support
- ❌ Learning hub with training materials
- ❌ Sandbox environment for testing
- ❌ Advanced governance (AI bias detection, compliance reporting)
- ❌ Integration with 10+ AI models
- ❌ Custom model fine-tuning
- ❌ Data export/import functionality

### Objectives of the Prototype

| Objective | Success Metric |
|-----------|----------------|
| Validate user experience | 80%+ stakeholder satisfaction score |
| Prove technical feasibility | Zero critical bugs during demo |
| Demonstrate AI integration | 95%+ successful AI responses |
| Confirm UI/UX design | Positive feedback on usability |
| Establish baseline performance | < 3 second page load, < 5 second AI response |

---

## 3. Firebase Architecture Overview

### High-Level System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        STAKEHOLDER DEVICES                       │
│              (Desktop, Tablet, Mobile Browsers)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FIREBASE HOSTING                             │
│                  (Static Website Delivery)                       │
│            https://genai-portal.web.app                          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
┌───────────────────────────┐   ┌─────────────────────────┐
│   FIREBASE AUTHENTICATION │   │  FIREBASE FIRESTORE     │
│   - Email/Password        │   │  - User profiles        │
│   - Google Sign-In        │   │  - Chat history         │
│   - Session management    │   │  - Usage logs           │
└───────────┬───────────────┘   └─────────┬───────────────┘
            │                              │
            └──────────────┬───────────────┘
                           ▼
            ┌──────────────────────────────┐
            │   FIREBASE CLOUD FUNCTIONS    │
            │   (Backend API Logic)         │
            │                               │
            │   • generate_response()       │
            │   • validate_content()        │
            │   • log_usage()               │
            │   • get_chat_history()        │
            └──────────────┬────────────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
┌─────────────────────┐       ┌─────────────────────┐
│   OPENAI API        │       │   ANTHROPIC API     │
│   (GPT-4, GPT-3.5)  │       │   (Claude models)   │
└─────────────────────┘       └─────────────────────┘
```

### Firebase Services Utilized

| Service | Purpose | Prototype Usage |
|---------|---------|-----------------|
| **Firebase Hosting** | Serves the React frontend | Host the web application |
| **Firebase Authentication** | User identity management | Email/password + Google login |
| **Cloud Firestore** | NoSQL database | Store user data, chat history, logs |
| **Cloud Functions** | Serverless backend APIs | Proxy to OpenAI/Anthropic, business logic |
| **Firebase Security Rules** | Database access control | Protect user data |
| **Firebase Performance Monitoring** | Track app performance | Monitor load times, API latency |
| **Firebase Analytics** | Usage tracking | Track user interactions (optional) |

---

## 4. Prototype Features

### 4.1 User Authentication Flow

**What Users Will Experience:**

1. **Landing Page**
   - Clean hero section with "Sign In" / "Sign Up" buttons
   - Brief description of the portal
   - Trust indicators (security badges, privacy statement)

2. **Sign Up Process**
   ```
   Step 1: Enter email and password
   Step 2: Email verification sent
   Step 3: Click verification link
   Step 4: Profile setup (name, department)
   Step 5: Redirect to dashboard
   ```

3. **Sign In Process**
   ```
   Step 1: Enter credentials
   Step 2: Optional 2FA (future enhancement)
   Step 3: Access dashboard
   ```

4. **Password Recovery**
   - "Forgot Password" link
   - Email with reset link
   - Set new password

**Firebase Implementation:**
```javascript
// Firebase Auth setup
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

const auth = getAuth();
signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // User signed in successfully
  });
```

### 4.2 AI Tool Catalog

**Featured AI Tools in Prototype:**

| Tool | Model | Use Case | Icon |
|------|-------|----------|------|
| **Text Assistant** | GPT-4 | Writing, summarization, Q&A | 📝 |
| **Code Helper** | GPT-4 | Code generation, debugging | 💻 |
| **Research Assistant** | Claude 3 | Document analysis, research | 🔬 |
| **Creative Writer** | GPT-4 | Brainstorming, creative content | ✨ |

**Catalog Page Features:**
- Filter by category (Text, Code, Research)
- Search functionality
- Tool cards with:
  - Name and icon
  - Short description
  - Capabilities badges
  - "Try Now" button

### 4.3 Chat Interface

**UI Components:**

```
┌────────────────────────────────────────────────────────┐
│  [Back] Text Assistant - GPT-4            [Clear Chat] │
├────────────────────────────────────────────────────────┤
│                                                        │
│  🤖 AI: Hello! How can I help you today?              │
│                                                        │
│  👤 You: Summarize the key points about AI safety     │
│                                                        │
│  🤖 AI: Here are the key points about AI safety...    │
│       1. Alignment with human values                  │
│       2. Robustness and reliability                   │
│       3. Transparency and explainability              │
│                                                        │
├────────────────────────────────────────────────────────┤
│  Type your message...                        [Send 📤] │
└────────────────────────────────────────────────────────┘
```

**Features:**
- Markdown rendering (bold, lists, code blocks)
- Copy response button
- Regenerate response option
- Token counter (optional)
- Streaming responses (appears word-by-word)

### 4.4 Chat History

**Implementation:**
- Last 10 conversations stored per user
- Firestore structure:
  ```
  users/{userId}/conversations/{conversationId}/
    - messages: Array
    - timestamp: Date
    - model: String
    - title: String (auto-generated from first message)
  ```

**History Sidebar:**
- "Today" section
- "Previous 7 Days" section
- "Older" section
- Delete conversation option

### 4.5 Basic Governance Features

**Content Filtering:**
```python
# Cloud Function: validate_content()
RESTRICTED_KEYWORDS = [
    "password", "ssn", "credit card",
    "api key", "private key"
]

def validate_content(text):
    for keyword in RESTRICTED_KEYWORDS:
        if keyword.lower() in text.lower():
            return {"allowed": False, "reason": f"Contains restricted term: {keyword}"}
    return {"allowed": True}
```

**Usage Logging:**
- Every AI interaction logged to Firestore:
  ```json
  {
    "userId": "user123",
    "timestamp": "2024-12-15T10:30:00Z",
    "model": "gpt-4",
    "promptTokens": 150,
    "completionTokens": 300,
    "cost": 0.015,
    "success": true
  }
  ```

---

## 5. Technology Stack

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.x | UI framework |
| **Next.js** | 14.x | React framework with SSR |
| **TypeScript** | 5.x | Type safety |
| **Tailwind CSS** | 3.x | Styling |
| **Firebase SDK** | 10.x | Firebase client library |
| **React Query** | 5.x | Data fetching and caching |
| **Zustand** | 4.x | State management |

### Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11 | Cloud Functions runtime |
| **Firebase Admin SDK** | 6.x | Server-side Firebase operations |
| **OpenAI Python SDK** | 1.x | OpenAI API integration |
| **Anthropic SDK** | 0.8.x | Claude API integration |
| **FastAPI** (optional) | 0.104.x | If more complex API needed |

### Infrastructure

| Service | Tier | Purpose |
|---------|------|---------|
| **Firebase Hosting** | Free/Spark | Static site hosting |
| **Cloud Functions** | Blaze (Pay-as-you-go) | Serverless API |
| **Firestore** | Free tier | Database |
| **Authentication** | Free tier | User management |

---

## 6. Firebase Services Configuration

### 6.1 Firebase Project Setup

**Project Structure:**
```
genai-portal-prototype/
├── firebase.json              # Firebase configuration
├── .firebaserc                # Project aliases
├── firestore.rules            # Database security rules
├── firestore.indexes.json     # Database indexes
├── storage.rules              # Storage security rules (if needed)
├── functions/                 # Cloud Functions
│   ├── main.py                # Python functions
│   ├── requirements.txt       # Python dependencies
│   └── .env.example           # Environment variables template
└── public/                    # Frontend build output
    └── (React build files)
```

### 6.2 Firebase Configuration File

**firebase.json:**
```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ],
    "headers": [
      {
        "source": "**/*.@(jpg|jpeg|gif|png|svg|webp)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=7200"
          }
        ]
      }
    ]
  },
  "functions": {
    "source": "functions",
    "runtime": "python311",
    "region": "us-central1"
  },
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  }
}
```

### 6.3 Firestore Security Rules

**firestore.rules:**
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // User profiles - users can only read/write their own data
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Chat history - users can only access their own conversations
    match /users/{userId}/conversations/{conversationId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Usage logs - write only, admin read
    match /usage_logs/{logId} {
      allow write: if request.auth != null;
      allow read: if request.auth.token.admin == true;
    }

    // AI tools catalog - public read, admin write
    match /ai_tools/{toolId} {
      allow read: if true;
      allow write: if request.auth.token.admin == true;
    }
  }
}
```

### 6.4 Environment Variables & Secrets

**Required Secrets:**
```bash
# Set using Firebase CLI
firebase functions:secrets:set OPENAI_API_KEY
firebase functions:secrets:set ANTHROPIC_API_KEY

# Optional secrets
firebase functions:secrets:set STRIPE_SECRET_KEY  # For future billing
firebase functions:secrets:set SENDGRID_API_KEY   # For email notifications
```

**Environment Configuration:**
```bash
# .env.local (for local development)
NEXT_PUBLIC_FIREBASE_API_KEY=your_firebase_api_key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your-project-id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456789
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456789:web:abcdef
```

---

## 7. Step-by-Step Deployment Guide

### Phase 1: Pre-Deployment Preparation (Day 1-2)

#### Step 1.1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add Project"
3. Enter project details:
   - **Project Name:** `genai-portal-prototype`
   - **Enable Google Analytics:** Yes (recommended)
   - **Analytics Location:** United States
4. Click "Create Project"

#### Step 1.2: Enable Firebase Services

Navigate to each service and enable:

**Authentication:**
```
1. Go to Build > Authentication
2. Click "Get Started"
3. Enable sign-in methods:
   - Email/Password ✓
   - Google ✓
4. Configure authorized domains (add your-app.web.app)
```

**Firestore Database:**
```
1. Go to Build > Firestore Database
2. Click "Create Database"
3. Select "Start in production mode"
4. Choose location: us-central1
5. Click "Enable"
```

**Cloud Functions:**
```
1. Go to Build > Functions
2. Upgrade to Blaze plan (required for external API calls)
3. Set up billing (add credit card)
4. Set budget alerts ($50/month for prototype)
```

#### Step 1.3: Install Required Tools

```bash
# Install Node.js (v18 or later)
# Download from: https://nodejs.org/

# Install Firebase CLI
npm install -g firebase-tools

# Verify installation
firebase --version

# Login to Firebase
firebase login

# Initialize Firebase in your project
cd D:\AI_HealthCare\Generative_A_IPortal
firebase init
```

**Firebase Initialization Prompts:**
```
? Which Firebase features do you want to set up?
  ◉ Firestore
  ◉ Functions
  ◉ Hosting
  ◯ Storage

? Please select an option:
  ❯ Use an existing project

? Select a default Firebase project:
  ❯ genai-portal-prototype

? What language would you like to use for Cloud Functions?
  ❯ Python

? File firestore.rules already exists. Overwrite?
  No

? What do you want to use as your public directory?
  public

? Configure as a single-page app?
  Yes

? Set up automatic builds and deploys with GitHub?
  No (we'll do this manually first)
```

### Phase 2: Frontend Development (Day 3-7)

#### Step 2.1: Create React Application

```bash
# Create Next.js app with TypeScript
npx create-next-app@latest frontend --typescript --tailwind --app

cd frontend

# Install Firebase SDK
npm install firebase

# Install additional dependencies
npm install @tanstack/react-query zustand react-markdown react-syntax-highlighter
npm install -D @types/react-syntax-highlighter
```

#### Step 2.2: Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx              # Root layout
│   │   ├── page.tsx                # Landing page
│   │   ├── login/
│   │   │   └── page.tsx            # Login page
│   │   ├── dashboard/
│   │   │   └── page.tsx            # Main dashboard
│   │   ├── catalog/
│   │   │   └── page.tsx            # AI tools catalog
│   │   └── chat/
│   │       └── [toolId]/
│   │           └── page.tsx        # Chat interface
│   ├── components/
│   │   ├── AuthProvider.tsx        # Authentication context
│   │   ├── ChatInterface.tsx       # Chat UI component
│   │   ├── ToolCard.tsx            # AI tool card
│   │   ├── Sidebar.tsx             # Chat history sidebar
│   │   └── Header.tsx              # Navigation header
│   ├── lib/
│   │   ├── firebase.ts             # Firebase initialization
│   │   ├── firestore.ts            # Firestore helpers
│   │   └── api.ts                  # API client
│   └── hooks/
│       ├── useAuth.ts              # Authentication hook
│       ├── useChat.ts              # Chat management hook
│       └── useChatHistory.ts       # History fetching hook
├── public/
│   ├── logo.svg
│   └── favicon.ico
└── package.json
```

#### Step 2.3: Key Component Implementation

**Firebase Initialization (src/lib/firebase.ts):**
```typescript
import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
```

**Authentication Hook (src/hooks/useAuth.ts):**
```typescript
import { useState, useEffect } from 'react';
import { User, onAuthStateChanged, signInWithEmailAndPassword, signOut } from 'firebase/auth';
import { auth } from '@/lib/firebase';

export function useAuth() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
      setLoading(false);
    });

    return unsubscribe;
  }, []);

  const login = async (email: string, password: string) => {
    return signInWithEmailAndPassword(auth, email, password);
  };

  const logout = async () => {
    return signOut(auth);
  };

  return { user, loading, login, logout };
}
```

#### Step 2.4: Build Frontend

```bash
# Build for production
npm run build

# Copy build output to Firebase public directory
# (or configure firebase.json to point to out/ directory)
cp -r out/* ../public/
```

### Phase 3: Backend Development (Day 8-10)

#### Step 3.1: Cloud Functions Setup

The existing [main.py](Portal/main.py) is a good start. Let's enhance it:

**Enhanced functions/main.py:**
```python
from firebase_functions import https_fn, options
from firebase_admin import initialize_app, firestore
import openai
import anthropic
import os
from datetime import datetime

# Initialize Firebase Admin
initialize_app()
db = firestore.client()

# API Configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

# Content filtering keywords
RESTRICTED_KEYWORDS = ["password", "ssn", "api key", "credit card", "private key"]

def validate_content(text):
    """Check for sensitive content"""
    text_lower = text.lower()
    for keyword in RESTRICTED_KEYWORDS:
        if keyword in text_lower:
            return False, f"Content contains restricted keyword: {keyword}"
    return True, ""

@https_fn.on_request(
    cors=options.CorsOptions(
        cors_origins=["*"],  # In production, restrict to your domain
        cors_methods=["post", "options"]
    ),
    region="us-central1",
    secrets=["OPENAI_API_KEY", "ANTHROPIC_API_KEY"]
)
def generate_response(req: https_fn.Request) -> https_fn.Response:
    """
    Main AI generation endpoint
    Supports both OpenAI and Anthropic models
    """

    # Verify authentication
    auth_header = req.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return https_fn.Response("Unauthorized", status=401)

    # Parse request
    try:
        data = req.get_json()
        user_id = data.get("userId")
        prompt = data.get("prompt")
        model = data.get("model", "gpt-4")  # Default to GPT-4
        conversation_id = data.get("conversationId")

        if not prompt or not user_id:
            return https_fn.Response("Missing required fields", status=400)

    except Exception as e:
        return https_fn.Response(f"Invalid request: {str(e)}", status=400)

    # Content validation
    is_valid, reason = validate_content(prompt)
    if not is_valid:
        log_usage(user_id, model, prompt, None, False, reason)
        return https_fn.Response(
            {"error": reason, "blocked": True},
            status=403,
            headers={"Content-Type": "application/json"}
        )

    # Route to appropriate AI service
    try:
        if model.startswith("gpt"):
            response = call_openai(prompt, model)
        elif model.startswith("claude"):
            response = call_anthropic(prompt, model)
        else:
            return https_fn.Response("Unsupported model", status=400)

        # Save to conversation history
        save_message(user_id, conversation_id, "user", prompt)
        save_message(user_id, conversation_id, "assistant", response)

        # Log usage
        log_usage(user_id, model, prompt, response, True)

        return https_fn.Response(
            {"response": response, "success": True},
            status=200,
            headers={"Content-Type": "application/json"}
        )

    except Exception as e:
        log_usage(user_id, model, prompt, None, False, str(e))
        return https_fn.Response(
            {"error": f"AI Error: {str(e)}", "success": False},
            status=500,
            headers={"Content-Type": "application/json"}
        )

def call_openai(prompt, model):
    """Call OpenAI API"""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful corporate AI assistant. Be concise and professional."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7
    )

    return completion.choices[0].message.content

def call_anthropic(prompt, model):
    """Call Anthropic Claude API"""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def save_message(user_id, conversation_id, role, content):
    """Save message to Firestore"""
    if not conversation_id:
        return

    db.collection('users').document(user_id).collection('conversations').document(conversation_id).collection('messages').add({
        'role': role,
        'content': content,
        'timestamp': firestore.SERVER_TIMESTAMP
    })

def log_usage(user_id, model, prompt, response, success, error=None):
    """Log usage to Firestore for analytics"""
    db.collection('usage_logs').add({
        'userId': user_id,
        'model': model,
        'promptLength': len(prompt),
        'responseLength': len(response) if response else 0,
        'success': success,
        'error': error,
        'timestamp': firestore.SERVER_TIMESTAMP
    })

@https_fn.on_request(
    cors=options.CorsOptions(cors_origins=["*"], cors_methods=["get", "options"]),
    region="us-central1"
)
def get_chat_history(req: https_fn.Request) -> https_fn.Response:
    """Retrieve user's chat history"""

    # Verify authentication
    auth_header = req.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return https_fn.Response("Unauthorized", status=401)

    user_id = req.args.get('userId')
    if not user_id:
        return https_fn.Response("Missing userId", status=400)

    try:
        # Get last 10 conversations
        conversations = db.collection('users').document(user_id).collection('conversations') \
            .order_by('timestamp', direction=firestore.Query.DESCENDING) \
            .limit(10) \
            .stream()

        result = []
        for conv in conversations:
            conv_data = conv.to_dict()
            conv_data['id'] = conv.id
            result.append(conv_data)

        return https_fn.Response(
            {"conversations": result},
            status=200,
            headers={"Content-Type": "application/json"}
        )

    except Exception as e:
        return https_fn.Response(f"Error: {str(e)}", status=500)
```

#### Step 3.2: Update requirements.txt

```
functions/requirements.txt:
firebase-admin>=6.0.0
firebase-functions>=0.4.0
openai>=1.0.0
anthropic>=0.8.0
```

### Phase 4: Deployment (Day 11-12)

#### Step 4.1: Deploy Cloud Functions

```bash
cd D:\AI_HealthCare\Generative_A_IPortal

# Set secrets
firebase functions:secrets:set OPENAI_API_KEY
# (Paste your OpenAI API key when prompted)

firebase functions:secrets:set ANTHROPIC_API_KEY
# (Paste your Anthropic API key when prompted)

# Deploy functions
firebase deploy --only functions

# Expected output:
# ✔ functions[us-central1-generate_response] Successful update operation.
# ✔ functions[us-central1-get_chat_history] Successful update operation.
```

#### Step 4.2: Deploy Firestore Rules

```bash
# Deploy security rules
firebase deploy --only firestore:rules

# Deploy indexes
firebase deploy --only firestore:indexes
```

#### Step 4.3: Deploy Frontend

```bash
# Build frontend
cd frontend
npm run build

# Deploy to Firebase Hosting
firebase deploy --only hosting

# Expected output:
# ✔ hosting[genai-portal-prototype]: file upload complete
# ✔ Deploy complete!
#
# Hosting URL: https://genai-portal-prototype.web.app
```

#### Step 4.4: Verify Deployment

**Checklist:**
- [ ] Visit hosting URL - site loads correctly
- [ ] Sign up with test email - receives verification email
- [ ] Log in - redirects to dashboard
- [ ] Browse AI catalog - tools display correctly
- [ ] Start chat - receives AI response
- [ ] Check chat history - previous conversations show
- [ ] Test on mobile - responsive design works
- [ ] Check Firebase Console > Functions logs - no errors

### Phase 5: Testing & Refinement (Day 13-14)

See [Section 9: Testing & Validation Plan](#9-testing--validation-plan)

---

## 8. Security & Access Control

### 8.1 Authentication Security

**Firebase Authentication Features:**
- Automatic password hashing (bcrypt)
- Session token management
- HTTPS-only communication
- Rate limiting on auth endpoints

**Additional Security Measures:**
```javascript
// Require email verification
const user = auth.currentUser;
if (!user.emailVerified) {
  await sendEmailVerification(user);
  // Block access until verified
}

// Password strength requirements
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
if (!passwordRegex.test(password)) {
  throw new Error("Password must be at least 8 characters with uppercase, lowercase, and number");
}
```

### 8.2 API Security

**Cloud Functions Security:**
- All functions require authentication token
- Token verification on every request
- Rate limiting (100 requests/minute per user)
- Input validation and sanitization

**Example Token Verification:**
```python
from firebase_admin import auth

def verify_token(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise ValueError("Missing Authorization header")

    token = auth_header.split('Bearer ')[1]
    decoded_token = auth.verify_id_token(token)
    return decoded_token['uid']
```

### 8.3 Data Protection

**Firestore Security:**
- User data isolated per user ID
- No cross-user data access
- Audit logging of all database operations

**Data Encryption:**
- Data encrypted at rest (Firebase default)
- Data encrypted in transit (HTTPS)
- API keys stored in Firebase Secrets (encrypted)

### 8.4 Stakeholder Access Control

**Demo Accounts:**
Create dedicated demo accounts for stakeholders:

```bash
# Create demo users via Firebase Console or script
demo-executive@example.com      # Executive stakeholder
demo-technical@example.com      # Technical reviewer
demo-security@example.com       # Security auditor
```

**Access Levels:**
| Account Type | Permissions |
|--------------|-------------|
| Executive Demo | Full access to all AI tools, limited history |
| Technical Demo | Full access + view logs/metrics |
| Security Demo | Read-only access to security logs |

---

## 9. Testing & Validation Plan

### 9.1 Functional Testing

**Test Cases:**

| Test ID | Scenario | Expected Result | Status |
|---------|----------|-----------------|--------|
| AUTH-01 | User signs up with valid email | Account created, verification email sent | ⬜ |
| AUTH-02 | User logs in with correct credentials | Redirected to dashboard | ⬜ |
| AUTH-03 | User logs in with wrong password | Error message displayed | ⬜ |
| AUTH-04 | User resets password | Reset email sent, password updated | ⬜ |
| CHAT-01 | User sends message to GPT-4 | Response received within 5s | ⬜ |
| CHAT-02 | User sends message to Claude | Response received within 5s | ⬜ |
| CHAT-03 | User sends restricted content | Blocked with warning message | ⬜ |
| CHAT-04 | User views chat history | Last 10 conversations displayed | ⬜ |
| CHAT-05 | User deletes conversation | Conversation removed from history | ⬜ |
| UI-01 | User accesses site on mobile | Responsive layout renders correctly | ⬜ |
| UI-02 | User toggles dark/light mode | Theme changes persist | ⬜ |
| PERF-01 | Page load time | < 3 seconds on 4G connection | ⬜ |
| PERF-02 | AI response time | < 5 seconds for typical query | ⬜ |

### 9.2 Security Testing

**Security Checklist:**
- [ ] Firestore rules prevent unauthorized data access
- [ ] Cloud Functions require valid authentication tokens
- [ ] API keys not exposed in frontend code
- [ ] No XSS vulnerabilities in chat interface
- [ ] Content filtering blocks restricted keywords
- [ ] Rate limiting prevents abuse

**Testing Tools:**
```bash
# Test Firestore security rules
firebase emulators:start --only firestore
npm run test:security-rules

# Scan for vulnerabilities
npm audit
pip-audit  # For Python dependencies
```

### 9.3 Performance Testing

**Load Testing Scenarios:**

```bash
# Install Apache Bench or similar tool
# Test 100 concurrent users
ab -n 1000 -c 100 https://genai-portal-prototype.web.app/

# Expected metrics:
# - 99% requests successful
# - Average response time < 2s
# - No server errors
```

**Firebase Performance Monitoring:**
- Automatically tracks page load times
- Monitors Cloud Function execution times
- Alerts if performance degrades

### 9.4 User Acceptance Testing (UAT)

**Stakeholder Demo Script:**

**Scenario 1: First-Time User Experience**
```
1. Open incognito browser window
2. Navigate to https://genai-portal-prototype.web.app
3. Click "Sign Up"
4. Enter email: demo-stakeholder@company.com
5. Create password
6. Verify email
7. Complete profile setup
8. Arrive at dashboard
   ✓ Process feels smooth and intuitive
```

**Scenario 2: Using AI for Real Work**
```
1. Click "Text Assistant" tool
2. Enter prompt: "Summarize the key benefits of AI in healthcare in 3 bullet points"
3. Observe response
   ✓ Response is relevant and well-formatted
   ✓ Appears within 5 seconds
4. Click "Regenerate" button
   ✓ New response generated
5. Click "Copy" button
   ✓ Response copied to clipboard
```

**Scenario 3: Reviewing History**
```
1. Return to dashboard
2. View chat history sidebar
3. Click on previous conversation
   ✓ Previous messages loaded correctly
4. Continue conversation in same thread
   ✓ Context maintained
```

**Feedback Collection:**
After demo, stakeholders complete survey:
- Usability (1-5 stars): ⭐⭐⭐⭐⭐
- Performance (1-5 stars): ⭐⭐⭐⭐⭐
- Design (1-5 stars): ⭐⭐⭐⭐⭐
- Would recommend for production: Yes / No
- Comments: [Open text field]

---

## 10. Stakeholder Demo Environment

### 10.1 Demo Setup

**Preparation Checklist (1 day before demo):**

- [ ] Verify all services are running
- [ ] Create demo accounts for all stakeholders
- [ ] Pre-load sample AI tools in catalog
- [ ] Test all demo scenarios
- [ ] Prepare backup plan (screen recording if live demo fails)
- [ ] Send access instructions to stakeholders

**Access Instructions Email Template:**
```
Subject: Generative AI Portal Prototype - Access Instructions

Dear [Stakeholder Name],

We're excited to share the Generative AI Portal prototype with you! Here's how to access it:

🔗 URL: https://genai-portal-prototype.web.app

📧 Demo Account:
   Email: [demo-email@company.com]
   Password: [temporary-password]

📱 Access from:
   - Desktop browser (Chrome, Edge, Safari recommended)
   - Tablet or mobile device

⏰ Demo Session: [Date & Time]
   We'll walk through the key features together

📋 What to Expect:
   - AI-powered chat interface
   - Multiple AI models (GPT-4, Claude)
   - Chat history and management
   - Modern, responsive design

Please test the login before our demo session. If you encounter any issues,
reply to this email or contact [Support Contact].

Looking forward to your feedback!

Best regards,
[Your Name]
```

### 10.2 Demo Presentation Flow

**Introduction (5 minutes):**
- Recap project goals
- Explain prototype scope
- Set expectations for what's included/excluded

**Live Demo (15 minutes):**

**Part 1: Authentication & Onboarding (3 min)**
- Show landing page
- Sign in with demo account
- Navigate to dashboard

**Part 2: AI Tool Catalog (3 min)**
- Browse available AI tools
- Show filtering and search
- Explain each tool's capabilities

**Part 3: Chat Experience (5 min)**
- Select "Text Assistant"
- Demonstrate real AI interaction
- Show response formatting
- Highlight copy/regenerate features

**Part 4: History & Management (2 min)**
- View chat history
- Resume previous conversation
- Delete conversation

**Part 5: Mobile Experience (2 min)**
- Open on mobile device (or use Chrome DevTools)
- Show responsive design

**Q&A and Feedback (10 minutes):**
- Address stakeholder questions
- Collect feedback on specific features
- Discuss next steps

### 10.3 Demo Talking Points

**Key Messages:**
✅ **Security First**: "All data is encrypted, no AI provider stores our conversations"
✅ **Easy to Use**: "Designed for non-technical users, no training required"
✅ **Fast & Reliable**: "Responses in seconds, 99.9% uptime"
✅ **Scalable**: "Can easily add more AI models and features"
✅ **Cost-Effective**: "Prototype costs < $50/month, production scales with usage"

**Addressing Common Concerns:**

| Concern | Response |
|---------|----------|
| "Is our data secure?" | "Yes - Firebase enterprise-grade encryption, no data shared with AI providers beyond the query, all conversations logged for audit" |
| "Can we integrate with SSO?" | "Absolutely - production version will support SAML/Azure AD, this prototype uses email for quick testing" |
| "What if AI gives wrong answer?" | "We'll implement human review workflows and feedback mechanisms in production" |
| "How much will this cost at scale?" | "Firebase scales automatically, estimated $500-2000/month for 1000 users based on usage patterns" |

---

## 11. Cost Estimation

### 11.1 Prototype Phase Costs

**Firebase Costs (Monthly):**

| Service | Free Tier | Prototype Usage | Estimated Cost |
|---------|-----------|-----------------|----------------|
| **Hosting** | 10 GB storage, 360 MB/day transfer | < 1 GB, minimal traffic | $0 |
| **Authentication** | 10k verifications/month | ~50 demo users | $0 |
| **Firestore** | 1 GB storage, 50k reads, 20k writes | < 100 MB, ~5k operations | $0 |
| **Cloud Functions** | 2M invocations, 400k GB-seconds | ~1000 invocations | $0-5 |
| **Total Firebase** | | | **$0-5/month** |

**AI API Costs (Monthly):**

| Provider | Model | Prototype Usage | Estimated Cost |
|----------|-------|-----------------|----------------|
| **OpenAI** | GPT-4 | ~100 queries, ~10k tokens | $10-20 |
| **Anthropic** | Claude 3 | ~50 queries, ~5k tokens | $5-10 |
| **Total AI** | | | **$15-30/month** |

**Total Prototype Cost: $15-35/month**

### 11.2 Production Phase Costs (Estimated)

**Assumptions:**
- 1000 active users
- Average 10 AI queries per user per day
- 200 tokens per query (input + output)

**Monthly Costs:**

| Category | Service | Cost |
|----------|---------|------|
| **Infrastructure** | Firebase Hosting | $50 |
| | Firestore | $200 |
| | Cloud Functions | $300 |
| | **Subtotal** | **$550** |
| **AI APIs** | OpenAI (GPT-4) | $800 |
| | Anthropic (Claude) | $400 |
| | **Subtotal** | **$1,200** |
| **Monitoring** | Firebase Performance | $0 (included) |
| | Error tracking (Sentry) | $25 |
| | **Subtotal** | **$25** |
| **Total** | | **$1,775/month** |

**Per-User Cost:** $1.78/month (extremely competitive compared to individual ChatGPT Plus at $20/user)

**Cost Optimization Strategies:**
- Implement caching for common queries (30% reduction)
- Use GPT-3.5-turbo for simple queries (50% AI cost reduction)
- Set per-user monthly limits (prevent runaway costs)
- Negotiate enterprise pricing with OpenAI/Anthropic (20-40% discount)

**Projected Savings:**
If 1000 users currently pay for individual AI subscriptions:
- Current cost: 1000 users × $20/month = $20,000/month
- Portal cost: $1,775/month
- **Monthly savings: $18,225 (91% reduction)**

---

## 12. Migration Path to Production

### 12.1 Firebase to Azure/AWS Migration

If stakeholders approve but require on-premise or different cloud provider:

**Data Export:**
```bash
# Export Firestore data
gcloud firestore export gs://[BUCKET_NAME]

# Export Authentication users
firebase auth:export users.json --format=JSON
```

**Architecture Mapping:**

| Firebase Service | Azure Equivalent | AWS Equivalent |
|------------------|------------------|----------------|
| Hosting | Azure Static Web Apps | S3 + CloudFront |
| Authentication | Azure AD B2C | Cognito |
| Firestore | Cosmos DB | DynamoDB |
| Cloud Functions | Azure Functions | Lambda |

**Migration Timeline:** 4-6 weeks

### 12.2 Minimal Changes Migration Path

**Option: Keep Firebase for Production**

Advantages:
- Zero migration effort
- Proven scalability (used by Duolingo, Lyft, The New York Times)
- Enterprise support available
- Firebase supports compliance (SOC 2, ISO 27001, HIPAA)

Enhancements for production:
- Enable Firebase App Check (prevent abuse)
- Set up VPC Service Controls (network security)
- Configure backup schedules
- Add multi-region replication
- Implement monitoring alerts

**Cost:** Similar to migration, but saves 6 weeks of development time

---

## 13. Timeline & Milestones

### Detailed Implementation Schedule

```
Week 1: Infrastructure Setup
├── Day 1-2: Firebase project creation and configuration
├── Day 3-4: Development environment setup
└── Day 5: Initial deployment test

Week 2: Frontend Development
├── Day 6-7: Authentication UI and logic
├── Day 8-9: Dashboard and AI catalog
└── Day 10: Chat interface development

Week 3: Backend & Integration
├── Day 11-12: Cloud Functions development
├── Day 13: AI API integration (OpenAI)
└── Day 14: AI API integration (Anthropic)

Week 4: Testing & Launch
├── Day 15-16: Testing and bug fixes
├── Day 17: Stakeholder access preparation
├── Day 18: Pre-demo dry run
└── Day 19: Stakeholder demo
```

**Milestones:**

| Milestone | Date | Deliverable | Success Criteria |
|-----------|------|-------------|------------------|
| M1: Infrastructure Ready | End Week 1 | Firebase project configured | All services enabled, billing set up |
| M2: Frontend Complete | End Week 2 | Working UI deployed | Can navigate all pages, UI responsive |
| M3: Backend Complete | End Week 3 | APIs functional | AI responses work, data persists |
| M4: Testing Complete | Day 16 | All tests passed | 100% critical tests green |
| M5: Stakeholder Demo | Day 19 | Live demonstration | Stakeholders approve for production |

---

## 14. Risk Mitigation

### Potential Risks & Mitigation Strategies

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| **API key exposed** | Medium | High | Use Firebase Secrets, never commit to Git, rotate regularly |
| **Unexpected AI costs** | Medium | Medium | Set budget alerts, implement rate limiting, use cheaper models for simple queries |
| **Performance issues during demo** | Low | High | Pre-test all demos, have screen recording backup, use demo data that's known to work |
| **Firestore quota exceeded** | Low | Medium | Monitor usage dashboard, implement caching, optimize queries |
| **AI provider outage** | Low | High | Implement fallback to alternative provider, show friendly error message |
| **Stakeholder access issues** | Medium | Medium | Send credentials 2 days early, provide test window, have IT support on standby |
| **Security vulnerability** | Low | High | Follow Firebase security best practices, regular security audits, input validation |
| **Slow AI responses** | Medium | Medium | Use streaming responses, show loading indicators, set timeout limits |

### Contingency Plans

**Scenario: OpenAI API is down during demo**
- Switch demo to Anthropic Claude
- Show pre-recorded video of OpenAI integration
- Explain redundancy in production system

**Scenario: Firebase hosting slow**
- Run local development server as backup
- Use screen sharing instead of live site
- Highlight CDN improvements for production

**Scenario: Stakeholder can't log in**
- Have admin panel to reset passwords instantly
- Create multiple backup accounts
- Use screen sharing to show their view

---

## 15. Approval Checklist

### Pre-Demo Checklist

**Technical Readiness:**
- [ ] All Firebase services deployed successfully
- [ ] Frontend accessible at public URL
- [ ] Backend APIs returning successful responses
- [ ] Test accounts created and verified
- [ ] All demo scenarios tested end-to-end
- [ ] Performance meets requirements (< 3s load, < 5s AI response)
- [ ] Security rules tested and validated
- [ ] Error handling tested (wrong password, network errors, etc.)

**Content Readiness:**
- [ ] AI tools catalog populated with descriptions
- [ ] Sample conversations pre-loaded (optional)
- [ ] Demo script prepared and practiced
- [ ] Backup screen recordings ready
- [ ] Feedback survey prepared

**Stakeholder Communication:**
- [ ] Demo invitations sent with URL and credentials
- [ ] Reminder sent 1 day before demo
- [ ] Support contact information provided
- [ ] Demo agenda shared

### Post-Demo Approval Criteria

**Stakeholders should evaluate:**

| Criteria | Rating (1-5) | Comments |
|----------|--------------|----------|
| User interface is intuitive and professional | ⬜⬜⬜⬜⬜ | |
| AI responses are accurate and helpful | ⬜⬜⬜⬜⬜ | |
| Performance is acceptable (speed, reliability) | ⬜⬜⬜⬜⬜ | |
| Security measures are adequate | ⬜⬜⬜⬜⬜ | |
| Mobile experience is satisfactory | ⬜⬜⬜⬜⬜ | |
| Feature set aligns with project goals | ⬜⬜⬜⬜⬜ | |
| Ready to proceed to production development | ⬜⬜⬜⬜⬜ | |

**Approval Decision:**

- [ ] ✅ **APPROVED** - Proceed with production development as planned
- [ ] ⚠️ **APPROVED WITH CHANGES** - Make requested modifications before production
- [ ] ❌ **NOT APPROVED** - Significant rework required

**Sign-Off:**

```
Executive Sponsor: _____________________  Date: __________

Technical Lead: ________________________  Date: __________

Security Officer: ______________________  Date: __________

Product Owner: _________________________  Date: __________
```

---

## Next Steps After Approval

### If Approved for Production:

1. **Transition Planning (Week 1)**
   - Document all feedback and change requests
   - Create detailed production requirements document
   - Plan production architecture (Firebase vs. other cloud)
   - Assemble production development team

2. **Production Development (Months 1-9)**
   - Follow the project timeline from original specification
   - Implement all six building blocks fully
   - Add SSO, RBAC, advanced governance
   - Integrate additional AI models
   - Build learning hub and sandbox

3. **Production Deployment (Month 10-12)**
   - Migrate to production infrastructure
   - Conduct security audit and penetration testing
   - Perform load testing with realistic user volumes
   - Plan phased rollout strategy
   - Create training materials and documentation

4. **Launch & Support**
   - Soft launch with pilot user group
   - Gather feedback and iterate
   - Full launch to organization
   - Ongoing monitoring and support

---

## Appendix A: Useful Commands Reference

### Firebase CLI Commands

```bash
# Login and project management
firebase login
firebase projects:list
firebase use [project-id]

# Deploy specific services
firebase deploy --only hosting
firebase deploy --only functions
firebase deploy --only firestore:rules

# Local development
firebase emulators:start
firebase serve

# Secrets management
firebase functions:secrets:set SECRET_NAME
firebase functions:secrets:access SECRET_NAME

# Logs and debugging
firebase functions:log
firebase functions:log --only function-name

# Database operations
firebase firestore:delete [document path] --recursive
```

### Testing Commands

```bash
# Frontend testing
npm run test
npm run build
npm run lint

# Backend testing
cd functions
pytest
python -m unittest discover

# Security testing
npm audit fix
pip-audit --fix
```

---

## Appendix B: Troubleshooting Guide

### Common Issues and Solutions

**Issue: "Firebase CLI not recognized"**
```bash
# Solution: Reinstall globally
npm uninstall -g firebase-tools
npm install -g firebase-tools
```

**Issue: "Cloud Function deployment fails"**
```bash
# Solution: Check Python version and dependencies
python --version  # Should be 3.11
pip install -r functions/requirements.txt
firebase deploy --only functions --debug
```

**Issue: "Firestore permission denied"**
```bash
# Solution: Check security rules
# Ensure user is authenticated and accessing their own data
# Test rules in Firebase Console > Firestore > Rules Playground
```

**Issue: "OpenAI API key not found"**
```bash
# Solution: Verify secret is set correctly
firebase functions:secrets:access OPENAI_API_KEY
# If empty, set again:
firebase functions:secrets:set OPENAI_API_KEY
```

**Issue: "CORS error when calling Cloud Function"**
```python
# Solution: Add CORS configuration to function
cors=options.CorsOptions(
    cors_origins=["https://your-app.web.app", "http://localhost:3000"],
    cors_methods=["get", "post", "options"]
)
```

---

## Appendix C: Contact & Support

**Project Team:**
- **Project Lead:** [Name, Email]
- **Frontend Developer:** [Name, Email]
- **Backend Developer:** [Name, Email]
- **DevOps Engineer:** [Name, Email]

**External Support:**
- **Firebase Support:** https://firebase.google.com/support
- **OpenAI Support:** https://help.openai.com
- **Anthropic Support:** https://support.anthropic.com

**Emergency Contacts:**
- **Firebase Console:** https://console.firebase.google.com
- **On-Call Support:** [Phone Number]

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-12-15 | [Your Name] | Initial version created |

---

**END OF DEPLOYMENT PLAN**

This document provides a complete roadmap for deploying the Generative AI Portal prototype on Firebase. Please review carefully and approve before proceeding with implementation.
