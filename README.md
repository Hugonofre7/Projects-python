# DevOps Toolkit

CLI utility for log parsing, service health simulation, and HTTP endpoint monitoring. Built as a Python systems automation project, integrating regex-based log parsing, structured data export, object-oriented service modeling, and production-style logging into a single command-line tool.

## Overview

devops_toolkit.py consolidates several independent automation modules into one entry point with three core actions:

ActionPurposeparseParses raw log files with regex, filters invalid entries, and exports structured results to JSON and CSV.fallaSimulates a service failure within a small modeled infrastructure and propagates cascading effects to dependent services.monitorPolls a list of HTTP endpoints at a fixed interval and logs their availability to console and file simultaneously.

Usage

bash# Parse a raw log file and export structured data
python3 devops_toolkit.py --action parse --file system.log --output reporte.json

# Simulate a failure in a modeled service and observe cascading effects
python3 devops_toolkit.py --action falla --servicio mysql

# Monitor a list of URLs, logging status every interval
python3 devops_toolkit.py --action monitor --urls https://example.com https://github.com --log monitor.log

## Project Architecture

The project is divided into independent modules that are integrated through a CLI interface.

```text
devops-toolkit/
```
├── devops_toolkit.py
├── log_cleaner.py
├── data_exporter.py
├── monitorear_servicios.py
├── servicio.py
├── tests/
│   └── test_servicio.py
├── logs/
└── README.md

Module Details
devops_toolkit.py

Main CLI entry point.

Responsible for:

parsing command arguments
routing actions
integrating project modules

Available commands:

--action parse
--action monitor
--action falla
log_cleaner.py

Processes log files using regular expressions.

Expected format:

TIMESTAMP LEVEL [SERVICE] MESSAGE

Example:

2026-06-01 10:20:30 ERROR [mysql] Connection failed

The parser extracts structured information:

{
    "timestamp": "...",
    "level": "ERROR",
    "service": "mysql",
    "message": "Connection failed"
}

Invalid lines are ignored instead of raising exceptions.

data_exporter.py

Handles structured data serialization.

Supports:

JSON export
CSV export

Example:

[
    {
        "service": "mysql",
        "level": "ERROR",
        "status": "error"
    }
]
monitorear_servicios.py

Provides HTTP health monitoring.

Features:

URL availability checks
HTTP status validation
console logging
file logging

Uses:

requests
Python logging
servicio.py

Defines the Servicio class.

Models a system service with:

name
state
port
dependencies

Example:

Servicio(
    "mysql",
    "activo",
    3306,
    []
)

The method:

simular_falla()

simulates service failure and propagates affected states to dependent services.

Example:

Before:

[ACTIVO] nginx
[ACTIVO] mysql
[ACTIVO] api

After mysql failure:

[AFECTADO] nginx
[ERROR] mysql
[AFECTADO] api

This represents a simplified model of cascading failures in distributed systems.

Installation

Clone the repository:

git clone <repository-url>

cd devops-toolkit

Create a virtual environment:

python3 -m venv .venv

Activate it:

macOS / Linux:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Usage
Parse logs

Parse a log file and export results:

python3 devops_toolkit.py \
--action parse \
--file system.log \
--output report.json

Output:

report.json
report.csv
Monitor services

Monitor HTTP endpoints:

python3 devops_toolkit.py \
--action monitor \
--urls https://example.com https://github.com \
--log monitor.log
Simulate service failure

Simulate failure propagation:

python3 devops_toolkit.py \
--action falla \
--servicio mysql
Testing

Run unit tests:

pytest tests/ -v

Current tests validate:

object creation
service state changes
failure propagation
Technologies
Python 3
argparse
requests
logging
JSON
CSV
pytest
Concepts Applied

This project applies:

Object-Oriented Programming
Modular design
Separation of responsibilities
Error handling
Logging practices
CLI development
Data processing
Automated testing
Future Improvements

Possible extensions:

Load services from JSON/YAML configuration
Add Docker container health checks
Add webhook/email notifications
Add persistent storage
Add REST API interface
Add asynchronous monitoring
Add configuration management system
Improve service dependency graph analysis
Author

Hugo Nofre

GitHub:
https://github.com/Hugonofre7