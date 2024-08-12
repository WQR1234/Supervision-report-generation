from Send_message import WechatBot
from Public_f import download_image, clear_directory
import pprint


def yclzbj(data: list):
    rb = WechatBot("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=5e3b40e1-3e76-4a35-9481-bb46f584df59")
    pic_path = "Temp"
    pic_id = 0
    for dic in data:
        # 发送报文
        if "生成报文" in dic:
            rb.send_text(dic["生成报文"])
        # 发送图片
        l1 = 0
        if "检查图片" in dic:
            clear_directory(pic_path)
            l1 = len(dic["检查图片"])
        l2 = 0
        if "图片描述" in dic:
            l2 = len(dic["图片描述"])
        for i in range(max(l1, l2)):
            if i < l1:
                pic = download_image(dic["检查图片"][i], str(pic_id), pic_path)
                rb.send_picture(pic)
            if i < l2:
                rb.send_text(dic["图片描述"][i])


if __name__ == "__main__":
    data = [{'生成报文': '2024年7月19日，端子箱入厂检查：\n'
             '所属变压器：Z24B030227,Z24B030227-2,Z24B030228,Z24B030228-2\n'
             '牌号、型号：TDX-02\n'
             '供应商检查：特变电工智慧能源有限公司\n'
             '文件检查：检查出厂试验报告、合格证内容无误\n'
             '外包装检查：检查包装密封良好，包装箱标识齐全，检查结果符合要求\n'
             '外观检查：0'},
            {'生成报文': '2024年7月24日，密封件入厂检查：\n'
             '所属变压器：Z24B030229\n'
             '供应商检查：江苏神马电力股份有限公司\n'
             '文件检查：检查出厂试验报告内容无误\n'
             '外包装检查：检查包装密封良好，包装箱标识齐全，检查结果符合要求\n'
             '外观检查：0'},
            {'图片描述': ['整体外观', '尺寸测量', '内部检查'],
             '检查图片': ['https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tqWDrdkabS1RuCGm1K7oprc_100.png'
                      '?Expires=1723410000&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature'
                      '=CCXzKqtsV7XzVsHtzqCkBNMzJAc%3D&response-cache-control=public%2Cmax-age%3D86400'],
             '生成报文': '2024年7月29日，1000kV出线装置入厂检查：\n'
             '所属变压器：Z24B030229\n'
             '牌号、型号：101405-20B\n'
             '供应商检查：魏德曼电力绝缘科技（嘉兴）有限公司\n'
             '文件检查：检查合格证、X光检查记录、供货清单内容无误\n'
             '外包装检查：检查包装密封良好，包装箱标识齐全，检查结果符合要求\n'
             '外观检查：检查出线装置支撑件外观无尖角毛刺，内部铝管焊接牢固、焊缝饱满，内部无黑色氧化层、焊渣、污渍。\n'
             '尺寸测量：符合要求\n'
             '内腔检查：干净无异物'}]
    pprint.pprint(data)
    yclzbj(data)
