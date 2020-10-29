import pandas as pd


name = []
purpose = []


def merge_Qiuchen():
    df = pd.read_csv("company_qiuchen.csv")
    name.extend(df['Name'])
    purpose.extend(df['Purpose'])


def merge_Pengfei():
    df = pd.read_csv("company_pengfei.csv")
    name.extend(df['Company'])
    purpose.extend(df['Purpose'])


def merge_Yuyang():
    df = pd.read_csv("company_yuyang.csv")
    name.extend(df['CompanyName'])
    purpose.extend(df['Purpose'])


def merge_Kairu():
    df = pd.read_csv("company_kairu.csv")
    name.extend(df['Name'])
    purpose.extend(df['Purpose'])


merge_Qiuchen()
merge_Pengfei()
merge_Yuyang()
merge_Kairu()
merge_df = pd.DataFrame({'Name': [],
                         'Purpose': []})

merge_df['Name'] = name
merge_df['Purpose'] = purpose
merge_df.to_csv('merged_file.csv')
