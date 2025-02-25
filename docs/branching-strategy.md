# Git Branching Strategy

## Overview
We follow a simplified branching model that maintains a stable main branch while supporting parallel release development.

## Branch Types

### Main Branch (`main`)
- Contains production-ready code
- Always reflects the current production state
- Protected branch - no direct commits allowed
- Updated only through merges from release branches during deployment

### Release Branches (`release-*`) OR dev
- dev is used for any long dev->release cycle, release branch can be created when its time for a release.
- Named as `release-YYYY.MM` or `release-YYYY.Q#` based on release schedule
- Created from `main` branch
- Used for collecting features for a specific release
- Example: `release-2024.03` or `release-2024.Q1`
- Protected branch - no direct commits allowed
- All feature development for a release happens through feature branches

### Feature Branches (`feature/*`)
- Created from the target release branch
- Named as `feature/JIRA-ID-brief-description`
- Used for individual feature development
- Example: `feature/PROJ-123-add-login-page`
- Merged back into release branch via Pull Request

## Deployment Strategy

### Environment-specific Deployments
- **Lower Environments (DEV/QA/UAT)**: Deploy from release branch (`release-*`)
- **Production**: Deploy from the SAME release branch after full validation
- **Post-deployment**: Fast-forward main branch to match release branch state

### Key Principle
The exact same code that was tested in lower environments must be deployed to production. No merges or code changes should occur between final testing and production deployment.

### Deployment Process
1. Deploy release branch to lower environments for testing
2. Once release is fully validated and approved:
   - Deploy THE SAME release branch to production
   - After successful deployment, sync main branch using fast-forward:
     ```bash
     git checkout main
     git merge --ff-only release-2024.03  # Only fast-forward, no merge commit
     git tag v2024.03.0
     git push origin main --tags
     ```
3. This ensures:
   - Production gets exactly what was tested
   - Main branch accurately reflects production state
   - No unexpected changes through merge commits

## Workflow Steps

1. **Release Branch Creation**
   - Release branch is created from `main` when planning a new release
   - Example: `git checkout -b release-2024.03 main`

2. **Feature Development**
   - Developer creates feature branch from release branch
   - Example:
     ```bash
     git checkout release-2024.03
     git pull
     git checkout -b feature/PROJ-123-add-login-page
     ```

3. **Feature Completion**
   - Developer raises PR to merge feature branch into release branch
   - After approval and testing, feature branch is merged into release branch

4. **Release Deployment**
   - Deploy release branch to lower environments (DEV/QA/UAT)
   - Perform testing and validation
   - When release is approved for production:
     1. Merge release branch into main
     2. Tag main branch with version number
     3. Deploy to production from main branch
   - This ensures production always deploys from main

## Key Rules

1. Never commit directly to `main` or release branches
2. Keep feature branches short-lived (1-2 weeks maximum)
3. Regularly sync release branch changes to feature branches
4. Delete feature branches after merging
5. Tag main branch after each release merge

## Sync Process

### Keeping Feature Branch Updated
```bash
# While on feature branch
git fetch origin
git rebase origin/release-2024.03
```

### Syncing Main after Release (For Code Owners)
```bash
git checkout main
git merge --ff-only release-2024.03  # Only fast-forward, no merge commit
git tag v2024.03.0
git push origin main --tags
```