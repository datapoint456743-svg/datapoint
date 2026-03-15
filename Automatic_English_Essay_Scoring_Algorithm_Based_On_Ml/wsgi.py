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
        model = tf.keras.models.load_model(model_path)  # Load the model
    return model

# Enable memory growth if using a GPU (Optional)
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
