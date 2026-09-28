📚 AI PYQ Analyzer

An AI-powered web application for analyzing Previous Year Question Papers (PYQs), identifying repeated questions, organizing questions chapter-wise, and generating useful exam statistics.

---

🚀 Step 6 — Install Required Packages

Open the Terminal in GitHub Codespaces.

Run:

pip install -r requirements.txt

Wait for the installation to finish.

Then verify that Streamlit is installed:

streamlit --version

You should see the installed Streamlit version.

---

▶️ Step 7 — Run the Application

In the Codespaces terminal, run:

streamlit run app.py

You should see something similar to:

You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501

GitHub Codespaces should detect the application running on port "8501".

Open the application in your browser.

---

📄 Step 8 — Test PDF Upload

Open the Streamlit application.

You should see:

«📚 AI PYQ Analyzer»

and:

«Upload your PYQ PDF files»

Select one or more previous-year question paper PDFs.

The current version only confirms that the files have been uploaded.

PDF analysis will be added in the next development stage.

---

🔨 Development Roadmap

The application will be developed step-by-step.

Version 1 — Basic Application

- [x] GitHub repository
- [x] GitHub Codespaces
- [x] Python environment
- [x] Streamlit
- [x] PDF upload interface
- [ ] PDF text extraction
- [ ] Display extracted text

---

Version 2 — Question Extraction

The application will extract individual questions from uploaded papers.

Example:

QUESTION PAPER

Q1. Define DFA.
Q2. What is epsilon closure?
Q3. Explain NFA with example.

will become:

1. Define DFA.

2. What is epsilon closure?

3. Explain NFA with example.

Planned components:

- PDF text extraction
- Question-number detection
- Question cleaning
- Section detection
- Marks detection

---

Version 3 — Exam Season and Year Detection

The application will identify the examination season and year.

Examples:

Winter 2021 → W21
Summer 2021 → S21
Winter 2022 → W22
Summer 2022 → S22

These codes will be associated with every extracted question.

---

Version 4 — Repeated Question Detection

The application will identify questions that are repeated across different examination papers.

Example:

Winter 2021:
What is Extra Closure?

Summer 2021:
Define Extra Closure.

The system should recognize that both questions refer to the same concept.

Expected result:

What is Extra Closure? (W21, S21)

Frequency: 2

Technologies initially considered:

- RapidFuzz
- Scikit-learn
- Text similarity
- Question normalization

AI/semantic matching may be added later for improved accuracy.

---

Version 5 — Syllabus and Chapter Mapping

Users will be able to provide the subject syllabus.

Example:

UNIT 1
Finite Automata
DFA
NFA
Regular Expressions
Epsilon Closure

UNIT 2
Context Free Grammar
Pushdown Automata
Parse Trees

The system will map questions to:

Question
   ↓
Topic
   ↓
Chapter
   ↓
Unit

---

Version 6 — Chapter-Wise Results

The application will organize questions by unit and chapter.

Example:

Unit 1 — Finite Automata

Question| Appeared| Count
What is Extra Closure?| W21, S21| 2
Explain DFA.| W21, W22, S23| 3
Define NFA.| S21, W23| 2

---

Version 7 — Search and Filters

Planned features:

- 🔎 Search questions
- Filter by unit
- Filter by chapter
- Filter by examination year
- Filter by season
- Show repeated questions only
- Select minimum repetition count

Example:

Search:
[ extra closure ]

Unit:
[ Unit 1 ▼ ]

Chapter:
[ Finite Automata ▼ ]

Minimum repetitions:
[ 2 ]

---

Version 8 — Statistics

The application will provide statistics such as:

- Total papers analyzed
- Total questions
- Unique questions
- Repeated questions
- Most repeated questions
- Questions by unit
- Questions by chapter
- Questions by examination year
- Repetition frequency

---

Version 9 — Export

Users will be able to export the analyzed results.

Planned formats:

- CSV
- Excel
- PDF

Example Excel columns:

Unit
Chapter
Question
Examination
Frequency

---

Version 10 — OCR Support

Some question papers may be scanned PDFs rather than text PDFs.

The application will eventually support:

Scanned PDF
     ↓
OCR
     ↓
Extracted Text
     ↓
Question Extraction

This will allow scanned/image-based question papers to be analyzed.

---

🤖 AI Integration

AI will be added after the basic analysis pipeline is working.

Possible AI features:

- Semantic question matching
- Question normalization
- Topic identification
- Chapter mapping
- Unit classification
- Syllabus understanding
- Improved duplicate detection
- Question summarization

The application should be designed so that the core application does not depend entirely on a paid AI API.

---

🏗️ Planned Project Structure

The project will eventually use a modular structure:

AI-PYQ-Analyzer/
│
├── app.py
│
├── pdf_processor.py
├── ocr_processor.py
├── question_extractor.py
├── question_cleaner.py
├── question_matcher.py
├── chapter_mapper.py
├── exam_detector.py
├── ai_analyzer.py
├── database.py
├── exporter.py
├── utils.py
│
├── requirements.txt
├── README.md
│
└── data/

---

🔄 Overall Processing Pipeline

                 PYQ PDF FILES
                       │
                       ↓
                PDF TEXT EXTRACTION
                       │
                       ↓
                 OCR IF REQUIRED
                       │
                       ↓
                QUESTION EXTRACTION
                       │
                       ↓
                 QUESTION CLEANING
                       │
              ┌────────┴────────┐
              ↓                 ↓
       SEASON/YEAR         QUESTION MATCHING
              ↓                 ↓
           W21/S21        SAME CONCEPT?
                                │
                                ↓
                         REPEATED QUESTIONS
                                │
                 ┌──────────────┴──────────────┐
                 ↓                             ↓
           UNIT/CHAPTER                    FREQUENCY
                 │                             │
                 └──────────────┬──────────────┘
                                ↓
                         FINAL RESULTS

---

💻 Development Environment

Current development environment:

GitHub
   ↓
GitHub Codespaces
   ↓
Python
   ↓
Streamlit

The application is being developed primarily as a web application and can be accessed through a browser.

---

📦 Current Dependencies

The initial project uses:

streamlit
pandas
PyMuPDF
openpyxl
rapidfuzz
scikit-learn

Install them with:

pip install -r requirements.txt

---

🧪 Development Principle

The application will be developed incrementally.

The recommended order is:

PDF Upload
     ↓
PDF Extraction
     ↓
Question Extraction
     ↓
Question Cleaning
     ↓
Season/Year Detection
     ↓
Repeated Question Detection
     ↓
Syllabus Mapping
     ↓
Chapter-Wise Organization
     ↓
Search & Filters
     ↓
Statistics
     ↓
Export
     ↓
AI Enhancement
     ↓
OCR

Each stage should be tested before moving to the next stage.

---

🎯 Final Goal

The final application should allow a student to upload multiple previous-year question papers and automatically generate an organized, searchable question bank showing:

Unit
Chapter
Question
Exam Season
Exam Year
Number of Occurrences
Occurrence History

Example:

Unit 1 → Finite Automata

What is Extra Closure?
(W21, S21)

Frequency: 2

The goal is to make PYQ analysis faster, more organized, and easier to use for exam preparation.# AI-PYQ-Analyzer
AI-powered previous year question paper analyzer
