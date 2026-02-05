# SafeSend 🔐

**SafeSend** is a secure file transfer system that enables encrypted file sharing using the **Diffie-Hellman Key Exchange** protocol and **AES encryption**. The project consists of a web application for cloud storage and a desktop application for local encryption/decryption.

## 📑 Table of Contents

- [Features](#-features)
- [Security Features](#-security-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
    - [Running the Web Application](#running-the-web-application)
    - [Running the Desktop Application](#running-the-desktop-application)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Configuration](#️-configuration)
- [Troubleshooting](#-troubleshooting)
- [Author](#-author)

## 🌟 Features

### Web Application

- **User Registration**: Generate unique public/private key pairs
- **Cloud Storage**: Upload and store encrypted files
- **File Directory**: Browse and download encrypted files
- **Public Key Directory**: Access public keys of registered users
- **Modern UI**: High-contrast, professional dark theme

### Desktop Application

- **File Encryption**: Encrypt files using receiver's public key
- **File Decryption**: Decrypt files using sender's public key
- **Modern GUI**: Clean, tabbed interface with real-time status
- **Quick Access**: Direct links to web application features

## 🔒 Security Features

- **Diffie-Hellman Key Exchange**: Secure key generation and exchange
- **AES Encryption**: Industry-standard symmetric encryption
- **End-to-End Encryption**: Files are encrypted before upload
- **No Key Storage**: Private keys are never stored on the server
