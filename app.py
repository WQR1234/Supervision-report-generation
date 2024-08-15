from flask import Flask, request, jsonify
import base64
import os

from File_Generation import *

from Online_mode.raw_material import raw_material

app = Flask(__name__)

# 定义保存图片的目录
UPLOAD_FOLDER = 'Online_mode/Temp'  # 确保该文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        print(request.args)
    elif request.method == "POST":
        data = request.json
        generate_file('The_group/交流监造联系单.docx', 'The_group/交流监造联系单-0.docx', data)
        return jsonify(data)
    return jsonify(request.args)


@app.route('/raw-material', methods=['POST'])
def origin_material():
    if request.method == "POST":
        data = request.json
        raw_material(data)
    
    return ''

@app.route('/upload-image', methods=['POST'])  
def upload_image():  
    data = request.get_json()  # 获取请求的 JSON 数据  
    if 'image' not in data:  
        return jsonify({'error': 'No image data provided'}), 400  
    
    # 获取 Base64 编码的字符串  
    base64_image = data['image']  

    # 获取图片名
    image_name = data.get("name", "default.png")

    # 解码 Base64  
    try:  
        # 移除可能的前缀，例如 "data:image/png;base64,"  
        if base64_image.startswith('data:image/png;base64,'):  
            base64_image = base64_image.split(',')[1]  
        
        # 解码  
        image_data = base64.b64decode(base64_image)  
        
        # 构建文件路径  
        file_path = os.path.join(UPLOAD_FOLDER, image_data)  

        # 保存图片到文件  
        with open(file_path, 'wb') as f:  
            f.write(image_data)  

        return jsonify({'message': 'Image uploaded successfully', 'file_path': file_path}), 200  

    except Exception as e:  
        return jsonify({'error': str(e)}), 500  


if __name__ == "__main__":
    app.run(debug=True)