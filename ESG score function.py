import pandas as pd
 

df = pd.read_csv('C:/Users/test/Desktop/info.csv')
score_dashbord = pd.read_csv('C:/Users/test/Desktop/csr/國家ESG 2.csv')


score_2017 = score_dashbord[['country_2017','Global Index Score_2017']]
score_2018 = score_dashbord[['country_2018','Global Index Score_2018']]
score_2019 = score_dashbord[['country_2019','Global Index Score_2019']]




fliter_target = (df['年月'] == 201712) & (df['公司代碼'] == 9942)

d_df = df[fliter_target]

country_list = d_df['國別'].unique().tolist()
tax_heaven_list_tw = ['台灣','薩摩亞', '巴拿馬', '英屬維京', '開曼', '關島', '模里西斯', '塞席爾' ,'百慕達', '賴索托', '尼加拉瓜', '維京', 
'安吉拉', '貝里斯', '馬紹爾群島', '科克群島', '澤西島', '盧森堡', '美屬薩摩亞', '根西島', '聖文森', '聖克里斯多', '多明尼加', '莫三比克'
,'巴哈馬','伊朗']
 

country_list = set(country_list ).difference(tax_heaven_list_tw)

cleanedList = [x for x in country_list if str(x) != 'nan']
d_df.reset_index(inplace=True, drop=True)
total_score = 0
count = 0
for i in d_df.index:
    print(i)
    if d_df['國別'][i] in cleanedList:
        score = score_2017.loc[score_2017['country_2017'] == d_df['國別'][i]]
        s = score['Global Index Score_2017'].tolist()
        s = s[0]
        total_score += s
        count += 1




def ESG_score(year, company):

    fliter_target = (df['年月'] == year) & (df['公司代碼'] == company)
    
    d_df = df[fliter_target]
    
    country_list = d_df['國別'].unique().tolist()
    tax_heaven_list_tw = ['台灣','薩摩亞', '巴拿馬', '英屬維京', '開曼', '關島', '模里西斯', '塞席爾' ,'百慕達', '賴索托', '尼加拉瓜', '維京', 
    '安吉拉', '貝里斯', '馬紹爾群島', '科克群島', '澤西島', '盧森堡', '美屬薩摩亞', '根西島', '聖文森', '聖克里斯多', '多明尼加', '莫三比克'
    ,'巴哈馬']
    
    
    country_list = set(country_list ).difference(tax_heaven_list_tw)
    
    cleanedList = [x for x in country_list if str(x) != 'nan']
    d_df.reset_index(inplace=True, drop=True)
    
    total_score = 0
    count = 0
    if year == 201712:
        for i in d_df.index:
            if d_df['國別'][i] in cleanedList:
                score = score_2017.loc[score_2017['country_2017'] == d_df['國別'][i]]
                s = score['Global Index Score_2017'].tolist()
                s = s[0]
                total_score += s
                count += 1
               
                
    if year == 201812:
        for i in d_df.index:
            if d_df['國別'][i] in cleanedList:
                score = score_2018.loc[score_2018['country_2018'] == d_df['國別'][i]]
                s = score['Global Index Score_2018'].tolist()
                s = s[0]
                total_score += s
                count += 1
                
                   
    if year == 201912:
        for i in d_df.index:
            if d_df['國別'][i] in cleanedList:
                score = score_2019.loc[score_2019['country_2019'] == d_df['國別'][i]]
                s = score['Global Index Score_2019'].tolist()
                s = s[0]
                total_score += s
                count += 1
    if count != 0:
        ESG_score_country = total_score/count
    else:
        ESG_score_country = ''
    return ESG_score_country


def Asset_ESG_score(year, company):
    fliter_target = (df['年月'] == 201812) & (df['公司代碼'] == 2330)
    d_df = df[fliter_target]
    country_list = d_df['國別'].unique().tolist()
    tax_heaven_list_tw = ['台灣','薩摩亞', '巴拿馬', '英屬維京', '開曼', '關島', '模里西斯', '塞席爾' ,'百慕達', '賴索托', '尼加拉瓜', '維京', 
    '安吉拉', '貝里斯', '馬紹爾群島', '科克群島', '澤西島', '盧森堡', '美屬薩摩亞', '根西島', '聖文森', '聖克里斯多', '多明尼加', '莫三比克'
    ,'巴哈馬']
    country_list = set(country_list ).difference(tax_heaven_list_tw)
    cleanedList = [x for x in country_list if str(x) != 'nan']
    d_df.reset_index(inplace=True, drop=True)
    
    AES  = 0
    
    asset_sum = pd.to_numeric(d_df['資產總額'], errors='coerce').sum()
    df_fillna = pd.to_numeric(d_df['資產總額'], errors='coerce').fillna(0)
    
    if year == 201712:
        for i in d_df.index:
            if d_df['國別'][i] in cleanedList:
                score = score_2017.loc[score_2017['country_2017'] == d_df['國別'][i]]
                s = score['Global Index Score_2017'].tolist()
                s = s[0]
                weight = df_fillna[i]/asset_sum
                asset_ESG = s * weight
                AES += asset_ESG
                return AES
    if year == 201812:
        for i in d_df.index:
            if d_df['國別'][i] in cleanedList:
                score = score_2018.loc[score_2018['country_2018'] == d_df['國別'][i]]
                s = score['Global Index Score_2018'].tolist()
                s = s[0]
                weight = df_fillna[i]/asset_sum
                asset_ESG = s * weight
                AES += asset_ESG
                return AES
    if year == 201912:
        for i in d_df.index:
            if d_df['國別'][i] in cleanedList:
                score = score_2019.loc[score_2019['country_2019'] == d_df['國別'][i]]
                s = score['Global Index Score_2019'].tolist()
                s = s[0]
                weight = df_fillna[i]/asset_sum
                asset_ESG = s * weight
                AES += asset_ESG
                return AES
    
    
    
    











e = ESG_score(201712,9942)
Asset_ESG_sc = Asset_ESG_score(201712,1104)     
        
        
        
        
        
        
        