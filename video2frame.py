import cv2
import sys
import os

OUTPUT_DIR = f"tmp{os.sep}cv2output"
TMP_DIR = "tmp"

def ShowHelp():
    print(f""">> By PRIME
Kullanım: python3 {sys.argv[0]} --video video.mp4 : Splits the video into frames.
          python3 {sys.argv[0]} --clsoutdir : Clears the output folder.""")
    sys.exit(0)


if len(sys.argv) < 2:
    ShowHelp()


if sys.argv[1] == "--help":
    ShowHelp()




if sys.argv[1] == "--clsoutdir":
    print(f"[+] {OUTPUT_DIR} Clearing content...")
    for element in os.listdir(OUTPUT_DIR):
        os.remove(f"{OUTPUT_DIR}{os.sep}{element}")
    print("[+] Finished... ")
    sys.exit(0)


if sys.argv[1] ==  "--video" and os.path.exists(sys.argv[2]):
    Target = sys.argv[2]

print(">> By PRIME")


if not os.path.exists(TMP_DIR) or not os.path.isdir(TMP_DIR):
    os.mkdir(TMP_DIR)

if not os.path.exists(OUTPUT_DIR) or not os.path.isdir(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
else:
    print(f"[+] {OUTPUT_DIR} Clearing content...")
    for element in os.listdir(OUTPUT_DIR):
        os.remove(f"{OUTPUT_DIR}{os.sep}{element}")




TargetVideo = cv2.VideoCapture(Target)
FrameNumber = 0



print("[+] Extracting frames from the video...")
while(True):
    is_succes, now_frame = TargetVideo.read()
    sys.stdout.write(f"\r> Frame: {FrameNumber}")
    sys.stdout.flush()
    if FrameNumber % 2 == 0:
        FrameNumber = FrameNumber + 1
        continue
    if is_succes:
        cv2.imwrite(f"tmp{os.sep}cv2output{os.sep}frame_{FrameNumber}.jpg", now_frame)
    else:
        break

    FrameNumber = FrameNumber + 1
print("\n[+] Finished...")
TargetVideo.release()
