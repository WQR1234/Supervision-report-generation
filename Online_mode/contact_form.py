import os.path

from .send_message import WechatBot
from .utils import download_image, clear_directory, is_url, compress_picture, formate_dic
import pprint
from docxtpl import DocxTemplate
from docxtpl import InlineImage


def contact_form(data: list):
    rb = WechatBot("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=5e3b40e1-3e76-4a35-9481-bb46f584df59")
    pic_path = "Online_mode/Temp"
    mode_path = "Online_mode/Mode/交流监造联系单.docx"
    tpl = DocxTemplate(mode_path)
    for dic in data:
        clear_directory(pic_path)
        if "图片信息0" in dic:
            l1 = len(dic["图片信息0"])
            if l1 % 2 == 1:
                l1 -= 1
                dic["图片信息ex"] = [{'图片描述ex': dic["图片描述0"][l1], '问题图片ex': dic["图片信息0"][l1]}]
            dic["图片信息"] = []
            for i in range(int(l1 / 2)):
                dic["图片信息"].append({
                    '图片描述1': dic["图片描述0"][2 * i],
                    '图片描述2': dic["图片描述0"][2 * i + 1],
                    '问题图片1': dic["图片信息0"][2 * i],
                    '问题图片2': dic["图片信息0"][2 * i + 1],
                })
            del dic["图片信息0"], dic["图片描述0"]
        formate_dic(dic, pic_path, tpl, 0)
        pprint.pprint(dic)
        tpl.render(dic)
        print(dic["联系单信息"][0]["期数"])
        new_name = str(dic["联系单信息"][0]["期数"]).zfill(3) + " " + dic["联系单信息"][0]["工程名称"].replace("/", " ") + " 监造联系单 " + dic["联系单信息"][0]["问题名称"] + ".docx"
        file_path = os.path.join(pic_path, new_name)
        tpl.save(file_path)
        f_id = rb.upload_file(file_path)
        if f_id:
            rb.send_file(f_id)


if __name__ == "__main__":
    data = [{'联系单信息':
                 [{'工程名称': '邢台扩建工程（邢台站）',
                   '问题名称': '第一台1000kV变压器绝缘成型件入厂检查问题',
                   '期数': 3,
                   '监造工作组': '驻特变沈变监造组',
                   '监造日期': 32000,
                   '监造要求': '针对上述问题，考虑套管使用需求，请沈变：\x07（1）对上述问题进行原因分析，并提供后续处理方案；\x07（2）对套管进行质量评估，判断其内部是否受到影响；\x07（3）针对ABB中压套管返修事宜，请沈变提交整体说明、应用计划及检验方案。',
                   '监造设备生产厂家': '特变电工沈阳变压器集团有限公司',
                   '监造负责单位': '国网电科院武汉南瑞',
                   '见证点名称': 'ABB中压套管入厂检查',
                   '问题描述': '2024年7月10日下午，沈变对4支返修后套管进行开箱检查，监造组现场见证，发现以下问题：\x07（1）4支返修套管接线端子普遍存在氧化、水渍；\x07（2）编号为No.1ZSCT14009437/01的套管接线端子处有磕碰凸起；\x07（3）编号为No.1ZSCT14009345/01的套管接线端子处存在较严重腐蚀，内部呈绿色。',
                   '驻厂监造工程师': '任宏飞'
                   }],
             '图片描述0': ['内部检查'],
             '图片信息0': 1 * ['https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tqWDrdkabS1RuCGm1K7oprc_100.png'
                        '?Expires=1723410000&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature'
                        '=CCXzKqtsV7XzVsHtzqCkBNMzJAc%3D&response-cache-control=public%2Cmax-age%3D86400']
             }]

    contact_form(data)
