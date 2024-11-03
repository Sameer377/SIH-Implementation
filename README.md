

# Social Media Forensic Data Parsing Tool : SIH1743
Author & Dev : Sameer Shaikh


## Project Overview

This project is a **Social Media Forensic Data Parsing Tool** designed for forensic investigators to streamline the collection, documentation, and analysis of social media data. It automatically captures and organizes screenshots of various social media activities (such as posts, messages, timelines, friend lists, followers, account info) from platforms like **Facebook**, **Instagram**, **WhatsApp**, **Twitter**, **Telegram**, and **Google Accounts**. By automating the process, this tool reduces human error, improves efficiency, and supports forensic investigations by enabling prompt-based searching and data documentation in structured formats.

## Key Features

1. **Automated Social Media Parsing**: Captures and organizes data from social media feeds, including posts, messages, and multimedia.
2. **Cross-Platform Support**: Supports both **Android** and **Windows** platforms to ensure compatibility with various devices.
3. **AI-Powered Content Analysis**: Uses **Natural Language Processing (NLP)** and **Image Recognition** to optimize data extraction and filter information based on prompts.
4. **Log File Creation**: Generates JSON logs containing metadata, context, and image paths for each screenshot.
5. **Prompt-Based Searching**: Allows investigators to search data based on custom prompts and extract relevant screenshots.
6. **PDF Export**: Compiles selected screenshots and associated data into a PDF or CSV file for documentation and reporting.

## Requirements

- **Operating Systems**: Android and Windows
- **Technologies and Frameworks**:
  - **Python**: Core programming language
  - **Libraries**:
    - **Tkinter** and **PyQt** for GUI
    - **OpenCV** for image processing
    - **NLTK**, **spaCy**, and **Transformers** for NLP
    - **TensorFlow** and **PyTorch** for machine learning and image recognition
    - **PyCryptodome** for encryption and security
    - **ReportLab** and **PyPDF2** for PDF generation
    - **SpeechRecognition** for handling audio files
  - **APIs**:
    - **Facebook Graph API** and other platform-specific APIs for data extraction
    - **ADB (Android Debug Bridge)** for Android automation
    - **OCR APIs** for text extraction from images

## Solution Architecture

The tool combines **data extraction**, **AI-powered analysis**, and **automated documentation** in a structured approach. Here’s an overview of the process:

### 1. Platform Integration & Adaptive Extraction
   - **Platform Selection**: Select the platform (WhatsApp, Instagram, etc.) to parse data from.
   - **API Integration**: Integrate with platform-specific APIs (like Facebook Graph API) to access social media data.
   - **Manual Extraction** (if required): Use **Android automation with ADB** to extract data if API access is limited.

### 2. Data Categorization & Organization
   - **Automatic Section Classification**: Classifies data into categories like chats, posts, media, and metadata.
   - **Content Optimization Using AI**:
     - **NLP**: Processes text content to detect entities, filter keywords, and create contextual information.
     - **Image Recognition**: Analyzes media content for context and descriptions.
   - **Creating Log File (JSON)**: Logs extracted data with metadata, including timestamps, paths, and content summaries.

### 3. Searching and Documentation
   - **Context Detection**: Uses topic modeling, named entity recognition, and keyword filtering to create search-ready data.
   - **Prompt Searching**: Enables investigators to search data based on custom prompts, filtering screenshots by relevance.
   - **Documentation Generation**: Compiles selected screenshots and data into PDF or CSV files for reporting.

### 4. Log File Creation
   - **Textual and Graphical Content Processing**: Uses OCR and image recognition to convert graphical content into searchable text.
   - **Audio File Processing**: Utilizes speech-to-text for converting audio files into searchable text.
   - **Natural Language Processing (NLP)**: Creates contextual information for the content using **Artificial Neural Networks (ANN)**.
   - **Log Generation**: Stores the processed content into structured log files with metadata for further analysis.

### Example JSON Log Structure
Each screenshot log entry contains metadata including ID, path, timestamp, and context description:

```json
{
    "id": 8,
    "path": "D:\\screenshot2.png",
    "timestamp": "2024-09-15T18:45:00Z",
    "context": "A red bus with 14 wheels, 40 students seated inside that bus"
}
```

### Example Prompt-Based Search
The tool allows investigators to search using prompts, providing a streamlined interface to filter relevant images:

```
Enter prompt: a girl in a vehicle
Enter threshold: 0.3
Selecting Images....
File ID: 8
Path: D:\OneDrive\Desktop\raw\usecase.png
Generating PDF.....
```

## Technical Approach

![Technical Approach](image.png)


### Workflow

1. **Platform Integration & Adaptive Extraction**: 
   - Integrate with APIs like **Facebook Graph API** and use **ADB** for Android data extraction.
   
2. **Data Categorization & Organization**:
   - AI-based **Content Optimization** for text, images, and metadata categorization.
   - **Log File Creation** for storing structured data in JSON format.

3. **Searching and Documentation**:
   - Context-based filtering with **Prompt Searching** and **Context Detection**.
   - **Documentation Generation** with selected images in **PDF/CSV** format.

### Log File Creation

- **Textual/Graphical Content Processing**:
  - Uses **OCR** and **Image Recognition** to convert images into text.
  - **NLP** and **ANN** for context generation and search readiness.

- **Audio File Processing**:
  - **SpeechRecognition** library is used to convert audio files to text.

## Technologies Used

- **Python** (core programming language)
- **Tkinter** and **PyQt** (GUI)
- **OpenCV** (Image processing and OCR)
- **NLTK**, **spaCy**, and **Transformers** (NLP)
- **TensorFlow** and **PyTorch** (Machine learning)
- **PyCryptodome** (Security and encryption)
- **ADB (Android Debug Bridge)** (Android automation)
- **ReportLab** and **PyPDF2** (PDF generation)
- **SpeechRecognition** (Audio file processing)
- **Platform APIs** (Facebook Graph API, Instagram API, etc.)

## Setup Instructions

1. **Install Dependencies**: Install the necessary Python libraries.

   ```bash
   pip install opencv-python-headless
   pip install nltk
   pip install spacy
   pip install transformers
   pip install tensorflow
   pip install torch
   pip install pycryptodome
   pip install reportlab
   pip install PyPDF2
   pip install SpeechRecognition
   ```

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/social-media-forensic-parser.git
   cd social-media-forensic-parser
   ```

3. **Run the Application**:

   ```bash
   python main.py
   ```

4. **Configure API Access**: Follow documentation to configure API credentials for platforms (Facebook, Instagram, etc.).

## Usage

1. Launch the tool and select the social media platform.
2. Connect via API or automation (e.g., ADB for Android).
3. Start parsing data to automatically capture and document screenshots.
4. Use prompt-based searching to filter data.
5. Export selected data into PDF/CSV format for reporting.

## Mind Map (Technical Approach Overview)

Here’s a suggested mind map structure based on the technical flow:

- **Social Media Forensic Data Parsing Tool**
  - **Platform Integration**
    - Platform Selection (WhatsApp, Instagram, etc.)
    - API Integration (Facebook Graph API, etc.)
    - Manual Extraction (ADB for Android automation)
  - **Data Categorization & Organization**
    - Automatic Section Classification
    - Content Optimization (NLP, Image Recognition)
    - Log File Creation (JSON)
  - **Searching and Documentation**
    - Context Detection (NLP, Entity Recognition)
    - Prompt-Based Search
    - Documentation Generation (PDF, CSV)
  - **Log File Creation**
    - Textual and Graphical Content Processing (OCR, Image Recognition)
    - Audio File Processing (SpeechRecognition)
    - NLP and ANN for Context
    - Generate Log File


