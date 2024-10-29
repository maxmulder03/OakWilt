import os 

APPLICATION_ROOT="/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
DESTINATION_PATH = "/dnr/sample_images/"
RESULTS_PATH = "/dnr/results"
MODEL_PATH = "oak_wilt_demo2.h5"
FEEDBACK_FILE_PATH = os.path.join(DESTINATION_PATH, "feedback.json")
