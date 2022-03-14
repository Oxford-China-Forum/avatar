from pathlib import Path

IMAGE_OUTPUT_QUALITY = 90

OUTPUT_DIR = Path('ocf/static/')

AVATAR_OUTPUT_MAX_SIZE = 1200
AVATAR_OUTPUT_DIR = OUTPUT_DIR / 'avatars/'
AVATAR_ALLOWED_FORMATS = ('jpg', 'jpeg', 'png', 'gif')
AVATAR_OVERLAY_IMAGE = Path('assets/overlay.png')

TICKET_OUTPUT_DIR = OUTPUT_DIR / 'tickets/'
TICKET_BASE_IMAGE = Path('assets/ticket.png')
TICKET_ID_DIGITS = 7

# Create necessary directories
AVATAR_OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
TICKET_OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# Ticket generation related
TICKET_MAJORS = ['病毒产品的高级生物科学', '古代历史', '人类学', '考古学', '区域研究', '天体物理学', '大气、海洋和行星物理学', '原子和激光物理', '自主智能机器和系统', '生物化学', '癌症科学', '心血管科学', '细胞结构生物学', '化学生物学', '细胞化学', '古典考古学', '古典语言文学', '临床医学', '临床神经科学', '临床心理学', '计算发现', '计算机科学', '凝聚态物理学', '犯罪学', '地球科学', '经济学', '教育', '工程科学', '环境研究', '实验心理学', '金融', '纯艺术', '未来的推进和动力', '基因组医学与统计学', '地理与环境', '健康数据科学', '科学医学史与经济社会史', '艺术史', '炎症和肌肉骨骼疾病', '信息、通信和社会科学', '无机化学', '未来制造业的无机化学', '跨学科生物科学', '国际发展', '国际关系', '健康和疾病中的离子通道和膜转运', '法律', '语言学', '音韵学', '管理', '中世纪和现代语言', '移民研究', '现代统计学和统计机器学习', '分子和细胞医学', '健康与疾病中的分子细胞生物学', '肌肉骨骼科学', '音乐', '神经科学结合', '肿瘤学', '有机化学', '东方学', '儿科', '粒子物理学', '药理', '哲学', '物理和理论化学', '生理学、解剖学和遗传学', '政治', '人口健康', '初级卫生保健', '精神病学', '公共政策', '社会数据科学', '社会干预和政策评估', '社会政策', '互联网社会科学', '信息传播与社会科学', '社会学', '统计数据', '外科科学', '生物医学科学的可持续方法', '生物学和医学合成', '神学与宗教', '理论物理', '转化健康科学', '风能和海洋能源系统和结构', '妇女和生殖健康']
TICKET_COLLEGES = [
    {'chinese': '万灵书院', 'english': 'All Souls College', 'year': 1438},
    {'chinese': '贝利奥尔书院', 'english': 'Balliol College', 'year': 1263},
    {'chinese': '布雷齐诺斯书院', 'english': 'Brasenose College', 'year': 1509},
    {'chinese': '基督堂书院', 'english': 'Christ Church', 'year': 1546},
    {'chinese': '基督圣体书院', 'english': 'Corpus Christi College', 'year': 1517},
    {'chinese': '埃克塞特书院', 'english': 'Exeter College', 'year': 1314},
    {'chinese': '格林坦普顿书院', 'english': 'Green Templeton College', 'year': 2008},
    {'chinese': '哈里斯·曼彻斯特书院', 'english': 'Harris Manchester College', 'year': 1786},
    {'chinese': '赫特福德书院', 'english': 'Hertford College', 'year': 1282},
    {'chinese': '耶稣书院', 'english': 'Jesus College', 'year': 1571},
    {'chinese': '基布尔书院', 'english': 'Keble College', 'year': 1870},
    {'chinese': '凯洛格书院', 'english': 'Kellogg College', 'year': 1990},
    {'chinese': '玛格丽特夫人学堂', 'english': 'Lady Margaret Hall', 'year': 1878},
    {'chinese': '李纳克尔书院', 'english': 'Linacre College', 'year': 1962},
    {'chinese': '林肯书院', 'english': 'Lincoln College', 'year': 1427},
    {'chinese': '莫德林书院', 'english': 'Magdalen College', 'year': 1458},
    {'chinese': '曼斯菲尔德书院', 'english': 'Mansfield College', 'year': 1886},
    {'chinese': '默顿书院', 'english': 'Merton College', 'year': 1264},
    {'chinese': '新书院', 'english': 'New College', 'year': 1379},
    {'chinese': '纳菲尔德书院', 'english': 'Nuffield College', 'year': 1937},
    {'chinese': '奥里尔书院', 'english': 'Oriel College', 'year': 1326},
    {'chinese': '彭布罗克书院', 'english': 'Pembroke College', 'year': 1624},
    {'chinese': '王后书院', 'english': 'The Queen\'s College', 'year': 1341},
    {'chinese': '圣安妮书院', 'english': 'St Anne\'s College', 'year': 1878},
    {'chinese': '圣安东尼书院', 'english': 'St Antony\'s College', 'year': 1950},
    {'chinese': '圣凯瑟琳书院', 'english': 'St Catherine\'s College', 'year': 1963},
    {'chinese': '圣十字书院', 'english': 'St Cross College', 'year': 1965},
    {'chinese': '圣埃德蒙学堂', 'english': 'St Edmund Hall', 'year': 1226},
    {'chinese': '圣希尔达书院', 'english': 'St Hilda\'s College', 'year': 1893},
    {'chinese': '圣休书院', 'english': 'St Hugh\'s College', 'year': 1886},
    {'chinese': '圣约翰书院', 'english': 'St John\'s College', 'year': 1555},
    {'chinese': '圣彼得书院', 'english': 'St Peter\'s College', 'year': 1929},
    {'chinese': '萨默维尔书院', 'english': 'Somerville College', 'year': 1879},
    {'chinese': '三一书院', 'english': 'Trinity College', 'year': 1554},
    {'chinese': '大学书院', 'english': 'University College', 'year': 1249},
    {'chinese': '瓦德汉书院', 'english': 'Wadham College', 'year': 1610},
    {'chinese': '沃弗森书院', 'english': 'Wolfson College', 'year': 1966},
]
TICKET_OCCUPATION = ['本科生', '硕士生', '博士生', '副教授', '正教授']
TICKET_LOCATIONS = ['考试院', '圣母玛利亚大学教堂', '拉德克利夫天文角', '谢尔登剧院', '大学公园', '植物园', '米尔城堡', '科学区', '高街', '阿什莫林艺术与考古博物馆', '皮特河博物馆', '叹息桥']
TICKET_TOPICS = ['突破思维边界：跨学科的挑战与未来', '工业资本主义与研究精细化', '学科鄙视链', '计算社会科学与化学哲学', '跨专业研究团队', '专业壁垒与学术螺丝钉', '“书院”的尝试', '妖镍、限电与俄乌冲突', '油价、气价与金属价', '新能源转型', '碳达峰与碳中和', '气候变化塑造下的国际格局', '环资行业中企出海', '城市化与逆城市化', '城乡结构性不平等', '乡村改造乡村振兴', '李子柒与滇西小哥', '个体觉醒与乡土情结', '乡村生态系统与建筑文化', '唐人街中餐厅', '民族商业与族群社区', '多文化聚集中的文化自演绎', '民族生活史的切片', '文化资本与政治权利', '移民历史与知识遗产', '身体年龄、社会年龄与心理年龄', '世界与中国的人口老龄化', '“35岁”年龄焦虑', '养老院的想象力', '老年学与人口学', '“银龄讲学计划”', '赛博朋克与赛博格', '雨果奖、星云奖与中国科幻作家', '脑机接口与基因编辑', '道德与人性', '国产科幻大片', '未来事务研讨会', '初音未来、嘉然、柳夜熙', '人工智能永不塌房', '社会心理学、传播学、哲学', '中国神话与希腊神话', '对元宇宙的惶恐或憧憬', '偶像的内核', 'Kaws、太阳花与玲娜贝儿', 'NFT、区块链与垄断', '资本爆款与艺术平等', '收藏家、观众、画廊与媒体的微妙关系', '文化艺术消费品', '艺术的衍生媒介形态']
TICKET_TEXT = '''
4044 年，来到未来的你，
入学成为了牛津大学建立于 {year} 年的
{chinese} {english} 的一名{occupation}，
正在潜心研究{major}专业。
有一天你沿着小路，慢慢来到了熟悉的{location}
准备好好享受一下美丽的春色。
突然听见有一段录像带在吱扭吱扭播放，
传来了来自古老远方地球蓝星上的智者声音，
在讲古早人类时期{topic}。
你不由听得入了神。

8088年，
录像带里的声音一直回荡在你心里，
通过不懈的努力，
你成功成为了这个时代次元该领域的头号人物。
'''.strip()
