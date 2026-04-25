# Security Policy

## Supported Versions

AgentVerse is currently in early pre-alpha development. Security fixes are applied to the latest version on the main development branch.

## Reporting a Vulnerability

Please do not open a public issue for suspected security vulnerabilities.

Report security concerns by emailing the maintainers or opening a private security advisory if the repository host supports it. Include:

- A short description of the vulnerability.
- Steps to reproduce the issue.
- The affected files, versions, or configurations.
- Any known impact or workaround.

We will acknowledge valid reports as soon as possible and coordinate fixes before public disclosure.

## Scope

Security reports may include:

- Unsafe dependency behavior.
- Secret leakage.
- Unsafe file or model loading.
- Remote code execution risks.
- Insecure default configuration.
- Data handling issues in simulation, training, or logging flows.

## Dependency Security

AgentVerse depends on simulation, ML, and infrastructure packages. Contributors should keep dependencies current and avoid adding packages that are unmaintained, unnecessary, or overly broad in permission scope.
