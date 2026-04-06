# KN Demo Session

This project demonstrates setting up a Python virtual environment and running Python applications using UV (a fast Python package manager).

## Project Overview

This is a simple demo project that showcases how to:
- Install and configure UV package manager
- Set up a Python 3.12 virtual environment
- Manage dependencies with UV
- Run Python scripts

## Prerequisites

- macOS or Linux system
- Bash or Zsh shell
- Internet connection for downloading packages

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Install UV Package Manager

UV is a fast, modern Python package manager written in Rust. Install it using:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

After installation, reload your shell configuration:

```bash
source ~/.zshrc
```

Verify the installation:

```bash
uv --version
```

### 2. Install Python 3.12

Install Python 3.12 using UV:

```bash
uv python install 3.12
```

Pin the project to use Python 3.12:

```bash
uv python pin 3.12
```

### 3. Initialize and Configure Project

Initialize the project with UV (creates `pyproject.toml`):

```bash
uv init
```

Sync dependencies to create the virtual environment:

```bash
uv sync
```

### 4. Add Dependencies

Add the required dependencies. For example, to add NumPy:

```bash
uv add numpy
```

This will update `pyproject.toml` and `uv.lock` files automatically.

### 5. Activate Virtual Environment (Optional)

If you need to directly activate the virtual environment:

```bash
source .venv/bin/activate
```

## Running the Project

To run the main Python script:

```bash
uv run python hello_world.py
```

Or if you have other Python scripts:

```bash
uv run python main.py
```

## Project Files

- `hello_world.py` - Simple hello world example
- `main.py` - Main application file
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Locked dependencies for reproducible builds
- `.gitignore` - Git ignore configuration
- `.python-version` - Python version specification

## Benefits of Using UV

- **Fast**: Written in Rust for optimal performance
- **Simple**: Easy to use command-line interface
- **Reliable**: Lockfile ensures reproducible environments
- **Modern**: Actively maintained and regularly updated

## Notes

- UV handles virtual environment creation automatically
- The `.venv` directory contains your isolated Python environment
- Use `uv add <package>` to add new dependencies
- Use `uv remove <package>` to remove dependencies
- Always commit `uv.lock` to version control for reproducibility

## Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [Python.org](https://www.python.org/)

## License

MIT
