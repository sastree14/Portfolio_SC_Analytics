# Security and permissions

- datasource credentials are injected at refresh/runtime
- development and production workspaces/sites should use separate identities
- row-level or user-level access must follow the organization access model
- exported files should not contain fields the viewer is not authorized to access
- refresh credentials are managed in the Power BI service rather than committed
