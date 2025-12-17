# Wine Cellar Management System

## Overview
This repository contains a microservice-based web application developed as a mandatory project
for the course **Continuous Integration and Delivery (KIII)**.

The project demonstrates the complete CI/CD lifecycle, including containerization,
automation pipelines, and Kubernetes-based deployment.

## Application Description
The Wine Cellar Management System allows users to manage a personal wine collection.
Users can store information about wines, including type, year, region, and quantity,
and receive basic recommendations.

## System Architecture
The system is composed of the following services:
- Frontend service (server-rendered web UI)
- Backend REST API service
- Wine recommendation microservice
- MongoDB database

Each service is containerized and deployed independently.

## Technologies
- Frontend: Django Templates (HTML/CSS)
- Backend: Django REST Framework
- Recommendation service: FastAPI
- Database: MongoDB
- Containerization: Docker, Docker Compose
- CI/CD: GitHub Actions
- Orchestration: Kubernetes

## Project Structure
- frontend/ - Frontend application
- backend/ - Backend REST API
- recommender/ - Recommendation microservice
- docker/ - Docker configuration files
- k8s/ - Kubernetes manifests
- docs/ - Documentation and project elaboration


## Project Status
Initial project setup and architecture definition completed.
