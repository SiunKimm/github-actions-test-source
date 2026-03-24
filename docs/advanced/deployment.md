# Deployment Guide

This guide covers deploying the application to production.

## Configuration

Before deploying, review the [configuration file](../../src/config.yaml).

## Prerequisites

- Docker 24+
- Access to container registry

## Steps

1. Run tests
2. Build Docker image
3. Push to container registry
4. Deploy to Kubernetes cluster

## Rollback

If issues arise, refer to the [Quickstart](../quickstart.md) guide or the [main README](../../README.md).

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_PORT` | Server port | `3000` |
| `APP_ENV` | Environment | `production` |
| `DB_HOST` | Database host | `db.example.com` |
| `REDIS_URL` | Redis connection | `redis://localhost:6379` |
