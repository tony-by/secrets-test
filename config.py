# Python configuration with secrets
import os

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'username': 'admin',
    'password': 'python_secret_password_2024',
    'database': 'production_db'
}

# API Keys
OPENAI_API_KEY = 'sk-1234567890abcdef1234567890abcdef1234567890abcdef'
ANTHROPIC_API_KEY = 'sk-ant-1234567890abcdef1234567890abcdef1234567890abcdef'
HUGGINGFACE_TOKEN = 'hf_1234567890abcdef1234567890abcdef1234567890abcdef'

# Cloud provider credentials
AWS_CREDENTIALS = {
    'access_key_id': 'AKIAIOSFODNN7EXAMPLE',
    'secret_access_key': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    'region': 'us-east-1'
}

AZURE_CREDENTIALS = {
    'client_id': '12345678-1234-1234-1234-123456789012',
    'client_secret': 'azure_secret_key_2024_very_long_and_secure',
    'tenant_id': '87654321-4321-4321-4321-210987654321'
}

GCP_CREDENTIALS = {
    'service_account_key': '{"type": "service_account", "project_id": "my-project", "private_key_id": "1234567890abcdef", "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...\\n-----END PRIVATE KEY-----\\n"}'
}

# JWT and encryption keys
JWT_SECRET_KEY = 'jwt-secret-key-for-python-app-2024'
ENCRYPTION_KEY = 'encryption-key-32-chars-long-2024'
SECRET_KEY = 'django-secret-key-very-long-and-secure-2024'

# Social media API keys
TWITTER_API_KEY = 'twitter_api_key_1234567890abcdef'
TWITTER_API_SECRET = 'twitter_api_secret_1234567890abcdef'
LINKEDIN_CLIENT_SECRET = 'linkedin_client_secret_1234567890abcdef'

# Payment processing
STRIPE_SECRET_KEY = 'sk_live_51234567890abcdef1234567890abcdef'
PAYPAL_CLIENT_SECRET = 'paypal_client_secret_1234567890abcdef'

# Email service credentials
SMTP_PASSWORD = 'smtp_password_2024_secure'
MAILGUN_API_KEY = 'key-1234567890abcdef1234567890abcdef'
