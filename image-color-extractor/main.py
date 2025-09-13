from flask import Flask, render_template, request, redirect, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from PIL import Image
from collections import Counter
import random


current_dir = os.getcwd()
UPLOAD_FOLDER = os.path.join(current_dir, 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'sdkfrnwer34gsfg'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

#----------------------------- Functions -----------------------------

def allowed_file(filename)->bool:
    '''
    This function takes the file name as input and checks if the it's a valid file format that is allowed.

    Parameters
    ----------
    filename : Name of the file including the extension.

    Returns
    -------
    out : Boolean value. True if it's a valid format otherwise False.
    '''
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def image_extractor(no_of_color:int, filename)->list:
    '''
    This function give the list of hex codes of colors present in the given image.

    Parameters
    ----------
    no_of_color : Number of colors for which we want the hex code.
    filename : The image from which we want to extract the colors.
    '''
    img_color_list = []
     # Load and resize the image for consistency
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename)).convert('RGB')
    img = img.resize((100, 100))  # Resize for performance and sampling uniformity
    
    pixels = list(img.getdata())
    
    # Optional: Sample a subset of pixels for speed
    sampled_pixels = random.sample(pixels, min(1000, len(pixels)))
    
    # Count most common colors
    color_counts = Counter(sampled_pixels)
    most_common = color_counts.most_common(no_of_color)
    
    # Convert RGB to hex and store
    for rgb, _ in most_common:
        hex_code = '#{:02x}{:02x}{:02x}'.format(*rgb)
        img_color_list.append(hex_code)
    return img_color_list


# ----------------------------- Routes -----------------------------
       
@app.route("/", methods=['GET','POST'])
def home():
    color_list = None
    uploaded_image = None 

    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']

        try:
            no_of_color = int(request.form.get('no_of_color'))
        except ValueError:
            flash('Number of color should be an integer.', 'danger')
            return redirect(request.url)

        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_image = filename
            color_list = image_extractor(no_of_color, uploaded_image)

        else:
            flash('Invalid file type. Please upload a PNG, JPG, or JPEG image.', 'danger')

            return redirect(request.url)
        
    return render_template('index.html', 
                           uploaded_image=uploaded_image, 
                           img_color_list=color_list)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)