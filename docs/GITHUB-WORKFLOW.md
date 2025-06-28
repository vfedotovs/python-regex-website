# GitHub Workflow Checklist

## 1. Create Issue
Create an issue using the GitHub web interface or GitHub CLI:
```sh
gh issue create --title "Issue title" --body "Issue description"
```

## 2. Create Feature Branch
Create a new branch from the main branch:
```sh
git checkout main
git pull origin main
git checkout -b issue-123-fix-bug
```

## 3. Implement Changes
Make your code changes and commit them:
```sh
git add .
git commit -m "Fix issue #123: Describe the fix"
```

## 4. Push Branch to GitHub
Push your feature branch to the remote repository:
```sh
git push origin issue-123-fix-bug
```

## 5. Create Pull Request
Create a pull request using the GitHub web interface or GitHub CLI:
```sh
gh pr create --title "Fix issue #123" --body "Description of changes"
```

## 6. Code Review and Merge
- Request reviews from team members
- Address feedback and make necessary changes
- Merge the pull request once approved

## 7. Create Git Tag
Tag the release commit with a version number:
```sh
# Ensure you are on the main branch
git checkout main

# Pull the latest changes
git pull origin main

# Tag the commit with a version number
git tag -a v1.0.0 -m "Release v1.0.0"

# Push the tag to the remote repository
git push origin v1.0.0
```

## 8. Create GitHub Release
- Go to the GitHub Releases section
- Create a new release based on the tag
- Specify the version number, release title, and release notes
- Include any relevant documentation or assets

## 9. Update Changelog
Update the project's changelog file with the new changes:
- Document new features, bug fixes, and breaking changes
- Follow the [Keep a Changelog](https://keepachangelog.com/) format
- Include issue numbers and contributor credits

## 10. Update Documentation
Update project documentation to reflect the new release:
- Update README files with new features or changes
- Update API documentation if applicable
- Update user guides and tutorials
- Update installation or setup instructions

## 11. Deploy Application
Deploy the application with the latest changes:
- Update production servers
- Deploy new containers or cloud services
- Update environment variables if needed
- Verify deployment configuration

## 12. Post-Deployment Testing
Perform necessary tests in the production environment:
- Run smoke tests
- Verify critical functionality
- Check performance metrics
- Validate user workflows

## 13. Monitor and Maintain
Monitor the deployed application:
- Set up monitoring and alerting
- Monitor application logs and metrics
- Watch for any issues or errors
- Be prepared to rollback if critical issues are discovered

## Additional Notes

### Branch Naming Convention
Use descriptive branch names following the pattern:
- `feature/description` for new features
- `fix/description` for bug fixes
- `hotfix/description` for urgent fixes
- `issue-123/description` for issue-specific work

### Commit Message Format
Follow conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Examples:
- `fix(auth): resolve login validation issue`
- `feat(api): add user profile endpoint`
- `docs(readme): update installation instructions`

### Version Numbering
Follow semantic versioning (SemVer):
- `MAJOR.MINOR.PATCH`
- Increment MAJOR for breaking changes
- Increment MINOR for new features
- Increment PATCH for bug fixes

