const DB_NAME = 'lt-quiz-db';
const DB_VERSION = 1;
const STORE_NAME = 'quizzes';

let db;

function openDB() {
  return new Promise((resolve, reject) => {
    if (db) {
      return resolve(db);
    }
    const request = indexedDB.open(DB_NAME, DB_VERSION);

    request.onerror = (event) => {
      reject('Error opening database');
    };

    request.onsuccess = (event) => {
      db = event.target.result;
      resolve(db);
    };

    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME, { keyPath: 'subject' });
      }
    };
  });
}

async function saveQuiz(subject, quizData, constructionSections, time) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const transaction = db.transaction([STORE_NAME], 'readwrite');
    const store = transaction.objectStore(STORE_NAME);
    const dataToStore = {
      subject: subject,
      quizData: quizData,
      constructionSections: constructionSections,
      time: time,
      timestamp: new Date().getTime()
    };
    const request = store.put(dataToStore);

    request.onsuccess = () => {
      resolve();
    };

    request.onerror = (event) => {
      reject('Error saving quiz data: ' + event.target.errorCode);
    };
  });
}

async function getQuiz(subject) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const transaction = db.transaction([STORE_NAME], 'readonly');
    const store = transaction.objectStore(STORE_NAME);
    const request = store.get(subject);

    request.onsuccess = (event) => {
      resolve(event.target.result);
    };

    request.onerror = (event) => {
      reject('Error getting quiz data: ' + event.target.errorCode);
    };
  });
}

async function getDownloadedSubjects() {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const transaction = db.transaction([STORE_NAME], 'readonly');
    const store = transaction.objectStore(STORE_NAME);
    const request = store.getAllKeys();

    request.onsuccess = (event) => {
      resolve(event.target.result);
    };

    request.onerror = (event) => {
      reject('Error getting subjects: ' + event.target.errorCode);
    };
  });
} 