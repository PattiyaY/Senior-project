# System Architecture Diagram Overview

## User

The user interacts with the system, initiating communication with the **Frontend** cluster.

## Frontend Cluster

- **NextJS**: Serves as the main user interface for the application, connecting directly to **NextAuth.js** for authentication and **GitLab** for user management.

## Backend Cluster

- **MongoDB**: Acts as the primary database, receiving and storing data from the **RabbitMQ** message broker.
- **RabbitMQ**: Functions as a message broker, facilitating communication between the Frontend and Backend. It manages message queues for processing requests and responses.
- **Terraform**: Responsible for infrastructure as code (IaC), allowing for automated provisioning and management of resources.
- **Azure VM**: Managed by **Terraform**, this represents the cloud infrastructure that hosts the backend services.
