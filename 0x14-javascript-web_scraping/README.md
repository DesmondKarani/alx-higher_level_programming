# JavaScript Web Scraping Project

This project focuses on demonstrating the fundamentals of web scraping, JSON data manipulation, and file I/O operations in JavaScript. It provides a hands-on approach to learning how to interact with the web programmatically using JavaScript and Node.js.

## Overview

The objectives of this project include understanding how to:

- Manipulate JSON data effectively.
- Utilize the `request` module and the Fetch API for making HTTP requests.
- Perform read and write operations on files using the `fs` module.

## Environment Setup

### Prerequisites

- Ubuntu 20.04 LTS
- Node.js version 14.x

### Installation Guide

1. **Install Node.js v14:**

```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

2. **Install Semi-Standard Linter:**

```bash
sudo npm install semistandard --global
```

3. **Install the Request Module (Deprecated):**

```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

*Note: The `request` module is deprecated. For new projects, consider using `fetch` or `axios`.*

## Project Structure

- `src/`: Contains all the source code for web scraping and data manipulation.
- `data/`: Directory where scraped data and manipulated JSON files are stored.
- `scripts/`: Utility scripts to run the project and perform tasks.

## Usage

To run a script, navigate to the project directory and execute:

```bash
./your_script_name.js
```

Ensure that your scripts have the executable permission:

```bash
chmod +x your_script_name.js
```

## Contributing

This project is for educational purposes. Contributions, issues, and feature requests are welcome!

## License

This project is [MIT licensed](LICENSE).

## Acknowledgments

- Thanks to Cohort 1 - San Francisco for insights into JSON data manipulation.
- Node.js documentation for providing guidance on `fs` module operations.
