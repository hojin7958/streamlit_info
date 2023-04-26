import streamlit as st
import pandas as pd
import pandas as pd
import os
import datetime



### 행번호 숨기기
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

######


st.header("대리점지사 사용인별 실적")


def save_uploadedfile(uploadedfile):
     with open('rawdata.xlsx',"wb") as f:
         f.write(uploadedfile.getbuffer())
    #  return st.success("File saved")


with st.expander("데이터 업데이트"):
    if st.button("새로고침하기"):
        # Clears all st.cache_resource caches:
        st.cache_resource.clear()



    datafile = st.file_uploader("파일을 업로드해주세요",type=['xlsx'])




@st.cache_resource
def read_excel():
    path = 'rawdata.xlsx'
    df = pd.read_excel(path)
    # df = df[df['현재지점조직명']=='GA2-3지점']
    time1 = os.path.getmtime(path)
    time2 = datetime.datetime.fromtimestamp(time1)
    return df, time2


if datafile is not None:
    file_details = {"FileName":datafile.name,"FileType":datafile.type}
    save_uploadedfile(datafile)
    # st.cache_resource.clear()
    df, mod_time = read_excel()
    # datafile = None

df, mod_time = read_excel()

st.caption("파일최종업로드날짜  : "+str(mod_time)+ "  업로드날짜 전일까지 실적 업데이트")

# 지점명 = 'GA2-3지점'

jisa_list = df.현재대리점지사명.unique()
search_jijum = st.selectbox("지점을 선택해주세요", ['GA2-3지점','GA2-1지점','GA2-2지점','GA2-4지점','GA2-5지점','GA2-6지점','GA2-7지점','GA2-8지점'])
search_jisa = st.text_input('지사명을 입력해주세요')



if search_jisa:
    df_temp = df[df['현재지점조직명']==search_jijum]
    search_jisa_list = df_temp[df_temp['현재대리점지사명'].str.contains(search_jisa)].현재대리점지사명.unique().tolist()
    # print(search_jisa_list)
    # st.write(search_jisa_list)s

    if search_jisa_list:
        jisa_selected = st.selectbox("지사를선택해주세요",search_jisa_list)

        if jisa_selected:
            df_l = df[df['현재대리점지사명']==jisa_selected]
            column_list = ['현재대리점설계사조직코드', 
                            '현재대리점설계사조직명',
                            '인보험실적',
                            '인정실적',
                            '이전월인정실적',
                            '전전월인정실적',
                            '실적_1주차',
                            '실적_2주차',
                            '실적_3주차',
                            '실적_4주차',
                            '실적_5주차',
                            '현재월연속가동',
                            '이전월연속가동'                         
                            ]
            
            columns_list_mod = ['조직코드',
                            '조직명',
                            '인보험',
                            '인정실적',
                            '인정실적-1',
                            '인정실적-2',
                            '실적1주',
                            '실적2주',
                            '실적3주',
                            '실적4주',
                            '실적5주',
                            '연속',
                            '연속-1',                            
                            ]
            df1 = df_l[column_list]
            df1.columns = columns_list_mod
            df1['조직코드'] = df1['조직코드'].astype(str)
            df1 = df1.sort_values('인정실적-1', ascending=False).copy()
            st.dataframe(df1.set_index(df1.columns[1]), use_container_width=True)
            # st.table(df1)
            # column_months = df_l.columns.tolist()
            # column_months = [i for i in column_months if i[:1]=="m"]
            # column_months.sort(reverse=True)
            # column_months = column_months[:5]

            # column_list = ['조직코드','조직명'] + column_months
            # df_l['조직코드'] = df_l['조직코드'].astype(str)
            # df_l = df_l[column_list]
            # df_l = df_l.sort_values('m202303', ascending=False).copy()
            # st.dataframe(df_l, use_container_width=True)
    else:
        pass

else:
    pass