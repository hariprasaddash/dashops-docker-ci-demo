# Security Policy

- Never commit `.env` files, API keys, tokens, certificates, or customer data.
- Use least-privilege GitHub Actions permissions.
- Review third-party Actions and pin verified commit SHAs before production use.
- Rebuild images regularly to receive base-image security updates.
- Scan images and review findings; a successful build is not proof of security.
- Do not deploy to production without written approval and a rollback plan.
