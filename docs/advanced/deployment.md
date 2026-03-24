# Deployment Guide

This guide covers deploying the application to production.

## Configuration

Before deploying, review the [configuration file](../../src/config.yaml).

## Steps

1. Run tests
2. Build the application
3. Deploy to server

## Rollback

If issues arise, refer to the [Getting Started](../getting-started.md) guide or the [main README](../../README.md).

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_PORT` | Server port | `8080` |
| `APP_ENV` | Environment | `production` |
| `DB_HOST` | Database host | `localhost` |
