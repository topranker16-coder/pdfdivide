import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

st.set_page_config(page_title="PDF 페이지 쪼개기", layout="centered")

st.title("✂️ PDF 페이지 분할 도구")
st.write("대용량 PDF 파일을 업로드하고 원하는 페이지 구간을 잘라내어 다운로드하세요.")

# 1. 웹에서 PDF 파일 업로드 받기
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    st.success(f"파일 업로드 성공! 총 페이지 수: **{total_pages}페이지**")
    
    # 2. 시작 페이지와 끝 페이지 설정
    col1, col2 = st.columns(2)
    with col1:
        start_page = st.number_input("시작 페이지", min_value=1, max_value=total_pages, value=1)
    with col2:
        end_page = st.number_input("끝 페이지", min_value=1, max_value=total_pages, value=min(100, total_pages))
        
    if start_page > end_page:
        st.error("⚠️ 시작 페이지가 끝 페이지보다 클 수 없습니다.")
    else:
        if st.button("🚀 PDF 쪼개기 실행"):
            writer = PdfWriter()
            for page_num in range(start_page - 1, end_page):
                writer.add_page(reader.pages[page_num])
                
            # 메모리 버퍼에 저장
            output_stream = io.BytesIO()
            writer.write(output_stream)
            output_stream.seek(0)
            
            output_filename = f"split_{start_page}_to_{end_page}.pdf"
            
            st.success(f"✨ {start_page}페이지부터 {end_page}페이지까지 성공적으로 분할되었습니다!")
            
            # 다운로드 버튼 제공
            st.download_button(
                label="📥 쪼개진 PDF 다운로드",
                data=output_stream,
                file_name=output_filename,
                mime="application/pdf"
            )
