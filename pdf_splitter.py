from pypdf import PdfReader, PdfWriter

def split_pdf(input_pdf_path, start_page, end_page, output_pdf_path):
    """
    input_pdf_path: 원본 PDF 파일 경로
    start_page: 시작 페이지 (1부터 시작)
    end_page: 끝 페이지 (포함)
    output_pdf_path: 저장될 쪼개진 PDF 파일 경로
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    # 0부터 시작하므로 -1 처리
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])
        
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)
        
    print(f"성공! {start_page}페이지부터 {end_page}페이지까지 '{output_pdf_path}'로 저장되었습니다.")

if __name__ == "__main__":
    # 사용 예시: '점검실무행정.pdf' 파일에서 1부터 100페이지까지 잘라내기
    input_file = "점검실무행정.pdf"
    
    # 예: 100페이지씩 쪼개고 싶을 때
    split_pdf(input_file, start_page=1, end_page=100, output_pdf_path="점검실무행정_Part1(1-100).pdf")
    split_pdf(input_file, start_page=101, end_page=200, output_pdf_path="점검실무행정_Part2(101-200).pdf")