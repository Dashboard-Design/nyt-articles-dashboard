import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to manage environment variables"""
    
    # NYT API Configuration
    NYT_API_KEY = os.getenv('NYT_API_KEY')
    NYT_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    
    # Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    
    @classmethod
    def validate_config(cls):
        """Validate that required environment variables are set"""
        if not cls.NYT_API_KEY:
            raise ValueError("NYT_API_KEY environment variable is required")
        
        if cls.ENVIRONMENT not in ['development', 'production', 'testing']:
            raise ValueError("ENVIRONMENT must be one of: development, production, testing")
        
        print(f"✅ Configuration loaded successfully for {cls.ENVIRONMENT} environment")
        return True

# Validate configuration on import
Config.validate_config()