"""Main application entry point."""

from utils import format_response


def main():
    """Start the application."""
    print("Starting Test Migration Project v2.0")
    print("Loading configuration...")
    print(format_response("Server ready", port=3000))


if __name__ == "__main__":
    main()
