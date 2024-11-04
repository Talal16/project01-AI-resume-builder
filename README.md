# project01-AI-resume-builder

AI CV Maker is a web application designed to assist users in creating professional CVs using audio recordings or text input. The application leverages advanced AI technologies for transcription and CV generation, providing a seamless and user-friendly experience.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features
- User registration and authentication
- Transcription of audio recordings using OpenAI's Whisper API
- Generation of CVs from transcribed text using Gemini AI
- Storage and management of chat history and generated PDFs
- Intuitive user interface built with Streamlit

## Technologies Used
- **Backend**: 
  - FastAPI: A modern web framework for building APIs with Python.
  - SQLAlchemy: An ORM (Object Relational Mapping) tool for database management.
  - SQLite: A lightweight database for development (can be replaced with other databases like PostgreSQL or MySQL).
  - Passlib: A password hashing library for securing user credentials.
  - Jose: A library for creating and verifying JWT tokens.

- **Frontend**:
  - Streamlit: A framework for building interactive web applications using Python.

- **APIs**:
  - OpenAI Whisper: For converting audio recordings to text.
  - Gemini AI: For generating CVs from text input.

## Requirements
- Python 3.8 or higher
- Libraries:
  - fastapi
  - sqlalchemy
  - passlib
  - jose
  - streamlit
  - requests
  - pydantic

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai_cv_maker.git
   cd ai_cv_maker
