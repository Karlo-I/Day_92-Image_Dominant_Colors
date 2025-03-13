import os
from flask import Flask, render_template, request, redirect
from image_processing import get_colour_dominance
from charts import generate_bar_chart

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"  # Folder where the uploaded images will be saved
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}  # Allowed image formats

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True) # Create the upload folder if it doesn't exist

# Check allowed file extensions
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/", methods=["GET", "POST"])
def home():
    uploaded_image_path = None
    dominant_colours = None
    if request.method == "POST":
        # Check if a file is part of the request
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]

        # If no file is selected
        if file.filename == "":
            return redirect(request.url)

        # If a valid file is selected
        if file and allowed_file(file.filename):
            # Save the uploaded file to static/uploads folder
            filename = file.filename
            uploaded_image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(uploaded_image_path)

            dominant_colours = get_colour_dominance(uploaded_image_path) # Get dominant colors for the uploaded image

            chart_image = generate_bar_chart(dominant_colours) # Generate bar chart as base64 string

            return render_template(
                "home.html",
                chart_image=chart_image,
                dominant_colours=dominant_colours,
                uploaded_image_path=filename
            )

    return render_template(
        "home.html",
        chart_image=None,
        dominant_colours=None,
        uploaded_image_path=None
    )

if __name__ == "__main__":
    app.run(debug=False)
