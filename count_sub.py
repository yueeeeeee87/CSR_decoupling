import pandas as pd

df = pd.read_csv('C:/Users/test/Desktop/info.csv')
score_dashbord = pd.read_csv('C:/Users/test/Desktop/csr/國家ESG 2.csv')
score_2017 = score_dashbord[['country_2017','Global Index Score_2017']]
score_2018 = score_dashbord[['country_2018','Global Index Score_2018']]
score_2019 = score_dashbord[['country_2019','Global Index Score_2019']]



def Count_Foreign_Company(year, company):
    fliter_target = (df['年月'] == year) & (df['公司代碼'] == company)
    fliter_tw = (df['國別'] == '台灣')
    
    d_df = df[fliter_target]
    
    
    #子公司總數
    num_total = df[fliter_target].count('columns')
    num_total = num_total.size
    
    #台灣子公司數
    num_taiwan = d_df[fliter_tw].count('columns')
    num_taiwan = num_taiwan.size
    
    
    print(df['國別'].unique())
    
    #避稅天堂名單
    tax_heaven_list = ['薩摩亞', '巴拿馬', '英屬維京', '開曼', '關島', '模里西斯', '塞席爾' ,'百慕達', '賴索托', '尼加拉瓜', '維京', 
    '安吉拉', '貝里斯', '馬紹爾群島', '科克群島', '澤西島', '盧森堡', '美屬薩摩亞', '根西島', '聖文森', '聖克里斯多', '多明尼加', '莫三比克'
    ,'巴哈馬']
    
    #避稅公司總數
    fliter_tax = (df['國別'].isin(tax_heaven_list))
    num_heaven = d_df[fliter_tax].count('columns')
    num_heaven = num_heaven.size
    
    #國外公司總數
    num_foreign = num_total - num_taiwan - num_heaven
    
    #國外公司所在地 總數
    fliter_tax = (~df['國別'].isin(tax_heaven_list))
    c_list = d_df[fliter_tax]
    uni = c_list['國別'].unique().tolist()
    if '台灣' in uni:
        uni.remove('台灣')
    country_list =  ' '.join(map(str, uni))
    country_size = len(uni)
    
    return num_total, num_taiwan, num_heaven, num_foreign, country_list, country_size

#避稅天堂名單中的伊朗因無伊朗的ESG分數才列入名單
def ESG_score(year, company):

    fliter_target = (df['年月'] == year) & (df['公司代碼'] == company)
    
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


def ESG_score_average(year, company):

    fliter_target = (df['年月'] == year) & (df['公司代碼'] == company)
    
    d_df = df[fliter_target]
    
    country_list = d_df['國別'].unique().tolist()
    tax_heaven_list_tw = ['台灣','薩摩亞', '巴拿馬', '英屬維京', '開曼', '關島', '模里西斯', '塞席爾' ,'百慕達', '賴索托', '尼加拉瓜', '維京', 
    '安吉拉', '貝里斯', '馬紹爾群島', '科克群島', '澤西島', '盧森堡', '美屬薩摩亞', '根西島', '聖文森', '聖克里斯多', '多明尼加', '莫三比克'
    ,'巴哈馬','伊朗']
    
    
    country_list = set(country_list ).difference(tax_heaven_list_tw)
    
    cleanedList = [x for x in country_list if str(x) != 'nan']
    d_df.reset_index(inplace=True, drop=True)
    total_score = 0
    if year == 201712:
        for i in cleanedList:            
            score = score_2017.loc[score_2017['country_2017'] == i]
            s = score['Global Index Score_2017'].tolist()
            s = s[0]
            total_score += s

    if year == 201812:
        for i in cleanedList:
            score = score_2018.loc[score_2018['country_2018'] == i]
            s = score['Global Index Score_2018'].tolist()
            s = s[0]
            total_score += s
                
                   
    if year == 201912:
        for i in cleanedList:
            score = score_2019.loc[score_2019['country_2019'] == i]
            s = score['Global Index Score_2019'].tolist()
            s = s[0]
            total_score += s
                
    if len(cleanedList) > 0:
        ESG_score_average = total_score/len(cleanedList)
    else:
        ESG_score_average = ''
    return ESG_score_average

data = pd.DataFrame(columns=['公司代碼', '簡稱', '年月', '子公司數', '台灣子公司數', '避稅子公司數', '外國子公司數', '子公司所在國家', '子公司所在國家數','ESG分數_國家加權'])




#c_name公司簡稱 #company公司代號
year_list = [201712, 201812, 201912]
company_list = list(df['公司代碼'].unique())
company_name = list(df['簡稱'].unique())
for name, company in enumerate(company_list):
    c_name = company_name[name]
    for year in year_list:
        print(year, company)
        num_total, num_taiwan, num_heaven, num_foreign, country_list, country_size = Count_Foreign_Company(year, company)
        ESG_country = ESG_score(year, company)
        ESG_score_ave = ESG_score_average(year, company)
        data = data.append({'公司代碼':company, '簡稱':c_name, '年月':year, '子公司數':num_total, '台灣子公司數':num_taiwan, '避稅子公司數':num_heaven, '外國子公司數':num_foreign, '子公司所在國家':country_list, '子公司所在國家數':country_size, 'ESG分數_國家加權':ESG_country, 'ESG分數_國家平均':ESG_score_ave}, ignore_index=True)






data.to_excel("output_ESG.xlsx")





        
    
    