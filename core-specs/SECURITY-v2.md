<!-- Original Creator: [LaVineLeo](https://github.com/LaVineLeo) Project: LaVine-harness-skills -->
# SECURITY

This repo should not encourage generated Harness systems to leak secrets or private context into durable docs.

## Security Rules

- never put secrets, tokens, or credentials into generated reference docs
- treat `docs/generated/` as generated knowledge, not a secret store
- prefer placeholder values and TODOs over copying sensitive data
- generated Harness docs should point to secret-management systems, not contain secrets
- when in doubt, keep private infrastructure details out of the generic template
