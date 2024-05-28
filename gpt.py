import pandas as pd
from openai import OpenAI
import time
import re
# API 클라이언트 설정
client = OpenAI(api_key="YOUR API KEY")

file_paths = [
    "essay.csv",  # 파일 경로 예시
]

dfs = []  # DataFrame들을 저장할 빈 리스트

# CSV 파일을 읽어 DataFrame으로 변환 후 리스트에 추가
for file_path in file_paths:
    df = pd.read_csv(file_path, sep=',')
    dfs.append(df)

# 모든 DataFrame을 하나로 합치기
all_df = pd.concat(dfs, ignore_index=True)

# 결과 파일 준비
output_file = "results.csv"
first_write = True  # 첫 번째 쓰기 작업 플래그

# 'create' 칼럼의 각 값을 content로 사용하여 메시지 생성 및 AI 응답 체크
for index, row in all_df.iterrows():
    # 메시지 생성
    a = row['create']
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=a
    )
    # AI가 처리하도록 요청
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id='asst_iagHMJBULYcHc2JhgHLnQlsF',
    )
    # 실행 결과 확인
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        ai_response = messages.data[0].content[0].text.value
    else:
        ai_response = run.status  # 실패 시 상태 출력
    pattern = r"\d+%"
    match = re.search(pattern, ai_response)
    if match:
        percent_value = match.group()
    else:
        percent_value =0
    # 결과 DataFrame 생성
    new_result = pd.DataFrame([{
        'id': row['id'],
        'Model': row['model'],
        'percent': percent_value,
        'AI Response': ai_response
    }])

    # 파일에 데이터 추가
    new_result.to_csv(output_file, mode='a', index=False, header=first_write)
    first_write = False  # 헤더는 처음에만 추가

print("모든 결과가 'results.csv' 파일에 저장되었습니다.")
