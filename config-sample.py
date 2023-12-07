import base64
CACHE = {}

# Openbravo API parameters

ob_api_url = "http://[your-openbravo-domain]/openbravo/org.openbravo.service.json.jsonrest/"
# Keep only one of the 2 sections below and comment out the other:
# 1) you may enter the Openbravo user and password
ob_user = 'your-ob-user'
ob_pass = 'your-ob-password'
userpass_b64 = base64.b64encode((ob_user+':'+ob_pass).encode('ascii')).decode('ascii')
# 2) you may enter the user:password base64 encoded
#userpass_b64 = "your-ob-user:your-ob-password-base64-encoded"

# You may use this one product as a 'comment' in order to print the invoice line description instead of the product description
comment_product = 'Comment/Note'

# Banqup API parameters
banqup_client_id = "73223"
banqup_platform_id = 15
gst_rate = "8"
bq_client_id = "your-client-id-here"
bq_client_secret = "your-secret-here"
bq_base_url = "https://v4-api.platform.eu.banqup.com/v4"
bq_auth_url = "https://iam.unifiedpost.com/auth/realms/upg-dev-portal/protocol/openid-connect/auth"
bq_access_token_url = "https://iam.unifiedpost.com/auth/realms/upg-dev-portal/protocol/openid-connect/token"
bq_redirect_uri = "https://v4-api.platform.eu.banqup.com/oauth2-redirect.html"
