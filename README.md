# 🧠 DocSearch – Cloud-Based Document Search API

**DocSearch** is a scalable, searchable document indexing system that extracts content from various document types (PDF, TXT, CSV, PNG), stores them in PostgreSQL, and provides a search API using FastAPI. Documents are sourced from an AWS S3 bucket and indexed only if not previously stored.

---

## 📚 Features

- 🔍 Full-text search using PostgreSQL's `tsvector` indexing  
- ☁️ Seamless document ingestion from AWS S3  
- 📄 Support for multiple file formats: `.txt`, `.pdf`, `.csv`, `.png`  
- ⚡ FastAPI-based REST API for document querying  
- 🔐 Duplicate indexing prevention  
- 🧱 Modular architecture with clean separation of concerns  

---

## 🧰 Tech Stack

| Component      | Tech                        |
|----------------|-----------------------------|
| Backend        | [FastAPI](https://fastapi.tiangolo.com/) |
| Search Engine  | PostgreSQL (with full-text indexing) |
| Cloud Storage  | AWS S3                      |
| File Parsers   | PyMuPDF, pandas, pytesseract, Pillow |
| ORM/DB Driver  | psycopg2                    |
| Language       | Python 3.10+                |

---

## 🚀 How It Works

```
[S3 Bucket]
     |
     |   → Supported File (.pdf, .txt, .csv, .png)
     |
[Extractor Factory] → Parse Content
     |
     ↓
[PostgreSQL Database with Full-Text Index]
     |
     ↓
[FastAPI] → /search?key=invoice → [Results]
```

---

## 📦 Project Structure

```

├── data
├── notebooks
├── src
│    └── core/
│         └── main.py                          # FastAPI app with /search endpoint
│         └── schema.py                        # Pydantic models (request & response)
│    └── infrastructure/
│         └── cloud/
│               └── s3_client.py               # AWS S3 interaction
│         └── index/
│               └── postgress_client.py        # PostgreSQL client
│    └── utils
│         ├── extractor_factory.py             # Chooses extractor based on file type
│         ├── txt_extractor.py
│         ├── pdf_extractor.py
│         ├── csv_extractor.py
│         └── image_extractor.py
│    └── main_pipeline.py                      # Indexes new documents from S3
├── README
├── requirements.txt


```

### . 🛠️ Setup & Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/Salmanvaliyakath/DocSearcher.git
cd docsearch
```

### 2. Set up environment variables (AWS credentials)

Ensure your AWS credentials are configured:
```bash
aws configure
```

Or use `.env` for boto3 (if extended).

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

Ensure PostgreSQL is running with:
- DB: `docsearch`
- User: `postgres`
- Password: `********`

> You can modify credentials in `postgress_client.py`.

### 5. Run document indexing

```bash
python src/main_pipeline.py
```

### 6. Start FastAPI server

```bash
uvicorn src.main:app --reload
```

Visit API docs at:  
📎 [`http://localhost:8000/search`](http://localhost:8000/search)

---

## 🔍 Sample API Usage

### ➕ Indexing Documents

```bash
python src/main_pipline.py
```

> Downloads files from S3 → Extracts content → Indexes into PostgreSQL.

---

### 🔎 Search API

```
GET /search?key=your key word
```

**Response:**
```json
{
  "results": [
    { "file_name": "fiename-1.pdf" },
    { "file_name": "fiename-2.txt" }
  ]
}
```

---

## 🔮 Future Enhancements

- [ ] Support `.docx`, `.xlsx`, `.jpg`
- [ ] Dockerize the project with `docker-compose`


---
