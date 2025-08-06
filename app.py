from flask import Flask, render_template, request, jsonify, send_file
from image_processor import process_image_for_guide, generate_instructions, draw_minimap
import os
import io
import uuid
import shutil

app = Flask(__name__)

SESSION_CACHE = {}
UPLOAD_FOLDER = 'uploads'
GENERATED_FOLDER = os.path.join('static', 'generated')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

def clean_old_sessions():
    for item in os.listdir(GENERATED_FOLDER):
        item_path = os.path.join(GENERATED_FOLDER, item)
        if os.path.isdir(item_path):
            try:
                shutil.rmtree(item_path)
            except OSError as e:
                print(f"Erro ao deletar pasta {item_path}: {e.strerror}")

@app.route('/')
def index():
    global SESSION_CACHE
    SESSION_CACHE = {}
    clean_old_sessions()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return "Erro: Nenhuma imagem enviada", 400
    image_file = request.files['image']
    if image_file.filename == '':
        return "Erro: Nenhum arquivo selecionado", 400

    size_text = request.form['size']
    center_x = int(request.form['coord_x'])
    center_y = int(request.form['coord_y'])
    include_white = 'include_white' in request.form
    
    grid_width, grid_height = map(int, size_text.split('x'))
    
    processed_pixels = process_image_for_guide(
        image_file.stream, grid_width, grid_height, include_white=include_white
    )
    
    if not processed_pixels:
        return "Erro: Não foi possível processar a imagem ou nenhum pixel para desenhar foi encontrado.", 400
        
    instructions = generate_instructions(processed_pixels, center_x, center_y, grid_width, grid_height)
    
    session_id = str(uuid.uuid4())
    SESSION_CACHE[session_id] = {
        "processed_pixels": processed_pixels,
        "grid_width": grid_width,
        "grid_height": grid_height,
        "instructions": instructions 
    }
    
    return render_template('results.html', session_id=session_id, instructions=instructions)

@app.route('/minimap/<session_id>/<int:step>.png')
def minimap_image(session_id, step):
    session_data = SESSION_CACHE.get(session_id)
    if not session_data:
        return "Sessão expirada ou não encontrada. Por favor, gere o guia novamente.", 404
        
    img_pil = draw_minimap(
        session_data["processed_pixels"],
        session_data["grid_width"],
        session_data["grid_height"],
        instructions=session_data["instructions"],
        highlight_index=step
    )
    
    img_io = io.BytesIO()
    img_pil.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
