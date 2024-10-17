# Senior-project (IDP System Architecture)

## Overview

This repository contains the implementation of the system architecture for an Identity Provider (IDP) application. It features a structured approach to managing user authentication, data storage, and infrastructure provisioning.

## Architecture Components

### User

- The user interacts with the system, initiating communication with the **Frontend** cluster.

### Frontend Cluster

- **React**: The main user interface for the application, facilitating user interactions.
- **NextAuth.js**: Provides authentication services, managing user sessions and security.
- **GitLab**: Used for user management, version control, and collaboration.

### Backend Cluster

- **MongoDB**: The primary database for storing user data and application-related information.
- **RabbitMQ**: Acts as a message broker, facilitating communication between the Frontend and Backend, and managing message queues for request processing.
- **Terraform**: Implements infrastructure as code (IaC) for automated provisioning and management of cloud resources.
- **Azure VM**: Represents the cloud infrastructure managed by Terraform, hosting the backend services.

## Features

- Seamless user authentication and management.
- Robust data storage and retrieval using MongoDB.
- Efficient communication between components through RabbitMQ.
- Automated infrastructure provisioning with Terraform on Azure.

## Getting Started

To set up the project locally, follow these steps:

1. **Install Graphviz and Diagram**:

   - For macOS users, download Graphviz via Homebrew:
     ```bash
     brew install graphviz
     ```
   - For Windows users with Chocolatey installed, run:
     ```bash
     choco install graphviz
     ```

   - Install Diagrams
      ```bash
      pip install diagram
      ```

2. **Clone the repository**:

   ```bash
   git clone <repository-url>
   ```

3. **Run the application**:
   ```bash
   python filename.py
   ```
   or
   ```bash
   python3 filename.py
   ```
