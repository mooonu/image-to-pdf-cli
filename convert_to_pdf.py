import sys
import argparse
from pathlib import Path
from PIL import Image

SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png')


def validate_and_open_image(image_path: Path):
    if not image_path.exists():
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {image_path}")
    if image_path.suffix.lower() not in SUPPORTED_FORMATS:
        raise ValueError(f"지원하지 않는 형식입니다: {image_path.name}")
    img = Image.open(image_path)
    return img.convert("RGB")  # PDF는 RGB 모드 필요


def convert_images_to_pdf(image_paths, output_path):
    images = [validate_and_open_image(Path(p)) for p in image_paths]
    if not images:
        raise ValueError("PDF로 변환할 이미지가 없습니다.")

    first_image = images[0]
    remaining_images = images[1:]

    first_image.save(
        output_path,
        save_all=True,
        append_images=remaining_images
    )
    print(f"PDF 저장 완료: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="이미지를 PDF로 변환합니다.")
    parser.add_argument("images", nargs="+", help="변환할 이미지 파일 경로들")
    parser.add_argument("-o", "--output", default="output.pdf", help="출력할 PDF 파일명")

    args = parser.parse_args()

    try:
        convert_images_to_pdf(args.images, args.output)
    except Exception as e:
        print(f"오류 발생: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
