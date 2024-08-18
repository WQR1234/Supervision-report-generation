import requests


payload = {'图片信息': [{'图片描述1': '接线端子氧化、水渍',
           '图片描述2': '接线端子氧化、水渍',
           '问题图片1': '图片1.jpg',
           '问题图片2': '图片2.jpg'},
          {'图片描述1': '接线端子氧化、水渍',
           '图片描述2': '接线端子氧化、水渍',
           '问题图片1': '图片3.jpg',
           '问题图片2': '图片4.jpg'}],
 '图片信息ex': [{'图片描述ex': None, '问题图片ex': None}],
 '联系单信息': [{'工程名称': '邢台扩建工程（邢台站）',
            '期数': 3,
            '监造工作组': '驻特变沈变监造组',
            '监造日期': 45484,
            '监造要求': '针对上述问题，考虑套管使用需求，请沈变：\n'
                    '（1）对上述问题进行原因分析，并提供后续处理方案；\n'
                    '（2）对套管进行质量评估，判断其内部是否受到影响；\n'
                    '（3）针对ABB中压套管返修事宜，请沈变提交整体说明、应用计划及检验方案。',
            '监造设备生产厂家': '特变电工沈阳变压器集团有限公司',
            '监造负责单位': '国网电科院武汉南瑞',
            '见证点名称': 'ABB中压套管入厂检查',
            '问题描述': '2024年7月10日下午，沈变对4支返修后套管进行开箱检查，监造组现场见证，发现以下问题：\n'
                    '（1）4支返修套管接线端子普遍存在氧化、水渍；\n'
                    '（2）编号为No.1ZSCT14009437/01的套管接线端子处有磕碰凸起；\n'
                    '（3）编号为No.1ZSCT14009345/01的套管接线端子处存在较严重腐蚀，内部呈绿色。',
            '驻厂监造工程师': '任宏飞'}]}

data = [
            {
             '检查图片': ["https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/t9Vd5JLaXF4z1gexAvAvwYB_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=KI%2Fz6C5PsUPTUe4QYwtrSetgVyY%3D&response-cache-control=public%2Cmax-age%3D86400",
                      "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tEHyeT4syCmoNS5wDTgCf9Q_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=sw5DMeIxzn9k64xvRTTaYf7OX2g%3D&response-cache-control=public%2Cmax-age%3D86400"],
             '生成报文': '2024年7月29日，1000kV出线装置入厂检查：\n'
             '所属变压器：Z24B030229\n'
             '牌号、型号：101405-20B\n'
             '供应商检查：魏德曼电力绝缘科技（嘉兴）有限公司\n'
             '文件检查：检查合格证、X光检查记录、供货清单内容无误\n'
             '外包装检查：检查包装密封良好，包装箱标识齐全，检查结果符合要求\n'
             '外观检查：检查出线装置支撑件外观无尖角毛刺，内部铝管焊接牢固、焊缝饱满，内部无黑色氧化层、焊渣、污渍。\n'
             '尺寸测量：符合要求\n'
             '内腔检查：干净无异物'}]

data = [
    {
        "检查图片": [
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/t9Vd5JLaXF4z1gexAvAvwYB_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=KI%2Fz6C5PsUPTUe4QYwtrSetgVyY%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tEHyeT4syCmoNS5wDTgCf9Q_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=sw5DMeIxzn9k64xvRTTaYf7OX2g%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/taWHAg9RQRu75r8e85iTjYN_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=1fmOChqcYmCQBuy%2F50bTgrtNJ%2Fk%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tRJLdEY13bf62GcHsJy8R7v_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=BQ852ZCrfttFct5jxJV0eophVy8%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tpiVJqbtk4wJx5GE8UKz8D2_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=5G5QWJXsuxLB4dR36FJgenStCRY%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tmyWXQKqdCfbi3UwddzwbF6_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=6nVL%2FqUPCKiyQfO59Ln97RT08Pc%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tQX3sVYEFsiGCiZsEUGYgrV_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=xOzDkn0cmRILccOs%2Bpt3wGtsjQs%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tFn5vCigueY1nfzR5Bvz1Gq_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=1VJAsWxxsBQaTXbOvDFdw%2FP2dRw%3D&response-cache-control=public%2Cmax-age%3D86400",
            "https://weboffice-temporary.ks3-cn-beijing.wpscdn.cn/thumbnail/tDWRTK8sPX3pdnQrxuMprjN_100.jpeg?Expires=1723496400&KSSAccessKeyId=AKLTmoJhggaFT1CHuozGZqbC&Signature=W%2B%2B3W7%2BFGqr92wQ2Pm4v8QKHkcg%3D&response-cache-control=public%2Cmax-age%3D86400"
        ],
        "生成报文": "2024年8月5日，电磁线入厂检查：\n所属变压器：Z24B030230\n牌号、型号：①HQQ-2.45 1.60*7.00/35；②ZB-2.95 1.00*15；③ZB-2.95 1.00*10.00；④ZB-3.95 1.00*10.00；⑤ZB-5.95 1.00*7.00 ；⑥HQQNBY-1.15 1.49*8.30/21；⑦HQQNBY-1.15 1.62*6.20/37；⑧HQQNBY-1.15 1.75*7.20/21；⑨HQQNBY-1.35 1.62*6.20/37；⑩HQQNBY-2.45 1.65*5.40/19；⑪HQQNBY-3.45 1.30*6.10/17\n供应商检查：沈阳宏远电磁线股份有限公司\n文件检查：检查材质单、合格证、检查报告内容无误\n外包装检查：检查包装密封良好，包装箱标识齐全，检查结果符合要求\n外观检查：检查电磁线表面光洁、无毛刺、无凹凸现象\n1、供应商检查：沈阳宏远电磁线股份有限公司\n2、外包装检查：检查出厂试验报告、合格证齐全，检查外包装和线轴完好无损，\n3、外观检查：检查电磁线无异物，外观漆膜内外表面平整，厚薄均匀，色泽基本一致，无褶皱。无明显凹凸，气泡，等缺陷.表面清洁无污；检查结果符合要求。\n4、尺寸检查：检查结果符合工艺要求。"
    }
]

data = [{'联系单信息':
                 [{'工程名称': '邢台扩建工程（邢台站）',
                   '问题名称': '第一台1000kV变压器绝缘成型件入厂检查问题',
                   '期数': 3,
                   '监造工作组': '驻特变沈变监造组',
                   '问题日期': 32000,
                   '监造要求': '针对上述问题，考虑套管使用需求，请沈变：\x07（1）对上述问题进行原因分析，并提供后续处理方案；\x07（2）对套管进行质量评估，判断其内部是否受到影响；\x07（3）针对ABB中压套管返修事宜，请沈变提交整体说明、应用计划及检验方案。',
                   '监造设备生产厂家': '特变电工沈阳变压器集团有限公司',
                   '监造负责单位': '国网电科院武汉南瑞',
                   '见证点名称': 'ABB中压套管入厂检查',
                   '问题描述': '2024年7月10日下午，沈变对4支返修后套管进行开箱检查，监造组现场见证，发现以下问题：\x07（1）4支返修套管接线端子普遍存在氧化、水渍；\x07（2）编号为No.1ZSCT14009437/01的套管接线端子处有磕碰凸起；\x07（3）编号为No.1ZSCT14009345/01的套管接线端子处存在较严重腐蚀，内部呈绿色。',
                   '驻厂监造工程师': '任宏飞'
                   }],
             '图片描述0': ['内部检查'],
             '图片信息0': 1 * ['1.jpg']
             }]


response = requests.post('http://127.0.0.1:5000/contact-form', json=data)
print(response.status_code)
print(response.json())
