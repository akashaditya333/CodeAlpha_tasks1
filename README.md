# 🌐 Translator Tool

A simple and responsive web-based Translator Tool built with **HTML**, **CSS**, and **JavaScript**. The application allows users to translate text between multiple languages using the **MyMemory Translation API**. It also supports **text-to-speech** and **copy-to-clipboard** functionality.

---

## 🚀 Features

- 🌍 Translate text between 90+ languages
- 🔊 Listen to the original and translated text using Speech Synthesis
- 📋 Copy source or translated text with one click
- 🎨 Clean and responsive user interface
- ⚡ Fast translation using the MyMemory Translation API

---

## 📂 Project Structure

```
TranslatorTool/
│── index.html        # Main HTML file
│── style.css         # Styling for the application
│── script.js         # JavaScript logic
│── countries.js      # Language codes and names
│── speaker.svg       # Speaker icon
│── copy.svg          # Copy icon
└── README.md         # Project documentation
```

---

## 🛠️ Technologies Used

- HTML5
- CSS3
- JavaScript (ES6)
- MyMemory Translation API
- Web Speech API (Speech Synthesis)
- Clipboard API

---

## 📸 Features Overview

### 1. Language Selection
- Select the source language.
- Select the target language.
- English is selected by default as the source language.
- Hindi is selected by default as the target language.

### 2. Translation
- Enter text in the left text area.
- Click the **Translate** button.
- The translated text appears in the right text area.

### 3. Text-to-Speech
Click the speaker icon to hear:
- Source text
- Translated text

### 4. Copy Text
Click the copy icon to copy:
- Source text
- Translated text

---

## ▶️ Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/translator-tool.git
```

### Navigate to the Project

```bash
cd translator-tool
```

### Run the Project

Simply open `index.html` in your web browser.

No installation or build process is required.

---

## 🌍 Translation API

This project uses the **MyMemory Translation API**:

```
https://api.mymemory.translated.net/get
```

Example request:

```
https://api.mymemory.translated.net/get?q=Hello&langpair=en-GB|hi-IN
```

---

## 💡 Future Improvements

- Language swap button
- Detect source language automatically
- Dark mode
- Translation history
- Voice input using Speech Recognition API
- Character counter
- Download translated text as a file
- Better error handling for API failures
- Loading spinner during translation

---

## 📷 Screenshot

Add a screenshot of your project here.

```
screenshots/app.png
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Create a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Akash Aditya**

If you found this project useful, consider giving it a ⭐ on GitHub.
