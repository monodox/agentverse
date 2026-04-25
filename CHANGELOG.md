# Changelog

All notable changes to AgentVerse will be documented in this file.

This project follows a simple changelog format while it is in early development.

## [Unreleased]

### Added

- TypeScript SDK package (`@agentverse/sdk`) mirroring the Python public API.
- npm workspaces monorepo structure with `packages/python` and `packages/npm`.
- CI workflow for Node.js alongside existing Python CI.

### Changed

- Restructured repository as a monorepo. Python package moved to `packages/python/`, TypeScript SDK lives in `packages/npm/`.
- Updated root README, .gitignore, and CI workflow for monorepo layout.

## [0.1.1] - 2026-04-25

### Added

- Initial haptics-first project documentation.
- Basic architecture, getting started, and API reference docs.
- Requirements file for simulation, ML, RL, data, visualization, and dev tooling.
- Open-source project files for security, conduct, contribution, roadmap, and environment setup.

### Changed

- Updated package metadata to reflect AgentVerse by Haptis.

## [0.1.0] - 2026-04-25

### Added

- Initial Python package scaffold.
- Base agent and environment interfaces.
- Haptic, robot, model, training, and simulation placeholders.
- Example scripts, tests, configs, and documentation skeleton.
