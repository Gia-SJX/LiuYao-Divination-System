import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
from datetime import datetime

# Names, Descriptions, and Categorized Interpretations of the 64 Hexagrams
HEXAGRAMS = {
    "111111": {
        "name": "乾为天 | Qian (The Creative)",
        "description": "元亨利贞。刚健中正，自强不息。\nOriginal success through perseverance. Strong and vigorous, constantly striving for self-improvement.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "状态极佳，好好发挥必能高分。复习要全面，自信很重要。\nExcellent condition, confident performance brings high scores. Comprehensive review and confidence are key.",
        "work": "升职有望，事业发展顺利。适合主动争取机会，展现领导力。\nPromotion likely, career develops smoothly. Good time to seize opportunities and show leadership.",
        "love": "主动出击成功率高。单身可大胆表白，有伴感情稳定甜蜜。\nTaking initiative brings success. Singles can confess boldly, couples enjoy stable sweetness.",
        "money": "财运旺盛，投资有利。但不要过于激进，适度即可。\nStrong fortune, investments favorable. But avoid being too aggressive, moderation is best.",
        "travel": "非常适合出行，旅途顺利愉快。商务出差也会有好收获。\nExcellent for travel, journey smooth and pleasant. Business trips also bring good results.",
        "health": "精力充沛，身体状况良好。注意不要过度劳累，适当休息。\nEnergetic, physical condition good. Avoid overwork, take proper rest."
    },
    "000000": {
        "name": "坤为地 | Kun (The Receptive)",
        "description": "元亨，利牝马之贞。厚德载物，柔顺包容。\nSuccess through gentle perseverance. Virtue carries all things, gentle and accommodating.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "稳扎稳打能过关。不要临时抱佛脚，基础知识要牢固。\nSteady progress brings success. No cramming, solid foundation is essential.",
        "work": "配合他人更顺利。不宜强出头，团队合作是关键。\nCooperation brings smoothness. Avoid standing out, teamwork is key.",
        "love": "温柔体贴能加分。包容理解对方，关系会更稳定。\nGentleness and care earn points. Understanding brings stability.",
        "money": "守财为主，不宜大投资。稳健理财，细水长流。\nFocus on preserving wealth, avoid large investments. Conservative approach, steady flow.",
        "travel": "适合跟团游或结伴同行。独自远行要多加小心。\nSuitable for group tours or traveling with companions. Be cautious if traveling alone.",
        "health": "注意调养，多休息。避免劳累，保持平和心态。\nFocus on rest and recuperation. Avoid exhaustion, maintain calm mindset."
    },
    "010001": {
        "name": "水雷屯 | Zhun (Difficulty at the Beginning)",
        "description": "元亨利贞，勿用有攸往，利建侯。初始艰难。\nSuccess through perseverance, not favorable for hasty action. Initial difficulties.",
        "fortune": "⭐⭐⭐",
        "exam": "开始会觉得难，但坚持就能过。多做练习题，别放弃。\nDifficult at first, but persistence brings passing. Do more practice, don't give up.",
        "work": "新项目会有困难，但前景不错。打好基础，慢慢会好起来。\nNew projects face challenges but have good prospects. Build foundation, things will improve.",
        "love": "刚开始可能有波折，需要耐心经营。真心相待终会开花结果。\nInitial setbacks possible, needs patient cultivation. Sincerity eventually bears fruit.",
        "money": "初期投资谨慎，不宜急于求成。先观望，再决定。\nBe cautious with early investments. Observe first, then decide.",
        "travel": "出行可能遇到小麻烦。做好充分准备，不要冲动出发。\nTravel may encounter minor troubles. Prepare well, don't depart impulsively.",
        "health": "小毛病较多，注意预防。保持锻炼，增强抵抗力。\nMinor ailments frequent, focus on prevention. Exercise to strengthen immunity."
    },
    "100010": {
        "name": "山水蒙 | Meng (Youthful Folly)",
        "description": "亨。匪我求童蒙，童蒙求我。启蒙教育。\nSuccess. Not me seeking the youth, but the youth seeking me. Education and enlightenment.",
        "fortune": "⭐⭐⭐",
        "exam": "虚心请教老师同学，成绩会提升。不懂就问，别装懂。\nHumbly seek guidance from teachers and peers, grades will improve. Ask when unsure, don't pretend.",
        "work": "多学习新技能会有帮助。遇到不会的主动请教前辈。\nLearning new skills helps. Actively seek advice from seniors on unclear matters.",
        "love": "需要多了解对方。不要盲目，慢慢培养感情。\nNeed to understand partner better. Don't be blind, cultivate feelings gradually.",
        "money": "投资前要多学习，不要盲目跟风。理财知识很重要。\nStudy before investing, don't blindly follow trends. Financial knowledge is important.",
        "travel": "适合学习性旅行，参观博物馆等。增长见识好时机。\nSuitable for educational travel, visiting museums. Good opportunity to gain knowledge.",
        "health": "了解养生知识，改善生活习惯。定期体检很必要。\nLearn health knowledge, improve lifestyle. Regular checkups necessary."
    },
    "010111": {
        "name": "水天需 | Xu (Waiting)",
        "description": "有孚，光亨贞吉，利涉大川。等待时机。\nSincerity brings success. Waiting for the right moment.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "现在不要急，再等等复习更充分。考前一周状态最佳。\nDon't rush now, wait for more thorough review. Best state comes a week before exam.",
        "work": "时机还没到，再等等会更好。不要着急跳槽或投简历。\nTiming not yet right, waiting brings better results. Don't rush to change jobs.",
        "love": "先别急着表白，再观察一段时间。时机成熟自然成。\nDon't rush to confess, observe more. Things happen naturally when time is right.",
        "money": "暂不投资，等待更好机会。现在入场容易套牢。\nDefer investment, wait for better opportunities. Entering now risks being trapped.",
        "travel": "计划可以定，但出发时间再推推。等天气好再走。\nPlan can be made, but defer departure. Wait for better weather.",
        "health": "养精蓄锐的好时期。调理身体，为将来做准备。\nGood period to build energy. Condition body for the future."
    },
    "111010": {
        "name": "天水讼 | Song (Conflict)",
        "description": "有孚窒惕，中吉，终凶。利见大人，不利涉大川。\nSincerity with caution brings initial fortune but eventual misfortune. Conflict and disputes.",
        "fortune": "⭐⭐",
        "exam": "答题时容易和标准答案有偏差。多看答案解析，理解出题思路。\nAnswers may deviate from standards. Study answer keys, understand question patterns.",
        "work": "容易和同事领导有矛盾。遇事多沟通，不要硬碰硬。\nProne to conflicts with colleagues and bosses. Communicate more, don't confront directly.",
        "love": "吵架可能性大，多包容少争执。冷静沟通才能解决问题。\nArguments likely, be more tolerant and less contentious. Calm communication solves problems.",
        "money": "避免金钱纠纷，不要借钱给别人。合同要看仔细。\nAvoid financial disputes, don't lend money. Review contracts carefully.",
        "travel": "容易和旅伴产生分歧。最好独自出行或选好脾气的同伴。\nProne to disagreements with travel companions. Better to travel alone or with easy-going people.",
        "health": "注意上火、炎症等问题。少吃刺激性食物，多喝水。\nWatch for inflammation issues. Avoid irritating foods, drink more water."
    },
    "000010": {
        "name": "地水师 | Shi (The Army)",
        "description": "贞，丈人吉，无咎。统率之道。\nPerseverance with experienced leadership brings fortune. The way of organization.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "制定学习计划很重要。按部就班复习，不能乱套。\nMaking study plans is important. Review systematically, don't be disorganized.",
        "work": "团队项目顺利，注意协调配合。做好规划，统筹安排。\nTeam projects go smoothly, coordinate well. Plan properly, organize comprehensively.",
        "love": "两人要有共同目标，一起努力。感情需要经营和计划。\nCouples need common goals, work together. Relationships need management and planning.",
        "money": "理财要有规划，不能乱花。记账很重要，控制支出。\nFinancial planning needed, don't spend randomly. Bookkeeping important, control expenses.",
        "travel": "跟团游更合适，有人安排省心。自助游要做好攻略。\nGroup tours more suitable, organized and worry-free. Independent travel needs good planning.",
        "health": "规律作息最重要。定时吃饭睡觉，养成好习惯。\nRegular routine most important. Eat and sleep on schedule, form good habits."
    },
    "010000": {
        "name": "水地比 | Bi (Holding Together)",
        "description": "吉。原筮，元永贞，无咎。亲密团结。\nGood fortune. Unity and intimacy.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "组队学习效果好。互相帮助，共同进步。\nGroup study works well. Mutual help, common progress.",
        "work": "贵人运强，会有人帮忙。多社交，拓展人脉很重要。\nStrong benefactor luck, help comes. Socialize more, expand network.",
        "love": "亲友支持，感情顺利。可以带对象见家长朋友。\nFriends and family support, relationship smooth. Can introduce partner to family and friends.",
        "money": "合作投资有利。但要选择靠谱的合伙人。\nCollaborative investment favorable. But choose reliable partners.",
        "travel": "结伴同行很开心。和朋友一起玩更有意思。\nTraveling with companions is joyful. More fun with friends.",
        "health": "朋友的建议值得听。可以一起运动，互相督促。\nFriends' advice worth heeding. Exercise together, mutual encouragement."
    },
    "110111": {
        "name": "风天小畜 | Xiao Xu (Small Accumulation)",
        "description": "亨。密云不雨，自我西郊。小有积蓄。\nSuccess. Dense clouds but no rain. Small accumulation.",
        "fortune": "⭐⭐⭐",
        "exam": "有点小进步，但还不够。继续努力，不要松懈。\nSlight progress, but not enough. Keep working, don't slack off.",
        "work": "小项目能完成，大项目要等等。先积累经验和资源。\nSmall projects achievable, large ones need waiting. Accumulate experience and resources first.",
        "love": "小恩小爱很甜蜜，但还没到谈婚论嫁。慢慢发展吧。\nSmall gestures of love are sweet, but not ready for marriage. Develop slowly.",
        "money": "有点小收入，但发不了大财。存钱为主，别乱花。\nSlight income, but no big fortune. Focus on saving, don't spend randomly.",
        "travel": "周边游可以，远途游再等等。短途放松挺好的。\nNearby trips okay, long journeys wait. Short trips for relaxation are good.",
        "health": "小毛病要注意，别拖成大问题。早预防早治疗。\nMind minor ailments, don't let them worsen. Early prevention and treatment."
    },
    "111011": {
        "name": "天泽履 | Lu (Treading)",
        "description": "履虎尾，不咥人，亨。谨慎前行。\nTreading on tiger's tail without being bitten. Success through caution.",
        "fortune": "⭐⭐⭐",
        "exam": "考试题目有点难，小心答题。仔细审题，不要粗心。\nExam questions somewhat difficult, answer carefully. Read questions carefully, avoid carelessness.",
        "work": "工作环境有点复杂，小心应对。说话做事都要谨慎。\nWork environment complex, handle carefully. Be cautious in words and actions.",
        "love": "对方可能有点难搞，要有耐心。别说错话惹对方生气。\nPartner may be difficult, need patience. Don't say wrong things to upset them.",
        "money": "投资有风险，要谨慎。不懂的项目别碰，保本为主。\nInvestments risky, be cautious. Don't touch unfamiliar projects, prioritize capital preservation.",
        "travel": "注意安全，财物保管好。人多的地方要警惕小偷。\nPay attention to safety, guard belongings. Be alert for pickpockets in crowded places.",
        "health": "小心意外受伤。出门注意安全，避免危险地方。\nBeware of accidental injuries. Be careful when going out, avoid dangerous places."
    },
    "000111": {
        "name": "地天泰 | Tai (Peace)",
        "description": "小往大来，吉亨。天地交泰。\nSmall departs, great arrives. Peace and prosperity.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "运气超好，发挥稳定肯定能过！正常考就行，别紧张。\nSuper lucky, stable performance ensures passing! Just take exam normally, don't be nervous.",
        "work": "升职加薪指日可待！工作顺利，老板赏识。\nPromotion and raise imminent! Work smooth, boss appreciates.",
        "love": "桃花运旺，单身能脱单。有伴的可以考虑结婚了。\nRomance luck strong, singles find love. Couples can consider marriage.",
        "money": "财运爆棚，赚钱机会多。投资理财都会有收益。\nWealth fortune explodes, many money-making opportunities. Investments and finance all profitable.",
        "travel": "出行超顺利，玩得很开心。是旅游的最佳时机。\nTravel super smooth, very enjoyable. Best time for tourism.",
        "health": "身体棒棒的，精力充沛。保持现在的生活习惯。\nBody excellent, energy abundant. Maintain current lifestyle."
    },
    "111000": {
        "name": "天地否 | Pi (Standstill)",
        "description": "否之匪人，不利君子贞，大往小来。闭塞不通。\nStandstill. Not favorable for the superior person. Stagnation.",
        "fortune": "⭐⭐",
        "exam": "运气不太好，可能会挂科。加倍努力，做好心理准备。\nLuck not good, may fail. Redouble efforts, prepare mentally.",
        "work": "工作不顺，处处碰壁。暂时守成，不要换工作。\nWork not smooth, obstacles everywhere. Maintain status quo, don't change jobs.",
        "love": "感情冷淡，可能会分手。给彼此空间，冷静一下。\nRelationship cold, may break up. Give each other space, calm down.",
        "money": "破财风险大，不要投资。守好钱包，能省就省。\nRisk of financial loss, don't invest. Guard wallet, save when possible.",
        "travel": "不适合出行，容易出岔子。能推迟就推迟。\nNot suitable for travel, prone to problems. Postpone if possible.",
        "health": "抵抗力下降，容易生病。多休息，加强营养。\nImmunity declining, prone to illness. Rest more, strengthen nutrition."
    },
    "111101": {
        "name": "天火同人 | Tong Ren (Fellowship)",
        "description": "同人于野，亨。利涉大川，利君子贞。和睦共处。\nFellowship in the open. Success. Harmonious coexistence.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "小组作业能拿高分。团队讨论很有帮助。\nGroup assignments get high scores. Team discussions very helpful.",
        "work": "团队协作项目很成功。同事关系融洽，配合默契。\nTeam collaboration projects successful. Colleague relations harmonious, cooperation smooth.",
        "love": "朋友介绍的对象不错。多参加社交活动，机会多。\nIntroduced prospects good. Attend more social activities, many opportunities.",
        "money": "众筹、合伙投资有利。但要选对合作对象。\nCrowdfunding and partnership investments favorable. But choose right collaborators.",
        "travel": "团体旅游很开心。公司团建或朋友聚会都不错。\nGroup tourism enjoyable. Company retreats or friend gatherings all good.",
        "health": "多参加集体活动有益。和朋友一起运动更有动力。\nParticipating in group activities beneficial. Exercising with friends more motivating."
    },
    "101111": {
        "name": "火天大有 | Da You (Great Possession)",
        "description": "元亨。丰收富足。\nGreat success. Abundant harvest.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "成绩优异，可能拿奖学金！努力得到回报了。\nExcellent grades, may get scholarship! Hard work rewarded.",
        "work": "事业巅峰期，成果显著。升职加薪、评优都有份。\nCareer peak, remarkable achievements. Promotions, raises, awards all coming.",
        "love": "爱情事业双丰收。可能求婚成功或喜结连理。\nLove and career both flourishing. Proposal may succeed or marriage occurs.",
        "money": "大赚一笔！投资收益、奖金都会有。\nBig profits! Investment returns and bonuses all coming.",
        "travel": "豪华游值得考虑。犒劳自己，好好放松。\nLuxury travel worth considering. Reward yourself, relax well.",
        "health": "身体状态很棒。但别忘了保持，不要放纵。\nPhysical condition excellent. But maintain it, don't indulge."
    },
    "000100": {
        "name": "地山谦 | Qian (Modesty)",
        "description": "亨，君子有终。谦虚谨慎。\nSuccess, the superior person brings things to conclusion. Modesty and humility.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "保持谦虚，成绩会更好。不要骄傲，继续努力。\nStay humble, grades will improve. Don't be arrogant, keep working.",
        "work": "低调做事反而更受认可。别炫耀，踏实工作。\nLow-key work gets more recognition. Don't show off, work steadily.",
        "love": "谦让体贴更讨人喜欢。少说多做，真心对待。\nModest and considerate more likable. Less talk more action, sincere treatment.",
        "money": "细水长流，收入稳定。不炫富，不乱花。\nSteady flow, stable income. Don't flaunt wealth, don't spend randomly.",
        "travel": "朴素的旅行也很美。不必追求豪华，体验最重要。\nSimple travels also beautiful. No need for luxury, experience matters most.",
        "health": "养生要适度，别太极端。平衡饮食，适量运动。\nHealth care should be moderate, not extreme. Balanced diet, moderate exercise."
    },
    "001000": {
        "name": "雷地豫 | Yu (Enthusiasm)",
        "description": "利建侯行师。欢乐喜悦。\nFavorable for establishing leaders and moving armies. Joy and enthusiasm.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "学习轻松愉快，效率高。心情好，记得也快。\nStudying easy and pleasant, efficient. Good mood, remember quickly.",
        "work": "工作氛围轻松，心情愉快。可能有团建活动。\nWork atmosphere relaxed, mood pleasant. Team building activities possible.",
        "love": "感情甜蜜，快乐多多。约会、旅行都很开心。\nRelationship sweet, much happiness. Dates and trips all enjoyable.",
        "money": "有意外收入或奖金。可以小小挥霍一下。\nUnexpected income or bonuses. Can splurge a little.",
        "travel": "度假好时机，尽情享受吧！放松心情，玩个痛快。\nGood time for vacation, enjoy fully! Relax, have great fun.",
        "health": "心情愉悦有助健康。保持好心态，笑口常开。\nJoyful mood aids health. Keep good mindset, smile often."
    },
    "011001": {
        "name": "泽雷随 | Sui (Following)",
        "description": "元亨利贞，无咎。顺应随从。\nGreat success through perseverance. Following and adapting.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "跟着老师的节奏走，稳过。听讲认真，作业完成。\nFollow teacher's pace, steady passing. Listen carefully, complete homework.",
        "work": "听从领导安排就好。不要自作主张，配合为主。\nJust follow leader's arrangements. Don't act on own, cooperation first.",
        "love": "随遇而安，顺其自然。不要强求，该来的会来。\nGo with the flow, let nature take its course. Don't force, what should come will come.",
        "money": "跟着大势走，稳赚。别逆势而为，顺势投资。\nFollow the trend, steady profits. Don't go against tide, invest with momentum.",
        "travel": "跟着导游走就行。别擅自行动，安全第一。\nJust follow tour guide. Don't act independently, safety first.",
        "health": "听医生的建议。按时吃药，遵医嘱。\nFollow doctor's advice. Take medicine on time, follow instructions."
    },
    "100110": {
        "name": "山风蛊 | Gu (Decay)",
        "description": "元亨，利涉大川。先甲三日，后甲三日。整治腐败。\nGreat success, favorable for undertaking. Work on what has been spoiled.",
        "fortune": "⭐⭐⭐",
        "exam": "要改变学习方法了。老方法不管用，试试新思路。\nTime to change study methods. Old ways don't work, try new approaches.",
        "work": "旧项目需要整顿改革。不要守旧，勇于创新。\nOld projects need reform. Don't be conservative, dare to innovate.",
        "love": "感情问题要解决了。积累的矛盾该摊开谈谈。\nRelationship issues need resolution. Accumulated conflicts should be discussed openly.",
        "money": "旧投资要清理。及时止损，重新规划。\nOld investments need clearing. Cut losses in time, replan.",
        "travel": "改变旅行方式。试试没去过的地方，换个心情。\nChange travel style. Try places not visited, change mood.",
        "health": "改掉坏习惯的好时机。戒烟戒酒，早睡早起。\nGood time to break bad habits. Quit smoking and drinking, sleep early rise early."
    },
    "000011": {
        "name": "地泽临 | Lin (Approach)",
        "description": "元亨利贞。至于八月有凶。居高临下。\nGreat success through perseverance. Approaching from a superior position.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "现在状态很好，抓紧时间冲刺。但别骄傲松懈。\nCurrent state good, seize time to sprint. But don't be arrogant or slack.",
        "work": "升职机会来了，好好把握。展现能力，争取晋升。\nPromotion opportunity comes, grasp well. Show ability, strive for advancement.",
        "love": "你现在魅力大增，追求者多。选择适合自己的。\nYour charm increases, many suitors. Choose suitable one.",
        "money": "收入上升，手头宽裕。但要居安思危，别乱花。\nIncome rising, financially comfortable. But prepare for danger, don't spend randomly.",
        "travel": "适合商务出差，会有收获。但别太频繁，注意休息。\nSuitable for business trips, will gain. But not too frequent, rest well.",
        "health": "身体不错，但别过度消耗。保持规律，别熬夜。\nBody good, but don't overconsume. Keep regular, don't stay up late."
    },
    "110000": {
        "name": "风地观 | Guan (Contemplation)",
        "description": "盥而不荐，有孚颙若。观察审视。\nAblution but not yet offering. Observation and contemplation.",
        "fortune": "⭐⭐⭐",
        "exam": "多看看别人怎么学的。取长补短，学习方法。\nObserve how others study. Learn from strengths, study methods.",
        "work": "先观察了解情况再行动。不要急于表现，多学习。\nObserve and understand first before acting. Don't rush to show off, learn more.",
        "love": "先观察对方是不是合适。不要急着确定关系。\nObserve if partner is suitable first. Don't rush to commit.",
        "money": "多观察市场再投资。了解清楚风险，别盲目。\nObserve market more before investing. Understand risks clearly, don't be blind.",
        "travel": "适合观光游览。博物馆、景点都值得看看。\nSuitable for sightseeing. Museums and attractions worth visiting.",
        "health": "观察自己的身体信号。不舒服要重视，及时检查。\nObserve your body's signals. Take discomfort seriously, check timely."
    },
    "101001": {
        "name": "火雷噬嗑 | Shi He (Biting Through)",
        "description": "亨，利用狱。咬合刑罚。\nSuccess. Favorable for legal matters. Biting through obstacles.",
        "fortune": "⭐⭐⭐",
        "exam": "遇到难题要果断攻克。别拖延，立刻解决。\nMeet difficult problems, tackle decisively. Don't procrastinate, solve immediately.",
        "work": "该处理的问题别拖着。困难户要坚决清除。\nProblems to handle, don't delay. Difficult situations must be resolved firmly.",
        "love": "有话直说，别憋着。问题不说清楚会越积越深。\nSpeak directly, don't hold back. Problems unsaid accumulate deeper.",
        "money": "该收回的欠款要追。合同纠纷要解决，别拖。\nDebts to collect, pursue. Contract disputes to resolve, don't delay.",
        "travel": "行程中的问题要及时处理。不要凑合，影响心情。\nProblems in itinerary handle timely. Don't make do, affects mood.",
        "health": "小病要及时治，别拖成大病。该看医生就去。\nMinor illness treat timely, don't let worsen. See doctor when needed."
    },
    "100101": {
        "name": "山火贲 | Bi (Grace)",
        "description": "亨，小利有攸往。文饰装扮。\nSuccess in small matters. Adorning and embellishment.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "卷面整洁很重要。字写好看点，印象分会高。\nNeat paper important. Better handwriting, higher impression score.",
        "work": "注意形象和细节。PPT做漂亮点，着装得体点。\nPay attention to image and details. Make PPT prettier, dress appropriately.",
        "love": "打扮一下更有魅力。约会要注意形象哦。\nDress up more charming. Pay attention to image on dates.",
        "money": "适度消费提升生活品质。但别只看表面，注重实用。\nModerate consumption improves quality of life. But don't just look at surface, focus on practicality.",
        "travel": "拍照留念的好时机。风景美，拍出来也好看。\nGood time for photos. Beautiful scenery, pictures turn out well.",
        "health": "外在保养也重要。护肤、美容适度就好。\nExternal care also important. Skincare and beauty in moderation."
    },
    "100000": {
        "name": "山地剥 | Bo (Splitting Apart)",
        "description": "不利有攸往。剥落衰败。\nNot favorable to go anywhere. Splitting apart and decline.",
        "fortune": "⭐⭐",
        "exam": "成绩可能下滑，小心挂科。要赶紧补救，别放弃。\nGrades may decline, beware failing. Need to remedy quickly, don't give up.",
        "work": "小心被排挤或降职。低调做人，别树敌。\nBeware of being squeezed out or demoted. Keep low profile, don't make enemies.",
        "love": "感情危机，可能有第三者。多关心对方，别冷落。\nRelationship crisis, possible third party. Care more for partner, don't neglect.",
        "money": "容易破财，守好钱包。不要借钱，投资要谨慎。\nProne to financial loss, guard wallet. Don't lend money, invest cautiously.",
        "travel": "不宜出行，容易遇到麻烦。能推就推，等等再说。\nNot suitable to travel, prone to troubles. Postpone if possible, wait and see.",
        "health": "抵抗力弱，容易生病。多休息，别太劳累。\nWeak immunity, prone to illness. Rest more, don't overwork."
    },
    "000001": {
        "name": "地雷复 | Fu (Return)",
        "description": "亨。出入无疾，朋来无咎。反复其道，七日来复。复返回归。\nSuccess. Coming and going without error. Return and renewal.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "之前不懂的现在明白了。重新复习会有收获。\nPreviously unclear now understood. Reviewing again brings gains.",
        "work": "困难时期过去了，开始好转。坚持下去会成功。\nDifficult period passed, starting to improve. Persistence brings success.",
        "love": "分手的可能复合。重新开始，珍惜机会。\nBroken up may reconcile. New start, cherish opportunity.",
        "money": "财运开始回升。之前的损失会慢慢补回来。\nFinancial fortune starts recovering. Previous losses gradually recovered.",
        "travel": "适合回老家或故地重游。重温美好回忆。\nSuitable to return home or revisit old places. Relive good memories.",
        "health": "身体开始恢复。继续调理，会越来越好。\nBody starts recovering. Continue conditioning, will get better."
    },
    "111001": {
        "name": "天雷无妄 | Wu Wang (Innocence)",
        "description": "元亨利贞。其匪正有眚，不利有攸往。真诚无妄。\nGreat success through perseverance. Innocence and sincerity.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "脚踏实地学习，不投机取巧。真实实力最重要。\nStudy steadily, no shortcuts. Real ability most important.",
        "work": "踏实工作，别想走捷径。投机取巧会出问题。\nWork steadily, don't seek shortcuts. Opportunism causes problems.",
        "love": "真心实意才能长久。别玩套路，真诚相待。\nSincerity lasts long. Don't play games, be genuine.",
        "money": "正当收入才安心。灰色收入别碰，会有麻烦。\nLegitimate income brings peace of mind. Avoid grey income, brings trouble.",
        "travel": "计划好再出发，别冲动。做好攻略，有备无患。\nPlan before departure, don't be impulsive. Prepare well, be ready for anything.",
        "health": "按照正常作息，别乱来。不要信偏方，科学养生。\nFollow normal schedule, don't mess around. Don't believe folk remedies, scientific health care."
    },
    "100111": {
        "name": "山天大畜 | Da Xu (Great Accumulation)",
        "description": "利贞，不家食吉，利涉大川。大力积蓄。\nPerseverance brings fortune. Great accumulation.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "现在是积累知识的好时候。多学习，打好基础。\nGood time to accumulate knowledge. Study more, build foundation.",
        "work": "充实自己，学习技能。现在积累，将来会有用。\nEnrich yourself, learn skills. Accumulate now, useful later.",
        "love": "慢慢培养感情，别急。感情要积累，不能速成。\nCultivate feelings slowly, don't rush. Relationships need accumulation, can't be rushed.",
        "money": "存钱的好时机。攒下来，将来有大用。\nGood time to save money. Save now, big use later.",
        "travel": "可以计划长途旅行。攒钱攒假期，好好准备。\nCan plan long trip. Save money and vacation days, prepare well.",
        "health": "积蓄健康本钱。多锻炼，强身健体。\nAccumulate health capital. Exercise more, strengthen body."
    },
    "100001": {
        "name": "山雷颐 | Yi (Nourishment)",
        "description": "贞吉。观颐，自求口实。养育颐养。\nPerseverance brings fortune. Nourishment and care.",
        "fortune": "⭐⭐⭐",
        "exam": "劳逸结合，别太累。注意营养，身体最重要。\nBalance work and rest, don't overwork. Pay attention to nutrition, health most important.",
        "work": "工作别太拼，注意身体。量力而行，别累坏了。\nDon't work too hard, mind health. Do what you can, don't exhaust yourself.",
        "love": "多关心对方的身体。互相照顾，共同养生。\nCare more about partner's health. Mutual care, health together.",
        "money": "投资健康最值得。吃好喝好，身体是本钱。\nInvesting in health most worthwhile. Eat and drink well, health is capital.",
        "travel": "养生游、温泉游不错。放松休息，调理身体。\nWellness travel, hot springs good. Relax and rest, condition body.",
        "health": "重点养生期。调理身体，注意饮食作息。\nKey health cultivation period. Condition body, mind diet and rest."
    },
    "011110": {
        "name": "泽风大过 | Da Guo (Great Exceeding)",
        "description": "栋桡，利有攸往，亨。大有过越。\nThe ridgepole sags. Preponderance of the great.",
        "fortune": "⭐⭐",
        "exam": "任务太多压力大。合理安排，别硬撑着。\nToo many tasks, pressure high. Arrange reasonably, don't force it.",
        "work": "工作量超负荷了。学会拒绝，别什么都接。\nWorkload overloaded. Learn to refuse, don't accept everything.",
        "love": "感情问题积累太多。该解决的别拖了，摊开谈。\nRelationship issues accumulated too much. Don't delay resolution, discuss openly.",
        "money": "支出太大，入不敷出。要控制消费，减少开支。\nExpenses too large, income insufficient. Control consumption, reduce spending.",
        "travel": "行程太满会很累。适当减少安排，留点自由时间。\nItinerary too full, will be exhausting. Reduce appropriately, leave free time.",
        "health": "身体负担重，要注意。别透支健康，该休息就休息。\nBody burden heavy, pay attention. Don't overdraw health, rest when needed."
    },
    "010010": {
        "name": "坎为水 | Kan (The Abysmal Water)",
        "description": "习坎，有孚维心亨，行有尚。重重险陷。\nThe abysmal repeated. Multiple dangers.",
        "fortune": "⭐⭐",
        "exam": "考试难度大，要做好心理准备。冷静应对，别慌。\nExam difficulty high, prepare mentally. Stay calm, don't panic.",
        "work": "工作困难多，小心应对。步步为营，稳扎稳打。\nWork difficulties many, handle carefully. Step by step, steady progress.",
        "love": "感情波折多，需要耐心。别轻易放弃，坚持过关。\nRelationship setbacks many, need patience. Don't give up easily, persist through.",
        "money": "投资风险大，谨慎为妙。能不投就不投，保本为主。\nInvestment risk high, caution best. Better not invest, capital preservation primary.",
        "travel": "出行不太顺，多加小心。备好应急方案，安全第一。\nTravel not smooth, be extra careful. Prepare emergency plans, safety first.",
        "health": "注意意外和疾病。多加小心，定期体检。\nWatch for accidents and illness. Be extra careful, regular checkups."
    },
    "101101": {
        "name": "离为火 | Li (The Clinging Fire)",
        "description": "利贞，亨。畜牝牛吉。光明附丽。\nPerseverance brings fortune. Light and attachment.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "找对导师很重要。跟着好老师，进步快。\nFinding right mentor important. Follow good teacher, progress fast.",
        "work": "找个好领导跟。有靠山，发展更顺。\nFind good leader to follow. With backing, development smoother.",
        "love": "找对人很关键。选择适合的对象，少走弯路。\nFinding right person crucial. Choose suitable partner, less detours.",
        "money": "跟对投资顾问。专业人士的建议值得听。\nFollow right investment advisor. Professional advice worth heeding.",
        "travel": "跟着经验丰富的人走。听向导的，不会错。\nFollow experienced people. Listen to guide, won't go wrong.",
        "health": "找对医生很重要。相信专业，遵医嘱。\nFinding right doctor important. Trust professionals, follow medical advice."
    },
    "011100": {
        "name": "泽山咸 | Xian (Mutual Influence)",
        "description": "亨，利贞，取女吉。感应交感。\nSuccess. Taking a maiden brings fortune. Mutual influence.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "学习氛围好，互相促进。小组学习效果佳。\nStudy atmosphere good, mutual promotion. Group study effective.",
        "work": "同事关系融洽，配合默契。团队氛围超棒。\nColleague relations harmonious, cooperation tacit. Team atmosphere excellent.",
        "love": "心有灵犀，感情升温快。表白成功率高，抓紧机会。\nMutual understanding, feelings warm quickly. Confession success rate high, seize opportunity.",
        "money": "贵人相助，财运好。合作投资有利。\nBenefactor helps, fortune good. Collaborative investment favorable.",
        "travel": "旅伴相处愉快。一拍即合，玩得很开心。\nCompanions get along well. Hit it off, very enjoyable.",
        "health": "心情愉悦身体好。保持好心态，健康自然来。\nHappy mood, healthy body. Keep good mindset, health comes naturally."
    },
    "001110": {
        "name": "雷风恒 | Heng (Duration)",
        "description": "亨，无咎，利贞，利有攸往。恒久持续。\nSuccess, no blame. Duration and perseverance.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "坚持学习会有好结果。别三天打鱼两天晒网。\nPersistent study brings good results. Don't be inconsistent.",
        "work": "踏实工作，稳步发展。别频繁跳槽，深耕更好。\nWork steadily, develop steadily. Don't job-hop frequently, deep cultivation better.",
        "love": "感情稳定长久。好好经营，白头偕老不是梦。\nRelationship stable and lasting. Manage well, growing old together possible.",
        "money": "长期投资有回报。定投、储蓄都不错。\nLong-term investment pays off. Regular investing and saving both good.",
        "travel": "养成旅行习惯。每年定期出游，丰富生活。\nDevelop travel habit. Regular annual trips enrich life.",
        "health": "坚持锻炼身体好。持之以恒，必有收获。\nPersistent exercise improves health. Persevere, rewards will come."
    },
    "111100": {
        "name": "天山遁 | Dun (Retreat)",
        "description": "亨，小利贞。退隐遁避。\nSuccess in small matters. Retreat and withdrawal.",
        "fortune": "⭐⭐⭐",
        "exam": "这次不行下次再来。别硬撑，考虑重修或延期。\nIf not this time, try next time. Don't force it, consider retake or delay.",
        "work": "暂时退一步更明智。换个环境可能更好。\nTemporarily stepping back wiser. Different environment might be better.",
        "love": "需要冷静期。暂时分开想想，给彼此空间。\nNeed cooling-off period. Temporarily separate to think, give space.",
        "money": "该撤就撤，止损为主。不要死扛，留得青山在。\nWithdraw when needed, cut losses primarily. Don't persist stubbornly, preserve resources.",
        "travel": "取消旅行计划也可以。在家休息也不错。\nCanceling travel plans okay. Resting at home also good.",
        "health": "该休息就休息。劳累了就请假，别硬撑。\nRest when needed. Take leave if tired, don't force it."
    },
    "001111": {
        "name": "雷天大壮 | Da Zhuang (Great Power)",
        "description": "利贞。强健壮大。\nPerseverance brings fortune. Great power and strength.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "信心满满，冲刺高分！全力以赴，会有好成绩。\nFull of confidence, sprint for high scores! Full effort brings good grades.",
        "work": "大展拳脚的好时机！争取项目，冲业绩。\nGreat time to show abilities! Compete for projects, push performance.",
        "love": "主动出击，成功率高。该表白的快表白。\nTake initiative, success rate high. Confess if you should.",
        "money": "收入大增，可以大胆投资。但别过头，适度就好。\nIncome increases greatly, can invest boldly. But don't overdo, moderation best.",
        "travel": "冒险游、挑战游都行。体力充沛，尽情撒欢。\nAdventure and challenge travel both fine. Energy abundant, enjoy freely.",
        "health": "精力旺盛，身体棒。但别过度消耗，注意休息。\nEnergy vigorous, body strong. But don't overconsume, mind rest."
    },
    "101000": {
        "name": "火地晋 | Jin (Progress)",
        "description": "康侯用锡马蕃庶，昼日三接。晋升进取。\nThe prince receives many horses. Progress and advancement.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "成绩一路上升！继续保持，更好的还在后面。\nGrades rising continuously! Keep it up, better things ahead.",
        "work": "升职在即，事业上升期！好好表现，抓住机会。\nPromotion imminent, career rising! Perform well, seize opportunity.",
        "love": "感情进展顺利，可以见家长了。谈婚论嫁好时机。\nRelationship progressing smoothly, can meet parents. Good time for marriage talks.",
        "money": "财运大涨，投资有利。收益会不断增加。\nFinancial fortune surges, investment favorable. Returns keep increasing.",
        "travel": "商务出行会有意外收获。边玩边工作都顺利。\nBusiness travel brings unexpected gains. Both play and work go smoothly.",
        "health": "身体状态越来越好。保持良好习惯。\nPhysical condition getting better. Maintain good habits."
    },
    "000101": {
        "name": "地火明夷 | Ming Yi (Darkening of the Light)",
        "description": "利艰贞。光明受伤。\nPerseverance in adversity brings fortune. Light is injured.",
        "fortune": "⭐⭐",
        "exam": "成绩可能不理想。别灰心，暗中努力，等待转机。\nGrades may not be ideal. Don't be discouraged, work quietly, wait for turn.",
        "work": "暂时不得志，被埋没。低调做事，总会被发现。\nTemporarily unappreciated, buried. Work low-key, will be discovered eventually.",
        "love": "感情不被看好。坚持真心，时间会证明一切。\nRelationship not favored. Persist sincerely, time proves everything.",
        "money": "收入不如预期。开源节流，度过困难期。\nIncome below expectations. Increase income reduce expenses, get through difficulty.",
        "travel": "不是旅行的好时机。宅在家里也不错。\nNot good time for travel. Staying home also fine.",
        "health": "情绪低落影响健康。保持乐观，多晒太阳。\nLow mood affects health. Stay optimistic, get more sun."
    },
    "110101": {
        "name": "风火家人 | Jia Ren (The Family)",
        "description": "利女贞。家庭和睦。\nFavorable for woman's perseverance. Family harmony.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "家人支持很重要。在家复习效果好。\nFamily support important. Studying at home effective.",
        "work": "家人的支持是后盾。工作稳定，家庭幸福。\nFamily support is backing. Work stable, family happy.",
        "love": "双方家人都支持。可以考虑结婚成家了。\nBoth families support. Can consider marriage now.",
        "money": "家庭理财要商量。共同规划，生活更美好。\nFamily finances discuss together. Plan jointly, life better.",
        "travel": "家庭游最合适。全家一起出游，温馨快乐。\nFamily travel most suitable. Whole family trips, warm and happy.",
        "health": "家人互相照顾。注意家人健康，共同养生。\nFamily members care for each other. Mind family health, wellness together."
    },
    "101011": {
        "name": "火泽睽 | Kui (Opposition)",
        "description": "小事吉。背离乖违。\nGood fortune in small matters. Opposition and divergence.",
        "fortune": "⭐⭐",
        "exam": "和老师的思路不太一样。多沟通，理解出题意图。\nThinking differs from teacher. Communicate more, understand question intent.",
        "work": "和领导意见不合。别硬顶，找机会解释清楚。\nDisagree with leader. Don't confront directly, find chance to explain.",
        "love": "两人想法差距大。多沟通，求同存异。\nBig difference in thinking. Communicate more, seek common ground.",
        "money": "投资理念不一致。别合伙，各做各的更好。\nInvestment philosophy inconsistent. Don't partner, better do separately.",
        "travel": "旅伴爱好不同。各玩各的，或者换个伴。\nTravel companions have different interests. Do own thing or change partner.",
        "health": "生活习惯有冲突。互相理解，别强迫对方。\nLifestyle habits conflict. Mutual understanding, don't force each other."
    },
    "010100": {
        "name": "水山蹇 | Jian (Obstruction)",
        "description": "利西南，不利东北。利见大人，贞吉。艰难困顿。\nFavorable southwest, unfavorable northeast. Difficulty and obstruction.",
        "fortune": "⭐⭐",
        "exam": "遇到难题了，求助老师同学。别一个人死磕。\nEncounter difficult problems, seek help from teachers and classmates. Don't struggle alone.",
        "work": "工作遇到瓶颈，找人帮忙。别硬扛，求助不丢人。\nWork hits bottleneck, find help. Don't tough it out, asking for help isn't shameful.",
        "love": "感情遇到困难，找朋友聊聊。旁观者清，听听建议。\nRelationship difficulties, chat with friends. Outsiders see clearly, listen to advice.",
        "money": "资金周转困难，找人借一下。信用好的话没问题。\nCash flow difficult, borrow from someone. No problem with good credit.",
        "travel": "行程受阻，找当地人帮忙。语言不通找翻译。\nItinerary obstructed, get local help. Language barrier find translator.",
        "health": "病情复杂，找专家看看。别拖延，及时就医。\nCondition complex, consult specialist. Don't delay, seek medical help timely."
    },
    "001010": {
        "name": "雷水解 | Jie (Deliverance)",
        "description": "利西南。无所往，其来复吉。有攸往，夙吉。解除困境。\nFavorable southwest. Deliverance from difficulty.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "难题开始解开了！坚持下去，会全懂的。\nDifficult problems starting to solve! Keep going, will understand all.",
        "work": "困难开始化解，工作转机来了。趁热打铁，继续努力。\nDifficulties resolving, work turning around. Strike while iron hot, keep trying.",
        "love": "误会解开了，感情回温。珍惜这次机会，别再犯错。\nMisunderstandings cleared, relationship warming. Cherish this chance, don't err again.",
        "money": "债务开始还清，压力减轻。继续努力，很快会翻身。\nDebts starting to clear, pressure lightens. Keep trying, will bounce back soon.",
        "travel": "之前的问题解决了，可以出发了。好好享受旅程。\nPrevious problems solved, can depart. Enjoy the journey well.",
        "health": "病情好转，继续治疗。听医生的话，会痊愈的。\nCondition improving, continue treatment. Follow doctor, will recover."
    },
    "100011": {
        "name": "山泽损 | Sun (Decrease)",
        "description": "有孚，元吉，无咎，可贞，利有攸往。损减少取。\nSincerity brings great fortune. Decrease and reduction.",
        "fortune": "⭐⭐⭐",
        "exam": "可能要放弃一些娱乐时间。专心学习，付出会有回报。\nMay need to give up some entertainment time. Focus on study, effort pays off.",
        "work": "可能要降薪学习新技能。长远来看是值得的。\nMay take pay cut to learn new skills. Worthwhile in long run.",
        "love": "要为对方做出一些牺牲。真心付出，感情会更好。\nNeed to make some sacrifices for partner. Sincere giving, relationship better.",
        "money": "投资可能要先割肉。止损及时，避免更大损失。\nInvestment may need cutting losses. Stop loss timely, avoid bigger losses.",
        "travel": "降低旅行预算。省钱游也可以玩得很开心。\nReduce travel budget. Budget travel can also be fun.",
        "health": "要忌口了，少吃垃圾食品。为健康放弃口腹之欲。\nNeed dietary restrictions, less junk food. Give up cravings for health."
    },
    "110001": {
        "name": "风雷益 | Yi (Increase)",
        "description": "利有攸往，利涉大川。增益获利。\nFavorable to undertake something. Increase and gain.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "成绩突飞猛进！方法对了，效率高。\nGrades leap forward! Right method, high efficiency.",
        "work": "业绩大涨，奖金丰厚！老板很满意。\nPerformance surges, bonus generous! Boss very satisfied.",
        "love": "感情大进展，可能订婚或结婚。惊喜不断。\nRelationship big progress, may get engaged or married. Continuous surprises.",
        "money": "意外之财，大赚一笔！投资收益超预期。\nWindfall, big earnings! Investment returns exceed expectations.",
        "travel": "旅途中会有惊喜。可能升舱或遇到好运。\nSurprises in journey. May get upgrade or meet good luck.",
        "health": "身体状况大幅改善。保持这个势头。\nPhysical condition greatly improved. Maintain this momentum."
    },
    "011111": {
        "name": "泽天夬 | Guai (Breakthrough)",
        "description": "扬于王庭，孚号有厉。告自邑，不利即戎，利有攸往。决断果断。\nProclaiming in the king's court. Decisive breakthrough.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "要果断舍弃不重要的科目。重点突破，合理分配时间。\nDecisively abandon unimportant subjects. Focus breakthrough, allocate time reasonably.",
        "work": "该做决定了，别拖延。当断不断反受其乱。\nTime to decide, don't delay. Indecision brings chaos.",
        "love": "该表白就表白，该分手就分手。别犹豫了。\nConfess if should confess, break up if should. Don't hesitate.",
        "money": "投资要果断，机会稍纵即逝。但别冲动，想清楚再决定。\nInvest decisively, opportunities fleeting. But not impulsive, think clearly first.",
        "travel": "改签就改签，说走就走。别磨磨蹭蹭的。\nChange booking if needed, go when ready. Don't dawdle.",
        "health": "该手术就手术，该治疗就治疗。别拖延。\nSurgery if needed, treatment if needed. Don't delay."
    },
    "111110": {
        "name": "天风姤 | Gou (Coming to Meet)",
        "description": "女壮，勿用取女。不期而遇。\nThe maiden is powerful. Unexpected encounter.",
        "fortune": "⭐⭐⭐",
        "exam": "可能遇到突击测验。平时多准备，别临时抱佛脚。\nMay encounter surprise quiz. Prepare normally, don't cram last minute.",
        "work": "突发情况较多，随机应变。保持警惕，别放松。\nMany sudden situations, adapt flexibly. Stay alert, don't relax.",
        "love": "可能有突然出现的追求者。看清对方，别被表面迷惑。\nSudden suitor may appear. See clearly, don't be deceived by appearance.",
        "money": "意外支出较多。保持警惕，别冲动消费。\nMany unexpected expenses. Stay alert, don't impulse buy.",
        "travel": "可能遇到计划外的情况。灵活调整，别太死板。\nMay encounter unplanned situations. Adjust flexibly, don't be too rigid.",
        "health": "小心突发疾病。保险要买，有备无患。\nBeware sudden illness. Buy insurance, be prepared."
    },
    "011000": {
        "name": "泽地萃 | Cui (Gathering Together)",
        "description": "亨，王假有庙。利见大人，亨，利贞。用大牲吉，利有攸往。聚集汇合。\nSuccess. The king approaches his temple. Gathering together.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "组织学习小组很有效。集思广益，共同进步。\nOrganizing study group effective. Pool wisdom, progress together.",
        "work": "团队建设活动多。聚餐、团建，气氛好。\nMany team building activities. Dinners, retreats, good atmosphere.",
        "love": "家族聚会，介绍对象。通过聚会可能遇到缘分。\nFamily gatherings, introductions. May meet destiny through gatherings.",
        "money": "众筹、集资项目可以参与。但要看清楚项目。\nCrowdfunding projects can participate. But examine project clearly.",
        "travel": "聚会、团建旅游。大家一起玩，热闹开心。\nGatherings, team travel. Play together, lively and fun.",
        "health": "集体体检、团体运动。互相督促更有效。\nGroup checkups, team sports. Mutual supervision more effective."
    },
    "000110": {
        "name": "地风升 | Sheng (Pushing Upward)",
        "description": "元亨，用见大人，勿恤。南征吉。上升提升。\nGreat success. Ascending and rising.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "成绩稳步提升！排名一直在上升。\nGrades steadily improving! Ranking continuously rising.",
        "work": "职位晋升、加薪在即！前途一片光明。\nPromotion and raise imminent! Bright future ahead.",
        "love": "关系升温，可能订婚或结婚。向前发展。\nRelationship warming, may get engaged or married. Moving forward.",
        "money": "收入持续增长。投资收益节节高。\nIncome continuously growing. Investment returns rising steadily.",
        "travel": "适合向上攀登。爬山、徒步都不错。\nSuitable for upward climbing. Mountain climbing, hiking both good.",
        "health": "身体越来越好。继续保持好习惯。\nBody getting better. Continue maintaining good habits."
    },
    "011010": {
        "name": "泽水困 | Kun (Oppression)",
        "description": "亨，贞大人吉，无咎。有言不信。困境穷困。\nSuccess for great person. Oppression and exhaustion.",
        "fortune": "⭐⭐",
        "exam": "手头紧，可能交不起学费。找家里帮忙，或申请助学金。\nFinances tight, may not afford tuition. Ask family help or apply for aid.",
        "work": "经济困难，工资不够花。开源节流，找兼职。\nFinancial difficulty, salary insufficient. Increase income reduce expenses, find side job.",
        "love": "经济压力影响感情。互相理解，共度难关。\nFinancial pressure affects relationship. Mutual understanding, overcome difficulty together.",
        "money": "资金紧张，要省着花。不借钱，不投资。\nFunds tight, spend sparingly. Don't borrow, don't invest.",
        "travel": "没钱出行。省钱攒着，等以后再去。\nNo money for travel. Save up, go later.",
        "health": "没钱看病很难受。找公立医院，医保能报销。\nNo money for medical care difficult. Find public hospital, insurance covers."
    },
    "010110": {
        "name": "水风井 | Jing (The Well)",
        "description": "改邑不改井，无丧无得，往来井井。汔至亦未繘井，羸其瓶，凶。井水养人。\nChanging town but not well. The well nourishes.",
        "fortune": "⭐⭐⭐",
        "exam": "基础知识很重要。回归课本，打好基础。\nFoundational knowledge important. Return to textbooks, build foundation.",
        "work": "做好本职工作。别分心，专注最重要。\nDo your job well. Don't be distracted, focus most important.",
        "love": "保持真实的自己。别改变太多，做自己就好。\nStay true to yourself. Don't change too much, be yourself.",
        "money": "稳定收入最可靠。别想着快速致富。\nStable income most reliable. Don't think about quick riches.",
        "travel": "回到熟悉的地方。老地方也有新感觉。\nReturn to familiar places. Old places have new feelings.",
        "health": "保持健康习惯。基础调理最重要。\nMaintain healthy habits. Basic conditioning most important."
    },
    "011101": {
        "name": "泽火革 | Ge (Revolution)",
        "description": "己日乃孚，元亨利贞，悔亡。变革改革。\nOn own day there is trust. Revolution and transformation.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "改变学习方法会更好。尝试新方法，别死读书。\nChanging study methods will be better. Try new methods, don't just memorize.",
        "work": "跳槽或转型的好时机。勇敢改变，会有好结果。\nGood time to change jobs or careers. Brave change brings good results.",
        "love": "关系可能有大改变。要么结婚，要么分手。\nRelationship may have big change. Either marry or break up.",
        "money": "改变理财方式。尝试新的投资渠道。\nChange financial management. Try new investment channels.",
        "travel": "换个从没去过的地方。尝试新体验，开阔眼界。\nGo somewhere never been. Try new experiences, broaden horizons.",
        "health": "改变生活方式。戒烟戒酒，开始健身。\nChange lifestyle. Quit smoking and drinking, start fitness."
    },
    "101110": {
        "name": "火风鼎 | Ding (The Cauldron)",
        "description": "元吉，亨。鼎新革故。\nGreat fortune and success. The cauldron, renewal.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "新学期新气象！全新开始，机会很多。\nNew semester new atmosphere! Fresh start, many opportunities.",
        "work": "新项目成功，新产品畅销。创新有回报。\nNew project successful, new product sells well. Innovation rewarded.",
        "love": "开始新恋情，或结婚开始新生活。新的开始很美好。\nStart new romance or marry start new life. New beginning beautiful.",
        "money": "新投资获利，新业务开展顺利。大胆尝试新领域。\nNew investment profitable, new business smooth. Boldly try new areas.",
        "travel": "去全新的目的地。探索未知，收获满满。\nGo to completely new destination. Explore unknown, gain much.",
        "health": "新养生方法有效。尝试新的健身方式。\nNew health method effective. Try new fitness approach."
    },
    "001001": {
        "name": "震为雷 | Zhen (The Arousing Thunder)",
        "description": "亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。震动警惕。\nSuccess. Shock and arousal.",
        "fortune": "⭐⭐⭐",
        "exam": "可能有突然宣布的考试。平时多准备，别慌。\nSudden announced exam possible. Prepare normally, don't panic.",
        "work": "突发大事件，变化很大。冷静应对，别慌乱。\nSudden major event, big changes. Stay calm, don't panic.",
        "love": "感情可能有突然变化。做好心理准备，沉着应对。\nRelationship may have sudden change. Prepare mentally, respond calmly.",
        "money": "市场波动大，别冲动操作。冷静观察，稳住心态。\nMarket volatility high, don't act impulsively. Observe calmly, steady mindset.",
        "travel": "可能遇到突发情况。买保险，做好应急预案。\nMay encounter emergencies. Buy insurance, prepare contingency plans.",
        "health": "注意突发疾病。保持冷静，及时就医。\nWatch for sudden illness. Stay calm, seek medical help timely."
    },
    "100100": {
        "name": "艮为山 | Gen (Keeping Still Mountain)",
        "description": "艮其背，不获其身。行其庭，不见其人，无咎。止息静止。\nKeeping still. Stillness and rest.",
        "fortune": "⭐⭐⭐",
        "exam": "暂时别冲刺，先休息调整。劳逸结合效率高。\nDon't sprint yet, rest and adjust first. Balance work and rest, higher efficiency.",
        "work": "手上的项目先暂停。休息一下，重新规划。\nPause current projects. Rest a bit, replan.",
        "love": "给彼此一些空间。冷静期不是坏事。\nGive each other space. Cooling period not bad thing.",
        "money": "暂停投资，观望为主。等机会明朗再出手。\nPause investing, mainly observe. Wait for clear opportunity before acting.",
        "travel": "取消旅行也行。在家休息也很好。\nCanceling travel okay. Resting at home also good.",
        "health": "休息是最好的治疗。停下来，好好养病。\nRest is best treatment. Stop, recuperate well."
    },
    "110100": {
        "name": "风山渐 | Jian (Gradual Progress)",
        "description": "女归吉，利贞。渐进发展。\nWoman's marriage brings fortune. Gradual development.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "慢慢进步最稳妥。别急于求成，按计划来。\nGradual progress most stable. Don't rush, follow plan.",
        "work": "稳扎稳打，步步为营。职业发展慢慢来，别着急。\nSteady progress, step by step. Career development gradual, don't rush.",
        "love": "感情慢慢培养最好。急不来，水到渠成。\nGradually cultivating relationship best. Can't rush, things happen naturally.",
        "money": "定投、储蓄长期有效。慢慢积累财富。\nRegular investing and saving long-term effective. Gradually accumulate wealth.",
        "travel": "深度游比走马观花好。慢慢体验，收获更多。\nDeep travel better than superficial sightseeing. Experience slowly, gain more.",
        "health": "慢慢调理身体。别求速效，循序渐进最好。\nGradually condition body. Don't seek quick results, step by step best."
    },
    "001011": {
        "name": "雷泽归妹 | Gui Mei (The Marrying Maiden)",
        "description": "征凶，无攸利。女子出嫁。\nUndertaking brings misfortune. The marrying maiden.",
        "fortune": "⭐⭐",
        "exam": "别临时抱佛脚，容易翻车。该准备的要早准备。\nDon't cram last minute, prone to failure. Prepare early what should be prepared.",
        "work": "别冲动辞职，考虑不周会后悔。想清楚再行动。\nDon't quit impulsively, insufficient consideration brings regret. Think clearly before acting.",
        "love": "闪婚要慎重，了解不够容易出问题。多相处再决定。\nQuick marriage be cautious, insufficient understanding causes problems. Spend more time together before deciding.",
        "money": "别被忽悠了，投资要谨慎。太快的决定易出错。\nDon't be fooled, invest cautiously. Too fast decisions prone to error.",
        "travel": "说走就走要当心。至少做个简单攻略。\nBe careful with spontaneous travel. At least make simple plan.",
        "health": "别信偏方特效药。正规治疗最保险。\nDon't believe folk remedies or miracle cures. Regular treatment most reliable."
    },
    "001101": {
        "name": "雷火丰 | Feng (Abundance)",
        "description": "亨，王假之，勿忧，宜日中。丰盛盛大。\nSuccess, the king attains abundance. Abundance and prosperity.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "成绩超好，可能拿第一！尽情庆祝吧。\nGrades super good, may rank first! Celebrate freely.",
        "work": "事业巅峰，名利双收！该得的荣誉都会有。\nCareer peak, fame and fortune! All deserved honors will come.",
        "love": "爱情美满，可能办婚礼。幸福感爆棚。\nLove fulfilled, wedding possible. Happiness overflowing.",
        "money": "大发一笔，财运爆棚！好好享受成果。\nBig windfall, fortune exploding! Enjoy the fruits well.",
        "travel": "豪华游就现在！犒劳自己，尽情享受。\nLuxury travel now! Reward yourself, enjoy fully.",
        "health": "身体状态极佳。但别得意忘形，保持就好。\nPhysical condition excellent. But don't get carried away, maintain is good."
    },
    "101100": {
        "name": "火山旅 | Lu (The Wanderer)",
        "description": "小亨，旅贞吉。旅行漂泊。\nSmall success, wanderer's perseverance brings fortune. Travel and wandering.",
        "fortune": "⭐⭐⭐",
        "exam": "可能要去外地考试。提前踩点，熟悉环境。\nMay need to take exam elsewhere. Scout location early, familiarize with environment.",
        "work": "可能要出差或外派。随遇而安，见识会增长。\nMay need business trip or assignment. Adapt to circumstances, knowledge grows.",
        "love": "异地恋或聚少离多。互相理解，常联系。\nLong-distance or rarely together. Mutual understanding, frequent contact.",
        "money": "收入不太稳定。多存点钱应急。\nIncome not very stable. Save more for emergencies.",
        "travel": "正是旅行的时候。走到哪算哪，随性点。\nRight time for travel. Go wherever, be spontaneous.",
        "health": "在外要注意身体。水土不服要小心。\nMind health while away. Be careful of acclimatization."
    },
    "110110": {
        "name": "巽为风 | Xun (The Gentle Wind)",
        "description": "小亨，利有攸往，利见大人。谦逊柔顺。\nSmall success. Gentleness and compliance.",
        "fortune": "⭐⭐⭐",
        "exam": "听话照做就能过。别太有个性，跟着走就行。\nFollow instructions can pass. Don't be too individualistic, just follow along.",
        "work": "听领导的安排。顺从配合，不出错。\nFollow leader's arrangements. Comply and cooperate, no mistakes.",
        "love": "温柔体贴讨人喜欢。别太强势，柔软点。\nGentle and considerate pleases people. Don't be too strong, be softer.",
        "money": "跟着大势走。别逆势操作，顺势而为。\nFollow the trend. Don't go against it, go with flow.",
        "travel": "跟团最省心。听导游的，轻松自在。\nGroup tour most worry-free. Follow guide, relaxed and comfortable.",
        "health": "遵医嘱最重要。别自作主张，听专业的。\nFollow medical advice most important. Don't act on own, listen to professionals."
    },
    "011011": {
        "name": "兑为泽 | Dui (The Joyous Lake)",
        "description": "亨，利贞。喜悦愉快。\nSuccess through perseverance. Joy and pleasure.",
        "fortune": "⭐⭐⭐⭐⭐",
        "exam": "心情好学得快。放松状态考得好。\nGood mood, learn fast. Relaxed state, test well.",
        "work": "工作轻松愉快。同事关系好，天天开心。\nWork relaxed and pleasant. Good colleague relations, happy daily.",
        "love": "甜甜蜜蜜，幸福满满。每天都是情人节。\nSweet and loving, full of happiness. Every day is Valentine's Day.",
        "money": "钱来得轻松。偏财运不错，可能中奖。\nMoney comes easily. Windfall luck good, may win prizes.",
        "travel": "旅途愉快，玩得超开心。笑声不断。\nJourney pleasant, super fun. Continuous laughter.",
        "health": "笑口常开，身体好。保持好心情最重要。\nSmile often, body good. Keeping good mood most important."
    },
    "110010": {
        "name": "风水涣 | Huan (Dispersion)",
        "description": "亨。王假有庙，利涉大川，利贞。涣散消散。\nSuccess. Dispersion and dissolution.",
        "fortune": "⭐⭐",
        "exam": "学习小组可能解散。要自己努力了。\nStudy group may dissolve. Need to work hard yourself.",
        "work": "团队可能重组或解散。做好心理准备。\nTeam may reorganize or dissolve. Prepare mentally.",
        "love": "可能分手或分居。别强求，顺其自然。\nMay break up or separate. Don't force, let nature take course.",
        "money": "合伙生意可能散伙。及时清算，好聚好散。\nPartnership business may dissolve. Settle accounts timely, part amicably.",
        "travel": "旅伴可能临时取消。一个人也能玩得好。\nTravel companion may cancel last minute. Can still have fun alone.",
        "health": "远离不良习惯。戒掉对身体不好的东西。\nStay away from bad habits. Quit things harmful to body."
    },
    "010011": {
        "name": "水泽节 | Jie (Limitation)",
        "description": "亨。苦节，不可贞。节制节俭。\nSuccess. Limitation and moderation.",
        "fortune": "⭐⭐⭐",
        "exam": "要控制游戏时间。自律才能学好。\nMust control gaming time. Self-discipline enables good study.",
        "work": "加班要适度，别太拼。注意工作生活平衡。\nOvertime in moderation, don't overdo. Balance work and life.",
        "love": "给彼此留点个人空间。太黏也不好。\nLeave some personal space for each other. Too clingy not good.",
        "money": "控制开支，别乱买。记账很重要，控制支出。\nControl spending, don't buy randomly. Bookkeeping important, control expenses.",
        "travel": "预算要控制好。穷游也可以很精彩。\nControl budget well. Budget travel can also be wonderful.",
        "health": "忌口很重要。该戒的一定要戒。\nDietary restrictions important. Must quit what should be quit."
    },
    "110011": {
        "name": "风泽中孚 | Zhong Fu (Inner Truth)",
        "description": "豚鱼吉，利涉大川，利贞。诚信守信。\nPigs and fishes bring fortune. Sincerity and trust.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "诚信考试最重要。别作弊，会出事。\nHonest exam taking most important. Don't cheat, will cause problems.",
        "work": "讲信用会有回报。承诺的事一定做到。\nKeeping word brings rewards. Must fulfill promises.",
        "love": "真诚相待感情好。别撒谎，诚实最重要。\nSincere treatment, relationship good. Don't lie, honesty most important.",
        "money": "合同要履行，别违约。信用是无形资产。\nFulfill contracts, don't breach. Credit is intangible asset.",
        "travel": "说好的行程要执行。别临时变卦，影响信用。\nExecute agreed itinerary. Don't change plans last minute, affects credibility.",
        "health": "对医生要诚实。有什么症状如实说。\nBe honest with doctor. Report symptoms truthfully."
    },
    "001100": {
        "name": "雷山小过 | Xiao Guo (Small Exceeding)",
        "description": "亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上，宜下，大吉。小有过越。\nSuccess. Good for small matters, not great matters. Small exceeding.",
        "fortune": "⭐⭐⭐",
        "exam": "做好日常作业就行。别想着一步登天。\nJust do daily homework well. Don't think of reaching sky in one step.",
        "work": "做好分内事。别野心太大，不切实际。\nDo own duties well. Don't be too ambitious, unrealistic.",
        "love": "小浪漫可以有。别搞大动作，平淡最真。\nSmall romance okay. Don't make big gestures, simple is most genuine.",
        "money": "小额投资可以。大项目别碰，风险大。\nSmall investments okay. Don't touch big projects, high risk.",
        "travel": "周边游就好。别想着环游世界，不现实。\nNearby travel fine. Don't think about world tour, unrealistic.",
        "health": "小保养就够了。别过度，适度最好。\nSmall maintenance enough. Don't overdo, moderation best."
    },
    "010101": {
        "name": "水火既济 | Ji Ji (After Completion)",
        "description": "亨小，利贞。初吉终乱。事已完成。\nSmall success. After completion.",
        "fortune": "⭐⭐⭐⭐",
        "exam": "考完了，该放松了。但别完全放飞自我。\nExam finished, time to relax. But don't completely let loose.",
        "work": "项目完成，可以庆祝。但要准备下个任务了。\nProject complete, can celebrate. But prepare for next task.",
        "love": "结婚了，圆满了。但婚后生活还要经营。\nMarried, complete. But married life still needs cultivation.",
        "money": "投资回本了。但别得意，继续规划。\nInvestment recovered. But don't be complacent, continue planning.",
        "travel": "旅程结束，该回家了。总结经验，计划下次。\nJourney ended, time to go home. Summarize experience, plan next time.",
        "health": "病好了，身体恢复了。但要继续保养，别复发。\nIllness cured, body recovered. But continue maintenance, don't relapse."
    },
    "101010": {
        "name": "火水未济 | Wei Ji (Before Completion)",
        "description": "亨。小狐汔济，濡其尾，无攸利。未完成事。\nSuccess. Little fox crossing, tail gets wet. Before completion.",
        "fortune": "⭐⭐⭐",
        "exam": "差一点就及格了。再努力一把，别放弃。\nAlmost passed. One more push, don't give up.",
        "work": "项目快完成了。坚持住，别掉链子。\nProject almost done. Hang in there, don't drop the ball.",
        "love": "差一步就在一起了。再加把劲，别功亏一篑。\nOne step from being together. Push harder, don't fail at last moment.",
        "money": "快回本了，别急着撤。再等等，马上就好。\nAlmost breaking even, don't rush to exit. Wait more, soon good.",
        "travel": "快到目的地了。别半途而废，坚持到底。\nAlmost at destination. Don't give up halfway, persist to end.",
        "health": "快痊愈了。继续治疗，别半途而废。\nAlmost recovered. Continue treatment, don't give up halfway."
    },
}


class LiuYaoGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("六爻占卜 | LiuYao Divination")
        self.root.geometry("900x700")
        
        self.bg_color = "#F5E6D3"
        self.accent_color = "#8B4513"
        self.text_color = "#2C1810" 
        self.highlight_color = "#D4AF37"
        
        self.root.configure(bg=self.bg_color)
        
        # Storing Hexagram Data
        self.yao_lines = []
        self.changing_lines = []
        self.coin_animation_running = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup User Interface"""
        # Title
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="六爻占卜系统 | LiuYao Divination System",
            font=("SimHei", 24, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title_label.pack()
        
        # Question Input Area
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10, padx=20, fill=tk.X)
        
        question_label = tk.Label(
            input_frame,
            text="请输入问题（必填）| Your Question (Required):",
            font=("Arial", 11),
            bg=self.bg_color,
            fg=self.text_color
        )
        question_label.pack(anchor=tk.W)
        
        self.question_entry = tk.Entry(
            input_frame,
            font=("Arial", 11),
            bg="white",
            fg=self.text_color,
            relief=tk.SOLID,
            borderwidth=1
        )
        self.question_entry.pack(fill=tk.X, pady=5)
        
        # Button Area
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=15)
        
        self.divine_button = tk.Button(
            button_frame,
            text="起卦 | Cast Hexagram 🎲",
            font=("Arial", 12, "bold"),
            bg=self.highlight_color,
            fg="white",
            activebackground=self.accent_color,
            activeforeground="white",
            relief=tk.RAISED,
            borderwidth=3,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.start_divination
        )
        self.divine_button.pack(side=tk.LEFT, padx=10)
        
        clear_button = tk.Button(
            button_frame,
            text="清除 | Clear 🔄",
            font=("Arial", 12),
            bg=self.accent_color,
            fg="white",
            activebackground=self.text_color,
            activeforeground="white",
            relief=tk.RAISED,
            borderwidth=2,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.clear_result
        )
        clear_button.pack(side=tk.LEFT, padx=10)
        
        # Coin Animation Display Area
        self.coin_frame = tk.Frame(self.root, bg=self.bg_color, height=80)
        self.coin_frame.pack(pady=10)
        
        self.coin_labels = []
        for i in range(3):
            label = tk.Label(
                self.coin_frame,
                text="",
                font=("Arial", 36),
                bg=self.bg_color,
                fg=self.text_color
            )
            label.pack(side=tk.LEFT, padx=20)
            self.coin_labels.append(label)
        
        # Result Display Area
        result_frame = tk.Frame(self.root, bg=self.bg_color)
        result_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            font=("SimSun", 11),
            bg="white",
            fg=self.text_color,
            relief=tk.SOLID,
            borderwidth=2,
            wrap=tk.WORD
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        self.result_text.tag_config("title", font=("SimHei", 16, "bold"), foreground=self.accent_color)
        self.result_text.tag_config("subtitle", font=("SimHei", 13, "bold"), foreground=self.text_color)
        self.result_text.tag_config("hexagram", font=("Courier New", 14, "bold"), foreground=self.accent_color)
        self.result_text.tag_config("interpretation", font=("SimSun", 11), foreground="#1a1a1a")
        self.result_text.tag_config("highlight", font=("SimSun", 11, "bold"), foreground="#D4AF37", background="#FFF8DC")
        
        # Footer Information
        footer_label = tk.Label(
            self.root,
            text="仅供娱乐和学习传统文化使用 | For entertainment and cultural learning purposes only",
            font=("Arial", 9, "italic"),
            bg=self.bg_color,
            fg=self.text_color
        )
        footer_label.pack(pady=10)
        
    def analyze_question(self, question):
        question_lower = question.lower()
        
        # Define Keyword Mapping
        keywords = {
            'exam': ['考试', '考', '测验', '考核', '复习', '学习', '成绩', '分数', '及格', '挂科', 
                    'exam', 'test', 'study', 'grade', 'score', 'assignment', 'homework', 'pass', 'degree', 
                    'diploma', 'thesis', 'retake', 'course', 'gpa', '论文', '学位', '学', '题', '答题', '作业'],
            'work': ['工作', '上班', '职', '跳槽', '升职', '加薪', '辞职', '面试', '老板', '同事', 
                    '项目', 'work', 'job', 'career', 'promotion', 'salary', 'office', 'company', 'boss', 'colleague', 
                    'interview', 'resume', 'hire', 'fire', 'raise', 'bonus', '公司', '领导', '职位'],
            'love': ['感情', '恋爱', '爱情', '喜欢', '表白', '结婚', '分手', '男朋友', '女朋友', '对象',
                    'love', 'relationship', 'marry', 'dating', 'bones','crush', 'heart', 'date', 'romance', 'ex', 
                    'wedding', 'divorce', 'boyfriend', 'girlfriend', 'partner', 'he', 'she', 'him', 'her', '相亲', 
                    '暗恋', '追', '情侣', '伴侣'],
            'money': ['钱', '财', '投资', '理财', '股票', '奖金', '基金', '赚', '收入', '创业', '生意',
                     'money', 'invest', 'finance', 'business', 'cash', 'payment', 'debt', 'loan', 'salary', 
                     'stock', 'crypto', 'buy', 'sell', 'profit', 'loss', 'earn', 'spend', 'fortune',
                     '买', '卖', '房', '财运', '发财'],
            'travel': ['旅游', '旅行', '出行', '去', '玩', '度假', '出差', '搬家', '外地', '远行', '回国', '出国',
                      'travel', 'trip', 'vacation', 'tour', 'abroad', 'overseas', 'flight', 'hotel', 'luggage', 
                      'passport', 'visa', 'go', 'return', 'move', '游', '飞机', '火车', '目的地'],
            'health': ['健康', '身体', '病', '医', '养生', '锻炼', '手术', '治疗', '体检', '生病', '药', '心理健康',
                       '焦虑', '抑郁', '医生', '医院', 'pain', 'ache', 'medicine', 'drug', 'surgery', 'mental health', 
                       'anxiety', 'depression', 'body', 'wellbeing', 'checkup', 'health', 'sick', 'doctor', 
                       'hospital', 'illness', '疼', '痛', '不舒服', '调理', '康复']
        }
        
        # Count Matching Degree for Each Category
        matches = {category: 0 for category in keywords.keys()}
        
        for category, words in keywords.items():
            for word in words:
                if word in question_lower:
                    matches[category] += 1
        
        # Find Category with Highest Match
        if max(matches.values()) > 0:
            primary_category = max(matches, key=matches.get)
            # Find Other Matching Categories
            related_categories = [cat for cat, count in matches.items() 
                                if count > 0 and cat != primary_category]
            return primary_category, related_categories
        else:
            # If No Match, Return None
            return None, []
    
    def is_english(self, text):
        """Simple Detection if Text is Mainly English"""
        # Count English Letters and Chinese Characters
        english_count = sum(1 for c in text if c.isalpha() and ord(c) < 128)
        chinese_count = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        
        # If English Letters Exceed Chinese, Judge as English
        return english_count > chinese_count
    
    def animate_coin_throw(self, throw_number, callback):
        """Animation: Throwing Coins"""
        self.coin_animation_running = True
        
        def animate(count=0):
            if count < 10:  # Animate 10 Times
                for label in self.coin_labels:
                    coin = random.choice(["X", "O"])
                    label.config(text=coin)
                self.root.after(100, lambda: animate(count + 1))
            else:
                # Animation Ends, Show Final Result
                final_coins = []
                for i in range(3):
                    value = random.choice([2, 3])
                    final_coins.append(value)
                    symbol = "X" if value == 3 else "O"  # "X" for Yang (heads), "O" for Yin (tails)
                    self.coin_labels[i].config(text=symbol)
                
                self.coin_animation_running = False
                callback(sum(final_coins))
        
        animate()
    
    def start_divination(self):
        """Start Divination"""
        if self.coin_animation_running:
            return
        
        # Validate Question Input
        question = self.question_entry.get().strip()
        if not question:
            messagebox.showwarning(
                "提醒 | Reminder",
                "请输入您的问题！\nPlease enter your question!"
            )
            return
        
        # Detect if English, Prompt User
        if self.is_english(question):
            response = messagebox.askyesno(
                "语言提示 | Language Notice",
                "检测到您使用了英文。\n为了获得最准确的占卜解读，建议使用中文提问。\n\n是否继续？\n\nEnglish detected. For the most accurate interpretation,\nChinese is recommended.\n\nContinue anyway?"
            )
            if not response:
                return
        
        self.divine_button.config(state=tk.DISABLED)
        self.yao_lines = []
        self.changing_lines = []
        self.result_text.delete(1.0, tk.END)
        
        question = self.question_entry.get().strip()
        
        # Display Start Information
        self.result_text.insert(tk.END, "═" * 50 + "\n")
        self.result_text.insert(tk.END, "🎋 六爻占卜 | LiuYao Divination\n", "title")
        self.result_text.insert(tk.END, "═" * 50 + "\n")
        self.result_text.insert(tk.END, f"时间 | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        if question:
            self.result_text.insert(tk.END, f"问题 | Question: {question}\n")
        self.result_text.insert(tk.END, "═" * 50 + "\n\n")
        self.result_text.insert(tk.END, "🎲 起卦中... | Casting hexagram...\n\n", "subtitle")
        
        # Throw Six Times One by One
        self.throw_index = 0
        self.throw_next()
    
    def throw_next(self):
        """Throw Next Line"""
        if self.throw_index < 6:
            yao_names = ["初爻 (1st)", "二爻 (2nd)", "三爻 (3rd)", "四爻 (4th)", "五爻 (5th)", "上爻 (6th)"]
            self.result_text.insert(tk.END, f"投掷 | Throwing {yao_names[self.throw_index]}...\n")
            
            def on_throw_complete(total):
                self.yao_lines.append(total)
                
                # Determine if Changing Line
                is_changing = total in [6, 9]
                if is_changing:
                    self.changing_lines.append(self.throw_index)
                
                yao_type = {
                    6: "老阴(变) | Old Yin (Changing)", 
                    7: "少阳 | Young Yang", 
                    8: "少阴 | Young Yin", 
                    9: "老阳(变) | Old Yang (Changing)"
                }[total]
                symbol = self.get_yao_symbol(total, is_changing)
                
                self.result_text.insert(tk.END, f"  {symbol}  ({yao_type})\n", "hexagram")
                
                self.throw_index += 1
                self.root.after(500, self.throw_next)
            
            self.root.after(200, lambda: self.animate_coin_throw(self.throw_index, on_throw_complete))
        else:
            # Six Lines Complete, Show Interpretation
            self.root.after(500, self.show_interpretation)
    
    def get_yao_symbol(self, value, is_changing=False):
        """Get Line Symbol"""
        if value in [7, 9]:
            return "━━━ ○" if is_changing else "━━━"
        else:
            return "— — ×" if is_changing else "— —"
    
    def get_hexagram_code(self, yao_values):
        """Convert Line Values to Hexagram Code"""
        code = ""
        for value in yao_values:
            if value in [7, 9]:
                code += "1"
            else:
                code += "0"
        return code
    
    def get_changed_hexagram_code(self):
        """Get Changed Hexagram Code"""
        changed_values = self.yao_lines.copy()
        for i in self.changing_lines:
            if changed_values[i] == 9:
                changed_values[i] = 8
            elif changed_values[i] == 6:
                changed_values[i] = 7
        return self.get_hexagram_code(changed_values)
    
    def show_interpretation(self):
        """Show Interpretation Result"""
        # Clear Coin Display
        for label in self.coin_labels:
            label.config(text="")
        
        # Analyze Question Category
        question = self.question_entry.get().strip()
        primary_category, related_categories = self.analyze_question(question)
        
        self.result_text.insert(tk.END, "\n" + "═" * 50 + "\n")
        self.result_text.insert(tk.END, "📖 解卦结果 | Interpretation\n", "title")
        self.result_text.insert(tk.END, "═" * 50 + "\n\n")
        
        # Display Original Hexagram
        original_code = self.get_hexagram_code(self.yao_lines)
        self.display_hexagram(original_code, "📌 本卦 | Original Hexagram", show_interpretation=False)
        
        # Decide Which Hexagram to Use for Interpretation
        interpretation_code = original_code
        interpretation_title_ch = "本卦"
        interpretation_title_en = "Original Hexagram"
        
        # If Changing Lines Exist, Show Changed Hexagram
        if self.changing_lines:
            yao_names = ['初爻(1st)', '二爻(2nd)', '三爻(3rd)', '四爻(4th)', '五爻(5th)', '上爻(6th)']
            changing_names = [yao_names[i] for i in self.changing_lines]
            self.result_text.insert(tk.END, f"\n🔄 变爻位置 | Changing Lines: {', '.join(changing_names)}\n\n", "subtitle")
            
            changed_code = self.get_changed_hexagram_code()
            self.display_hexagram(changed_code, "🎯 变卦 | Changed Hexagram", show_interpretation=False)
            
            # With Changing Lines, Use Changed Hexagram Interpretation
            interpretation_code = changed_code
            interpretation_title_ch = "变卦"
            interpretation_title_en = "Changed Hexagram"
            
            
            self.result_text.insert(tk.END, "\n" + "─" * 50 + "\n")
            self.result_text.insert(tk.END, "💡 断卦要点 | Judgment Guide\n", "subtitle")
            self.result_text.insert(tk.END, "─" * 50 + "\n")
            
            guidance = {
                1: "只有一个变爻，以本卦变爻的爻辞为主来判断吉凶。\nWith one changing line, judge primarily by the line text of the changing line in the original hexagram.",
                2: "有两个变爻，以本卦这两个变爻的爻辞为主，以上爻的爻辞为主。\nWith two changing lines, judge by both line texts, giving more weight to the upper line.",
                3: "有三个变爻，以本卦和变卦的卦辞为主，以本卦的卦辞为主。\nWith three changing lines, judge by both hexagram texts, emphasizing the original hexagram.",
                4: "有四个变爻，以变卦中两个不变爻的爻辞为主，以下爻的爻辞为主。\nWith four changing lines, judge by the two unchanging lines in the changed hexagram, emphasizing the lower line.",
                5: "有五个变爻，以变卦中唯一不变的爻的爻辞来判断吉凶。\nWith five changing lines, judge by the single unchanging line in the changed hexagram.",
                6: "六爻皆变，以乾坤两卦的用九和用六的辞来判断吉凶。\nWith all six lines changing, use the special texts for Qian and Kun hexagrams."
            }
            
            self.result_text.insert(tk.END, guidance[len(self.changing_lines)] + "\n")
            self.result_text.insert(tk.END, f"\n💬 根据变爻情况，详细解读将以{interpretation_title_ch}为主。\nBased on the changing lines, the detailed interpretation will focus on the {interpretation_title_en}.\n")
        else:
            self.result_text.insert(tk.END, "\n" + "─" * 50 + "\n")
            self.result_text.insert(tk.END, "💡 断卦要点 | Judgment Guide\n", "subtitle")
            self.result_text.insert(tk.END, "─" * 50 + "\n")
            self.result_text.insert(tk.END, "无变爻，以本卦卦辞判断吉凶。\nNo changing lines. Judge by the original hexagram text.\n")
            self.result_text.insert(tk.END, f"\n💬 详细解读将以{interpretation_title_ch}为主。\nThe detailed interpretation will be based on the {interpretation_title_en}.\n")
        
        # Display Detailed Interpretation (Only Once, Based on Changing Lines)
        hexagram = HEXAGRAMS[interpretation_code]
        self.display_detailed_interpretation(hexagram, primary_category, related_categories)
        
        self.divine_button.config(state=tk.NORMAL)
        self.result_text.see(tk.END)
    
    def display_hexagram(self, code, title, show_interpretation=False):
        """Display Hexagram Information"""
        if code not in HEXAGRAMS:
            self.result_text.insert(tk.END, f"错误：找不到卦码 | Error: Hexagram code {code} not found\n")
            return
        
        hexagram = HEXAGRAMS[code]
        
        self.result_text.insert(tk.END, "─" * 50 + "\n")
        self.result_text.insert(tk.END, f"{title}: {hexagram['name']}\n", "subtitle")
        self.result_text.insert(tk.END, "─" * 50 + "\n")
        self.result_text.insert(tk.END, f"卦辞 | Classical Text:\n{hexagram['description']}\n\n")
        
        self.result_text.insert(tk.END, "卦象 | Hexagram Lines:\n", "subtitle")
        yao_names = ["初爻 1st", "二爻 2nd", "三爻 3rd", "四爻 4th", "五爻 5th", "上爻 6th"]
        for i in range(5, -1, -1):
            symbol = "━━━" if code[i] == "1" else "— —"
            self.result_text.insert(tk.END, f"  {symbol}  {yao_names[i]}\n", "hexagram")
        
        self.result_text.insert(tk.END, "─" * 50 + "\n")
        
        # Only Show Detailed Interpretation When show_interpretation is True
        if show_interpretation:
            self.display_detailed_interpretation(hexagram)
    
    def display_detailed_interpretation(self, hexagram, primary_category=None, related_categories=None):
        """Display Detailed Categorical Interpretation"""
        self.result_text.insert(tk.END, "\n")
        self.result_text.insert(tk.END, "═" * 50 + "\n")
        self.result_text.insert(tk.END, "📊 详细解读 | Detailed Interpretation\n", "title")
        self.result_text.insert(tk.END, "═" * 50 + "\n\n")
        
        # If Question Analysis Result Exists, Show Prompt
        if primary_category:
            category_names_ch = {
                'exam': '📚 考试/学习',
                'work': '💼 工作/职业',
                'love': '💑 感情/恋爱 ',
                'money': '💰 投资/财运',
                'travel': '🚗 出行/旅游',
                'health': '🏥 健康/养生'
            }
            category_names_en = {
                'exam': '📚 Exam/Study',
                'work': '💼 Work/Career',
                'love': '💑 Love/Romance',
                'money': '💰 Money/Finance',
                'travel': '🚗 Travel',
                'health': '🏥 Health/Wellness'
            }
            
            self.result_text.insert(tk.END, "🎯 问题分析 | Question Analysis:\n", "subtitle")
            self.result_text.insert(tk.END, f"   您的问题主要关注：{category_names_ch[primary_category]}\n")
            self.result_text.insert(tk.END, f"   Your question mainly focuses on: {category_names_en[primary_category]}\n")
            if related_categories:
                related_names_ch = [category_names_ch[cat] for cat in related_categories]
                related_names_en = [category_names_en[cat] for cat in related_categories]
                self.result_text.insert(tk.END, f"   同时涉及: {', '.join(related_names_ch)}\n")
                self.result_text.insert(tk.END, f"   Also involves: {', '.join(related_names_en)}\n")
            self.result_text.insert(tk.END, "   ⭐ 标记为重点关注的解读内容\n")
            self.result_text.insert(tk.END, "   ⭐ Marked as priority interpretation content\n\n")
        
        # Fortune Index
        self.result_text.insert(tk.END, f"🌟 运势指数 | Fortune Index: {hexagram['fortune']}\n\n", "subtitle")
        
        # Six Aspects Interpretation
        categories = [
            ("📚", "考试 | Exam", "exam"),
            ("💼", "工作 | Work", "work"),
            ("💑", "感情 | Love", "love"),
            ("💰", "投资 | Money", "money"),
            ("🚗", "出行 | Travel", "travel"),
            ("🏥", "健康 | Health", "health")
        ]
        
        for icon, label, key in categories:
            # Determine if Primary Category
            is_primary = (key == primary_category)
            is_related = (related_categories and key in related_categories)
            
            # Primary Category Bold with Star
            if is_primary:
                self.result_text.insert(tk.END, f"{icon} {label}: 【重点 | Priority】 ⭐ \n", "subtitle")
                # Use Special Style
                self.result_text.insert(tk.END, f"   {hexagram[key]}\n\n", "highlight")
            elif is_related:
                self.result_text.insert(tk.END, f"{icon} {label}: 【相关 | Related】 ✨\n", "subtitle")
                self.result_text.insert(tk.END, f"   {hexagram[key]}\n\n", "interpretation")
            else:
                self.result_text.insert(tk.END, f"{icon} {label}:\n", "subtitle")
                self.result_text.insert(tk.END, f"   {hexagram[key]}\n\n", "interpretation")
        
        self.result_text.insert(tk.END, "═" * 50 + "\n")
    
    def clear_result(self):
        """Clear Result"""
        self.result_text.delete(1.0, tk.END)
        self.question_entry.delete(0, tk.END)
        self.yao_lines = []
        self.changing_lines = []
        for label in self.coin_labels:
            label.config(text="")


def main():
    root = tk.Tk()
    app = LiuYaoGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()