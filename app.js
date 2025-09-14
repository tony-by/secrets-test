// JavaScript application with embedded secrets
const express = require('express');
const app = express();

// API Keys and tokens in code
const STRIPE_SECRET_KEY = 'sk_live_51234567890abcdef1234567890abcdef';
const AWS_ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE';
const AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY';
const GITHUB_TOKEN = 'ghp_1234567890abcdef1234567890abcdef12345678';
const JWT_SECRET = 'my-super-secret-jwt-key-for-production-2024';

// Database credentials
const DB_CONFIG = {
    host: 'localhost',
    port: 5432,
    username: 'admin',
    password: 'super_secret_db_password_2024',
    database: 'production_db'
};

// Third-party service credentials
const SENDGRID_API_KEY = 'SG.1234567890abcdef1234567890abcdef.1234567890abcdef1234567890abcdef';
const TWILIO_ACCOUNT_SID = 'AC1234567890abcdef1234567890abcdef';
const TWILIO_AUTH_TOKEN = '1234567890abcdef1234567890abcdef';

// OAuth secrets
const GOOGLE_CLIENT_SECRET = 'GOCSPX-1234567890abcdef1234567890abcdef';
const FACEBOOK_APP_SECRET = '1234567890abcdef1234567890abcdef';

app.get('/api/data', (req, res) => {
    // Using secrets in API calls
    const apiKey = 'ak_prod_1234567890abcdef1234567890abcdef';
    res.json({ message: 'Data retrieved successfully' });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
