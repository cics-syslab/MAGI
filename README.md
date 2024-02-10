# MAGI - Modular Assignment Generator & Inspector

## Description

MAGI is a python framework for generating programming assignments and autograders for Gradescope, with extensible
modules and plugins.

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

![Windows Badge](https://img.shields.io/badge/Windows-Supported-green)
![macOS Badge](https://img.shields.io/badge/macOS-Supported-green)
![Linux Badge](https://img.shields.io/badge/Linux-Supported-green)
![x86 Badge](https://img.shields.io/badge/x86-Supported-green)
![x64 Badge](https://img.shields.io/badge/x64-Supported-green)
| Platform/Architecture | Status |
|-----------------------|---------------|
| Windows | Supported |
| macOS | Supported |
| Linux | Supported |
| x86 | Supported |
| x64 | Supported |
| ARM | Supported with limited feature |
---

## Documentation

For detailed documentation, please visit our [GitHub Wiki](https://github.com/cics-syslab/MAGI/wiki).

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
    container_name: magi
    image: ghcr.io/cics-syslab/magi:latest
    volume:
      - ${pwd}/settings:/app/settings
    network_mode: bridge
    ports:
      - "8501:8501"
```

## Building from Source

If you prefer to build the application from source, follow the instructions in
the [Build](https://github.com/cics-syslab/MAGI/wiki/Build).

## Usage

Access the web interface through http://host:port

For detailed usage instructions, please refer to [Usage](https://github.com/cics-syslab/MAGI/wiki/Usage).

## Contributing

We welcome contributions! Please check out our [Contributing](https://github.com/cics-syslab/MAGI/wiki/Contributing)
page for guidelines.

---

## Support & Feedback

For support or to provide feedback, please raise an issue on
our [GitHub repository](https://github.com/cics-syslab/MAGI/issues).

---

## License

MAGI is released under the [MIT License](LICENSE).

---

## Acknowledgments

Special thanks to the community and everyone who contributed to making this project possible.

---

## Changelog

For a detailed changelog, refer to [Changelog](https://github.com/cics-syslab/MAGI/wiki/Changelog).

---

<!-- TODO: Code of Conduct -->
<!-- TODO: Creative Commons license -->
