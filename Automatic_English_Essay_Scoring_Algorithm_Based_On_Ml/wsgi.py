import os
from django.core.wsgi import get_wsgi_application
import tensorflow as tf

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Automatic_English_Essay_Scoring_Algorithm_Based_On_Ml.settings')

# Initialize the application
application = get_wsgi_application()

# Initialize model variable globally
model = None

# Function to lazily load the model
def load_model():
    global model
    if model is None:  # Check if model is already loaded
        model_path = os.getenv("MODEL_PATH", "/path/to/default/model")  # Get model path from environment variable
        
        # Check if the model exists at the given path
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}")  # Raise an error if model is missing
        
        model = tf.keras.models.load_model(model_path)  # Load the model
        print(f"Model loaded from {model_path}")  # Optional: print a message indicating model loading
    return model

# Enable memory growth if using a GPU (Optional, only if you have a GPU available)
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        tf.config.set_memory_growth(physical_devices[0], True)  # Set memory growth for GPU
        print("Memory growth set for GPU.")
    except RuntimeError as e:
        print(f"Error while setting memory growth: {e}")

# Optional: If using CPU only, you may skip the above GPU setup but ensure the model loads properly
