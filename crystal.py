import random

hero = {}
hero_world = {}

worlds = ['第四世界','第八世界','第九世界','第十一世界']
jobs = ['戦士','ナイト','暗黒騎士','ガンブレイカー','モンク','忍者','竜騎士','侍',\
        '吟遊詩人','機工士','踊り子','黒魔道士','赤魔道士','召喚士',\
        '白魔道士','学者','占星術師']

main_hero = input("Enter Your Job:")

for i in range(7):
    hero[i] = jobs[random.randint(0,len(jobs)-1)]
    hero_world[i] = worlds[random.randint(0,len(worlds)-1)]

print('水晶公「さあ・・・時空を超えて来たれ・・・！」')
print('水晶公「ひとたび我らに力を貸したまえ・・・！」')
print('水晶公「彼方の勇士、稀なるつわものたちよ・・・ッ！」')
print('\ピカー！/')
print('水晶公「イカれた英雄たちを紹介するぜ！！」')

for i in range(7):
    print('水晶公「' + hero_world[i] + 'の' + hero[i] + '！！」')
    
print('水晶公「そして、原初世界の' + main_hero + '！！！ 以上だ！！！」')

