"""Utility functions for the application."""


def format_response(message, **kwargs):
    """Format a standard response."""
    return {"message": message, **kwargs}


def validate_config(config):
    """Validate configuration values."""
    required = ["app", "database"]
    for key in required:
        if key not in config:
            raise ValueError(f"Missing required config: {key}")
    return True
