import glob
import requests
import mimetypes
from docxtpl import DocxTemplate, InlineImage
import pprint
import os
from PIL import Image
from datetime import datetime, timedelta
from docx.shared import Mm
import re
import urllib.request


def clear_directory(directory):
    """
    清空指定目录中的所有文件。

    参数:
    directory (str): 需要清空的目录路径。
    """
    files = glob.glob(os.path.join(directory, '*'))  # 获取目录中所有文件
    for file in files:
        os.remove(file)  # 删除文件
    print(f"已清空目录: {directory}")


def get_image_extension(url):
    """
    根据 URL 获取图片的扩展名。

    参数:
    url (str): 图片的 URL。

    返回:
    str: 图片的扩展名（包括点），如果无法识别则返回 '.jpg'。
    """
    # 获取 MIME 类型
    mime_type, _ = mimetypes.guess_type(url)

    if mime_type:
        # 从 MIME 类型中提取扩展名
        extension = mimetypes.guess_extension(mime_type)
        return extension if extension is not None else '.jpg'

    return '.jpg'  # 默认扩展名


def download_image(url, filename_without_extension, save_directory):
    """
    根据给定的 URL 下载图片并保存到指定位置。

    参数:
    url (str): 图片的 URL。
    filename_without_extension (str): 保存图片的文件名（无扩展名）。
    save_directory (str): 保存图片的目录路径。
    """
    try:
        # 发送请求并获取响应
        response = requests.get(url, stream=True, timeout=5)
        response.raise_for_status()  # 检查请求是否成功

        # 确保保存目录存在
        os.makedirs(save_directory, exist_ok=True)

        # 获取文件扩展名
        extension = get_image_extension(url)
        save_path = os.path.join(save_directory, f"{filename_without_extension}{extension}")

        # 保存图片
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"图片已保存至: {save_path}")
        return save_path

    except requests.exceptions.RequestException as e:
        print(f"下载图片失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


def is_url(s):
    # 正则表达式来匹配URL
    if "http" in s:
        return True
    else:
        return False


def compress_picture(image_path, max_size=1024 * 1024):
    # 调整图片尺寸为8cm x 6cm
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = width / height
    new_width = 8 * 72  # 8cm转换为磅
    new_height = new_width / aspect_ratio
    if new_height > 6 * 72:  # 6cm转换为磅
        new_height = 6 * 72
        new_width = new_height * aspect_ratio
    image = image.resize((int(new_width), int(new_height)))

    # 压缩图片
    quality = 85
    while os.path.getsize(image_path) > max_size and quality >= 5:
        image.save(image_path, optimize=True, quality=quality)

    return image_path


def trans_date(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            trans_date(value)  # 递归调用process_dict函数来处理子字典
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    trans_date(item)  # 递归调用process_dict函数来处理字典
        elif isinstance(key, str) and '日期' in key:
            try:
                date_value = datetime(1900, 1, 1) + timedelta(days=value)
                formatted_date = date_value.strftime('%Y年%m月%d日')  # 将日期格式化为yyyy年mm月dd日的字符串
                dictionary[key] = formatted_date  # 更新键值为格式化后的日期字符串
            except ValueError:
                pass  # 忽略无效日期数字


def formate_dic(dic, pic_path, tpl, pic_id):
    for key, value in dic.items():
        if isinstance(value, dict):
            pic_id = formate_dic(value, pic_path, tpl, pic_id)  # 递归调用process_dict函数来处理子字典
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    pic_id = formate_dic(item, pic_path, tpl, pic_id)  # 递归调用process_dict函数来处理字典
        else:
            # 格式化日期
            if isinstance(key, str) and '日期' in key:
                if isinstance(value, int):
                    try:
                        date_value = datetime(1900, 1, 1) + timedelta(days=value)
                        formatted_date = date_value.strftime('%Y年%m月%d日')  # 将日期格式化为yyyy年mm月dd日的字符串
                        dic[key] = formatted_date  # 更新键值为格式化后的日期字符串
                    except ValueError:
                        pass  # 忽略无效日期数字
                elif isinstance(value, str):
                    try:
                        date_object = datetime.strptime(value, "%Y/%m/%d")  
                        formatted_date = date_object.strftime("%Y年%m月%d日")
                        dic[key] = formatted_date  # 更新键值为格式化后的日期字符串
                    except ValueError:
                        pass  # 忽略无效日期数字
            # 格式化图片
            elif isinstance(key, str) and '图片' in key:
                print(key, value)
                is_pic = False
                if is_url(value):
                    print(2)
                    is_pic = True
                    pic_name = download_image(value, str(pic_id), pic_path)
                    print(pic_name)
                    pic_id += 1
                if value.lower().endswith(('.jpg', '.jpeg', '.png')):
                    is_pic = True
                    pic_name = os.path.join(pic_path, value)
                if is_pic:
                    compress_picture(pic_name)
                    dic[key] = InlineImage(tpl, image_descriptor=pic_name, width=Mm(60))
            # 格式化一般段落
            else:
                if isinstance(value, str):
                    dic[key] = value.replace('\n', '\a')
    return pic_id


# def generate_file(mode, new_name, data, pic_path='Temp'):
#     tpl = DocxTemplate(mode)
#     if isinstance(data, str):
#         dic = generate_dic(data)
#     if isinstance(data, dict):
#         dic = data
#
#     formate_dic(dic, pic_path, tpl)
#     pprint.pprint(dic)
#     tpl.render(dic)
#     tpl.save(new_name)
