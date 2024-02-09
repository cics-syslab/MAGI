# MAGI - Modular Assignment Generator & Inspector

## Description

MAGI is a python framework for generating programming assignments and autograders for Gradescope, with extensible modules and plugins.

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

![Windows Badge](https://img.shields.io/badge/Windows-Supported-green)
![macOS Badge](https://img.shields.io/badge/macOS-Supported-green)
![Linux Badge](https://img.shields.io/badge/Linux-Supported-green)
![x86 Badge](https://img.shields.io/badge/x86-Supported-green)
![x64 Badge](https://img.shields.io/badge/x64-Supported-green)
| Platform/Architecture | Status        |
|-----------------------|---------------|
| Windows               | Supported     |
| macOS                 | Supported     |
| Linux                 | Supported     |
| x86                   | Supported     |
| x64                   | Supported     |
| ARM                   | Supported with limited feature |
---

## Quick Start

The easiest way to get started with our application is by using our pre-built [Docker](https://www.docker.com/) image.

```bash
docker run -d --name magi -p 8501:8501 -v ./settings:/app/settings ghcr.io/cics-syslab/magi:latest
```

### Docker Compose
```yaml
version: '3'
services:
  magi:
    image: ghcr.io/cics-syslab/magi:latest
    volume:
      - ${pwd}/settings:/app/settings
    network_mode: bridge
    ports:
      - "8501:8501"
```

## Building from Source

If you prefer to build the application from source, follow the instructions in the [Build](https://github.com/cics-syslab/MAGI/wiki/Build) page.

## Usage

Access the web interface through http://host:port
<!-- Start the gui


```bash

```

The interface is organized into tabs, with two default tabs: Preview and Basic Settings. When you enable different modules or plugins, their respective settings (if available) will appear in newly created tabs.

### Basic Settings

This page includes the generic information about the assignment and overall settings. The attributes are listed below,
  
- Project Name:
The title for the project and also the name shown on the generated material such as the documentation.

- Project Desc:
Optional. A paragraph long brief description for the project. Could be a scenario or something related.

- Submission Files:
A list of file required for submission. In case of the student's submission doesn't include one or more files in the list, the autograder will not run or produce the test result but throws an error message to notify the student.

- Enabled Module:
Choose the module you wish to use. Please note that modules are mutually exclusive, allowing only one module to be enabled at a time.

  List of modules currently available:
  - [Network Project Engine](https://github.com/nightdawnex/gsgen/tree/main/modules/NetworkProjectEngine)
  
<!-- - [Thread Project Engine](https://github.com/nightdawnex/gsgen/tree/main/modules/ThreadingProjectEngine) -->

<!-- - Enabled Plugins:
Select the plugins you want to use. You can enable multiple plugins simultaneously.

  List of Plugins currently available: -->

<!-- ### Preview

On the preview page, you can choose where to generate the output project files.

The files will be generated in a folder named after the project. If the folder already exists, it will be appended with the current time. -->

### Upload the autograder to Gradescope 

In gradescope, select Ubuntu-22.04 as base image and upload the generated zip file. 

<!-- For more detailed usage instructions, please refer to the [User Guide](link-to-user-guide.md). -->
<!-- ---

## Contributing

We welcome contributions! Please check out our [CONTRIBUTING.md](link-to-contributing-guide.md) for guidelines. -->

---

## Support & Feedback

For support or to provide feedback, please raise an issue on our [GitHub repository](https://github.com/cics-syslab/MAGI).

---

## License

MAGI is released under the [MIT License](LICENSE).

---

## Acknowledgments

Special thanks to the community and everyone who contributed to making this project possible.

---

## Changelog


For a detailed changelog, refer to the [Changelog page](https://github.com/cics-syslab/MAGI/wiki/Changelog).

---
