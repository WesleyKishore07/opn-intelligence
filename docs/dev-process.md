# Software Development Process Guide

## Overview

This document outlines the mandatory development process for all contributors. Following these
guidelines ensures consistent code quality and smooth integration with our systems.

## Pre-requisites

Before beginning development work:

- Access and review provided Git codebase
- Review and understand coding guidelines, architecture..etc mentioned in the git ReadMe
- Set up development environment (Refer to README.md)
- Understand branching strategy and version control workflow (Refer to [Branching strategy](branching-strategy.md))
- Complete any required training or documentation review
- Verify access to necessary internal tools and resources (JIRA, Git, CI/CD..etc)

## Development Workflow

### 1. Story Assignment

- Receive JIRA story assignment
- Review acceptance criteria and requirements thoroughly

### 2. Design Phase

- Create git feature branch out of the corresponding release-* or dev branch following naming
  convention: `feature/JIRA-ID-feature-name`
- Create design document addressing: (Use this [DesignTemplate](design/design-template.md))
    - Proposed solution architecture
    - Data flow diagrams (if applicable)
    - API specifications (if applicable)
    - Database changes (if applicable)
    - Security considerations
    - Performance considerations
- Submit design for review
- Incorporate feedback

### 3. Development Phase

- Regular code commits (at least daily) - (feature branches can be pushed to remote frequently even
  if its not fully complete)
- Follow provided coding guidelines for Python/Java
- Maintain comprehensive unit test coverage (Mainly cover the framework components, key processing
  logic/components)
- Document all key methods and classes (Documentation not needed for obvious ones like Pojo's..etc)

### 4. Quality Checks Before PR

Mandatory checks before raising PR:

- Run all unit tests locally
- Execute static code analysis
- Verify code coverage meets minimum threshold (>80%)
- Self-review the complete changeset

### 5. Pull Request Process

PR must include:

- Update the key details in the PR template (below are some of the key things)
    - Clear description referencing JIRA story
    - Screenshots/videos of UI changes (if applicable)
    - Test results and coverage reports
    - Design document link
    - Database migration scripts (if applicable)
    - Deployment instructions

### 6. PR Review and Fixes

- Check for any build, test, quality check failures reported by the CI/CD process and fix them
- Address all reviewer comments promptly
- Update PR with requested changes
- Re-request review after implementing changes
- Obtain required approvals

### 7. Handoff to Operations

- Assign the JIRA to operations team for deployment and hand-off to QA. Reference the PR or update
  the JIRA ticket with the details needed for operations to deploy and QA to verify.

Key Information Needed:

- Deployment instructions
- Configuration changes
- Environment requirements
- Rollback procedures
- Monitoring requirements

### 8. Quality Assurance

- Support QA team during testing
- Fix identified issues promptly
- Update documentation based on QA feedback

### 9. Release

- Project Manager will work with operations/engineering team to release the build to any other test
  or production env's. 