import streamlit as st
import pandas as pd


import pandas as pd

st.header("GA2-3지점 대리점지사 사용인별 실적")
st.subheader("지사명 입력후에 활용 --update 202303")

@st.cache_data
def read_excel():
    df = pd.read_excel('사용인별실적.xlsx')
    return df

df = read_excel()

지점명 = 'GA2-3지점'

jisa_list = df.대리점지사명.unique()

search_jisa = st.text_input('지사명을 입력해주세요')

if search_jisa:
    search_jisa_list = df[df['대리점지사명'].str.contains(search_jisa)].대리점지사명.unique().tolist()
    # print(search_jisa_list)
    # st.write(search_jisa_list)

    if search_jisa_list:
        jisa_selected = st.selectbox("지사를선택해주세요",search_jisa_list)

        if jisa_selected:
            df_l = df[df['대리점지사명']==jisa_selected]
            column_months = df_l.columns.tolist()
            column_months = [i for i in column_months if i[:1]=="m"]
            column_months.sort(reverse=True)
            column_months = column_months[:5]

            column_list = ['조직코드','조직명'] + column_months
            df_l['조직코드'] = df_l['조직코드'].astype(str)
            df_l = df_l[column_list]
            df_l = df_l.sort_values('m202303', ascending=False).copy()
            st.dataframe(df_l, use_container_width=True)
    else:
        pass

else:
    pass