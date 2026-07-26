import cv2
import numpy as np
from pathlib import Path


# File paths
INPUT_IMAGE_PATH = Path("input/test-image.jpg")
OUTPUT_FOLDER = Path("output")
MASK_OUTPUT_PATH = OUTPUT_FOLDER / "color-mask.png"
RESULT_OUTPUT_PATH = OUTPUT_FOLDER / "final-result.png"


# Create output folder if it does not exist
OUTPUT_FOLDER.mkdir(exist_ok=True)


# Color ranges in HSV format
# Each color has a lower and upper range.
COLOR_RANGES = {
    "Red": [
        (np.array([0, 100, 100]), np.array([10, 255, 255])),
        (np.array([160, 100, 100]), np.array([179, 255, 255]))
    ],
    "Green": [
        (np.array([35, 80, 80]), np.array([85, 255, 255]))
    ],
    "Blue": [
        (np.array([90, 80, 80]), np.array([130, 255, 255]))
    ],
    "Yellow": [
        (np.array([20, 100, 100]), np.array([35, 255, 255]))
    ]
}


def create_color_mask(hsv_image, color_ranges):
    """
    Creates a combined mask for all selected colors.
    """
    combined_mask = np.zeros(hsv_image.shape[:2], dtype=np.uint8)

    for ranges in color_ranges.values():
        for lower, upper in ranges:
            mask = cv2.inRange(hsv_image, lower, upper)
            combined_mask = cv2.bitwise_or(combined_mask, mask)

    return combined_mask


def detect_colors(image, hsv_image, color_ranges):
    """
    Detects colored regions and draws rectangles around them.
    """
    result_image = image.copy()

    for color_name, ranges in color_ranges.items():
        color_mask = np.zeros(hsv_image.shape[:2], dtype=np.uint8)

        for lower, upper in ranges:
            mask = cv2.inRange(hsv_image, lower, upper)
            color_mask = cv2.bitwise_or(color_mask, mask)

        # Reduce noise in the mask
        kernel = np.ones((5, 5), np.uint8)
        color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, kernel)
        color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(
            color_mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:
            area = cv2.contourArea(contour)

            # Ignore very small areas/noise
            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    result_image,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    3
                )

                cv2.putText(
                    result_image,
                    color_name,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

    return result_image


def main():
    if not INPUT_IMAGE_PATH.exists():
        print(f"Error: Could not find image at {INPUT_IMAGE_PATH}")
        print("Make sure your image is named test-image.jpg and placed inside the input folder.")
        return

    image = cv2.imread(str(INPUT_IMAGE_PATH))

    if image is None:
        print("Error: Could not read the image file.")
        return

    # Resize image if it is too large
    max_width = 900
    height, width = image.shape[:2]

    if width > max_width:
        scale = max_width / width
        new_width = int(width * scale)
        new_height = int(height * scale)
        image = cv2.resize(image, (new_width, new_height))

    # Convert image from BGR to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create combined color mask
    combined_mask = create_color_mask(hsv_image, COLOR_RANGES)

    # Detect colors and draw results
    result_image = detect_colors(image, hsv_image, COLOR_RANGES)

    # Save output files
    cv2.imwrite(str(MASK_OUTPUT_PATH), combined_mask)
    cv2.imwrite(str(RESULT_OUTPUT_PATH), result_image)

    print("Color recognition completed successfully.")
    print(f"Mask saved to: {MASK_OUTPUT_PATH}")
    print(f"Final result saved to: {RESULT_OUTPUT_PATH}")

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Color Mask", combined_mask)
    cv2.imshow("Final Result", result_image)

    print("Press any key on the image window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()