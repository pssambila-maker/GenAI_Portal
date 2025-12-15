# Quick Start Guide - Firebase Prototype Deployment

**For developers who want to get started immediately**

## Prerequisites Checklist

- [ ] Node.js 18+ installed ([Download](https://nodejs.org/))
- [ ] Python 3.11 installed
- [ ] Git installed
- [ ] OpenAI API key ([Get one](https://platform.openai.com/api-keys))
- [ ] Anthropic API key ([Get one](https://console.anthropic.com/))
- [ ] Google account for Firebase
- [ ] Credit card for Firebase Blaze plan (required for external API calls)

## 10-Minute Setup

### Step 1: Install Firebase CLI (2 min)

```bash
npm install -g firebase-tools
firebase login
```

### Step 2: Create Firebase Project (3 min)

1. Go to https://console.firebase.google.com/
2. Click "Add Project"
3. Name: `genai-portal-prototype`
4. Enable Google Analytics: Yes
5. Click "Create Project"

### Step 3: Enable Firebase Services (2 min)

In Firebase Console:

**Authentication:**
- Build > Authentication > Get Started
- Enable "Email/Password"
- Enable "Google"

**Firestore:**
- Build > Firestore Database > Create Database
- Start in "production mode"
- Location: us-central1

**Upgrade to Blaze Plan:**
- Upgrade (in left sidebar)
- Add credit card
- Set budget alert: $50/month

### Step 4: Initialize Project (3 min)

```bash
cd D:\AI_HealthCare\Generative_A_IPortal

# Initialize Firebase
firebase init

# Select:
# - Firestore
# - Functions
# - Hosting

# Use existing project: genai-portal-prototype
# Functions language: Python
# Accept default file names
```

## 5-Minute Backend Deployment

### Step 1: Set API Keys

```bash
firebase functions:secrets:set OPENAI_API_KEY
# Paste your OpenAI API key when prompted

firebase functions:secrets:set ANTHROPIC_API_KEY
# Paste your Anthropic API key when prompted
```

### Step 2: Deploy Functions

The [main.py](Portal/main.py) file is already created. Deploy it:

```bash
firebase deploy --only functions
```

**Expected Output:**
```
✔ functions[us-central1-generate_response] Successful update
Function URL: https://us-central1-genai-portal-prototype.cloudfunctions.net/generate_response
```

### Step 3: Deploy Firestore Rules

```bash
firebase deploy --only firestore:rules
```

## Frontend Setup (Next Steps)

### Option A: Use Pre-built Template (Fastest)

```bash
# Clone a Next.js Firebase starter
npx create-next-app@latest frontend --typescript --tailwind --app

cd frontend

# Install Firebase
npm install firebase

# Install additional packages
npm install @tanstack/react-query zustand react-markdown
```

### Option B: Custom Development

Follow the detailed instructions in [FIREBASE_DEPLOYMENT_PLAN.md](FIREBASE_DEPLOYMENT_PLAN.md) Section 7.2

## Testing Your Backend

### Test with cURL

```bash
# Get your function URL from deployment output
FUNCTION_URL="https://us-central1-genai-portal-prototype.cloudfunctions.net/generate_response"

# Test the API (replace with valid Firebase auth token)
curl -X POST $FUNCTION_URL \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_FIREBASE_TOKEN" \
  -d '{
    "userId": "test-user",
    "prompt": "Say hello!",
    "model": "gpt-4"
  }'
```

### Get Firebase Token for Testing

```bash
# Install Firebase tools locally
npm install firebase

# Create a test script
cat > test-auth.js << 'EOF'
const { initializeApp } = require('firebase/app');
const { getAuth, signInWithEmailAndPassword } = require('firebase/auth');

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "genai-portal-prototype.firebaseapp.com",
  projectId: "genai-portal-prototype"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

signInWithEmailAndPassword(auth, 'test@example.com', 'password123')
  .then((userCredential) => {
    return userCredential.user.getIdToken();
  })
  .then((token) => {
    console.log('Token:', token);
  });
EOF

node test-auth.js
```

## Common Commands

### Deploy Everything
```bash
firebase deploy
```

### Deploy Only Specific Service
```bash
firebase deploy --only functions
firebase deploy --only hosting
firebase deploy --only firestore:rules
```

### View Logs
```bash
firebase functions:log
```

### Local Development
```bash
firebase emulators:start
```

### Check Project Info
```bash
firebase projects:list
firebase use --add  # Switch projects
```

## Troubleshooting

### "Billing account not configured"
```bash
# Solution: Upgrade to Blaze plan in Firebase Console
# Go to Project Settings > Usage and billing > Modify plan
```

### "Module 'openai' not found"
```bash
# Solution: Ensure requirements.txt exists in functions/ directory
cd functions
cat > requirements.txt << 'EOF'
firebase-admin>=6.0.0
firebase-functions>=0.4.0
openai>=1.0.0
anthropic>=0.8.0
EOF

firebase deploy --only functions
```

### "CORS error"
```python
# Solution: Already configured in main.py
# Verify the cors_origins includes your domain
cors=options.CorsOptions(
    cors_origins=["*"],  # Change to your domain in production
    cors_methods=["post", "options"]
)
```

## Next Steps

1. ✅ Backend deployed and tested
2. ⬜ Build React frontend (see Section 7.2 in deployment plan)
3. ⬜ Deploy frontend to Firebase Hosting
4. ⬜ Create demo accounts for stakeholders
5. ⬜ Schedule stakeholder demo

## Getting Help

- **Full Deployment Plan:** [FIREBASE_DEPLOYMENT_PLAN.md](FIREBASE_DEPLOYMENT_PLAN.md)
- **Firebase Docs:** https://firebase.google.com/docs
- **Project Issues:** Create an issue in this repository

## Estimated Costs

- **Development/Testing:** $5-15/month
- **Prototype with ~50 users:** $15-35/month
- **Production with 1000 users:** $1,500-2,000/month

Set budget alerts in Firebase Console to avoid surprises!
