# Lt Quiz - Test Page

## 🎯 Overview
This project contains a quiz application with a test page (`test.html`) that lists all available quizzes and allows downloading them for offline use.

## 📁 Files
- `test.html` - Test page with quiz listing and download functionality
- `index.html` - Main quiz home page
- `quiz.html` - Quiz taking interface
- `offline.js` - Offline storage functionality
- `sw.js` - Service worker for PWA
- `manifest.json` - PWA manifest

## 🚀 How to Test

### 1. Start Local Server
```bash
python -m http.server 8000
```

### 2. Open Test Page
Navigate to: `http://localhost:8000/test.html`

### 3. What You Should See
- **Debug Panel**: Real-time status information
- **4 Quiz Cards**: Maths, Science, English, Oromo
- **Take Quiz Button**: Navigates to quiz.html#subject
- **Download Button**: Downloads quiz for offline use

## ✅ Features Working

### Quiz Display
- ✅ All 4 quizzes show properly
- ✅ Each quiz shows description, difficulty, time
- ✅ Online/Offline status badges

### Download Functionality
- ✅ Download button works when online
- ✅ Shows "Downloading..." with spinner
- ✅ Changes to "Downloaded" when complete
- ✅ Saves to IndexedDB for offline use

### Navigation
- ✅ "Take Quiz" button navigates to quiz.html#subject
- ✅ Passes quiz selection via URL hash
- ✅ localStorage integration with quiz.html

### Firebase Integration
- ✅ Same config as quiz.html
- ✅ Proper initialization
- ✅ Error handling

### Offline Support
- ✅ Shows downloaded quizzes when offline
- ✅ Proper status indicators
- ✅ Works without internet connection

## 🔧 Debug Information
The test page includes a debug panel that shows:
- Firebase initialization status
- Quiz rendering progress
- Download status
- Error messages
- localStorage operations

## 🎉 Success Criteria
- [x] Quizzes display properly (not blank)
- [x] Download buttons work
- [x] Navigation to quiz.html works
- [x] Firebase integration works
- [x] localStorage connection works
- [x] Offline functionality works

## 🐛 Troubleshooting
If quizzes don't show:
1. Check browser console for errors
2. Verify Firebase is initialized
3. Check debug panel for status
4. Ensure you're online for initial load

## 📱 PWA Features
- Service worker for offline caching
- Manifest for app-like experience
- Responsive design for mobile 